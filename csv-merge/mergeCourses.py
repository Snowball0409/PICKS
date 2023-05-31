import os
import pandas as pd

# 指定資料夾路徑
folder_path = 'csv-merge/course'

# 取得資料夾列表
folder_list = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]



for i in range(len(folder_list)):
    # 建立一個空的 DataFrame 來存放結果
    result_df = pd.DataFrame()
    # 開啟當學期的資料夾
    path = "csv-merge/course/"+folder_list[i]
    # 讀取資料夾中的 Excel 檔案
    for filename in os.listdir(path):
        if filename.endswith('.xlsx') or filename.endswith('.xls'):  # 確認副檔名為 .xlsx 或 .xls
            file_path = os.path.join(path, filename)
            df = pd.read_excel(file_path)
            df['學期'] = folder_list[i]  # 新增學期的欄位
            result_df = pd.concat([result_df, df], ignore_index=True)
    # 匯出結果為 CSV 檔案
    #print(result_df.head(3))
    output_path = 'csv-merge/output/'+folder_list[i]+'.csv'
    result_df.to_csv(output_path, index=False, encoding='utf-8')
