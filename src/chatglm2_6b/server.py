import functools

import anyio
import uvicorn
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

app = FastAPI()

chat_glm2 = None


class ChatParams(BaseModel):
    prompt: str
    do_sample: bool = True
    max_length: int = 2048
    temperature: float = 0.8
    top_p: float = 0.8


@app.post("/generate")
def generate(params: ChatParams):
    input_params = params.dict()
    text = chat_glm2.generate(**input_params)
    return {"text": text}


@app.websocket("/streamGenerate")
async def stream_generate(websocket: WebSocket):
    await websocket.accept()
    params = await websocket.receive_json()
    func = functools.partial(chat_glm2.stream_generate, **params)
    stream = await anyio.to_thread.run_sync(func)
    for resp in stream:
        await websocket.send_json({"text": resp})
    await websocket.close()


@app.websocket("/streamChat")
async def stream_chat(websocket: WebSocket):
    await websocket.accept()
    params = await websocket.receive_json()
    func = functools.partial(chat_glm2.stream_chat, **params)
    stream = await anyio.to_thread.run_sync(func)
    for resp, history in stream:
        await websocket.send_json({"resp": resp, "history": history})
    await websocket.close()


def runserver(model_client):
    global chat_glm2
    chat_glm2 = model_client
    uvicorn.run(app, host="0.0.0.0", port=10001)
