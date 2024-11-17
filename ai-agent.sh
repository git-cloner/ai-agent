#!/bin/bash  

# 检查参数数量  
if [ "$#" -lt 1 ]; then  
    echo "用法: $0 <镜像名称> [端口号]"  
    exit 1  
fi  

# 获取镜像名称和端口号
IMAGE="61.133.217.142:20800/$1"
# 如果未传递端口参数，使用默认值8501  
PORT=${2:-8501}  

# 执行 podman pull 命令  
podman pull $IMAGE --tls-verify=false  

# 执行 podman run 命令  
podman run -p $PORT:$PORT -it $IMAGE