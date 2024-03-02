import streamlit as st
import random

# 设置页面标题
st.title('猜数字游戏')

# 初始化会话状态
if 'number' not in st.session_state or 'attempts' not in st.session_state:
    st.session_state.number = random.randint(1, 100)  # 随机生成1到100之间的数字
    st.session_state.attempts = 0  # 尝试次数

# 猜数字的表单
with st.form("guess_number"):
    st.write("我想了一个1到100之间的数字，你能猜到是哪个数字吗？")
    guess = st.number_input("请输入你的猜测：", min_value=1, max_value=100, value=50, step=1)
    submitted = st.form_submit_button("猜!")

    if submitted:
        st.session_state.attempts += 1  # 用户每猜一次，尝试次数加1
        if guess < st.session_state.number:
            st.error("太小了！再试一次吧。")
        elif guess > st.session_state.number:
            st.error("太大了！再试一次吧。")
        else:
            st.success(f"恭喜你！猜对了，数字就是 {st.session_state.number}。")
            st.balloons()
            # 重置游戏
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0

# 显示尝试次数
st.write(f"你已经尝试了 {st.session_state.attempts} 次。")

# 重置游戏的按钮
if st.button("重新开始游戏"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.experimental_rerun()