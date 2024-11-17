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
# RUN git clone https://github.com/Significant-Gravitas/AutoGPT
COPY AutoGPT AutoGPT
# 检出历史版本
RUN cd AutoGPT && git checkout 227cf41
# 拷贝本地文件到容器中
COPY requirements.txt ./AutoGPT/
COPY .env ./AutoGPT/autogpt/  
# 安装依赖环境
RUN cd AutoGPT && pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple
# 切换到forge目录
RUN cd AutoGPT && cd forge && \
    pip3 install -e . -i https://pypi.mirrors.ustc.edu.cn/simple && \
    pip3 install pydantic==1.10.9 -i https://pypi.mirrors.ustc.edu.cn/simple
# 切换目录到autogpt
WORKDIR /workspace/AutoGPT/autogpt
# 启动应用  
CMD ["python3", "-m", "autogpt","run","--skip-news"]