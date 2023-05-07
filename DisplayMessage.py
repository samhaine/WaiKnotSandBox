import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

font = pygame.font.SysFont('Arial', 84)
text_surface = font.render('WaiKnot is the best', True, (25, 155, 225), (22, 22, 22))
texture_data = pygame.image.tostring(text_surface, "RGBA", True)
texture = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_surface.get_width(), text_surface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

rot_y = 10000
rot_x = 88

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)

    glPushMatrix()
    glRotatef(rot_y, 0, 1, 0)
    glRotatef(rot_x, 1, 0, 0)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 0)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 0)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 0)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 0)
    glEnd()

    glPopMatrix()

    rot_y += 1
    rot_x += 0.5

    pygame.display.flip()
    pygame.time.wait(10)
