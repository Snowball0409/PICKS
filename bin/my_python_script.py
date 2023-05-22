import sys

# 接收父程式傳遞的輸入參數
user_input = sys.argv[1] if len(sys.argv) > 1 else None

# 在腳本中使用輸入參數進行處理
if user_input:
    result = user_input.upper()
else:
    result = "沒有收到輸入參數"

# 將結果輸出到控制台
print(result)