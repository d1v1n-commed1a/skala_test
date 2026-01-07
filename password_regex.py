import re #re는 파이썬의 정규표현식으로 문자열 처리 도구

def validate_password(password):#새롭게 함수 정의, 관리 용이
    # 비밀번호 조건 정의
    if len(password) < 8:
        return "비밀번호는 최소 8자 이상이어야 합니다."

    if not re.search(r"[a-z]", password): #r은 raw string(원시 문자열) 을 의미, /를 해석하지 않도록 함.
        return "비밀번호는 최소 한 개의 영문 소문자를 포함해야 합니다."

    if not re.search(r"[A-Z]", password):
        return "비밀번호는 최소 한 개의 영문 대문자를 포함해야 합니다."

    if not re.search(r"[0-9]", password):
        return "비밀번호는 최소 한 개의 숫자를 포함해야 합니다."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "비밀번호는 최소 한 개의 특수문자(!@#$%^&*(),.?\":{}|<>)를 포함해야 합니다."

    return "비밀번호가 유효합니다."

# 사용자 입력 받기
password = input("비밀번호를 입력하세요: ")
result = validate_password(password)
print(result)
