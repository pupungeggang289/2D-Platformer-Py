import pygame
import sys

import var
import asset

import title

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.screen_size)
    pygame.display.set_caption('2D-Platformer')
    var.clock = pygame.time.Clock()
    load_font()
    load_image()

def load_font():
    pygame.font.init()
    var.Font.title = pygame.font.Font('Font/neodgm.ttf', 32)
    var.Font.main_1 = pygame.font.Font('Font/neodgm.ttf', 24)
    var.Font.main_2 = pygame.font.Font('Font/neodgm.ttf', 16)

def load_image():
    pass 

def main():
    while True:
        var.clock.tick(var.FPS)
        input_handle()
        loop_scene()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def loop_scene():
    pass

init()
main()
