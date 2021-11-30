import pygame
import os

# 화면 사이즈 설정
SCREEN_SIZE = (960, 640)
SCREEN = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

# 화면을 초당 몇 번 출력하는가, 화면 FPS 설정
CLOCK = pygame.time.Clock()

# 파일 경로
DIR_PATH = os.path.dirname(__file__)
DIR_IMAGE = os.path.join(DIR_PATH, 'image')
DIR_SOUND = os.path.join(DIR_PATH, 'sound')
DIR_FONT = os.path.join(DIR_PATH, 'font')

# 속도와 질량 기본 값
VELOCITY = 7
MASS = 2


# 버튼 클래스
class Button:
    def __init__(self, image, x, y, w, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.rect = pygame.Rect(x, y, w, h)
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            SCREEN.blit(image, (x, y))
        else:
            SCREEN.blit(image, (x, y))


# 스프라이트 시트 클래스
class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position):
        super(AnimatedSprite, self).__init__()

        # 이미지를 Rect 안에 넣기 위해 Rect 크기 지정
        size = (200, 200)

        # 여러 장의 이미지를 리스트로 저장한다
        images = []

        # 달리기 0 ~ 3
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'run1.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'run2.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'run3.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'run4.png')))

        # 점프 4 ~ 9
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'jump1.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'jump2.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'jump3.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'jump4.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'jump5.png')))
        images.append(pygame.image.load(os.path.join(DIR_IMAGE, 'jump6.png')))

        # rect 만들기
        self.rect = pygame.Rect(position, size)

        # rect 크기와 Image 크기 맞추기
        self.images = [pygame.transform.scale(image, size) for image in images]

        # 캐릭터의 현재 상태
        # 0 - run 상태, 1 - jump 상태
        self.state = 0
        # 속도
        self.velocity_x = 4

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(100 / len(self.images * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0

        self.v = VELOCITY  # 속도
        self.m = MASS  # 질량


    def update(self, mt):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.

        # 현재 상태에 따라 반복해줄 이미지의 index 설정과 속도
        if self.state == 0:
            count = 4
            start_index = 0
        elif self.state == 1:
            count = 6
            start_index = 4


        # loop 시간 더하기
        self.current_time += mt

        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # 상태에 따라 이미지 index 범위를 다르게 설정한다.
            # run 상태는 0 ~ 3, jump 상태는 4 ~ 9
            self.index = (self.index % count) + start_index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        # 좌우 위치값 변경, 이동
        # self.rect.x += self.velocity_x

