import streamlit as st 
from PIL import Image 

st.set_page_config(page_title = 'BookMark' , page_icon = "📌") 
st.title("북마크GPT 💬")
st.write("**그 내용이 어디있었더라...??**") 

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-WAtOwGaR-JpWDMRp27_um8BcyFfNuKTW3A&s')

st.write("\n")  # 위에 공간 추가

st.write(
    """
    사용자의 북마크 URL을 업로드하여 **북마크된 페이지를 기반으로 대화하는 GPT**입니다.  
    아래 안내를 따라 북마크 파일을 다운로드하고 업로드하세요.
    """
)
st.write("-" * 40)
#img = Image.open('https://r2.jjalbot.com/2023/03/2S-U1gPwbc.jpeg')

st.subheader("☝🏼 파일 다운로드 방법 (Chrome)")
st.write("1. Chrome에서 오른쪽 상단의 메뉴 버튼( ⋮ )을 클릭하세요.")
st.write("2. **북마크 및 목록** → **북마크 관리자**를 선택하세요.")
st.write("3. 오른쪽 상단의 메뉴 버튼( ⋮ )을 클릭한 후 **북마크 내보내기**를 선택하세요.")
st.write("4. `search bookmark` 페이지에서 다운로드한 파일을 업로드하세요.")


st.subheader("✌🏼링크 바로 추가하기 ")
st.write("`1. search bookmark` 페이지에서 추가하길 원하는 페이지 URL 입력")