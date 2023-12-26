import os
import glob
import whisper

def find_mp3_files(root_path):
    mp3_files = []
    # 주어진 경로 아래의 모든 하위 디렉토리를 탐색
    for root, dirs, files in os.walk(root_path):
        for file in files:
            # .mp3 파일을 찾음
            if file.endswith(".mp3"):
                full_path = os.path.join(root, file)
                mp3_files.append(full_path)
    return mp3_files

def transcribe_audio(file_path):
    # 모델 로드 (예: 'base' 모델 사용)
    model = whisper.load_model("base")

    # 오디오 파일에서 텍스트 추출
    result = model.transcribe(file_path, language='ko')

    # 추출된 텍스트 반환
    return result['segments']

output_file = "../../datasets/voice2text.txt"  # 텍스트를 추가할 파일 경로

# 사용 예시
root_path = "../../datasets/audios"  # 오디오 파일 경로
mp3_files = find_mp3_files(root_path)

# 찾은 mp3 파일들의 경로를 출력
for file in mp3_files:
    print(file)
    segments = transcribe_audio(file)
    with open(output_file, 'a', encoding='utf-8') as f:  # 파일을 append 모드로 열기
        for segment in segments:
            text = segment['text']
            f.write(text + "\n")  # 변환된 텍스트를 파일에 추가