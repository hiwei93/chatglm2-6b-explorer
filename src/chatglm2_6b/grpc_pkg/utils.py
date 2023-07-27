from chatglm2_6b.grpc_pkg import chatglm_pb2


def history2list(history: chatglm_pb2.ChatHistory):
    return [[s for s in turn.strings] for turn in history.turns]


def list2history(str_list):
    history = chatglm_pb2.ChatHistory()
    for sub_list in str_list:
        turn = chatglm_pb2.ChatTurn()
        turn.strings.extend(sub_list)
        history.turns.append(turn)
    return history
