# -*- coding: utf-8 -*-
import openai
import re
import sys

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


# 接收父程式傳遞的輸入參數
user_input = sys.argv[1] if len(sys.argv) > 1 else None

if user_input:
    retry  =  5
    while retry > -1:
        result = skills(user_input)
        if result:
            # 將結果輸出到控制台
            print(result)
            break
        if retry ==  0:
            print("五次請求失敗")
            break
        else: 
            retry -= 1
            #print("retry") #測試用
else:
    result = "沒有收到輸入參數"