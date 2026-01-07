# 사용자가 입력을 반복적으로 받아 출력하는 프로그램

def main():
    while True:  # 무한 루프 시작
        user_input = input("문장을 입력하세요 (!quit 입력 시 종료): ")

        if user_input == "!quit":  # 종료 조건 확인
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break  # 루프 종료 → 프로그램 종료

        print("입력하신 문장은:", user_input)

if __name__ == "__main__":
    main()
