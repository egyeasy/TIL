# 30분 뒤에 알려주는 앱

from time import sleep

def finish():
    sleep(5) # 초 단위로 인자 설정
    print("수업 종료되었습니다.")

print("수업중")
finish()
print("땡땡땡")