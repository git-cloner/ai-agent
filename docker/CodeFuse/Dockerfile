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

# 安装基础环境
RUN git clone https://github.com/codefuse-ai/codefuse-chatbot && \
    cd codefuse-chatbot && git checkout d6932ec && \
    pip3 install -r requirements.txt --use-pep517 \
    -i https://pypi.mirrors.ustc.edu.cn/simple && \
    pip3 install streamlit==1.36.0  \
    -i https://pypi.mirrors.ustc.edu.cn/simple

COPY model_download.py ./

# 下载词嵌入模型
RUN python3 model_download.py --e \
    --repo_id shibing624/text2vec-base-chinese \
    --token YPY8KHDQ2NAHQ2SG

# 拷贝配置文件到容器
COPY model_config.py server_config.py /workspace/codefuse-chatbot/configs/
COPY dialogue.py /workspace/codefuse-chatbot/examples/webui/

# 切换到examples
WORKDIR /workspace/codefuse-chatbot/examples

ENV SANDBOX_DO_REMOTE=false
ENV DOCKER_SERVICE=false
ENV LLM_MODEL=glm4
ENV API_BASE_URL=https://gitclone.com/aiit/ollama/v1 

# 显示容器将使用的端口  
EXPOSE 8501 7861 7862 8510

# 启动应用  
CMD ["bash"]