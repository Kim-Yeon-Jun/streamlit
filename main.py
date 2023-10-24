import streamlit as st

import pandas as pd
from io import BytesIO
from io import StringIO
from PIL import Image

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
radio1_selected = st.radio('(5 x 5 + 5)은 얼마인가요?', radio1_options) #질문, 선택 옵션 - 선택한 값이 변수에 저장됨
st.write('**선택한 답**', radio1_selected)
if radio1_selected == '30':
    st.write('정답입니다!')
else:
    st.write("틀렸습니다.ㅠㅠ")
    
radio2_options = ('마라톤', '축구', '수영', '승마')
radio2_selected = st.radio('당신이 좋아하는 운동은?', radio2_options, index=2, horizontal=True)
st.write('**당신의 선택**', radio2_selected)

st.title("셀렉트 박스")

selectbox1_options = ['하이든', '모차르트', '베토벤', '슈만']
your_option1 = st.selectbox('좋아하는 음악가는?', selectbox1_options)
st.write('**당신의 선택**', your_option1)


st.sidebar.title("텍스트 입력")
user_id = st.sidebar.text_input('아이디(ID) 입력', value="streamlit", max_chars=15) #value : 입력 창 초기에 보이는 문자열. 지정하지 않으면 빈칸으로 출력
user_password = st.sidebar.text_input('비밀번호(PW) 입력', value="abcd", type="password")

if user_id == "streamlit":
    if user_password == "1234":
        st.sidebar.write('로그인 됐습니다. 서비스를 이용할 수 있습니다.')
    else:
        st.sidebar.write('잘못된 패스워드 입니다. 다시 입력해주세요')
else:
    st.sidebar.write('없는 ID입니다. 회원가입 혹은 올바른 ID를 입력해주세요')
    
st.title("스트림릿의 파일 업로더 사용 예")

uploaded_file = st.file_uploader("Text 파일을 선택하세요.", type="txt")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data[:100])
    
uploaded_file = st.file_uploader("MP3 파일을 선택하세요.", type="mp3")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data[:100])
    
# st.title("스트림릿의 이미지 표시 사용 예")
# st.subheader("1. 깃허브에서 이미지 파일 표시")
# image_file='https://github.com/Kim-Yeon-Jun/streamlit/blob/main/goldwhi.jpg'
# image_local = Image.open(image_file)
# st.image(image_local, width=350, caption = "금휘사진")

st.subheader("웹 상에 있는 이미지 표시")
image_url = "https://gifsf.com/files/attach/images/19406/502/179/006/5920acdeb6cbe0e79e9acc44c5938474.jpg"
st.image(image_url, width=350, caption="웹 상에 있는 이미지")

st.title("스트림릿에서 화면 분할 사용 예")
[col1, col2] = st.columns(2)
with col1:
    st.subheader("유튜브 비디오1")
    url_col1 = "https://www.youtube.com/watch?v=P9S53OUJHn8&ab_channel=%EA%B8%88%ED%9C%98"
    st.video(url_col1)
with col2:
    st.subheader("유튜브 비디오2")
    url_col2 = "https://www.youtube.com/watch?v=CDBuALLcAI8&t=335s&ab_channel=%EA%B8%88%ED%9C%98"
    st.video(url_col2)

#배열과 for문을 사용하여 1줄을 여러개로 분할하여 사용하는 것도 가능함.

st.title("세션 상태 사용 예")

if 'count' not in st.session_state:
    st.session_state['count'] = 0

if 'registered' not in st.session_state:
    st.session_state['registered'] = []

user_input = st.text_input('이름', value = "이름을 입력하세요.", key='name')

clicked = st.button('등록')

if clicked:
    st.session_state['count'] = st.session_state['count'] + 1
    st.write("버튼 입력 회수:", st.session_state['count'])
    
    name = st.session_state['name']
    st.session_state['registered'].append(name)
    st.write("등록 이름 리스트:", st.session_state['registered'])
    
st.title("콜백 함수 사용 예제")

if 'lang' not in st.session_state:
    st.session_state['lang'] = '영어'

def button_callback(sel_lang):
    st.session_state['lang'] = sel_lang

radio_options = ['영어', '프랑스어', '독일어']
radio_selected = st.radio('한국어를 어떤 언어로 번역하겠습니까?', radio_options)

clicked_lang = st.button('선택', on_click=button_callback, args=[radio_selected])

st.write(f"한국어를 {st.session_state['lang']}로 번역하는 것을 선택했습니다.")
