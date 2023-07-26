from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GreetRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ChatHistory(_message.Message):
    __slots__ = ["turns"]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    turns: _containers.RepeatedCompositeFieldContainer[ChatTurn]
    def __init__(self, turns: _Optional[_Iterable[_Union[ChatTurn, _Mapping]]] = ...) -> None: ...

class ChatTurn(_message.Message):
    __slots__ = ["strings"]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    strings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, strings: _Optional[_Iterable[str]] = ...) -> None: ...

class GenerateResponse(_message.Message):
    __slots__ = ["generated_text"]
    GENERATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    generated_text: str
    def __init__(self, generated_text: _Optional[str] = ...) -> None: ...

class GenerateRequest(_message.Message):
    __slots__ = ["prompt", "do_sample", "max_length", "temperature", "top_p"]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    DO_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    do_sample: bool
    max_length: int
    temperature: float
    top_p: float
    def __init__(self, prompt: _Optional[str] = ..., do_sample: bool = ..., max_length: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ["generated_text", "new_history"]
    GENERATED_TEXT_FIELD_NUMBER: _ClassVar[int]
    NEW_HISTORY_FIELD_NUMBER: _ClassVar[int]
    generated_text: str
    new_history: ChatHistory
    def __init__(self, generated_text: _Optional[str] = ..., new_history: _Optional[_Union[ChatHistory, _Mapping]] = ...) -> None: ...

class ChatRequest(_message.Message):
    __slots__ = ["query", "history", "do_sample", "max_length", "temperature", "top_p"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    DO_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    query: str
    history: ChatHistory
    do_sample: bool
    max_length: int
    temperature: float
    top_p: float
    def __init__(self, query: _Optional[str] = ..., history: _Optional[_Union[ChatHistory, _Mapping]] = ..., do_sample: bool = ..., max_length: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ...) -> None: ...
