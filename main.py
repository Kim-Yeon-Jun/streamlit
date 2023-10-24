import streamlit as st

import pandas as pd
from io import BytesIO

st.title("st.title(문자열): 제목")
st.header("st.header(문자열): 헤더")
st.subheader("st.subheader(문자열): 서브헤더")
st.text("st.text(문자열): 일반 텍스트입니다.")

st.text("st.code(code): 파이썬 코드 표시")
code = '''
def hello():
    print("Hello, Streamlit!!")
'''
st.code(code)

st.markdown('스트림릿에서 **마크다운**을 사용할 수 있습니다.:sunglasses:')

st.title("스트림릿의 버튼 입력 사용 예")

clicked = st.button('버튼1')
st.write('버튼 1 클릭 상태:', clicked)

if clicked:
    st.write('버튼 1을 클릭했습니다.')
else:
    st.write('버튼 1을 클릭하지 않았습니다.')


st.title("스트림릿의 체크박스 사용 예")

checked1 = st.checkbox('체크박스1')
st.write('체크박스 1 상태', checked1)

if checked1:
    st.write('체크박스 1을 체크했습니다.')
else:
    st.write('체크박스 1을 체그하지 않았습니다.')
    
