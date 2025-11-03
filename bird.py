from pickle import FRAME

from pico2d import load_image, get_time
import random
import game_world
import game_framework
from state_machine import StateMachine

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

# Bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH  = 20.0
FLY_SPEED_MPM   = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS   = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS   = (FLY_SPEED_MPS * PIXEL_PER_METER)

class Bird:
    def __init__(self, boundary_left = 100, boundary_right = 1500):

        self.frames = 15
        # self.x, self.y = 400, 90
        self.x, self.y = random.randrange(100,700), random.randrange(200,300)
        # self.frame = 0
        self.frame = random.randrange(0, 4)
        self.face_dir = 1
        self.dir = 1
        self.image = load_image('bird_animation.png')

        self.boundary_left, self.boundary_right = boundary_left, boundary_right

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frames

        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x > self.boundary_right:
            self.x = self.boundary_right
            self.dir = self.face_dir = -1
        elif self.x < self.boundary_left:
            self.x = self.boundary_left
            self.dir = self.face_dir = 1
        pass


    def draw(self):
        if self.face_dir == 1:  # 오른쪽
            self.image.clip_draw((int(self.frame) % 5) * 183, (int(self.frame) // 5) * 168,
                                 180, 167, self.x, self.y)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 183, (int(self.frame) // 5) * 168,
                                            180, 167, 0, 'h', self.x, self.y, 180, 167)
        pass


