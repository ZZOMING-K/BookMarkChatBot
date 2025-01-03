import streamlit as st 
from gemini import get_conversation_chain
from langchain.memory import StreamlitChatMessageHistory
from langchain.callbacks import get_openai_callback
from dataloader import page_content 
from embeddings import text_split , vector_store
import os

GOOGLE_API_KEY = st.secrets["google"]["api_key"]
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

st.set_page_config(
    page_title="북마크 GPT",
    page_icon=":books:")

st.title("북마크 :orange[GPT] 📚")

if "conversation" not in st.session_state:
        st.session_state.conversation = None

if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

if "processComplete" not in st.session_state:
        st.session_state.processComplete = None


if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "assistant", 
                                     "content": "안녕하세요! 궁금한 것이 있으면 언제든지 물어봐주세요!"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

history = StreamlitChatMessageHistory(key="chat_messages")

# Chat logic
if user_input := st.chat_input("질문을 입력해주세요."):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)
    
     # 다른 페이지에서 저장된 URL 목록 가져오기
    if "url_list" in st.session_state:
        urls = list(st.session_state.url_list.url_title_mapping().values())
    else:
        st.warning("저장된 URL이 없습니다.")
        urls = []    
    
    #st.write(urls)

    splits = page_content(urls)
    
    chunks =  text_split(splits)
    
    vetorestore = vector_store(chunks)
    
    st.session_state.conversation = get_conversation_chain(vetorestore) 
    st.session_state.processComplete = True

    with st.chat_message("assistant"):
        chain = st.session_state.conversation

        with st.spinner("Thinking..."):
            result = chain({"question": user_input})
            with get_openai_callback() as cb:
                st.session_state.chat_history = result['chat_history']
            response = result['answer']
            source_documents = result['source_documents']
            
            st.session_state.messages.append({"role": "assistant", "content": response})

            st.markdown(response)
            with st.expander("참고 문서 확인"):
                st.markdown(source_documents[0].metadata['source'], help = source_documents[0].page_content)