import uvicorn

from chatglm2_6b.server import app


def runserver():
    uvicorn.run(app, host="0.0.0.0", port=10001)


if __name__ == '__main__':
    runserver()