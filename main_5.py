
OPENAI_API_KEY = "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"
from langchain_openai import ChatOpenAI
import streamlit as st

chat_model = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo")

st.title('AI 작사가')

content = st.text_input('작사할 주제를 제시해주세요.')
if st.button('작사 요청하기'):
    if content=="노래":
        content="노래가 주제야. 노래"
    result = chat_model.invoke(content + "에 대한 노래의 작사를 해 줘")
    st.write(result.content)


