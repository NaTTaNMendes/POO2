import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Initialize Pygame
pygame.init()
size = (800, 600)
pygame.display.set_mode(size, DOUBLEBUF | OPENGL)

# Initialize GLUT
glutInit()

# Set up OpenGL perspective projection
glMatrixMode(GL_PROJECTION)
gluPerspective(70, size[0]/size[1], 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

# Set up cube vertices and edges
vertices = [(1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
            (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)]

edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3),
         (2, 7), (3, 6), (4, 6), (4, 5), (5, 7), (6, 7)]

# Define a function to draw the cube


def draw_cube(angle):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    glRotate(angle[0], 1, 0, 0)  # Rotate around X axis
    glRotate(angle[1], 0, 1, 0)  # Rotate around Y axis
    for i, vertex in enumerate(vertices):
        glBegin(GL_LINES)
        for edge in edges:
            if i in edge:
                glVertex3fv(vertices[edge[0]])
                glVertex3fv(vertices[edge[1]])
        glEnd()
        glRasterPos3f(*vertex)
        for c in str(i):
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))
    pygame.display.flip()


# Main game loop
angle = [0, 0]  # Initial rotation angles
clock = pygame.time.Clock()
done = False
rotate = False  # Flag to indicate if cube is being rotated
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button pressed
                rotate = True
                pygame.mouse.get_rel()  # Reset relative mouse movement
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                rotate = False

    # Update cube angle based on mouse movement
    if rotate:
        mouse_rel = pygame.mouse.get_rel()
        angle[0] += mouse_rel[1] * 0.1  # Update rotation around X axis
        angle[1] += mouse_rel[0] * 0.1  # Update rotation around Y axis

    draw_cube(angle)
    clock.tick(60)

pygame.quit()