import re

def validate_password(password):
    if len(password) < 8:
        return "비밀번호는 최소 8자 이상이어야 합니다."
    if not re.search(r"[a-z]", password):
        return "비밀번호는 최소 한 개의 영문 소문자를 포함해야 합니다."
    if not re.search(r"[A-Z]", password):
        return "비밀번호는 최소 한 개의 영문 대문자를 포함해야 합니다."
    if not re.search(r"[0-9]", password):
        return "비밀번호는 최소 한 개의 숫자를 포함해야 합니다."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "비밀번호는 최소 한 개의 특수문자를 포함해야 합니다."
    return "비밀번호가 유효합니다."

def main():
    while True:
        pw = input("비밀번호를 입력하세요 (!quit 입력 시 종료): ")
        if pw == "!quit":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break

        print(validate_password(pw))

if __name__ == "__main__": #이 파일이 메인 프로그램으로 실행될 때만 사용자 입력을 받고 출력하는 로직을 수행하라
    main()
