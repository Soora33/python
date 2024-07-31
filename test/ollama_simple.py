import ollama

# 流式输出
def api_generate(text:str):
    print(f'提问：{text}')

    stream = ollama.generate(
        stream=True,
        model='llama3-cn:latest',
        prompt=text,
    )

    print('-----------------------------------------')
    for chunk in stream:
        if not chunk['done']:
            print(chunk['response'], end='', flush=True)
        else:
            print('\n')
            print('-----------------------------------------')
            print('-----------------------------------------')


if __name__ == '__main__':
    str = '如何评价特朗普'
    # 流式输出
    api_generate(str)

    # 非流式输出
    # content = ollama.generate(model='llama3-cn:latest', prompt='天空为什么是蓝色的？')
    # print(content)