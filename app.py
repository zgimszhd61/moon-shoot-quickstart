from openai import OpenAI
def askMoonshoot(mprompt):
    sprompt = "下面内容是粗译的结果，请整理原文并意译，使之更符合中国人阅读理解习惯，注意说人话。直接说内容，不要说其他冗余的话。"
    if 1==1:
        client = OpenAI(
            api_key = "sk-",
            base_url = "https://api.moonshot.cn/v1",
        )
        
        completion = client.chat.completions.create(
            model = "moonshot-v1-8k",
            messages = [
                {"role": "system", "content": sprompt},
                {"role": "user", "content": mprompt}
            ],
            temperature = 0.3,
        )
        result = completion.choices[0].message.content.strip()
        print(result)
        writecontent(result + "\n\n")
        return(result)
askMoonshoot("hello")
