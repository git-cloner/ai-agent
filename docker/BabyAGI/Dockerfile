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

# 复制程序
COPY babyagi ./babyagi

# 安装依赖库
RUN cd babyagi && pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple

# 设置启动目录
WORKDIR /workspace/babyagi

# 设置环境变量
ENV TABLE_NAME=test

# 启动应用  
CMD ["python3","babyagi.py"]