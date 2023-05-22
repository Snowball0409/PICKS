from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 選擇使用的瀏覽器驅動程式，例如 Chrome 需要下載 ChromeDriver
# 設定瀏覽器驅動程式的路徑
driver_path = "path_to_driver/chromedriver"  # 替換為驅動程式的路徑

# 初始化瀏覽器驅動程式
driver = webdriver.Chrome(executable_path=driver_path)

# 前往目標網頁
url = "https://example.com"  # 替換為目標網站的 URL
driver.get(url)

# 使用 Selenium 提供的方法和選擇器進行網頁操作
# 假設要點擊一個按鈕並等待特定元素的出現
button = driver.find_element(By.XPATH, "//button[@id='my-button']")
button.click()

# 使用顯式等待等待特定元素的出現
wait = WebDriverWait(driver, 10)  # 最多等待 10 秒
element = wait.until(EC.presence_of_element_located((By.ID, "my-element")))

# 其他網頁操作和資料處理...
# 可以進行表單填寫、資料提取、截圖、模擬鍵盤操作等

# 關閉瀏覽器驅動程式
driver.quit()
