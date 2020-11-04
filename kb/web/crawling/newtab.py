from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://google.com')
time.sleep(1)

driver.execute_script('window.open("https://naver.com");') #자바스크스크립트 실행
time.sleep(1)

driver.switch_to_window(driver.window_handles[0])
time.sleep(1)

driver.close()

print(driver.window_handles)

