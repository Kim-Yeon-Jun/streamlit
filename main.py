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


# st.title("스트림릿의 다운로드 버튼 사용 예")
# st.subheader("텍스트 파일 다운로드 예제")

# folder='C:/Users/com/Desktop/'

# with open(folder + "UNIV.txt", encoding='utf-8') as text_file:
#     text_data = text_file.read()
#     st.download_button(
#         label = "텍스트 파일 다운로드",
#         data = text_data,
#         file_name = "UNIV.txt"
#     )

# st.subheader("이미지 파일 다운로드 예제")

# with open(folder + "kfc.jpg") as image_file:
#     st.download_button(
#         label = "이미지 파일 다운로드",
#         data = image_file,
#         file_name = "sample_image.png",
#         mime="image/png"
#     )
    
# st.subheader("오디오 파일 다운로드 예제")

# with open(folder + "audio.mp3", 'rb') as audio_file:
#     st.download_button(
#         label = "오디오 파일 다운로드",
#         data = audio_file,
#         file_name = "오디오 파일 예제.mp3",
#         mime = "audio/mpeg"
#     )
    

st.title("스트림릿의 체크박스 사용 예")

checked1 = st.checkbox('체크박스1')
st.write('체크박스 1 상태', checked1)

if checked1:
    st.write('체크박스 1을 체크했습니다.')
else:
    st.write('체크박스 1을 체그하지 않았습니다.')
    

st.title("라디오 버튼")

radio1_options = ['10','20','30','40','50']
radio1_selected = st.radio('(5 x 5 + 5)은 얼마인가요?', radio1_options)
st.write('**선택한 답**', radio1_selected)

radio2_options = ('마라톤', '축구', '수영', '승마')
radio2_selected = st.radio('당신이 좋아하는 운동은?', radio2_options, index=2, horizontal=True)
st.write('**당신의 선택**', radio2_selected)

