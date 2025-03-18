from openai import OpenAI

# Replace 'your-api-key-here' with your actual OpenAI API key
client = OpenAI(api_key='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')

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "write me a 50-word essay"}
    ],
    temperature=1,
    max_tokens=1576,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response from the assistant
print(response.choices[0].message.content)