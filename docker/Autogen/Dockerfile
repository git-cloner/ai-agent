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

# 安装基础环境
RUN pip3 install pyautogen==0.2.18 \
    -i https://pypi.mirrors.ustc.edu.cn/simple && \
    pip3 install gradio==4.37.2 \
    -i https://pypi.mirrors.ustc.edu.cn/simple

# 拷贝配置文件到容器
COPY autogen-demo.py /workspace/

# 显示容器将使用的端口  
EXPOSE 8501

# 启动应用  
CMD ["python3","autogen-demo.py"]