"""
- 로그 생성 -> 파일 기록
- json 형태, 텍스트(한줄에 로그기록 작성) 형태
"""

# 1. 모듈 가져오기
import datetime
import json
import os
import time

# 2. 로그가 저장되는 디렉토리 지정/생성
log_dir = './sensor_logs'
if not os.path.exists(log_dir):
  os.makedirs(log_dir)


# 3. 로그 발생 및 저장
def generate_logs():
  # 로그 샘플 (고정된 장비 1대로 지정)
  data = {
    'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'sensor_id': 'AI-FACTORY-001',
    'temperature': 87.5,
    'humidity': 42.1,
    'status': 'running',
  }

  # json 형태로 파일 기록(한줄에 로그 1개씩) -> dict 객체의 직렬화 처리
  # 파일명 ./sensor_logs/sensor_json.log
  # 한줄에 JSON 객체 1개씩 문자열로 기록 (JSON Lines : JSONL)
  jsonStr = json.dumps(data)
  with open(f"{log_dir}/sensor_json.log', 'a', encoding='UTF-8") as f:
    f.write(jsonStr + '\n')
  # 구현하시오

  # text 형태로 파일 기록(한줄에 로그 1개씩) -> f-string 구성
  # 파일명 ./sensor_logs/sensor_text.log
  text = f'[{data["timestamp"]}] ID={data["sensor_id"]} | TEMP:{data["temperature"]} | HUMI:{data["humidity"]} | STAT:{data["status"]}'
  jsonStr = json.dumps(data)
  with open(f'{log_dir}/sensor_text.log', 'a', encoding='UTF-8') as f:
    f.write(text + '\n')
    print(f'로그 발생 완료 {data["timestamp"]}')

  pass


def main():
  try:
    while True:
      generate_logs()
      time.sleep(2)
  except Exception:
    print('종료')


if __name__ == '__main__':
  print('로그 발생 시작.')
  main()
