# AI-Agent使用方法

AI-Agent是一个一键运行ai-agent的方法，由podman（或docker）环境和ai-agent.sh脚本组成。目前支持的Agent如下：

| 名称             | 简介                                                      | 运行方法                              | 访问方法               |
| ---------------- | --------------------------------------------------------- | ------------------------------------- | ---------------------- |
| aicode           | 支持多种模型的Chat应用                                    | ai-agent.sh aicode                    | http://服务器IP:8501   |
| AutoGPT          | 经典的AI Agent应用，自动完成用户设定的任务                | ai-agent.sh autogpt                   | 命令行交互             |
| MemGPT           | 长记忆GPT应用                                             | ai-agent.sh memgpt                    | 命令行交互（启动略慢） |
| BabyAGI          | 任务分解型AGI应用，根据用户设定的任务自动分解任务，并逐步 | ai-agent.sh babyagi                   | 命令行交互             |
| Camel            | 多角色扮演完成用户设定的任务                              | ai-agent.sh camel                     | 命令行交互             |
| CodeFuse-ChatBot | 软件开发工具类AI Agent                                    | ai-agent.sh codefuse python3 start.py | http://服务器IP:8501   |

## 1、安装

```shell
curl -o install.sh https://aliendao.cn/ai-agent/install.sh && bash install.sh
```

## 2、使用

```shell
ai-agent.sh 镜像名
或
ai-agent.sh 镜像名 端口号

# 举例
ai-agent.sh aicode
或
ai-agent.sh aicode 8501
```

## 3、原理

将以上AI Agent的应用或例程打包成Docker镜像，使用脚本调用Podman装载。

