# page1.py
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