import random

class SmartOddEven:
    def __init__(self):
        self.user_history = []

    def predict_user(self):
        # 유저가 많이 낸 숫자 패턴 분석
        if not self.user_history:
            return random.randint(0, 5)

        avg = sum(self.user_history) / len(self.user_history)

        # 평균 기반 예측 (심리전)
        if avg > 2.5:
            return random.randint(3, 5)
        else:
            return random.randint(0, 2)

    def computer_move(self, guess):  
        predicted = self.predict_user()

        # 컴퓨터는 무조건 이기려고 계산
        for num in range(6):
            total = num + predicted
            if (total % 2 == 0 and guess == "짝") or \
               (total % 2 == 1 and guess == "홀"):
                return num

        return random.randint(0, 5)

    def play(self):
        print("🎮 고급 홀짝 게임 시작!")

        for round in range(5):
            print(f"\n--- Round {round+1} ---")

            user_num = int(input("숫자 선택 (0~5): "))
            guess = input("홀 or 짝: ")

            comp_num = self.computer_move(guess)

            self.user_history.append(user_num)

            total = user_num + comp_num

            print(f"너: {user_num}, 컴퓨터: {comp_num}, 합: {total}")

            if (total % 2 == 0 and guess == "짝") or \
               (total % 2 == 1 and guess == "홀"):
                print("🔥 승리!")
            else:
                print("💀 패배...")


# 실행
game = SmartOddEven()
game.play()