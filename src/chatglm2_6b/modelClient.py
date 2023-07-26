from typing import List, Tuple

import torch
from transformers import AutoModel, AutoTokenizer
from transformers.generation.logits_process import LogitsProcessor
from transformers.generation.utils import LogitsProcessorList

DEFAULT_MODEL_PATH = "THUDM/chatglm2-6b"


class InvalidScoreLogitsProcessor(LogitsProcessor):
    def __call__(
        self, input_ids: torch.LongTensor, scores: torch.FloatTensor
    ) -> torch.FloatTensor:
        if torch.isnan(scores).any() or torch.isinf(scores).any():
            scores.zero_()
            scores[..., 5] = 5e4
        return scores


class ChatGLM2(object):
    def __init__(self, model_path=None):
        self.model_path = DEFAULT_MODEL_PATH
        if model_path:
            self.model_path = model_path
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, trust_remote_code=True
        )
        model = (
            AutoModel.from_pretrained(self.model_path, trust_remote_code=True)
            .half()
            .cuda()
        )
        self.model = model.eval()

    def generate(
        self,
        prompt: str,
        do_sample: bool = True,
        max_length: int = 8192,
        num_beams: int = 1,
        temperature: float = 0.8,
        top_p: float = 0.8,
    ):
        logits_processor = LogitsProcessorList()
        logits_processor.append(InvalidScoreLogitsProcessor())
        gen_kwargs = {
            "max_length": max_length,
            "num_beams": num_beams,
            "do_sample": do_sample,
            "top_p": top_p,
            "temperature": temperature,
            "logits_processor": logits_processor,
        }
        inputs = self.tokenizer([prompt], return_tensors="pt")
        inputs = inputs.to(self.model.device)
        outputs = self.model.generate(**inputs, **gen_kwargs)
        outputs = outputs.tolist()[0][len(inputs["input_ids"][0]) :]
        response = self.tokenizer.decode(outputs)
        response = self.model.process_response(response)
        return response

    def stream_generate(
        self,
        prompt: str,
        do_sample: bool = True,
        max_length: int = 8192,
        temperature: float = 0.8,
        top_p: float = 0.8,
    ):
        logits_processor = LogitsProcessorList()
        logits_processor.append(InvalidScoreLogitsProcessor())
        gen_kwargs = {
            "max_length": max_length,
            "do_sample": do_sample,
            "top_p": top_p,
            "temperature": temperature,
            "logits_processor": logits_processor,
        }
        inputs = self.tokenizer([prompt], return_tensors="pt")
        inputs = inputs.to(self.model.device)
        for outputs in self.model.stream_generate(**inputs, **gen_kwargs):
            outputs = outputs.tolist()[0][len(inputs["input_ids"][0]) :]
            response = self.tokenizer.decode(outputs)
            if response and response[-1] != "�":
                response = self.model.process_response(response)
                yield response

    def stream_chat(
        self,
        query: str,
        history: List[Tuple[str, str]],
        max_length: int = 8192,
        do_sample=True,
        top_p=0.8,
        temperature=0.8,
    ):
        stream = self.model.stream_chat(
            self.tokenizer,
            query,
            history,
            max_length=max_length,
            do_sample=do_sample,
            top_p=top_p,
            temperature=temperature,
        )
        for resp, new_history in stream:
            yield resp, new_history


class FakeModelClient(object):
    def generate(self, **kwags):
        return f"gRPC request generated successfully. The params are {kwags}"

    def stream_generate(self, **kwags):
        yield "gRPC request stream_generate successfully. The params are:"
        for k, v in kwags.items():
            yield f"{k}: {v}"

    def stream_chat(self, **kwags):
        history = kwags['history']
        history.append([kwags['query'], ""])
        text = "gRPC request stream_chat successfully. The params are:"
        history[-1][-1] += text
        yield text, history
        for k, v in kwags.items():
            text = f"\n{k}: {v}"
            history[-1][-1] += text
            yield text, history
