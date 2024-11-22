import streamlit as st

card_data = [
    {"title": "ChatBot：多种模型的聊天应用", "link": "https://gitclone.com/aiit/chat1/",
        "description": "ai-agent.sh aicode",
        "image_path": "https://gitclone.com/download1/ai-agent/Chat-bot.png"},
    {"title": "AutoGPT：经典通用型AI Agent", "link": "https://github.com/Significant-Gravitas/AutoGPT",
        "description": "ai-agent.sh autogpt",
        "image_path": "https://gitclone.com/download1/ai-agent/AutoGPT.png"},
    {"title": "MemGPT：长记忆型AI Agent", "link": "https://github.com/letta-ai/letta",
        "description": "ai-agent.sh memgpt",
        "image_path": "https://gitclone.com/download1/ai-agent/MemGPT.png"},
    {"title": "BabyAGI：任务分解型AI Agent", "link": "https://github.com/yoheinakajima/babyagi",
        "description": "ai-agent.sh babyagi",
        "image_path": "https://gitclone.com/download1/ai-agent/BabyAGI.png"},
    {"title": "Camel：多角色扮演型AI Agent", "link": "https://github.com/camel-ai/camel",
        "description": "ai-agent.sh camel",
        "image_path": "https://gitclone.com/download1/ai-agent/Camel.png"},
    {"title": "CodeFuse：软件开发工具类AI Agent", "link": "https://github.com/codefuse-ai/codefuse-chatbot",
        "description": "ai-agent.sh codefuse\npython3 start.py",
        "image_path": "https://gitclone.com/download1/ai-agent/Codefuse.png"},
    {"title": "QAnything: 网易开源的检索增强应用", "link": "https://github.com/netease-youdao/QAnything",
        "description": "ai-agent.sh qanything",
        "image_path": "https://gitclone.com/download1/ai-agent/QAnything.png"},
    {"title": "crewAI：多角色协同AI Agent应用", "link": "https://github.com/crewAIInc/crewAI", 
        "description": "ai-agent.sh crewai",
        "image_path": "https://gitclone.com/download1/ai-agent/crewAI.png"},
    {"title": "Autogen：微软开源的开发类AI Agent", "link": "https://github.com/microsoft/autogen",
        "description": "ai-agent.sh autogen",
        "image_path": "https://gitclone.com/download1/ai-agent/Autogen.png"},
]


def create_card(title, link, description, image_path):
    with st.container(border=True):
        st.image(image_path, use_column_width=True)
        st.markdown(f"[{title}]({link})")
        st.markdown(f"```shell\n{description}\n```")


st.set_page_config(
    page_title="AI Agent Hub",
    page_icon=" ",
    layout="centered"
)


def init_sidebar():
    st.sidebar.title('AI Agent hub')
    st.sidebar.divider()
    st.sidebar.markdown("## 使用说明")
    st.sidebar.markdown("### 安装ai-agent工具")
    st.sidebar.markdown(
        "curl -o install.sh https://aliendao.cn/ai-agent/install.sh && bash install.sh")
    st.sidebar.markdown(
        "```shell\n以上命令会自动安装podman\n和ai-agent.sh脚本\n目前只支持Linux\n```")
    st.sidebar.markdown("### 运行AI Agent")
    st.sidebar.markdown("```shell\n命令：ai-agent.sh 镜像名 端口\n端口：非必填，默认为8501\n```")
    st.sidebar.markdown(
        "![](https://gitclone.com/download1/ai-agent/agent-hub.gif)")
    st.sidebar.markdown(f'''
        <a href={'https://github.com/git-cloner/ai-agent'}>源码</a>
        ''',
        unsafe_allow_html=True)
    st.markdown(
        """  
        <style>  
        .st-emotion-cache-1huvf7z {display: none;}  
        .st-emotion-cache-w3nhqi {display: none;} 
        .st-emotion-cache-13ln4jf {padding:3rem}
        .st-emotion-cache-kgpedg  {display: none;}
        .stApp {  
            max-width: 1200px;
            margin: 0 auto;
            min-width: 1000px;
        }
        </style>  
        """,
        unsafe_allow_html=True
    )


def init_agents():
    for i in range(0, len(card_data), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(card_data):
                with cols[j]:
                    card = card_data[i + j]
                    create_card(card['title'], card['link'], card['description'],
                                card['image_path'])


if __name__ == '__main__':
    init_sidebar()
    init_agents()
