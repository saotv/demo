import streamlit as st
from streamlit import cli as stcli
import sys
import subprocess

# 设置页面标题
st.title('欢迎来到游戏中心')

# 创建侧边栏选择器来选择不同的游戏
st.sidebar.title('游戏选择')
page = st.sidebar.radio("请选择一个游戏：", ['猜数字游戏', '游戏2', '游戏3'])

# 根据选择的页面，运行对应的游戏
if page == '猜数字游戏':
    # 运行game1.py
    if st.button('开始猜数字游戏'):
        subprocess.run(['streamlit', 'run', 'game1.py'])
elif page == '游戏2':
    st.write('这里将会是游戏2的内容。')
elif page == '游戏3':
    st.write('这里将会是游戏3的内容。')