def equation_maker(gradient,xpoint,ypoint):
    y_inter = ypoint - gradient * xpoint
    r_y_inter = round(y_inter)
    
    if r_y_inter < 0:
        equation = "y" + "=" + str(gradient) + "x" + str(r_y_inter)
    elif r_y_inter == 0:
        equation = "y" + "=" + str(gradient) + "x"
    else:
        equation = "y" + "=" + str(gradient) + "x" + "+" + str(r_y_inter)
            
    print("")
    print(equation)

def another_equation():
    print("")
    confirm_another = input("Would you like to make another equation?: ").lower()
    print("")
    if confirm_another == "yes":
        main()

def main():
    print("Welcome! Enter a point and a gradient, and I'll make the straight line equation. i will automatically round up the numbers")
    print("")
    gradient = int(input("Enter gradient: "))
    
    print("")
    xpoint = int(input("Enter x-coordinate: "))
    ypoint = int(input("Enter y-coordinate: "))
    
    equation_maker(gradient,xpoint,ypoint)
    another_equation()
    
main()

#y = mx + c
#mx + c = y
#c = y - mx