# AI-Code

## 1、环境

```shell
# 建立虚拟环境
conda create -n ai-code python=3.12 -y
# 激活虚拟环境
conda activate ai-code
# 安装依赖库
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## 2、运行

```shell
# 激活虚拟环境
conda activate ai-code
# 运行Chat程序
streamlit run chat_bot.py
# 后台运行程序
nohup streamlit run chat_bot.py >aicode.log 2>&1 &
```

## 3、制作Docker镜像

```bash
# 构建镜像
sudo docker build -t aicode .
# 测试镜像（交互式）
sudo docker run -p 8501:8501 -it aicode
# 测试镜像（后台服务）
sudo docker run -p 8501:8501 -d aicode
# 上传到本地镜像库（以本机IP=172.16.62.156为例）
# 本地镜像库：sudo docker run -d -p 5000:5000 --name registry registry:2
# 查看本地镜像库情况：http://172.16.62.156/v2/_catalog
sudo docker tag aicode 172.16.62.156/aicode  
sudo docker push 172.16.62.156/aicode
# 用Podman测试
# 安装Podman
sudo apt-get update
sudo apt-get -y install podman
podman --version
# 测试
podman pull 172.16.62.156/aicode --tls-verify=false
podman run -p 8501:8501 -it 172.16.62.156/aicode
```

## 4、Docker配置镜像的方法

```shell
sudo vi /etc/docker/daemon.json
# 增加以下内容
{
 "registry-mirrors": [
        "https://docker.unsee.tech"
    ]
}
# 重启服务
sudo systemctl daemon-reload && sudo systemctl restart docker
```

## 5、Nginx代理Docker registry

```shell
location /v2/ {
         proxy_redirect off;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Host $http_host;
         proxy_pass http://127.0.0.1:5000/v2/;
    }
```

