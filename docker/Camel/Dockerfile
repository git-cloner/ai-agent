# 使用 Ubuntu 基础镜像  
FROM ubuntu:jammy-20240808

# 设置环境变量以避免交互模式  
ENV DEBIAN_FRONTEND=noninteractive  

# 更新包列表并安装 Python 3.10 及其依赖  
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.10 python3.10-distutils \
    && apt-get install -y python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  

# 确保 Python 3.10 可执行  
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1  

# 安装git
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
    
# 设置工作目录  
WORKDIR /workspace

# clone源码
RUN git clone https://github.com/camel-ai/camel && \
    cd camel && git checkout a42d029 && \
    pip3 install -e .[all] --use-pep517 \
    -i https://pypi.mirrors.ustc.edu.cn/simple

# 环境变量
ENV OPENAI_API_KEY=EMPTY
ENV OPENAI_API_BASE_URL=https://gitclone.com/aiit/ollama/v1

WORKDIR /workspace/camel
# 启动应用  
CMD ["python3", "examples/ai_society/role_playing.py"]