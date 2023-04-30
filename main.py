import openai

openai.api_key = ""
with open('data.txt') as f:
    lines = f.readlines()
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "user", "content": f"Виведи на екран статистику по кількості слів, речень та іменованих сутностей у тексті:'{lines}'"}
    ]
    )
    print(completion.choices[0].message.content)
