import matplotlib.pyplot as plt

x_axis = [-3,-2,-1,0,1,2,3]
y_axis = []
  
def plotter(x_axis,y_axis,gradient,y_inter):
    line_name = "gradient = " + str(gradient) + "," + " y-intercept = " + str(y_inter)
    plt.plot(x_axis,y_axis, label = line_name)
    plt.title('yes')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    
def equation(x_axis,gradient,y_inter):
    for x in x_axis:
        y = gradient * x + y_inter
        y_axis.append(y)

def another_line(y_axis):
    confirm_another = input("Would you like to plot another line?: ").lower()
    print("")
    if confirm_another == "yes":
        y_axis.clear()
        main()
    else:
        plt.show()
        
def main():
    print("Welcome to the Line Plotter!")
    print("")
    gradient = int(input("Enter gradient: "))
    y_inter = int(input("Enter y-intercept: "))
    
    equation(x_axis,gradient,y_inter)
    plotter(x_axis,y_axis,gradient,y_inter)
    another_line(y_axis)
    
main()