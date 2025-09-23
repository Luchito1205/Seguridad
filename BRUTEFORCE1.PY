import time
import turtle

alfa = "abcdefghijklmnñopqrstuvwxyz"
alfa += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfa += "1234567890"
alfa += "!@#$%^&*()_+-=[]|;:',.<>?/"

contra = "abcd"
inten1 = 0

tiempo_inicio = time.time()

screen = turtle.Screen()
screen.title("Gráfico de líneas parabólica: Fuerza Bruta")
screen.setup(width=900, height=700) 
screen.tracer(0)

axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)

line = turtle.Turtle()
line.hideturtle()
line.speed(0)
line.width(4)        
line.pencolor("blue") 
line.penup()

PLOT_WIDTH = 700
PLOT_HEIGHT = 500  
PLOT_X0 = -PLOT_WIDTH / 2
PLOT_Y0 = -300

alfa_len = len(alfa)
total_combinations = 0
for l in range(1, 5):
    total_combinations += alfa_len ** l

def map_x(attempts):
    return PLOT_X0 + (attempts / total_combinations) * PLOT_WIDTH

def map_y(progress_frac):

    return PLOT_Y0 + (progress_frac**2) * (PLOT_HEIGHT * 2)

axis.penup()
axis.goto(PLOT_X0, PLOT_Y0)
axis.pendown()
axis.forward(PLOT_WIDTH)
axis.penup()
axis.goto(PLOT_X0, PLOT_Y0)
axis.pendown()
axis.left(90)
axis.forward(PLOT_HEIGHT)
axis.right(90)
axis.penup()

line.goto(PLOT_X0, PLOT_Y0)
line.pendown()

UPDATE_EVERY = 5000

for largo in range(1, 5):
    index = [0] * largo
    while True:
        inten = "".join(alfa[i] for i in index)
        inten1 += 1
        frac = inten1 / total_combinations

        if inten1 % UPDATE_EVERY == 0:
            x = map_x(inten1)
            y = map_y(frac)
            line.goto(x, y)
            screen.update()

        if inten == contra:
            tiempo_termina = time.time()
            x = map_x(inten1)
            y = map_y(frac)
            line.goto(x, y)
            screen.update()
            print("Contraseña encontrada:", inten)
            print("Número de intentos:", inten1)
            print("Tiempo de ejecución:", tiempo_termina - tiempo_inicio, "segundos")
            time.sleep(3)
            turtle.bye()
            exit()

        for i in range(largo - 1, -1, -1):
            if index[i] + 1 < len(alfa):
                index[i] += 1
                break
            else:
                index[i] = 0
        else:
            break


