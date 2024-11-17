#!/bin/bash  

# 检查操作系统版本  
. /etc/os-release  

# 检查是否已安装 podman  
if ! command -v podman &> /dev/null; then  
    echo "Podman 尚未安装，正在安装"  

    # 针对 Ubuntu 系统  
    if [[ "$ID" == "ubuntu" ]]; then  
        echo "检测到 Ubuntu，正在添加 Podman 源"  
        echo "deb https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list  
        curl -L https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/xUbuntu_${VERSION_ID}/Release.key | sudo apt-key add -  

        # 更新软件包列表并安装 Podman  
        sudo apt-get update  
        sudo apt-get -y install podman  
        echo "Podman 安装完成！"  

    # 针对 CentOS 系统  
    elif [[ "$ID" == "centos" || "$ID" == "rhel" ]]; then  
        echo "检测到 CentOS 或 RHEL，正在安装 Podman" 
        sudo yum search podman
        sudo yum -y install podman  
        echo "Podman 安装完成！"  

    else  
        echo "不支持的操作系统: $ID"  
        exit 1  
    fi  
else  
    echo "Podman 已安装"  
fi  

# 下载 ai-agent.sh 文件  
DOWNLOAD_URL="https://aliendao.cn/ai-agent/ai-agent.sh"  
OUTPUT_FILE="ai-agent.sh"  

echo "正在下载 ai-agent.sh"  
curl -o $OUTPUT_FILE $DOWNLOAD_URL  

# 对 ai-agent.sh 授权  
chmod +x $OUTPUT_FILE
echo "已对 $OUTPUT_FILE 赋予执行权限"  
sudo mv $OUTPUT_FILE /usr/local/bin/
echo "已将 $OUTPUT_FILE 移动到/usr/local/bin/"  
echo "ai-agent 安装完成"