def equation_maker(a_xpoint,a_ypoint,b_xpoint,b_ypoint):
    gradient = (b_ypoint - a_ypoint) / (b_xpoint - a_xpoint)
    y_inter = a_ypoint - gradient * a_xpoint
    r_gradient = round(gradient)
    r_y_inter = round(y_inter)
    
    if r_gradient == 0:
        equation = "y" + "=" + str(r_y_inter)
            
    elif r_gradient == 1:
        if r_y_inter < 0:
            equation = "y" + "=" + "x" + str(r_y_inter)
        else:
            equation = "y" + "=" + "x" + "+" + str(r_y_inter)
        
    else:
        if r_y_inter < 0:
            equation = "y" + "=" + str(r_gradient) + "x" + str(r_y_inter)
        elif r_y_inter == 0:
            equation = "y" + "=" + str(r_gradient) + "x"
        else:
            equation = "y" + "=" + str(r_gradient) + "x" + "+" + str(r_y_inter)
            
    print("")
    print(equation)
        
def another_equation():
    print("")
    confirm_another = input("Would you like to make another equation?: ").lower()
    print("")
    if confirm_another == "yes":
        main()

def main():
    print("Welcome! Enter two points, and I'll make the straight line equation. i will automatically round up the numbers")
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