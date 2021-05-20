import matplotlib.pylab as plt

def algoritDDAL(x1,y1,x2,y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)

    xinc = float(dx / steps)
    yinc = float(dy / steps)


    for i in range(0, int(steps + 1)): 
        plt.plot(round(x1),round(y1), "b.")
        x1 += xinc
        y1 += yinc

        print('(', x1, ',', y1, ')')

    plt.title('GRAFICA DDA')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(color='b',linestyle='dotted',linewidth=1)
    plt.show()

    print("Valor dx: ", dx)
    print("Valor dy: ", dy)
    print("Valor steps: ", steps)
    print("Valor xinc: ", xinc)
    print("Valor yinc: ", yinc)

def main():

    x1 = int(input("Valor de X1: "))
    y1 = int(input("Valor de y1: "))
    x2 = int(input("Valor de x2: "))
    y2 = int(input("Valor de y2: "))

    algoritDDAL(x1, y1, x2 , y2)

if __name__=='__main__':
    main()
