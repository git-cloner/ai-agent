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
RUN git clone https://github.com/eosphoros-ai/DB-GPT && \
    cd DB-GPT && git checkout 374b6ad && \
    pip3 install -e ".[default]" --use-pep517 \
    -i https://pypi.mirrors.ustc.edu.cn/simple && \
    pip3 install pymysql==1.1.1 -i https://pypi.mirrors.ustc.edu.cn/simple

# 拷贝配置文件到容器
COPY .env /workspace/DB-GPT

# 显示容器将使用的端口  
EXPOSE 5760

# 设置工作目录 
WORKDIR /workspace/DB-GPT

# 启动应用  
CMD ["python3","dbgpt/app/dbgpt_server.py"]