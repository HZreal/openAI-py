import openai


openai.api_key = 'xxx'


prompt = "请编一个童话故事"
response = openai.Completion.create(
    engine="text-davinci-003",
    # engine="gpt-3.5-turbo",  # unsupported
    prompt=prompt,
    temperature=0.8,
    max_tokens=1000,
    n=1,
    stop=None,
    # timeout=20,
)

print(response.choices[0].text)
