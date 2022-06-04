from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy as np

aspecto = 1.0
CamX = 4.0
CamY = 4.0
CamZ = 3.0
RotatAnguloX = 0.0
RotatAnguloY = 0.0
RotatAnguloZ = 0.0

GIRO = 90/180*math.pi

MRZ_h = [math.cos(GIRO), -math.sin(GIRO), 0], [math.sin(GIRO), math.cos(GIRO), 0], [0,0,1]
MRZ_a = [math.cos(-GIRO), -math.sin(-GIRO), 0], [math.sin(-GIRO), math.cos(-GIRO), 0], [0,0,1]
MRX_h = [1,0,0],[0, math.cos(GIRO), -math.sin(GIRO)], [0, math.sin(GIRO), math.cos(GIRO)]
MRX_a = [1,0,0],[0, math.cos(-GIRO), -math.sin(-GIRO)], [0, math.sin(-GIRO), math.cos(-GIRO)]
MRY_h = [math.cos(GIRO), 0, -math.sin(GIRO)], [0,1,0], [math.sin(GIRO), 0, math.cos(GIRO)]
MRY_a = [math.cos(-GIRO), 0, -math.sin(-GIRO)], [0,1,0], [math.sin(-GIRO), 0, math.cos(-GIRO)]

cubos =  [[1,1,-1],[0,1,-1],[0,0,-1],[1,0,-1],\
         [1,1,-1],[1,1,0], [0,1,0], [0,1,-1],\
         [1,1,0], [1,0,0], [1,0,-1],[1,1,-1],\
         [1,1,0], [0,1,0], [0,0,0], [1,0,0], \
         [0,0,0], [0,0,-1],[1,0,-1],[1,0,0], \
         [0,1,0], [0,1,-1],[0,0,-1],[0,0,0]],\
        [[-1,1,-1],[0,1,-1],[0,0,-1],[-1,0,-1],\
         [-1,1,-1],[-1,1,0],[0,1,0],[0,1,-1],\
         [-1,1,0],[-1,0,0],[-1,0,-1],[-1,1,-1],\
         [-1,1,0],[0,1,0],[0,0,0],[-1,0,0],\
         [0,0,0],[0,0,-1],[-1,0,-1],[-1,0,0],\
         [0,1,0],[0,1,-1],[0,0,-1],[0,0,0]],\
        [[-1,-1,-1],[0,-1,-1],[0,0,-1],[-1,0,-1], \
         [-1,-1,-1],[-1,-1,0],[0,-1,0],[0,-1,-1], \
         [-1,-1,0],[-1,0,0],[-1,0,-1],[-1,-1,-1], \
         [-1,-1,0],[0,-1,0],[0,0,0],[-1,0,0], \
         [0,0,0],[0,0,-1],[-1,0,-1],[-1,0,0], \
         [0,-1,0],[0,-1,-1],[0,0,-1],[0,0,0]],\
        [[1,-1,-1],[0,-1,-1],[0,0,-1],[1,0,-1], \
         [1,-1,-1],[1,-1,0],[0,-1,0],[0,-1,-1], \
         [1,-1,0],[1,0,0],[1,0,-1],[1,-1,-1], \
         [1,-1,0],[0,-1,0],[0,0,0],[1,0,0], \
         [0,0,0],[0,0,-1],[1,0,-1],[1,0,0], \
         [0,-1,0],[0,-1,-1],[0,0,-1],[0,0,0]],\
        [[1,1,1],[0,1,1],[0,0,1],[1,0,1], \
         [1,1,1],[1,1,0],[0,1,0],[0,1,1], \
         [1,1,0],[1,0,0],[1,0,1],[1,1,1], \
         [1,1,0],[0,1,0],[0,0,0],[1,0,0], \
         [0,0,0],[0,0,1],[1,0,1],[1,0,0], \
         [0,1,0],[0,1,1],[0,0,1],[0,0,0]],\
        [[-1,1,1],[0,1,1],[0,0,1],[-1,0,1], \
         [-1,1,1],[-1,1,0],[0,1,0],[0,1,1], \
         [-1,1,0],[-1,0,0],[-1,0,1],[-1,1,1], \
         [-1,1,0],[0,1,0],[0,0,0],[-1,0,0], \
         [0,0,0],[0,0,1],[-1,0,1],[-1,0,0], \
         [0,1,0],[0,1,1],[0,0,1],[0,0,0]],\
        [[-1,-1,1],[0,-1,1],[0,0,1],[-1,0,1], \
         [-1,-1,1],[-1,-1,0],[0,-1,0],[0,-1,1], \
         [-1,-1,0],[-1,0,0],[-1,0,1],[-1,-1,1], \
         [-1,-1,0],[0,-1,0],[0,0,0],[-1,0,0], \
         [0,0,0],[0,0,1],[-1,0,1],[-1,0,0], \
         [0,-1,0],[0,-1,1],[0,0,1],[0,0,0]],\
        [[1,-1,1],[0,-1,1],[0,0,1],[1,0,1], \
         [1,-1,1],[1,-1,0],[0,-1,0],[0,-1,1], \
         [1,-1,0],[1,0,0],[1,0,1],[1,-1,1], \
         [1,-1,0],[0,-1,0],[0,0,0],[1,0,0], \
         [0,0,0],[0,0,1],[1,0,1],[1,0,0], \
         [0,-1,0],[0,-1,1],[0,0,1],[0,0,0]]
Cubos = np.array(cubos)

Faces = [[1,1,1], [-1,1,1], [-1,-1,1], [1,-1,1]], \
        [ [1,1,-1], [-1,1,-1], [-1,-1,-1], [1,-1,-1]],\
        [[1,1,-1], [1,-1,-1], [1,1,1], [1,-1,1]],\
        [[-1,1,-1], [-1,-1,-1], [-1,1,1], [-1,-1,1]],\
        [[1,1,-1], [-1,1,-1], [1,1,1], [-1,1,1]],\
        [[-1,-1,-1], [1,-1,-1], [-1,-1,1], [1,-1,1]]
faces = np.array(Faces)

def gera_plano():
    glBegin (GL_LINES)
    #eixo X
    glColor3f ( 0.0, 0.0, 0.0)
    glVertex3f(-20.0, 0.0, 0.0)
    glColor3f ( 1.0, 0.0, 0.0)
    glVertex3f( 20.0, 0.0, 0.0)
    #eixo Y
    glColor3f (0.0, 0.0, 0.0)
    glVertex3f(0.0,-20.0, 0.0)
    glColor3f (0.0, 1.0, 0.0)
    glVertex3f(0.0, 20.0, 0.0)
    #eixo Z
    glColor3f (0.0,  0.0, 0.0)
    glVertex3f(0.0,  0.0,-20.0)
    glColor3f (0.0,  0.0, 1.0)
    glVertex3f(0.0,  0.0, 20.0)
    glEnd ()
def gera_cubo():
    
    glPushMatrix()
    cubos.cubo1()
    glPopMatrix()
    
    glPushMatrix()
    cubos.cubo2()
    glPopMatrix()
    
    glPushMatrix()
    cubos.cubo3()
    glPopMatrix()
    
    glPushMatrix()
    cubos.cubo4()
    glPopMatrix()
    
    glPushMatrix()
    cubos.cubo5()
    glPopMatrix()
    
    glPushMatrix()
    cubos.cubo6()
    glPopMatrix()
    
    glPushMatrix()
    cubos.cubo7()
    glPopMatrix()
    
    glPushMatrix()
    cubos.cubo8()
    glPopMatrix()  
    
class cubos(): 
    def cubo1():
        glBegin(GL_POLYGON)
        glColor(1,0.5,0)
        for i in range(0, 4):
            glVertex3d(Cubos[0][i][0], Cubos[0][i][1], Cubos[0][i][2])
        glEnd()

        glBegin(GL_POLYGON)
        glColor(0,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[0][i][0], Cubos[0][i][1], Cubos[0][i][2])
        glEnd()

        glBegin(GL_POLYGON)
        glColor(1,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[0][i][0], Cubos[0][i][1], Cubos[0][i][2])
        glEnd()

        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[0][i][0], Cubos[0][i][1], Cubos[0][i][2])
        glEnd()

        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[0][i][0], Cubos[0][i][1], Cubos[0][i][2])
        glEnd()

        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[0][i][0], Cubos[0][i][1], Cubos[0][i][2])
        glEnd()  
    def cubo2():
        glBegin(GL_POLYGON)
        glColor(1,0.5,0)
        for i in range(0, 4):
            glVertex3d(Cubos[1][i][0], Cubos[1][i][1], Cubos[1][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(0,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[1][i][0], Cubos[1][i][1], Cubos[1][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(0,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[1][i][0], Cubos[1][i][1], Cubos[1][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[1][i][0], Cubos[1][i][1], Cubos[1][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[1][i][0], Cubos[1][i][1], Cubos[1][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[1][i][0], Cubos[1][i][1], Cubos[1][i][2])
        glEnd()  
    def cubo3():
        glBegin(GL_POLYGON)
        glColor(1,0.5,0)
        for i in range(0, 4):
            glVertex3d(Cubos[2][i][0], Cubos[2][i][1], Cubos[2][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[2][i][0], Cubos[2][i][1], Cubos[2][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(0,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[2][i][0], Cubos[2][i][1], Cubos[2][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[2][i][0], Cubos[2][i][1], Cubos[2][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[2][i][0], Cubos[2][i][1], Cubos[2][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[2][i][0], Cubos[2][i][1], Cubos[2][i][2])
        glEnd()  
    def cubo4():
        glBegin(GL_POLYGON)
        glColor(1,0.5,0)
        for i in range(0, 4):
            glVertex3d(Cubos[3][i][0], Cubos[3][i][1], Cubos[3][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[3][i][0], Cubos[3][i][1], Cubos[3][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[3][i][0], Cubos[3][i][1], Cubos[3][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[3][i][0], Cubos[3][i][1], Cubos[3][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[3][i][0], Cubos[3][i][1], Cubos[3][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[3][i][0], Cubos[3][i][1], Cubos[3][i][2])
        glEnd()   
    def cubo5():
        glBegin(GL_POLYGON)
        glColor(1,0,0)
        for i in range(0, 4):
            glVertex3d(Cubos[4][i][0], Cubos[4][i][1], Cubos[4][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(0,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[4][i][0], Cubos[4][i][1], Cubos[4][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[4][i][0], Cubos[4][i][1], Cubos[4][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[4][i][0], Cubos[4][i][1], Cubos[4][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[4][i][0], Cubos[4][i][1], Cubos[4][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[4][i][0], Cubos[4][i][1], Cubos[4][i][2])
        glEnd()    
    def cubo6():
        glBegin(GL_POLYGON)
        glColor(1,0,0)
        for i in range(0, 4):
            glVertex3d(Cubos[5][i][0], Cubos[5][i][1], Cubos[5][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(0,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[5][i][0], Cubos[5][i][1], Cubos[5][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(0,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[5][i][0], Cubos[5][i][1], Cubos[5][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[5][i][0], Cubos[5][i][1], Cubos[5][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[5][i][0], Cubos[5][i][1], Cubos[5][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[5][i][0], Cubos[5][i][1], Cubos[5][i][2])
        glEnd()  
    def cubo7():
        glBegin(GL_POLYGON)
        glColor(1,0,0)
        for i in range(0, 4):
            glVertex3d(Cubos[6][i][0], Cubos[6][i][1], Cubos[6][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[6][i][0], Cubos[6][i][1], Cubos[6][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(0,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[6][i][0], Cubos[6][i][1], Cubos[6][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[6][i][0], Cubos[6][i][1], Cubos[6][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[6][i][0], Cubos[6][i][1], Cubos[6][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[6][i][0], Cubos[6][i][1], Cubos[6][i][2])
        glEnd()  
    def cubo8():
        glBegin(GL_POLYGON)
        glColor(1,0,0)
        for i in range(0, 4):
            glVertex3d(Cubos[7][i][0], Cubos[7][i][1], Cubos[7][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,0)
        for i in range(4, 8):
            glVertex3d(Cubos[7][i][0], Cubos[7][i][1], Cubos[7][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,0,1)
        for i in range(8, 12):
            glVertex3d(Cubos[7][i][0], Cubos[7][i][1], Cubos[7][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        glColor(1,1,1)
        for i in range(12, 16):
            glVertex3d(Cubos[7][i][0], Cubos[7][i][1], Cubos[7][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(16, 20):
            glVertex3d(Cubos[7][i][0], Cubos[7][i][1], Cubos[7][i][2])
        glEnd()
        
        glBegin(GL_POLYGON)
        for i in range(20, 24):
            glVertex3d(Cubos[7][i][0], Cubos[7][i][1], Cubos[7][i][2])
        glEnd()

def rotaciona(lista, F):
    for i in lista:
            Cubos[i] = np.round(np.dot(Cubos[i], F))

def localiza(ponto, face):
    teste = 0
    for i in range(0,3):
        if(ponto[i] == face[i]):
            teste += 1
    if(teste == 3):
        return True
    
def keyboard (key, posX, posY):
    global RotatAnguloX, RotatAnguloY, RotatAnguloZ
    
    if (key == b'X'):
        RotatAnguloX += 1.0
    elif(key == b'x'):
            RotatAnguloX -= 1.0
    elif(key == b'Y'):
            RotatAnguloY += 1.0
    elif(key == b'c'):
            RotatAnguloY -= 1.0
    elif(key == b'C'):
            RotatAnguloZ += 1.0
    elif(key == b'z'):
            RotatAnguloZ -= 1.0 
    elif(key == b'q' or key == b'w'):
        lista = [] 
        for i in range(0,8):
            for j in range(0,4):
                if(localiza(Cubos[i][0], faces[0][j]) == True):
                    lista.append(i)
        if(key == b'q'):
            rotaciona(lista, MRZ_h)
        elif(key == b'w'):
            rotaciona(lista, MRZ_a)
    elif(key == b'a' or key == b's'):
        lista = [] 
        for i in range(0,8):
            for j in range(0,4):
                if(localiza(Cubos[i][0], faces[1][j]) == True):
                    lista.append(i)
        if(key == b'a'):
            rotaciona(lista, MRZ_h)
        elif(key == b's'):
            rotaciona(lista, MRZ_a)
            
    elif(key == b'e' or key == b'd'):
        lista = [] 
        for i in range(0,8):
            for j in range(0,4):
                if(localiza(Cubos[i][0], faces[2][j]) == True):
                    lista.append(i)
        if(key == b'e'):
            rotaciona(lista, MRX_h)
        elif(key == b'd'):
            rotaciona(lista, MRX_a)
            
    elif(key == b'r' or key == b'f'):
        lista = [] 
        for i in range(0,8):
            for j in range(0,4):
                if(localiza(Cubos[i][0], faces[3][j]) == True):
                    lista.append(i)
        if(key == b'r'):
            rotaciona(lista, MRX_h)
        elif(key == b'f'):
            rotaciona(lista, MRX_a)
            
    elif(key == b't' or key == b'g'):
        lista = [] 
        for i in range(0,8):
            for j in range(0,4):
                if(localiza(Cubos[i][0], faces[4][j]) == True):
                    lista.append(i)
        if(key == b't'):
            rotaciona(lista, MRY_h)
        elif(key == b'g'):
            rotaciona(lista, MRY_a)
    elif(key == b'y' or key == b'h'):
        lista = [] 
        for i in range(0,8):
            for j in range(0,4):
                if(localiza(Cubos[i][0], faces[5][j]) == True):
                    lista.append(i)
        if(key == b'y'):
            rotaciona(lista, MRY_h)
        elif(key == b'h'):
            rotaciona(lista, MRY_a)     
    key1 = str(key)
    print("Tecla Pressionada:", key1[2])
    glutPostRedisplay()

def draw ():
    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    confCamera()
    
    glRotatef(RotatAnguloX, 1, 0, 0)
    glRotatef(RotatAnguloY, 0, 1, 0)
    glRotatef(RotatAnguloZ, 0, 0, 1)

    gera_plano()
    gera_cubo()
    glFlush ()
  
def confCamera ():
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective (45.0, aspecto , 0.1, 100)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity ()
    gluLookAt (CamX,CamY,CamZ, 0,0,0, 0,0,1)
  
def main():
    glutInit()
    glutCreateWindow('Alan Marinho')
    glutInitWindowSize(1000, 1000)
    glClearColor (0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()