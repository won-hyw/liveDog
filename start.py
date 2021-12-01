# [Python pygame] Live Dog : 리브도그
# 실행 파일 start.py
import sys
from datafile import *
import pygame.mixer
from game_info import Info
import pyautogui

# 메인 클래스
class Main:
    def __init__(self):
        # 초기화
        pygame.init()

        # window 타이틀 설정
        title = "리브도그"
        pygame.display.set_caption(title)

        # window 아이콘 설정
        icon = pygame.image.load("image/dog_icon.png")
        pygame.display.set_icon(icon)

        # pygame screen 설정
        self.screen_scaled = pygame.Surface((SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] / 4))

        # 게임 시작 화면
        self.background = pygame.image.load(os.path.join(DIR_IMAGE, 'background.gif'))
        self.button_image = pygame.image.load(os.path.join(DIR_IMAGE,'game_start_button.png'))

        # 배경음 실행
        pygame.mixer.music.load(os.path.join(DIR_SOUND, 'happiness.wav'))
        pygame.mixer.music.play(loops=-1)

        # 게임 실행
        self.run()

    def run(self):
        # 이벤트 루프
        running = True
        while running:  # 게임이 진행 중인가?
            cursor = pyautogui.position() # 마우스 커서 좌표 가져오기
            SCREEN.blit(self.background, (0, 0))  # 배경화면 설정
            start_button = Button(self.button_image, 345, 445, 275, 154)
            pygame.display.update()
            CLOCK.tick(15)
            for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
                if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        esc_alert = pyautogui.confirm(text='정말로 종료하시겠습니까?', title='경고', buttons=['확인', '취소'])
                        if esc_alert == '확인':
                            running = False
                if event.type == pygame.MOUSEBUTTONDOWN: # 버튼이 눌리면 화면 전환
                    if 825 < cursor[0] < 1095 and 685 < cursor[1] < 775: # 커서의 좌표를 이용, 버튼 위치의 좌표 값 안에 커서가 있는가?
                        Info()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Main()
