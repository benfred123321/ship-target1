import pgzrun
import random
import itertools

HEIGHT = 400
WIDTH = 400

BLOCK_POSITIONS = [
    (350,50),(350,350),(50,350),(50,50)
]

block_positions = itertools.cycle(BLOCK_POSITIONS)
block = Actor("block",center = (50,50))
ship = Actor("ship",center = (200,200))

def draw():
    screen.clear()
    ship.draw()
    block.draw()

def move_block():
    animate(block,"bounce_end",duration = 1,pos =next(block_positions))

move_block()
clock.schedule_interval(move_block,0.1)

def move_ship():
    x = random.randint(75,325)
    y = random.randint(75,325)
    ship.tatget =(x,y)
    target_angle = ship.angle_to(ship.target)
    target_angle += 360 * ((ship.angle - target_angle + 180) //360)
    animate(ship,tween = "accel_decel",pos = ship.target,duration = ship.distance_to(ship.target)/200,on_finished = move_ship)


pgzrun.go()