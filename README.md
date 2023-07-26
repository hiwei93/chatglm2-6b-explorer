# ChatGLM2-6B 探索

[ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B) 是 [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) 第二代版本，已经发布就一直位列 Huggingface 模型下载榜单前几位。

ChatGLM2-6B 相交前代模型在推理效果、推理速度和上下文长度上都有提升，具体效果如何，就让我们一起探索吧。

查看项目：

- [【huggingface space】: hiwei/chatglm2-6b-explorer](https://huggingface.co/spaces/hiwei/chatglm2-6b-explorer)

- [【github】: chatglm2-6b-explorer](https://github.com/hiwei93/chatglm2-6b-explorer)

- [【aistudio project】: 探索 ChatGLM2-6B](https://aistudio.baidu.com/aistudio/projectdetail/6460572)

## 项目介绍

本项目是对 ChatGLM2-6B 模型能力的探索

### 项目体系结构

项目的主要结构，如下图所示：

![](https://ai-studio-static-online.cdn.bcebos.com/d63c0f803c52468aa78da15ff8ef88502883b74257b244dba34037afe39d8e0f)

### 包含组件

主要包含以下组件

#### 1. websocket 模型服务

以 websocket API 的方式访提供模型能力，解耦 Gradio 开发与模型加载，提高开发速度

#### 2. GRPC 模型服务

使用 RPC 通信的方式提供模型能力，通信效率高，支持单向流式传输方式，建议使用

#### 3. Gradio Web 应用展廊

1) 原生通用对话 Web 应用

   ![](https://ai-studio-static-online.cdn.bcebos.com/84375e78e52742c9afdf1f94446866a0d423768495d14280b616eb23c9ba9002)
   
2) 基于设定指令的对话 Web 应用

   ![](https://ai-studio-static-online.cdn.bcebos.com/1589a111dfa54426a04eaa50a9ead628efbf559e55014f5093d7c1084fcfb7b1)
   
3) 翻译器

   ![](https://ai-studio-static-online.cdn.bcebos.com/68deb5f5d57a4ce6957bbf96b912f3829c4271ff7e144b9889212adf01dc5d53)
   
> Gradio Web 应用参考 [Falcon-Chat demo](https://huggingface.co/spaces/HuggingFaceH4/falcon-chat)


## 一、安装依赖


```bash
pip install -r chatglm2_6b_explorer/requirements.txt --user
```

## 二、设置

通过配置环境变量来进行设置，有以下配置项

| 配置项             | 说明                                                                                                                             | 默认值                                   |
| ------------------ |--------------------------------------------------------------------------------------------------------------------------------| ---------------------------------------- |
| CHAT_CLIENT        | 指定使用的对话客户端，有两个客户端类型可选：<br>- ChatGLM2APIClient：通过 API 访问模型<br>- ChatGLM2GRPCClient：使用 GPRC 方式访问<br>- ChatGLM2ModelClient：直接访问模型 | ChatGLM2APIClient                        |
| MODEL_WS_URL       | 模型websocket API的访问地址                                                                                                           | ws://localhost:10001                     |
| CHATGLM_MODEL_PATH | 模型的路径                                                                                                                          | 默认从Huggingface下载，THUDM/chatglm2-6b |

### 1. `CHAT_CLIENT`

`CHAT_CLIENT` 指定应用使用的对话客户端类型，有两个客户端类型可选

- ChatGLM2APIClient：通过 API 的方式访问模型的能力（需要启动 websocket 服务，操作请看：`三、运行模型 websocket 服务`）
- ChatGLM2GRPCClient：通过 GRPC 的方式访问模型的能力（需要启动 GRPC 服务，操作请看：`四、运行模型 GRPC 服务`）
- ChatGLM2ModelClient：直接加载模型访问

> 💡如果有开发基础，建议选择 **ChatGLM2APIClient** 或 **ChatGLM2GRPCClient** 方式，可以将 Gradio Web 界面开发与模型加载分离，提高开发与调试速度。
> 
> 💡如果需要部署到Huggingface或者其他托管平台，建议使用 **ChatGLM2ModelClient** 方式，能够实现直接部署。
> 
> ❗️强烈不建议在开发的时候使用 **ChatGLM2ModelClient** 方式，导致不断加载模型，拖慢开发速度。

### 2. `MODEL_WS_URL`

`MODEL_WS_URL` 指定模型 websocket 服务 URL，如果 `CHAT_CLIENT=ChatGLM2APIClient`，则必须填写


### 3. `CHATGLM_MODEL_PATH`

`CHATGLM_MODEL_PATH` 指定使用的模型路径，如果是 `THUDM/chatglm2-6b` 则会从 Huggingface 拉取模型；如果指定本地模型路径，则使用本地模型。


## 三、运行模型 websocket 服务

前提：

- 安装了依赖、配置好 `CHATGLM_MODEL_PATH`
- 配置 `SERVER_TYPE=websocket`

```bash
cd chatglm2_6b_explorer/src
python runserver.py
```

## 四、运行模型 GRPC 服务

前提：

- 安装了依赖、配置好 `CHATGLM_MODEL_PATH`
- 配置 `SERVER_TYPE=grpc`

```bash
cd chatglm2_6b_explorer/src
python runserver.py
```

## 五、运行 Web 应用

```bash
cd chatglm2_6b_explorer/src
python gallery.gradio.py
```