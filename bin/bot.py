import openai
import re
import sys

# 設定 ChatGPT 的 API 金鑰
keyfile = open("bin/key.txt", "r")
key = keyfile.readline()
#openai.api_key = key

def query_skills(query):
    # 使用 ChatGPT 查詢技能
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"我想學習{query}，我可以在大學上什麼課？",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # 從回應中提取技能
    # 從response提取數字加句點開頭並以冒號結尾的課程名稱到gptclass
    pattern = "\d+\.\s*(.*?)："
    gptclass = re.findall(pattern, response)
    
    return gptclass

# 接收父程式傳遞的輸入參數
user_input = sys.argv[1] if len(sys.argv) > 1 else None

# 在腳本中使用輸入參數進行處理
if user_input:
    result = query_skills(user_input)
else:
    result = "沒有收到輸入參數"

# 將結果輸出到控制台
print(result)