from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import threading
import time

chat_queue = []

def wrtn_crawl(url):
    # 웹 드라이버 초기화
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 웹 페이지 열기
    driver.get(url)

    # 페이지가 완전히 로드될 때까지 기다리기
    time.sleep(5)

    # login button
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#__main > div.sc-e417efbe-0.chBXqr > div:nth-child(1) > div.sc-7821c8fa-1.sc-e417efbe-6.oZhIg.iWuXIE > div.sc-7821c8fa-1.sc-e417efbe-12.oZhIg.kzAsHV > div'))
        )
        login_button.click()
    except Exception as e:
        print("Error:", e)

    # 이메일 필드 찾기 및 입력
    email_element = driver.find_element(By.CSS_SELECTOR, '#email')
    email_element.send_keys('ttd8591@gmail.com')  # 실제 이메일 주소로 변경

    # 비밀번호 필드 찾기 및 입력
    password_element = driver.find_element(By.CSS_SELECTOR, '#password')
    password_element.send_keys('Psj0207@')  # 실제 비밀번호로 변경

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.CSS_SELECTOR,
                                       'body > main > div > div > div > div > div > div.flex.flex-col.gap-\\[56px\\] > form > div.flex.flex-col.justify-center.w-full.gap-4 > button')
    login_button.click()

    time.sleep(5)

    idx = 1
    get_output_able = False
    while True:
        try:
            # 요소 검색
            element = driver.find_element(By.CSS_SELECTOR,
                                          '#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-dUYLmH.gzAnjS > div > div > button > svg > path')

            if len(chat_queue) > 0:
                chat = 'Input: ['
                for c in chat_queue[:5]:
                    chat += f'\"{c}\", '
                chat += ']'

                print(chat)
                chat_queue.clear()

                # 메시지 필드 찾기 및 입력
                message_element = driver.find_element(By.CSS_SELECTOR,
                                                      '#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-dUYLmH.gzAnjS > div > textarea')
                message_element.send_keys(chat)  # 원하는 메시지로 변경

                # 모드 버튼 클릭
                mode_button = driver.find_element(By.CSS_SELECTOR,
                                                  '#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-dUYLmH.gzAnjS > div > div > div > div:nth-child(2)')
                mode_button.click()

                # 전송 버튼 클릭
                send_button = driver.find_element(By.CSS_SELECTOR,
                                                  '#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-dUYLmH.gzAnjS > div > div > button')
                send_button.click()
                idx += 2
                get_output_able = True

            while get_output_able:
                try:
                    # 요소 검색
                    element = driver.find_element(By.CSS_SELECTOR,
                                                  '#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-dUYLmH.gzAnjS > div > div > button > svg > path')

                    try:
                        output1 = driver.find_element(By.CSS_SELECTOR,
                                                      f'#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-eqUAAy.sc-fyVfxW.hgevtQ.cYVeog > div:nth-child({idx}) > div > div > div.sc-epqpcT.PxJqo > div > div > p:nth-child(1)')
                        output2 = driver.find_element(By.CSS_SELECTOR,
                                                      f'#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-eqUAAy.sc-fyVfxW.hgevtQ.cYVeog > div:nth-child({idx}) > div > div > div.sc-epqpcT.PxJqo > div > div > p:nth-child(2)')
                        output3 = driver.find_element(By.CSS_SELECTOR,
                                                      f'#__main > main > div > div.sc-eqUAAy.sc-eZYNyq.hgevtQ.ecpiaE > div.sc-eqUAAy.sc-bddgXz.hgevtQ.fkDTor > div.sc-eqUAAy.sc-fyVfxW.hgevtQ.cYVeog > div:nth-child({idx}) > div > div > div.sc-epqpcT.PxJqo > div > div > p:nth-child(3)')


                        if len(output1.text) > 0:
                            print(output2.text)
                            print(output3.text)

                            get_output_able = False
                            break

                    except NoSuchElementException:
                        continue
                except NoSuchElementException:
                    continue

        except NoSuchElementException:
            continue
    # 웹 드라이버 종료
    driver.quit()

def streaming_crawl(url):
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
            element = driver.find_element(By.CSS_SELECTOR,
                                          f'#layout-body > section > aside > div.live_chatting_list_container__vwsbZ > div > div:nth-child({idx}) > div > button > span.live_chatting_message_text__DyleH')
        except:
            try:
                element = driver.find_element(By.CSS_SELECTOR,
                                              f'#layout-body > section > aside > div.live_chatting_list_container__vwsbZ > div > div:nth-child({idx}) > div > em')
            except:
                try:
                    element = driver.find_element(By.CSS_SELECTOR,
                                                  f'#layout-body > section > aside > div.live_chatting_list_container__vwsbZ > div > div:nth-child({idx}) > div > div > p')
                except:
                    continue

        new_text = element.text
        if new_text != pre_text:
            chat_queue.append(new_text)
            pre_text = new_text

        if idx < 200:
            idx += 1

    # 웹 드라이버 종료
    driver.quit()

# 각 URL에 대해 별도의 스레드 생성 및 시작
threads = []

thread = threading.Thread(target=wrtn_crawl, args=('https://wrtn.ai/store/details/chatbot/658ac57f0b975aea2d3859e3',))
thread.start()
threads.append(thread)

thread = threading.Thread(target=streaming_crawl, args=('https://chzzk.naver.com/live/19e3b97ca1bca954d1ac84cf6862e0dc',))
thread.start()
threads.append(thread)

# 모든 스레드가 종료될 때까지 기다림
for thread in threads:
    thread.join()
