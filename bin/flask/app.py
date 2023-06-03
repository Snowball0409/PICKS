from flask import Flask, request, jsonify
import openai
import re
import sys

app = Flask(__name__)
keyfile = open("key/openaiKey.txt", "r")
key = keyfile.readline()
openai.api_key = key

def skills(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": f"我想學習{user_input}，我可以在大學上什麼課"}
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    # 從回應中提取技能
    # 從response提取數字加句點開頭並以冒號結尾的課程名稱到gptclass
    pattern = "\d+\.\s*(.*?)："
    gptclass = re.findall(pattern, result)
    
    return gptclass

@app.route('/process', methods=['POST'])
def process():
    # 接收 HttpRequest 請求的字串輸入
    user_input = request.get_data(as_text=True)
    response = ""
    # 處理字串
    for i in range(5,-1,-1):
        if i == 0:
            response = "五次請求失敗"
            break
        result = skills(user_input)
        response = jsonify(result)
        if response:
            break

    # 回傳
    return response

if __name__ == '__main__':
    app.run()