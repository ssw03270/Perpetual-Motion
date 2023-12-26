from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import re

def sanitize_filename(name):
    # 윈도우 시스템에서 유효하지 않은 문자를 제거하거나 대체
    return re.sub(r'[<>:"/\\|?*]', '', name)

def create_owner_directory(owner_name):
    # 경로 생성 (여기서는 datasets/owner_name)
    path = os.path.join('..', '..', 'datasets', 'videos', owner_name)

    # 해당 경로에 디렉토리가 존재하지 않는 경우 새로 생성
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

    # 경로 생성 (여기서는 datasets/owner_name)
    path = os.path.join('..', '..', 'datasets', 'audios', owner_name)

    # 해당 경로에 디렉토리가 존재하지 않는 경우 새로 생성
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")


def download_audio_from_youtube(url, output_path=""):
    # YouTube 객체 생성
    yt = YouTube(url)

    # 비디오의 제목을 가져옵니다 (파일 이름으로 사용)
    title = sanitize_filename(yt.title)

    # 가장 높은 해상도의 스트림을 선택
    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # 비디오 다운로드
    video_stream.download(output_path=output_path, filename=title + '.mp4')

    # 다운로드된 비디오 파일 경로
    video_path = f"{output_path}/{title}.mp4"

    # 비디오 파일에서 오디오 추출
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(f"{output_path.replace('videos', 'audios')}/{title}.mp3")

    # 사용한 자원 해제
    video_clip.close()
    audio_clip.close()

# YouTube 채널의 모든 비디오에 대해 위의 함수를 반복 실행
def download_channel_videos(channel_url):
    # 플레이리스트 URL을 이용해 Playlist 객체 생성
    playlist = Playlist(channel_url)
    owner = playlist.owner
    create_owner_directory(owner)

    for video_url in playlist.video_urls:
        print(f"Downloading and extracting audio from {video_url}")
        download_audio_from_youtube(video_url, output_path=f'../../datasets/videos/{owner}/')

# 여기에 YouTube 채널 URL을 입력하세요
channel_url = "https://youtube.com/playlist?list=PLfKOmegfviFpEttWXWhDibMIVCHEQga1e&si=erLmAERIBAurTzng"
download_channel_videos(channel_url)
