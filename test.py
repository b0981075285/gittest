import random


WELCOME_MESSAGE = "猜數字"

MAX_ATTEMPTS = 9



def play_game():
    answer = random.randint(1, 100)

    print(WELCOME_MESSAGE)
    print(" 1 到 100 。")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = int(input(f"第 {attempt} 次猜測："))

        if guess == answer:
            print("恭喜你答對了！")
            return

        if guess < answer:
            print("答案再大一點。")
        else:
            print("答案再小一點。")

    print(f"挑戰失敗，正確答案是 {answer}。")


if __name__ == "__main__":
    play_game()
