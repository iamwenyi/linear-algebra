def equation_maker(a_xpoint,a_ypoint,b_xpoint,b_ypoint):
    gradient = (b_ypoint - a_ypoint) / (b_xpoint - a_xpoint)
    y_inter = a_ypoint - gradient * a_xpoint
    rounded_gradient = round(gradient)
    rounded_y_inter = round(y_inter)
    
    if rounded_y_inter < 0:
        neg_equation = "y" + "=" + str(rounded_gradient) + "x" + str(rounded_y_inter)
        print("")
        print(neg_equation)
    else:
        equation = "y" + "=" + str(rounded_gradient) + "x" + "+" + str(rounded_y_inter)
        print("")
        print(equation)
        
def another_equation():
    print("")
    confirm_another = input("Would you like to plot another line?: ").lower()
    print("")
    if confirm_another == "yes":
        main()

def main():
    print("Welcome! Enter two points, and I'll make the straight line equation.")
    print("")
    print("Point A")
    a_xpoint = int(input("Enter x-coordinate: "))
    a_ypoint = int(input("Enter y-coordinate: "))
    
    print("")
    print("Point B")
    b_xpoint = int(input("Enter x-coordinate: "))
    b_ypoint = int(input("Enter y-coordinate: "))
    
    equation_maker(a_xpoint,a_ypoint,b_xpoint,b_ypoint)
    another_equation()
    
main()

#y = mx + c
#mx + c = y
#c = y - mx
