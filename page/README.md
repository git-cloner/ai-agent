# AI-Agent

## 1、环境

```shell
# 建立虚拟环境
conda create -n ai-agent python=3.12 -y
# 激活虚拟环境
conda activate ai-agent
# 安装依赖库
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## 2、运行

```shell
# 激活虚拟环境
conda activate ai-agent
# 运行ai-agent程序
streamlit run ai-agent.py
# 后台运行程序
nohup streamlit run ai-agent.py --server.port 8502 >ai-agent.log 2>&1 &
```

