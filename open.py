from openai import OpenAI
import streamlit as st 
# from che import o

text= st.text_input("Enter your question")
ans=st.button("Check Answer")


def output(t):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
    )

    completion = client.chat.completions.create(
    extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-r1-distill-llama-70b:free",
    messages=[
    {
        "role": "user",
        "content": t
    }
    ]
    )
    return completion.choices[0].message.content

if ans:
    st.write(output(text))
    