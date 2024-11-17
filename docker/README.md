# 镜像

## 1、制作

```shell
sudo docker build -t 镜像名 .
```

## 2、上传

```shell
# tag
sudo docker tag 镜像名 172.16.62.156/镜像名
# push
sudo docker push 172.16.62.156/镜像名
# test
http://172.16.62.156/v2/_catalog
```

## 3、运行

```shell
ai-agen.sh 镜像名
```

