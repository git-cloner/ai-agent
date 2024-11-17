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

# 设置工作目录  
WORKDIR /workspace

# 安装依赖库
RUN pip3 install pymemgpt[local]==0.3.22 -i https://pypi.mirrors.ustc.edu.cn/simple

COPY model_download.py ./

# 下载词嵌入模型
RUN python3 model_download.py --e \
    --repo_id BAAI/bge-small-en-v1.5 \
    --token YPY8KHDQ2NAHQ2SG && \
    mkdir -p BAAI/bge-small-en-v1.5 && \
    cp -R ./dataroot/models/BAAI/bge-small-en-v1.5/* \
    ./BAAI/bge-small-en-v1.5/ && \
    rm -fr ./dataroot

# 拷贝配置文件到容器
COPY .memgpt /root/.memgpt

# 复制nltk_data文件夹到容器
COPY nltk_data /root/nltk_data

# 启动应用  
CMD ["memgpt" ,"run","--agent","agent_test"]