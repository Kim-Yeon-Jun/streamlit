import streamlit as st

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

