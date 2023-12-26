from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time

def crawl_page(url):
    # 웹 드라이버 초기화
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 웹 페이지 열기
    driver.get(url)

    # 페이지가 완전히 로드될 때까지 기다리기
    time.sleep(5)

    idx = 1
    pre_text = ''
    while True:
        time.sleep(0.1)
        try:
            # CSS 선택자를 사용하여 특정 요소 찾기
            element = driver.find_element(By.CSS_SELECTOR, f'#layout-body > section > aside > div.live_chatting_list_container__vwsbZ > div > div:nth-child({idx}) > div > button > span.live_chatting_message_text__DyleH')
        except:
            try:
                element = driver.find_element(By.CSS_SELECTOR, f'#layout-body > section > aside > div.live_chatting_list_container__vwsbZ > div > div:nth-child({idx}) > div > em')
            except:
                try:
                    element = driver.find_element(By.CSS_SELECTOR, f'#layout-body > section > aside > div.live_chatting_list_container__vwsbZ > div > div:nth-child({idx}) > div > div > p')
                except:
                    continue

        output_file = "../../datasets/chatting.txt"  # 텍스트를 추가할 파일 경로

        new_text = element.text
        if new_text != pre_text:
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(new_text + '\n')
            pre_text = new_text

        if idx < 200:
            idx += 1

    # 웹 드라이버 종료
    driver.quit()

# 크롤링할 웹 페이지 URL 리스트
urls = [
    "https://chzzk.naver.com/live/75cbf189b3bb8f9f687d2aca0d0a382b",
    "https://chzzk.naver.com/live/7ce8032370ac5121dcabce7bad375ced",
    "https://chzzk.naver.com/live/dec8d19f0bc4be90a4e8b5d57df9c071",
    "https://chzzk.naver.com/live/1c231568d0b13de5703b3f6a5e86dc47",
    "https://chzzk.naver.com/live/0dad8baf12a436f722faa8e5001c5011"

]

# 각 URL에 대해 별도의 스레드 생성 및 시작
threads = []
for url in urls:
    thread = threading.Thread(target=crawl_page, args=(url,))
    thread.start()
    threads.append(thread)

# 모든 스레드가 종료될 때까지 기다림
for thread in threads:
    thread.join()
