import logging
import re
import openai
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    userInput = req.params.get('userInput')
    if not userInput:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userInput = req_body.get('userInput')

    if userInput:
        output = ""
        # 問gpt五次
        for i in range(5,-1,-1):
            if i == 0:
                output = "五次請求失敗"
                break
            openaiResponse = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a chatbot"},
                    {"role": "user", "content": f"我想學習{userInput}，我可以在大學上什麼課"}
                ]
            )
            result = ''
            for choice in openaiResponse.choices:
                result += choice.message.content
            # 提取數字加句點開頭並以冒號結尾的課程名稱到 output
            pattern = "\d+\.\s*(.*?)："
            output = re.findall(pattern, result) # 課程list
            if output:
                break
        # 包起來
        response = {
                    "Input": userInput,
                    "Output": output
                }
        return func.HttpResponse(response, mimetype="application/json")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )