import mysql.connector

# 連接到 MySQL 資料庫
cnx = mysql.connector.connect(
    host="hellomysql20230529.mysql.database.azure.com",
    user="zing",
    password="Ab123456789",
    database="test0529"
)

# 建立游標
cursor = cnx.cursor()

# 清單包含的課程名稱
course_list = ["心理學", "社會學"]

# 執行查詢
query = "SELECT * FROM test0529.`1111` WHERE 中文課程名稱 IN (%s)"
placeholders = ', '.join(['%s'] * len(course_list))
query = query % placeholders
cursor.execute(query, course_list)

# 取得結果
results = cursor.fetchall()

# 輸出結果
for row in results:
    print(row)

# 關閉連線
cursor.close()
cnx.close()
