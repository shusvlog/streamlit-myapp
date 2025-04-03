import streamlit as st
import time

st.title('Streamlit ころものアプリ')

st.write('Progress bar')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteratiion {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

    'Done!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問問い合わせ')
expander.write('お問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの好きな趣味は、', text, "です。"
# 'コンディション', condition

# if st.checkbox('Show Image'):
#     img = Image.open('./display-image.jpg')
#     st.image(img, caption="思い出", use_container_width=True)
