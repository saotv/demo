# # main.py
# import streamlit as st
# import page1
# import page2
# import page3

# # 首页布局
# st.title('多页面 Streamlit 应用')
# st.write('请选择一个页面：')

# # 创建一个字典，将按钮标签映射到相应的页面模块
# pages = {
#     "页面 1": page1,
#     "页面 2": page2,
#     "页面 3": page3
# }

# # 为每个页面创建按钮，并使用回调函数切换页面
# for page_name, page_module in pages.items():
#     if st.button(page_name):
#         # 调用与按钮关联的页面模块的run函数
#         page_module.run()

import streamlit as st
import random

def run():
    st.title('猜数字游戏')
    st.write('我想了一个1到100之间的数字，你能猜到是多少吗？')

    # 在session state中存储数字，如果还没有生成数字的话
    if 'number' not in st.session_state:
        st.session_state['number'] = random.randint(1, 100)
    if 'guesses' not in st.session_state:
        st.session_state['guesses'] = []

    # 创建一个表单，用户可以在其中输入他们的猜测
    with st.form("my_form"):
        user_guess = st.number_input('输入你的猜测', min_value=1, max_value=100, value=50)
        submitted = st.form_submit_button("猜！")

    if submitted:
        st.session_state.guesses.append(user_guess)
        if user_guess < st.session_state.number:
            st.error('太小了！再试一次。')
        elif user_guess > st.session_state.number:
            st.error('太大了！再试一次。')
        else:
            st.success(f'恭喜你！答案就是 {st.session_state.number}。')
            st.session_state.number = random.randint(1, 100)  # 重新生成数字
            st.session_state.guesses = []  # 清空猜测历史

    # 显示用户之前的所有猜测
    if st.session_state.guesses:
        st.write('你的猜测历史：', st.session_state.guesses)