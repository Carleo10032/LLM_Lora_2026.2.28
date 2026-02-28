from openai import OpenAI

client = OpenAI(
    base_url='https://ms-ens-f7b6721b-eaf8.api-inference.modelscope.cn/v1',
    api_key='ms-xxxxxxxx',#这里需要填写我的魔搭api，如果需要请联系我
)

messages = [
    {
        'role': 'system',
        'content': 'You are a helpful assistant.'
    }
]

while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit']:
        break
    
    messages.append({
        'role': 'user',
        'content': user_input
    })
    
    response = client.chat.completions.create(
        model='lqw1203/private_model_06B',
        messages=messages,
        stream=True
    )
    
    print('Assistant: ', end='', flush=True)
    assistant_response = ''
    for chunk in response:
        if chunk.choices:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end='', flush=True)
                assistant_response += content
    print()
    
    messages.append({
        'role': 'assistant',
        'content': assistant_response
    })
