import streamlit as st
from streamlit_multipage import MultiPage

# 创建一个MultiPage对象
app = MultiPage()

# 设置页面标题
st.title('欢迎来到游戏中心')

# 导入其他页面的函数
from game1 import game1_page

# 添加页面到应用
app.add_page("猜数字游戏", game1_page)

# 你可以继续添加其他游戏的页面
# from game2 import game2_page
# app.add_page("游戏2", game2_page)

# from game3 import game3_page
# app.add_page("游戏3", game3_page)

# 运行应用
app.run()