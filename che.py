from openai import OpenAI


def output():
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
        "content": "What is solar system?"
    }
    ]
    )
    return completion.choices[0].message.content