import random

player_choice = ''
play_again = True
wins = 0
losses = 0
ties = 0

possible_choices = ['가위', '바위', '보']

def rock_paper_scissors():
    return random.choice(possible_choices)

while play_again:
    computer_choice = rock_paper_scissors()

    try:
        player_choice = input('가위, 바위, 보 중 하나를 선택하세요: ').strip().lower()

        if player_choice not in ['가위', '바위', '보']:
            raise ValueError('유효한 입력이 아닙니다.')

        if player_choice == computer_choice:
            print('무승부 입니다!')
            ties += 1
        elif player_choice == '가위' and computer_choice == '바위':
            print('졌습니다. 컴퓨터 승리!')
            losses += 1
        elif player_choice == '바위' and computer_choice == '보':
            print('졌습니다. 컴퓨터 승리!')
            losses += 1
        elif player_choice == '보' and computer_choice == '가위':
            print('졌습니다. 컴퓨터 승리!')
            losses += 1
        elif player_choice == '가위' and computer_choice == '보':
            print('이겼습니다. 사용자 승리!')
            wins += 1
        elif player_choice == '바위' and computer_choice == '가위':
            print('이겼습니다. 사용자 승리!')
            wins += 1
        elif player_choice == '보' and computer_choice == '바위':
            print('이겼습니다. 사용자 승리!')
            wins += 1

        restart = input('게임을 재시작하시겠습니까? (y/n)').strip().lower()
        if restart == 'y':
            continue
        elif restart == 'n':
            print('게임을 종료합니다')
            print(f'승: {wins} 패: {losses} 무승부: {ties}')
            play_again = False
        else:
            print('올바른 형식의 입력값이 아닙니다. 게임을 종료합니다.')
            print(f'승: {wins} 패: {losses} 무승부: {ties}')
            play_again = False
    except ValueError:
        print('유효한 입력이 아닙니다.')