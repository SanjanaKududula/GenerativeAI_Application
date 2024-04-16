from openai import OpenAI
import streamlit as st


f = open("Keys/.Openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

############################
st.title("🔎An AI Code Reviewer")

############################

prompt = st.text_area("Enter your code here..", height=200)

if st.button("generate") == True:

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a helpfull assistent.
                                             Please analyze the code and identify potential bugs, errors, or areas of improvement and 
                                             also provide the fixed code snippets """},
            { "role":"user","content":prompt}
        ]
    )

    st.write(response.choices[0].message.content)