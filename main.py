# main.py
import streamlit as st
import page1
import page2
import page3

# 首页布局
st.title('多页面 Streamlit 应用')
st.write('请选择一个页面：')

# 创建一个字典，将按钮标签映射到相应的页面模块
pages = {
    "页面 1": page1,
    "页面 2": page2,
    "页面 3": page3
}

# 为每个页面创建按钮，并使用回调函数切换页面
for page_name, page_module in pages.items():
    if st.button(page_name):
        # 调用与按钮关联的页面模块的run函数
        page_module.run()