# 使用 Ubuntu 基础镜像  
FROM ubuntu:jammy-20240808

# 设置环境变量以避免交互模式  
ENV DEBIAN_FRONTEND=noninteractive  

# 设置环境变量  
ENV NODE_VERSION=20 

# 安装必要的依赖  
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash -  && \
    apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*  

# 验证Node.js和npm的安装  
RUN node -v && npm -v 

# 安装git和pnpm
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    npm install pnpm -g

RUN npm config set registry https://registry.npmmirror.com/  
    
# 设置工作目录  
WORKDIR /workspace

# clone源码
RUN git clone https://github.com/little51/bolt.new.local

# 安装依赖库
RUN cd bolt.new.local && pnpm install

# 显示容器将使用的端口  
EXPOSE 8501 

# 设置工作目录
WORKDIR /workspace/bolt.new.local

# 启动应用  
CMD ["pnpm", "run", "dev", "--host"]