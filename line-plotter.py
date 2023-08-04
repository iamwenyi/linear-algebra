import matplotlib.pyplot as plt

x_axis = [-3,-2,-1,0,1,2,3]
y_axis = []

def plotter(x_axis,y_axis):
    plt.plot(x_axis,y_axis)
    plt.title('yes')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
def equation(x_axis,gradient,y_inter):
    for x in x_axis:
        y = gradient * x + y_inter
        y_axis.append(y)
    
def main():
    print("Welcome to the Line Plotter!")
    print("")
    gradient = int(input("Enter gradient: "))
    y_inter = int(input("Enter y-intercept: "))
    
    equation(x_axis,gradient,y_inter)
    plotter(x_axis,y_axis)
    
main()