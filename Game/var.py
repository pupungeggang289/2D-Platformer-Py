screen = None
screen_size = [960, 540]
FPS = 60
clock = None

scene = 'title'
state = ''

class Font():
    title = None
    main_1 = None
    main_2 = None

class Level():
    level_list = [
        {'ID' : 0, 'name' : '1-1', 'cleared' : False, 'locked' : False, 'next_level' : [1]},
        {'ID' : 1, 'name' : '1-2', 'cleared' : False, 'locked' : True, 'next_level' : [2]},
        {'ID' : 2, 'name' : '1-3', 'cleared' : False, 'locked' : True, 'next_level' : []},
    ]

class World():
    level = -1
    field = []
    thing = []
    gravity = 400

    class Camera():
        x = 0
        y = 0

    class Player():
        x = 0
        y = 0
        speed = 160
        jump_power = 400
        jump_num = 1
