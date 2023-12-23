import os
import googleapiclient.discovery
from tqdm import tqdm

# YouTube Data API 키 설정
os.environ["GOOGLE_API_KEY"] = "AIzaSyAHwXvG1HeV7JTNzrcQ2h2JtIW8Gnqoxkc"

# YouTube Data API 클라이언트 생성
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=os.environ["GOOGLE_API_KEY"])

# 채널 ID 설정
channel_id = "UCpJw2H9KKqwCCGQKRh1Bf2w"  # 대상 채널의 ID로 바꾸세요

# 채널의 모든 동영상 ID를 가져오기
video_links = []
next_page_token = None

while True:
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=50,  # 한 페이지에 최대 50개의 동영상 검색 결과를 가져옵니다.
        pageToken=next_page_token
    )
    response = request.execute()
    for item in response.get("items", []):
        if item["id"]["kind"] == "youtube#video":
            video_links.append(f"https://www.youtube.com/watch?v={item['id']['videoId']}")

    next_page_token = response.get("nextPageToken")
    print(next_page_token)
    if not next_page_token:
        break

# 채널의 모든 동영상을 다운로드
from pytube import YouTube

for link in tqdm(video_links):
    yt = YouTube(link)
    video_length = yt.length
    if video_length < 120:      # shorts
        continue
    print(link)
    print("Downloading:", yt.title)
    yt.streams.filter(res='720p', file_extension='mp4').first().download()