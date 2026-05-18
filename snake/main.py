import pygame as pg
import sys
import random
import array 
import moderngl
import ctypes

class Snake:
    def __init__(self):
        self.size = 10
        self.body = [(100, 50), (90, 50), (80, 50)]  # Head at index 0
        self.direction = 'RIGHT'
        self.change_to = self.direction  # Buffer for direction changes

    def change_direction(self):
        if any((self.change_to == 'UP' and not self.direction == 'DOWN',
                self.change_to == 'DOWN' and not self.direction == 'UP',
                self.change_to == 'LEFT' and not self.direction == 'RIGHT',
                self.change_to == 'RIGHT' and not self.direction == 'LEFT')):
            self.direction = self.change_to

    def move(self):
        x, y = self.body[0]

        if self.direction == 'UP':
            y -= self.size
        elif self.direction == 'DOWN':
            y += self.size
        elif self.direction == 'LEFT':
            x -= self.size
        elif self.direction == 'RIGHT':
            x += self.size
        
        self.body = [(x, y)] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, surface):
        for segment in self.body:
            pg.draw.rect(surface, (0, 255, 0),
                            pg.Rect(segment[0], segment[1], self.size, self.size))

    def check_collision(self, width, height):
        x, y = self.body[0]
        if x < 0 or x >= width or y < 0 or y >= height:
            return True
        if (x, y) in self.body[1:]:
            return True
        else:
            return False




class Food:
    def __init__(self, width, height):
        self.size = 10

        self.position = (random.randint(0, (width - self.size) // self.size) * self.size,
                        random.randint(0, (height - self.size) // self.size) * self.size)

    def spawn(self, width, height):
        self.position = (random.randint(0, (width - self.size) // self.size) * self.size,
                        random.randint(0, (height - self.size) // self.size) * self.size)

    def draw(self, surface):
        pg.draw.rect(surface, (255, 0, 0),
                        pg.Rect(self.position[0], self.position[1], self.size, self.size))

def Quit():
    pg.quit()
    sys.exit()

pg.init()
ctypes.windll.user32.SetProcessDPIAware()
width, height = 320,180

screen = pg.surface.Surface((width, height))
REALRES = (ctypes.windll.user32.GetSystemMetrics(78), ctypes.windll.user32.GetSystemMetrics(79))
display = pg.display.set_mode(REALRES,pg.OPENGL|pg.FULLSCREEN|pg.DOUBLEBUF)
ctx = moderngl.create_context()
pg.display.set_caption("Snake Game")
clock = pg.time.Clock()

quad_buffer = ctx.buffer(data=array.array('f',[
    -1.0,1.0,
    1.0,1.0,
    -1.0,-1.0,
    1.0,-1.0,
]))

vert_shader = open("vertex.txt","r").read()
frag_shader = open("fragment.txt").read()

program = ctx.program(vertex_shader=vert_shader,fragment_shader=frag_shader)
render_object = ctx.vertex_array(program,[(quad_buffer,"2f","vert")])

def surf_to_texture(surf):
    tex = ctx.texture(surf.get_size(),4)
    tex.filter=(moderngl.NEAREST,moderngl.NEAREST)
    tex.write(pg.image.tobytes(surf,"RGBA",1))
    return tex

snake = Snake()
food = Food(width, height)

score = 0
font = pg.font.SysFont('Arial', 24)
fps=8
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake.change_to = 'UP'
            elif event.key == pg.K_DOWN:
                snake.change_to = 'DOWN'
            elif event.key == pg.K_LEFT:
                snake.change_to = 'LEFT'
            elif event.key == pg.K_RIGHT:
                snake.change_to = 'RIGHT'
            if event.key == pg.K_ESCAPE:
                Quit()
    
    if snake.body[0] == food.position:
        snake.grow()        # Make snake longer
        food.spawn(width, height)  # Move food to new position
        score += 1
        fps+=5//score+1

    snake.change_direction()
    snake.move()
    
    

    if snake.check_collision(width, height):
        if snake.body[0] in snake.body[1:]:
            pg.quit()
            sys.exit()
        else:
            snake.body[0]=(snake.body[0][0]%width,snake.body[0][1]%height)
    
    screen.fill((0, 0, 0))  # Clear screen
    food.draw(screen)       # Food draws itself
    snake.draw(screen)      # Snake draws itself
    score_text = font.render(f'Score: {score}', False, (255, 255, 255)) #draw score
    score_text.set_colorkey((0,0,0))
    screen.blit(score_text, (10, 10)) #write score to main buffer

    frame_tex = surf_to_texture(screen)
    frame_tex.repeat_x = True
    frame_tex.repeat_y = True
    frame_tex.use(0)
    program['tex'] = 0
    program['R'].value = pg.display.get_window_size()
    #program['time'].value = pg.time.get_ticks()
    render_object.render(mode=moderngl.TRIANGLE_STRIP)

    pg.display.flip()

    frame_tex.release()

    clock.tick(fps)