from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 웹 드라이버 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 웹 페이지 열기
driver.get("https://chzzk.naver.com/live/8a59b34b46271960c1bf172bb0fac758")

# 페이지가 완전히 로드될 때까지 기다리기
time.sleep(5)  # 5초 대기, 필요에 따라 조정 가능

idx = 1
pre_text = ''
while True:
    print(idx)
    # 특정 요소 찾기
    try:
        element = driver.find_element(By.CSS_SELECTOR,
                                      f'#layout-body > section > aside > div.live_chatting_list_container__vwsbZ > div > div:nth-child({idx}) > div > button > span.live_chatting_message_text__DyleH')
        new_text = element.text
        if new_text != pre_text:
            print(idx, new_text)  # 요소의 텍스트 출력
            pre_text = new_text
            if idx < 200:
                idx += 1
    except:
        continue

# 웹 드라이버 종료
driver.quit()

