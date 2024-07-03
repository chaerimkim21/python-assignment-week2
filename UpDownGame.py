import random

min_try_cnt = 0
play_again = True
def generate_rand_num():
    return random.randint(1,100)

while play_again:
    num = generate_rand_num()
    guess = 0
    try_cnt = 0

    while guess != num:
        try:
            guess = int(input('1에서 100사이의 정수를 입력하세요: '))

            if guess < num:
                print('up')
                try_cnt += 1
            elif guess > num:
                print('down')
                try_cnt += 1
            else:
                print(f'정답! 숫자는 {num}입니다. {try_cnt}번 만에 성공했습니다.')
                # 최고 시도 횟수 갱신
                if try_cnt < min_try_cnt or min_try_cnt == 0:
                    min_try_cnt = try_cnt

                restart = input('게임을 재시작하시겠습니까? (y/n)').strip().lower()

                if restart == 'y':
                    try_cnt = 0
                    print(f'이전 게임 플레이어 최고 시도 횟수: {min_try_cnt}')
                    break
                elif restart == 'n':
                    print('게임을 종료합니다')
                    play_again = False
                    break
                else:
                    print('올바른 형식의 입력값이 아닙니다. 게임을 종료합니다.')
                    play_again = False
                    break
        except ValueError:
            print('유효한 범위 내의 정수를 입력하세요')