import streamlit as st

#布局streamlit应用 布局一般放在最前面布局
# st.set_page_config(layout="wide") - 将应用的内容以宽屏模式呈现（默认情况下以一固定宽度的列的形式呈现）
# st.sidebar - 将组件/文字/图片显示在侧边栏中
# st.expander - 将组件/文字/图片显示在一个可折叠的容器中
# st.columns - 创建表格布局（或列布局）来容纳内容

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')


# st.markdown
st.markdown('Streamlit Demo')

# 设置网页标题
st.title('一个傻瓜式构建可视化 web的 Python 神器 -- streamlit')

# 展示一级标题
st.header('1. 安装')

st.text('和安装其他包一样，安装 streamlit 非常简单，一条命令即可')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')


# 展示一级标题
st.header('2. 使用')

# 展示二级标题
st.subheader('2.1 生成 Markdown 文档')

# 纯文本
st.text('导入 streamlit 后，就可以直接使用 st.markdown() 初始化')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')

#table
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(10,5),
    columns=('第%d列' % (i+1) for i in range(5))
)
st.table(df.style.highlight_max(axis=0))

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)


st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

#write 传入的df对象
df_2 = pd.DataFrame({
     "class":[0,1,2,3,4,5],
     "name":["A","B","C","D","E","F"]
})
st.write(df_2)

#write 传入matplotlib对象
import matplotlib.pyplot as plt

# 画一个折线图 当然可以用 st.line_chart
x = np.arange(10)
y = np.random.randint(0,20,10)
c = plt.figure(figsize=(8,8))
plt.plot(x,y)
st.write(c)


# st.button 按钮
st.header("st.button")

if st.button("Say Hello"):
     st.write("why hello there")
else:
     st.write("Goodbye")


# st.slider滑条组件
from datetime import time, datetime

st.header('st.slider')

# 样例 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 样例 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 样例 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# 样例 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

# st.line_chart折线图

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# selectbox 选择组件 

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option) # 使用一个变量来存储选择的内容

# multiselect 多选组件
st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

# checkbox 复选框
st.header("st.checkbox")

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

# 另外的组件 component API


# st.latex 显示数学公式

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

# 自定义streamlit主题
st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


# 存储秘密信息 st.secrets
# st.title('st.secrets')

# st.write(st.secrets['message'])

#上传文件组件 st.file_uploader
st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
  


# 进度条：st.progress
# import time
# st.title('st.progress')

# with st.expander('About this app'):
#      st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

# my_bar = st.progress(0) #定义一个进度条 默认值为0

# for percent_complete in range(100):
#      time.sleep(0.05) #一定要加这个间隔
#      my_bar.progress(percent_complete + 1)

# st.balloons() #可以播放气球动画的一个函数


# st.form 表单组件 并带有一个submit按钮
# 两种方法：
# 1、 使用with语句向表单添加对象（推荐）
# 2、 将其作为一个对象直接调用其对象的方法（将表单存储为一个变量，调用该变量的streamlit方法）

# 1 with语句
st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# 2 存储变量方法
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)


# st.experimental_get_query_params 获取用户所用链接中的查询参数 详情看官网

# st.cache 缓存机制的使用

st.title('st.cache')
from time import time
# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True) # 需要使用@st.cache放在一个函数前面来声明这个函数存入到缓存
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)


# st.session_state 会话状态
# 我们将通过一个浏览器标签页访问 Streamlit 应用定义为一个会话（Session）。每个连接至 Streamlit 服务器的标签页都将创建一个会话。每当你与应用中组件交互时，Streamlit 将从上到下地重新运行整个应用。每次重新运行都将会清空历史：没有变量将被保留下来。

# 而会话状态（Session State）是一个在同一会话的不同次重新运行间共享变量的方法。除了能够存储和保留状态，Streamlit 还提供了使用回调函数更改状态的支持。

# 在此教程中，我们将构建一个重量换算应用，并描述会话状态以及回调函数的用法。

# st.session_state 将允许我们在 Streamlit 应用中使用会话状态。

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input') 
col1, spacer, col2 = st.columns([2,1,2])  #插入布局为 side-by-side 列的容器。[2,1,2]创建三列第一列是第二列的两倍，第三列是第二列的两倍
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)      #数字输入框 st.number_input
with col2: 
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)  #数字输入框

st.header('Output')
st.write("st.session_state object:", st.session_state)



# 通过构建Bored API应用学习如何使用API

import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

#上述选择的活动类型会通过 f-字符串追加到请求链接之后，然后被用于请求 JSON 数据：
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

#以下我们将通过 st.expander 命令显示应用的说明以及获取到的 JSON 数据：
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)

#最后，我们也会显示所建议活动随附的信息，比如参与人数、活动类型与价格。
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta= '') #以大粗体显示度量，并带有一个可选的度量如何变化的指示器。
  #delta:指标如何变化的指标，在指标下方用箭头表示。如果 delta 为负数 (int/float) 或以减号 (str) 开头，则箭头指向下方且文本为红色；否则箭头指向上方，文本为绿色。如果无(默认)，则不显示增量指示器。
  #label:指标的标题或标题
  #value:指标的值。 None 被呈现为长破折号。
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta= '')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta= '')


#构建可拖拽放缩的仪表盘 streamlit Elements
# 需要安装Streamlit Elements组件到你的环境中：pip install streamlit-elements == 0.1.*
# streamlit elements repositories 的地址：https://github.com/okld/streamlit-elements#getting-started

# streamlit-shap 显示shap图表功能的组件
# 由于需要安装依赖，具体看官网展示

# 接下来是项目 零样本 zero-shot learning text classifier 锻炼一个零样本学习文本分类器




