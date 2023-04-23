import math
from fractions import Fraction
import matplotlib.pyplot as plt

# Input value

a = float(input("Enter value of x²: \n"))  # Variable "a" contain the value of x²
b = float(input("Enter value of xy: \n"))  # Variable "b" contain the value of xy
c = float(input("Enter value of y²: \n"))  # Variable "c" contain the value of y²
d = float(input("Enter value of x: \n"))  # Variable "d" contain the value of x
e = float(input("Enter value of y: \n"))  # Variable "e" contain the value of y
f = float(input("Enter value of f: \n"))  # Variable "f" contain the value of f

# Process
# Determine if input is a line
if a == 0 and b == 0 and c == 0 and d != 0 and e != 0 and f != 0:
    print("The input is a line.")
    print("Standard form of a line")
    print(d, "x + ", e, "y + ", f, " = 0 \n")

    # Transpose the value of x
    d1 = d * -1
    # Transpose the value of f
    f1 = f * -1

    # Cancel out the value of y
    y1 = e / e  # Divide the value of y  to itself
    # Cancel out the value of y
    d2 = d1 / e  # Divide the value of y  to itself
    # Cancel out the value of y
    f2 = f1 / e  # Divide the value of y  to itself
    print("Slope Intercept Form of a Line")  # print Slope Intercept Form of a Line
    print("y = ", d2, "x + ", f2)  # print the value of slope(m) and y - intercept(b)
    print("Slope = ", d2)  # print the value of slope
    print("Y-Intercept = ", f2)  # print the value of y - intercept

    plt.plot(d2, f2)  # input plot in graph
    plt.title('Graph of a line')  # title of graph
    # Plot the two points.
    plt.plot(d2, d2, 'bo')
    plt.annotate('slope', (d2, d2), color='blue')
    plt.plot(f2, f2, 'ro')
    plt.annotate('y intercept', (f2, f2), color='red')
    # Plot the line.
    plt.plot(d2, f2)
    x = [d2]
    y = [f2]
    plt.plot(d2)
    plt.plot(f2)
    # Draw the axes.
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    # Draw the grid lines.
    plt.minorticks_on()
    plt.grid(True, 'minor', markevery=2, linestyle='--')
    plt.grid(True, 'major', markevery=10)
    # show the graph
    plt.show()
    plt.show()
# Determine if input is a parabola
elif a != 0 and b == 0 and c == 0 and d != 0 and e != 0 and f != 0:
    print("The input is a parabola.")
    print("General form of Parabola.")
    print(a, "x² + ", d, "x + ", e, "y + ", f, " = 0 \n")  # print the input into general form of a parabola
    lst = "opens upward"  # when the parabola open upward
    lst2 = "opens downward"  # when the parabola open downward
    lss = "open to the right"  # when the parabola open to the right
    lss2 = "open to the left"  # when the parabola open to the left
    # Transpose the value of y and f
    y = e * -1
    f1 = f * -1

    # Divide both side by the value of x² or a
    x_squa = a / a  # x²
    x = d / a  # x
    y1 = y / a  # y
    f2 = f1 / a  # f or constant

    # this is the process of how p is obtained
    x33 = d / a
    x333 = x33 / a
    p = x333
    p2 = p / 4
    k1 = x33 / 2
    k2 = k1 * k1
    h1 = k2 * a
    c1 = f * -1
    k = k2 / k1
    k4 = k * -1  # this is the process why the focus was obtained
    # Completing the square of the left side
    x1 = x / 2  # the value of x is divided in 2
    x2 = x1 * x1  # The answer of this will we the constant of the left side

    # We will add also to the right side to make it equal
    f3 = f2 + x2
    # Factoring the Right side
    f4 = f3 / y1
    k2 = x1 * - 1
    k3 = f4 * - 1
    h2 = c1 + h1
    h3 = h2 / a
    h = h3 / p
    h4 = h * -1  # this is the process why the focus was obtained when h4 and p2 subtract
    h6 = h4 + p  # this is the process why the directrix was obtained
    p3 = 2 * p2
    h5 = h4 - p2  # directrix

    print("Standard form of the Parabola")
    print("(x + ", x1, ")² = ", y1, "(y + ", f4)  # print the input into standard form of a parabola
    print("vertex:", "h:", k2, ",", "k:", k3)  # show the vertex
    print("value of P:", p2)  # show the value of p
    if y1 >= 0.01:
        print("directrix:y =", h6)  # show the directrix
        print("focus:", k4, ",", h4 - p2)  # show the focus
        print("direction of the opening:", lst)  # show the direction of the opening
        # show the end of latus rectum
        print("ends of latus rectum:", "(", k4 + p3, ",", h4 + p2, ")", "(", k4 - p3, ",", h4 + p2, ")")
        # if the value of p is negative the direction of the opening is downward
    else:
        print("directrix:y =", h5)  # show the directrix
        print("focus:", k4, ",", h4 + p2)  # show the focus
        print("direction of the opening:", lst2)  # when the parabola open downward
        print("ends of latus rectum:")  # show the end of latus rectum
        print("(", k4 + p3, ",", h4 - p2, ")" "(", k4 - p3, ",", h4 - p2, ")")
# Determine if input is a parabola
elif a == 0 and b == 0 and c != 0 and d != 0 and e != 0 and f != 0:
    print("The input is a parabola.")
    print("General form of Parabola.")
    print(c, "y² + ", d, "x + ", e, "y + ", f, " = 0 \n")  # print the input into general form of a parabola
    lst = "opens upward"  # when the parabola open upward
    lst2 = "opens downward"  # when the parabola open downward
    lss = "open to the right"  # when the parabola open to the right
    lss2 = "open to the left"  # when the parabola open to the left
    # Transpose the value of x and f
    x = d * -1
    f1 = f * -1

    # Divide both side by the value of y² or c
    y_squa = c / c  # x²
    x1 = x / c  # y
    y = e / c  # x
    f2 = f1 / c  # f or constant
    # Completing the square of the left side
    p = x1
    y1 = y / 2
    y2 = y1 * y1  # The answer of this will we the constant of the left side
    y3 = y2 / y1
    h1 = y3 * c
    h2 = h1 + f1
    h3 = h2 / c
    h = h3 / p
    h4 = h * -1  # h
    k4 = y3 * -1  # k
    # We will add also to the right side to make it equal
    f3 = f2 + y2
    # Factoring the Right side
    f4 = f3 / x1
    p2 = p / 4
    h5 = h4 - p2  # directrix if the value of p is positive
    p3 = 2 * p2
    h6 = h4 + p2  # directrix  if the value of p is negative
    print("Standard form of the Parabola")
    print("(y + ", y1, ")² = ", x1, "(x + ", f4)  # print the input into standard form of a parabola
    print("vertex:", "h:", Fraction(h4), ",", "k:", Fraction(k4))  # show the vertex
    print("value of P:", Fraction(p2))  # show the value of p
    # if the value of p is positive the direction of the opening is to the right
    if p >= 0.01:
        # show the directrix
        print("directrix:", "( x =", Fraction(h5), ")")
        # show the focus
        print("focus:", Fraction(h4 + p2), ",", Fraction(k4))
        # show the focus
        print("direction of the opening:", lss)
        # show the end point of latus rectum
        print("end point of latus rectum")
        print("(", Fraction(h4 + p2), ",", Fraction(k4 + p3), ")", ",", "(", Fraction(h4 + p2), ",", Fraction(k4 - p3),
              ")")
        # else if the value of p is negative the direction of the opening is to the left
    else:
        # show the directrix
        print("directrix:", "( x =", Fraction(h6), ")")
        # show the focus
        print("focus:", Fraction(h4 - p2), ",", Fraction(k4))
        # show the direction of the opening
        print("direction of the opening:", lss2)
        # show the end point of latus rectum
        print("end point of latus rectum")
        print("(", Fraction(h4 - p2), ",", Fraction(k4 - p3), ")", ",", "(", Fraction(h4 - p2), ",", Fraction(k4 + p3),
              ")")
# in 3rd condition statement, here is the formula of number 3 and that is  ax² + by + d = 0

# Determine if the input is Parabola
elif a != 0 and b == 0 and c == 0 and d == 0 and e != 0 and f != 0:
    print("The input is a parabola.")
    print(a, "x² + ", e, "y + ", f, " = 0 \n")  # print the input into general form of a parabola
    lst = "opens upward",  # when the parabola open upward
    lst2 = "opens downward"  # when the parabola open downward
    lss = "open to the right"  # when the parabola open to the right
    lss2 = "open to the left"  # when the parabola open to the left
    xx_squared = a / a  # divide the value of x² to x²
    y1 = e * -1  # Transpose the value of x
    c1 = f * -1  # Transpose the value of c
    y2 = y1 / a  # divide the value of x to y²
    c2 = c1 / a  # divide the value of c to y²
    # what you will see under these are the containers these are the conditions of the placed input
    p = y2
    c = c2 / p
    c2 = c * -1
    p2 = p / 4
    p3 = 2 * p2
    print("Standard form of the Parabola")  # Print the standard form
    print("x² =", Fraction(p), "(y +", Fraction(c), ")")  # display the standard form
    print("vertex: (h: 0", "k:", Fraction(c2), ")")  # show the vertex
    print("value of p:", "(", Fraction(p2), ")")  # show the value of p
    # if the value of p is positive the direction of the opening is upwards
    if p >= 0.01:
        # show the directrix
        print("directrix: (y =", "(", Fraction(c2 + p2), ")")
        # show the focus
        print("focus:( 0 ,", Fraction(c2 - p2), ")")
        # show the direction of the opening
        print("direction of the opening:", lst)
        # show the end point of latus rectum
        print("end point of latus rectum:", "(", Fraction(0 + p3), ",", Fraction(c2 + p2), ")", ",", "(",
              Fraction(0 - p3), ",", Fraction(c2 + p2), ")")
    # else if the value of p is negative the direction of the opening is downward
    else:
        # show the directrix
        print("directrix: y =", Fraction(c2 - p2))
        # show the focus
        print("focus:( 0 ,", Fraction(c2 + p2), ")")
        # show the direction of the opening
        print("direction of the opening:", lst2)
        # show the end point of latus rectum
        print("end point of latus rectum:", "(", Fraction(0 + p3), ",", Fraction(c2 - p2), ")", ",", "(",
              Fraction(0 - p3), ",", Fraction(c2 - p2), ")")
# in 4th condition statement, here is the formula of number 4 and that is ay² + bx + d = 0

elif a == 0 and b == 0 and c != 0 and d != 0 and e == 0 and f != 0:
    print("The input is a parabola.")
    print(c, "y² + ", d, "x + ", f, " = 0 \n")  # print the input into general form of a parabola
    lst = "opens upward"  # when the parabola open upward
    lst2 = "opens downward"  # when the parabola open downward
    lss = "open to the right"  # when the parabola open to the right
    lss2 = "open to the left"  # when the parabola open to the left
    # divide the value of y² to y²
    yy_squared = c / c
    # Transpose the value of x
    x1 = d * -1
    # Transpose the value of c
    c1 = f * -1
    # divide the value of x to y²
    x2 = x1 / c
    # divide the value of c to y²
    c2 = c1 / c
    # what you will see under these are the containers these are the conditions of the placed input
    p = x2
    c = c2 / p
    c2 = f * -1
    p2 = p / 4
    p3 = 2 * p2
    # Print the standard form
    print("Standard form of the Parabola")
    print("y² =", Fraction(p), "(x +", Fraction(c), ")")
    # show the vertex
    print("vertex: (h:", Fraction(c2), ",", "k: 0)")
    # show the value of p
    print("value of p:", "(", Fraction(p2), ")")
    # if the value of p is positive the direction of the opening is to the right
    if p >= 0.01:
        # show the directrix
        print("directrix:( x =", Fraction(c2 - p2), ")")
        # show the focus
        print("focus:", Fraction(c2 + p2), ", 0")
        # show the direction of the opening
        print("direction of the opening:",
              lss)  # if the value of p is negative the direction of the opening is to the left
        # show the end point of latus rectum
        print("end point of latus rectum:")
        print("(", Fraction(c2 + p2), ",", Fraction(0 + p3), ")", ",", "(", Fraction(c2 + p2), ",", Fraction(0 - p3),
              ")")
    else:
        # show the directrix
        print("directrix:( x =", Fraction(c2 + p2), ")")
        # show the focus
        print("focus:", "(", Fraction(c2 - p2), ", 0 )")
        # show the direction of the opening
        print("direction of the opening:", lss2)
        # show the end point of latus rectum
        print("end point of latus rectum:", "(", Fraction(c2 - p2), ",", Fraction(0 + p3), ")", ",", "(",
              Fraction(c2 - p2), ",", Fraction(0 - p3), ")")
# else if, you should only choose from the formulas mentioned

# Determine if input is a hyperbola1
elif a >= .01 and b == 0 and c <= -.01 and d != 0 and e != 0 and f != 0:
    print("The input is a hyperbola.")
    print("General form of the hyperbola.")
    print(a, "x² + ", c, "y² + ", d, "x + ", e, "y + ", f, " = 0 \n")  # General form of Hyperbola
    f1 = f * -1  # Transpose the value of f
    ax = d / a  # Factor out the coefficient of x²
    cy = e / c  # Factor out the coefficient of y²

    # Completing the square of x
    # 9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    ax1 = ax / 2  # -4x/2
    ax2 = ax1 * ax1  # Then here we multiply it by itself

    # Completing the square of y
    # 9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    cy1 = cy / 2  # 2y/2
    cy2 = cy1 * cy1  # Then here we multiply it by itself

    # Right side of the hyperbola
    f2 = f1 + (a * ax2) + (c * cy2)

    # Right side of the Hyperbola to make it equal to 1
    f3 = f2 / f2  # divide the value by itself

    # Factor out the value of x² and x
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    ax3 = ax / 2

    # Factor out the value of y² and y
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    cy3 = cy / 2

    # Now we're going to get the value of a²
    a2 = f2 / a

    # Now we're going to get the value of b²
    b2 = f2 / c

    print("(x + ", ax3, ")² / ", a2, " - ", " (y + ", cy3, ")² / ", b2 * -1, " = ", f3)
    a3 = a2 ** 2  # This is the value of our a
    b3 = b2 ** 2  # This is the value of our a
    c = (a3 + b3) ** 2  # This is the value of our c
    h = ax3 * -1  # Transpose the value of h
    k = cy3 * -1  # Transpose the value of k
    print("Hyperbola with Horizontal Focal Axis")
    print("Center: (", h, ", ", k, ")")  # Here we are printing out the position of the center
    print("Vertices: ( ", h + a3, ", ", k, ") & ( ", h - a3, ", ", k,
          " )")  # Here we are printing out the position of the Vertices
    print("Foci: ( ", h + c, ", ", k, ") & ( ", h - c, ", ", k,
          " )")  # Here we are printing out the position of the Foci
    print("Endpoints of Transverse Axis: ( ", h + a3, ", ", k, ") & ( ", h - a3, ", ", k,
          " )")  # Here we are print out the E.T.A.
    print("Endpoints of Conjugate Axis: ( ", h, ", ", k + b3, ") & ( ", h, ", ", k - b3,
          " )")  # Here we are print out the E.C.A.
    print("Endpoints of Latus Rectum: ( ", h - c, ", ", k + b2 / a3, ") & ( ", h + c, ", ", k + b2 / a3,
          " )")  # Here we are print out the E.L.R.
    print("Asymptote: y = ", k, "±", a3, "/", b3, "( ", "x -", h, " )")
    print("Directrix: x = ", h, "±", a3, "/", c, ")")

# Determine if input is a hyperbola2
elif a <= -.01 and b == 0 and c >= .01 and d != 0 and e != 0 and f != 0:
    print("The input is a hyperbola.")
    print("General form of the hyperbola.")
    print(a, "x² + ", c, "y² + ", d, "x + ", e, "y + ", f, " = 0 /n")
    f1 = f * -1  # Transpose the value of f
    ax = d / a  # Factor out the coefficient of x²
    cy = e / c  # Factor out the coefficient of y²

    # Completing the square of x
    # -9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    ax1 = ax / 2  # -4x/2
    ax2 = ax1 * ax1  # Then here we multiply it by itself
    print("x =", ax2)

    # Completing the square of y
    # 9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    cy1 = cy / 2  # 2y/2
    cy2 = cy1 * cy1  # Then here we multiply it by itself
    print("y =", cy2)

    # Right side of the hyperbola
    f2 = f1 + (a * ax2) + (c * cy2)

    # Right side of the Hyperbola to make it equal to 1
    f3 = f2 / f2  # divide the value by itself

    # Factor out the value of x² and x
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    ax3 = ax / 2

    # Factor out the value of y² and y
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    cy3 = cy / 2

    # Now we're going to get the value of a²
    a2 = f2 / c

    # Now we're going to get the value of b²
    b2 = f2 / a * -1

    print("(y + ", cy3, ")² / ", a2, " - ", " (x + ", ax3, ")² / ", b2 * -1, "= ", f3)
    a3 = a2 ** 2  # This is the value of our a
    b3 = b2 ** 2  # This is the value of our a
    c = (a3 + b3) ** 2  # This is the value of our c
    h = ax3 * -1  # Transpose the value of h
    k = cy3 * -1  # Transpose the value of k
    print("Hyperbola with Horizontal Focal Axis")
    print("Center: (", k, ", ", h, ")")  # Here we are printing out the position of the center
    print("Vertices: ( ", h, ", ", k + a3, ") & ( ", h, ", ", k - a3,
          " )")  # Here we are printing out the position of the Vertices
    print("Foci: ( ", h, ", ", k + c, ") & ( ", h, ", ", k - c,
          " )")  # Here we are printing out the position of the Foci
    print("Endpoints of Transverse Axis: ( ", h, ", ", k + a3, ") & ( ", h, ", ", k - a3,
          " )")  # Here we are print out the E.T.A.
    print("Endpoints of Conjugate Axis: ( ", h + b3, ", ", k, ") & ( ", h - b3, ", ", k,
          " )")  # Here we are print out the E.C.A.
    print("Endpoints of Latus Rectum: ( ", h + b2 / a3, ", ", k + c, ") & ( ", h + b2 / a3, ", ", k - c,
          " )")  # Here we are print out the E.L.R.
    print("Asymptote: y = ", k, "±", a3, "/", b3, "( ", "x -", h, " )")
    print("Directrices: x = ", k, "±", a3, "/", c, ")")

# Determine if input is a hyperbola3
elif a >= .01 and b == 0 and c <= -.01 and d == 0 and e == 0 and f != 0:
    print("The input is a hyperbola.")
    print("General form of the hyperbola.")
    print(a, "x² + ", c, "y² + ", f, " = 0 \n")  # General form of Hyperbola

    # In this part since we don't have the value of x and y lets proceed to part of getting the value of a² and b²
    f1 = f * -1  # Transpose the value of f
    a2 = f1 / a  # We divide the value of our constant to the value of x²
    b2 = f1 / c  # We divide the value of our constant to the value of y²

    f2 = f1 / f1  # Let's divide the value of f1 to itself to make the right side equal to 1

    print("( x )² / ", a2, " - ", " ( y )² / ", b2, "= ", f2)  # Print the standard form
    a3 = a2 ** 2  # This is the value of our a
    b3 = b2 ** 2  # This is the value of our b
    c = (a3 + b3) ** 2  # This is the value of our c
    print("Hyperbola with Horizontal Focal Axis")
    print("Center: ( 0", " 0 )")  # Here we are printing out the position of the center
    print("Vertices: ( ", a3, ", 0 ) & ( ", -a3, ", 0 )")  # Here we are printing out the position of the Vertices
    print("Foci: ( ", c, ", 0 ) & ( ", -c, ", 0 )")  # Here we are printing out the position of the Foci
    print("Endpoints of Transverse Axis: ( ", a3, ", 0 ) & ( ", -a3, ", 0 )")  # Here we are print out the E.T.A.
    print("Endpoints of Conjugate Axis: ( 0", b3, ") & ( 0, ", -b3, " )")  # Here we are print out the E.C.A.
    print("Endpoints of Latus Rectum: ( ", -c, "±", b2 / a, ") & ( ", c, "±", b2 / a,
          " )")  # Here we are print out the E.L.R.
    print("Asymptote: y = ±", b3, "/", a3, "( x )")
    print("Directrices: x = ±", a2, "/", c, ")")

# Determine if input is a hyperbola4
elif a <= -.01 and b == 0 and c >= .01 and d == 0 and e == 0 and f != 0:
    print("The input is a hyperbola.")
    print("General form of the hyperbola.")
    print(a, "x² + ", c, "y² + ", f, " = 0 \n")  # General form of Hyperbola

    # In this part since we don't have the value of x and y lets proceed to part of getting the value of a² and b²
    f1 = f * -1  # Transpose the value of f
    a2 = f1 / c  # We divide the value of our constant to the value of y²
    b2 = f1 / a  # We divide the value of our constant to the value of x²

    f2 = f1 / f1  # Let's divide the value of f1 to itself to make the right side equal to 1
    print("( y )² / ", a2, " - ", " ( x )² / ", b2, "= ", f2)  # Print the standard form
    a3 = a2 ** 2  # This is the value of our a
    b3 = b2 ** 2  # This is the value of our b
    c = (a3 + b3) ** 2  # This is the value of our c
    print("Hyperbola with Vertical Focal Axis")
    print("Center: ( 0", " 0 )")  # Here we are printing out the position of the center
    print("Vertices: ( 0", -a3, ") & ( 0,", a3, " )")  # Here we are printing out the position of the Vertices
    print("Foci: ( 0", -c, ") & ( 0,", c, " )")  # Here we are printing out the position of the Foci
    print("Endpoints of Transverse Axis: ( 0", -a3, ") & ( 0,", a3, " )")  # Here we are print out the E.T.A.
    print("Endpoints of Conjugate Axis: ( ", b3, " 0 ) & ( ", -b3, ", 0 )")  # Here we are print out the E.C.A.
    print("Endpoints of Latus Rectum: ( ±", b2 / a, -c, ") & ( ±", b2 / a, c, " )")  # Here we are print out the E.L.R.
    print("Asymptote: y = ±", a3, "/", b3, "( x )")
    print("Directrices: x = ±", a2, "/", c, ")")
# Determine if input is an ellipse 1
elif a >= .01 and b == 00 and a != c and c >= .01 and d != 0 and e != 0 and f != 0:
    print("The input is an ellipse.")
    print("General form of the Ellipse")
    print(a, "x² + ", c, "y² + ", d, "x + ", e, "y + ", f, " = 0 \n")  # General form of Ellipse
    f1 = f * -1  # Transpose the value of f
    ax = d / a  # Factor out the  coefficient  of x²
    cy = e / c  # Factor out the coefficient of y²

    # Completing the square of x
    # 9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    ax1 = ax / 2  # -4x/2
    ax2 = ax1 * ax1  # Then here we multiply it by itself

    # Completing the square of y
    # 9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    cy1 = cy / 2  # 2y/2
    cy2 = cy1 * cy1  # Then here we multiply it by itself

    # Right side of the hyperbola
    f2 = f1 + (a * ax2) + (c * cy2)

    # Right side of the Hyperbola to make it equal to 1
    f3 = f2 / f2  # divide the value by itself

    # Factor out the value of x² and x
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    ax3 = ax / 2

    # Factor out the value of y² and y
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    cy3 = cy / 2
    # Now we're going to get the value of a²
    af2 = f2 / a

    # Now we're going to get the value of b²
    cf2 = f2 / c
    cy5 = cf2 ** 2    # square root of b²
    ax4 = ax3 * -1  # if the value is positive/negative transpose it into negative/positive
    cy4 = cy3 * -1  # if the value is positive/negative transpose it into negative/positive
    c6 = ax4 - cy4  # the value of h and k is subtracting
    # Were going to test the value of af2 and cf2 to get the value of a2 and b2
    if af2 > cf2:  # If the value of af2 is greater-than to cf2, a2 will hold the value of af2
        a2 = af2  # Here we hold the value of af2 to a2
        b2 = cf2  # Here we hold the value of cf2 to b2
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("standard form of ellipse:")
        print("(x + ", ax3, ")² / ", a2, " + ", " (y + ", cy3, ")² / ", b2, " = ", f3)
        print("major axis: horizontal major axis")
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("center:", "h:", ax4, "k:", cy4)  # the value of the center is shown and that is h and k
        print("distance between center and focus (C): (C=√a²-b²) =", c3)    # getting the value of C
        print("Focus:", "F1:", ax4 - c3, ",", cy4)  # getting the focus f1
        print("Focus:", "F2:", ax4 + c3, ",", cy4)  # getting the focus f2
        print("vertex:", ax4, "±", a3, ",", cy4)    # getting the value of vertex
        print("v1:", ax4 + a3, ",", cy4)            # getting the value of v1
        print("v2:", ax4 - a3, ",", cy4)            # getting the value of v2
        print("co-vertex:", ax4, cy4, "±", b3)      # getting the value of co - vertex
        print("b1:", ax4, ",", cy4 + b3)            # getting the value of b1
        print("b2:", ax4, ",", cy4 - b3)            # getting the value of b2
        print("latus rectum:", "b²/a", "=", lt)     # getting the value of latus rectum
        print("LR1:", ax4 - lt, ",", cy4 - c3)      # getting the value of  LR1
        print("LR2:", ax4 + lt, ",", cy4 - c3)      # getting the value of  LR2
        print("LR3:", ax4 - lt, ",", cy4 + c3)      # getting the value of  LR3
        print("LR4:", ax4 + lt, ",", cy4 + c3)      # getting the value of  LR4
    # then if the value of cf2 is greater-than af2, b2 will hold the value of af2
    else:
        a2 = cf2  # Here we hold the value of cf2 to a2
        b2 = af2  # Here we hold the value of af2 to b2
        print("standard form of ellipse:")
        print("(x + ", ax3, ")² / ", b2, " + ", " (y + ", cy3, ")² / ", a2, " = ", f3)
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("Major axis: vertical major axis")
        print("center:", "h:", ax4, "k:", cy4)  # the value of the center is shown and that is h and k
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("distance between center and focus (C): (C=√a²-b²) =", c3)    # getting the value of C
        print("Focus:", "F1:", ax4, ",", cy4 - c3)  # getting the focus f1
        print("Focus:", "F2:", ax4, ",", cy4 + c3)  # getting the focus f2
        print("vertex:", ax4, ",", cy4, "±", a3)    # getting the value of vertex
        print("v1:", ax4, ",", (cy4 + a3))          # getting the value of v1
        print("v2:", ax4, ",", (cy4 - a3))          # getting the value of v2
        print("co-vertex:", ax4, "±", b3, cy4)      # getting the value of co - vertex
        print("b1:", (ax4 + b3), ",", cy4)          # getting the value of b1
        print("b2:", (ax4 - b3), ",", cy4)          # getting the value of b2
        print("latus rectum:", "b²/a", "=", lt)     # getting the value of latus rectum
        print("LR1:", ax4 - lt, ",", cy4 - c3)      # getting the value of  LR1
        print("LR2:", ax4 + lt, ",", cy4 - c3)      # getting the value of  LR2
        print("LR3:", ax4 - lt, ",", cy4 + c3)      # getting the value of  LR3
        print("LR4:", ax4 + lt, ",", cy4 + c3)      # getting the value of  LR4


# Determine if input is an ellipse2
elif a <= -.01 and b == 0 and a != c and c <= -.01 and d != 0 and e != 0 and f != 0:
    print("The input is an ellipse.")
    print("General form of the Ellipse")
    print(a, "x² + ", c, "y² + ", d, "x + ", e, "y + ", f, " = 0 \n")  # General form of Ellipse
    f1 = f * -1  # Transpose the value of f
    ax = d / a  # Factor out the coefficient of x²
    cy = e / c  # Factor out the coefficient of y²

    # Completing the square of x
    # 9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    ax1 = ax / 2  # -4x/2
    ax2 = ax1 * ax1  # Then here we multiply it by itself

    # Completing the square of y
    # 9(x² -4x + 4) + 16(y² + 2y + 1) = 164
    cy1 = cy / 2  # 2y/2
    cy2 = cy1 * cy1  # Then here we multiply it by itself

    # Right side of the hyperbola
    f2 = f1 + (a * ax2) + (c * cy2)

    # Right side of the Hyperbola to make it equal to 1
    f3 = f2 / f2  # divide the value by itself

    # Factor out the value of x² and x
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    ax3 = ax / 2

    # Factor out the value of y² and y
    # Like this → 9(x-2)² + 16(y² + 1)² = 144
    cy3 = cy / 2

    # Now we're going to get the value of a²
    af2 = f2 / a

    # Now we're going to get the value of b²
    cf2 = f2 / c
    cy5 = math.sqrt(cf2)  # square root of b²
    ax4 = ax3 * -1  # if the value is positive/negative transpose it into negative/positive
    cy4 = cy3 * -1  # if the value is positive/negative transpose it into negative/positive
    c6 = ax4 - cy4  # the value of h and k is subtracting
    # Were going to test the value of af2 and cf2 to get the value of a2 and b2
    if af2 > cf2:  # If the value of af2 is greater-than to cf2, a2 will hold the value of af2
        a2 = af2  # Here we hold the value of af2 to a2
        b2 = cf2  # Here we hold the value of cf2 to b2
        print("(x + ", ax3, ")² / ", a2, " + ", " (y + ", cy3, ")² / ", b2, " = ", f3)
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("standard form of ellipse:")
        print("(x + ", ax3, ")² / ", a2, " + ", " (y + ", cy3, ")² / ", b2, " = ", f3)
        print("major axis: horizontal major axis")
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("center:", "h:", ax4, "k:", cy4)  # the value of the center is shown and that is h and k
        print("distance between center and focus (C): (C=√a²-b²) =", c3)    # getting the value of C
        print("Focus:", "F1:", ax4 - c3, ",", cy4)  # getting the focus f1
        print("Focus:", "F2:", ax4 + c3, ",", cy4)  # getting the focus f2
        print("vertex:", ax4, "±", a3, ",", cy4)    # getting the value of vertex
        print("v1:", ax4 + a3, ",", cy4)            # getting the value of v1
        print("v2:", ax4 - a3, ",", cy4)            # getting the value of v2
        print("co-vertex:", ax4, cy4, "±", b3)      # getting the value of co - vertex
        print("b1:", ax4, ",", cy4 + b3)            # getting the value of co - vertex b1
        print("b2:", ax4, ",", cy4 - b3)            # getting the value of co - vertex b1
        print("latus rectum:", "b²/a", "=", lt)     # getting the value of latus rectum
        print("LR1:", ax4 - lt, ",", cy4 - c3)      # getting the value of  LR1
        print("LR2:", ax4 + lt, ",", cy4 - c3)      # getting the value of  LR2
        print("LR3:", ax4 - lt, ",", cy4 + c3)      # getting the value of  LR3
        print("LR4:", ax4 + lt, ",", cy4 + c3)      # getting the value of  LR4
    else:  # then if the value of cf2 is greater-than af2, b2 will hold the value of af2
        print("vertical major axis")
        a2 = cf2  # Here we hold the value of cf2 to a2
        b2 = af2  # Here we hold the value of af2 to b2
        print("standard form of ellipse:")
        print("(x + ", ax3, ")² / ", b2, " + ", " (y + ", cy3, ")² / ", a2, " = ", f3)
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("Major axis: vertical major axis")
        print("center:", "h:", ax4, "k:", cy4)  # the value of the center is shown and that is h and k
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("distance between center and focus (C): (C=√a²-b²) =", c3)     # getting the value of C
        print("Focus:", "F1:", ax4, ",", cy4 - c3)  # getting the focus f1
        print("Focus:", "F2:", ax4, ",", cy4 + c3)  # getting the focus f2
        print("vertex:", ax4, ",", cy4, "±", a3)  # getting the value of vertex
        print("v1:", ax4, ",", (cy4 + a3))        # getting the value of v1
        print("v2:", ax4, ",", (cy4 - a3))        # getting the value of v2
        print("co-vertex:", ax4, "±", b3, cy4)    # getting the value of co - vertex
        print("b1:", (ax4 + b3), ",", cy4)        # getting the value of co - vertex b1
        print("b2:", (ax4 - b3), ",", cy4)        # getting the value of co - vertex b2
        print("latus rectum:", "b²/a", "=", lt)   # getting the value of latus rectum
        print("LR1:", ax4 - lt, ",", cy4 - c3)    # getting the value of  LR1
        print("LR2:", ax4 + lt, ",", cy4 - c3)    # getting the value of  LR2
        print("LR3:", ax4 - lt, ",", cy4 + c3)    # getting the value of  LR3
        print("LR4:", ax4 + lt, ",", cy4 + c3)    # getting the value of  LR4

# Determine if input is an ellipse 3
elif a >= .01 and b == 00 and a != c and c >= .01 and d == 0 and e == 0 and f != 0:
    print("The input is an ellipse.")
    print("General form of the Ellipse")
    print(a, "x² + ", c, "y² + ", f, " = 0 \n")  # General form of Ellipse

    # In this part since we don't have the value of x and y lets proceed to part of getting the value of a² and b²
    f1 = f * -1  # Transpose the value of f
    af1 = f1 / a  # We divide the value of our constant to the value of the denominator
    cf1 = f1 / c  # We divide the value of our constant to the value of the denominator

    f2 = f1 / f1  # Let's divide the value of f1 to itself to make the right side equal to 1

    af2 = af1 ** 2  # This is our denominator
    cf2 = cf1 ** 2  # This is our denominator
    cy5 = math.sqrt(cf2)  # square root of b²

    if af2 > cf2:  # If the value of af2 is greater-than to cf2, a2 will hold the value of af2
        a2 = af2  # Here we hold the value of af2 to a2
        b2 = cf2  # Here we hold the value of cf2 to b2
        print("standard form of ellipse:")
        print("( x )² / ", a2, " - ", " ( y )² / ", b2, "= ", f2)  # Print the standard form
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("major axis: horizontal major axis")  # the ellipse is horizontal axis
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("center:", "h: 0", "k: 0")  # the value of the center is shown and that is h and k
        print("distance between center and focus (C): (C=√a²-b²) =", c3)    # getting the value of C
        print("Focus:", "F1:", 0 - c3, ", 0")      # getting the focus f1
        print("Focus:", "F2:", 0 + c3, ", 0")      # getting the focus f2
        print("vertex:", "0 ±", a3, ", 0")        # getting the value of vertex
        print("v1:", 0 + a3, ", 0")                # getting the value of v1
        print("v2:", 0 - a3, ", 0")                # getting the value of v2
        print("co-vertex:", "0, 0", "±", b3)       # getting the value of co - vertex
        print("b1: 0", ",", 0 + b3)                # getting the value of co - vertex b1
        print("b2: 0", ",", 0 - b3)                # getting the value of co - vertex b2
        print("latus rectum:", "b²/a", "=", lt)    # getting the value of latus rectum
        print("LR1:", 0 - lt, ",", 0 - c3)         # getting the value of  LR1
        print("LR2:", 0 + lt, ",", 0 - c3)         # getting the value of  LR2
        print("LR3:", 0 - lt, ",", 0 + c3)         # getting the value of  LR3
        print("LR4:", 0 + lt, ",", 0 + c3)         # getting the value of  LR4
    else:
        a2 = cf2  # Here we hold the value of af2 to a2
        b2 = af2  # Here we hold the value of cf2 to b2
        print("( x )² / ", b2, " - ", " ( y )² / ", a2, "= ", f2)  # Print the standard form
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("Major axis: vertical major axis")
        print("center:", "h: 0", "k: 0")  # the value of the center is shown and that is h and k
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("distance between center and focus (C): (C=√a²-b²) =", c3)      # getting the value of C
        print("Focus:", "F1: 0", ",", 0 - c3)       # getting the value of f1
        print("Focus:", "F2: 0", ",", 0 + c3)       # getting the value of f2
        print("vertex: 0", ", 0", "±", a3)          # getting the value of vertex
        print("v1: 0", ",", (0 + a3))               # getting the value of v1
        print("v2: 0", ",", (0 - a3))               # getting the value of v2
        print("co-vertex: 0", "±", b3, "0")         # getting the value of co - vertex
        print("b1:", (0 + b3), ",", "0")            # getting the value of co - vertex b1
        print("b2:", (0 - b3), ",", "0")            # getting the value of co - vertex b2
        print("latus rectum:", "b²/a", "=", lt)     # getting the value of latus rectum
        print("LR1:", 0 - lt, ",", 0 - c3)          # getting the value of LR1
        print("LR2:", 0 + lt, ",", 0 - c3)          # getting the value of LR2
        print("LR3:", 0 - lt, ",", 0 + c3)          # getting the value of LR3
        print("LR4:", 0 + lt, ",", 0 + c3)          # getting the value of LR4
# Determine if input is an ellipse4
elif a <= -.01 and b == 0 and a != c and c <= -.01 and d == 0 and e == 0 and f != 0:
    print("The input is an ellipse.")
    print("General form of the Ellipse")
    print(a, "x² + ", c, "y² + ", f, " = 0 \n")  # General form of Ellipse

    # In this part since we don't have the value of x and y lets proceed to part of getting the value of a² and b²
    f1 = f * -1  # Transpose the value of f
    af1 = f1 / a  # We divide the value of our constant to the value of the denominator
    cf1 = f1 / c  # We divide the value of our constant to the value of the denominator

    f2 = f1 / f1  # Let's divide the value of f1 to itself to make the right side equal to 1

    af2 = af1 ** 2  # This is our denominator
    cf2 = cf1 ** 2  # This is our denominator

    if af2 > cf2:  # If the value of af2 is greater-than to cf2, a2 will hold the value of af2
        a2 = af2  # Here we hold the value of af2 to a2
        b2 = cf2  # Here we hold the value of cf2 to b2
        print("standard form of ellipse:")
        print("( x )² / ", a2, " - ", " ( y )² / ", b2, "= ", f2)  # Print the standard form
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("major axis: horizontal major axis")
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("center:", "h: 0", "k: 0")  # the value of the center is shown and that is h and k
        print("distance between center and focus (C): (C=√a²-b²) =", c3)    # getting the value of C
        print("Focus:", "F1:", 0 - c3, ",", "0")     # getting the value of f1
        print("Focus:", "F2:", 0 + c3, ",", "0")     # getting the focus f2
        print("vertex:", "0", "±", a3, ",", "0")     # getting the value of vertex
        print("v1:", 0 + a3, ",", "0")               # getting the value of v1
        print("v2:", 0 - a3, ",", "0")               # getting the value of v2
        print("co-vertex:", "0 , 0", "±", b3)        # getting the value of co - vertex
        print("b1:", "0,", 0 + b3)                  # getting the value of co - vertex b1
        print("b2:", "0,", 0 - b3)                  # getting the value of co - vertex b2
        print("latus rectum:", "b²/a", "=", lt)     # getting the value of latus rectum
        print("LR1:", 0 - lt, ",", 0 - c3)          # getting the value of LR1
        print("LR2:", 0 + lt, ",", 0 - c3)          # getting the value of  LR2
        print("LR3:", 0 - lt, ",", 0 + c3)          # getting the value of  LR3
        print("LR4:", 0 + lt, ",", 0 + c3)          # getting the value of  LR4
    else:
        a2 = cf2  # Here we hold the value of af2 to a2
        b2 = af2  # Here we hold the value of cf2 to b2
        print("standard form of ellipse:")
        print("( x )² / ", b2, " - ", " ( y )² / ", a2, "= ", f2)  # Print the standard form
        a3 = math.sqrt(a2)  # square root of a²
        b3 = math.sqrt(b2)  # square root of a²
        lt = b2 / a3  # b²/a
        c2 = a2 - b3  # a²-b²
        c3 = math.sqrt(c2)  # getting the square root of c2 or a²-b²
        print("Major axis: vertical major axis")
        print("center:", "h: 0", "k: 0")  # the value of the center is shown and that is h and k
        print("square root of a is:", a3)  # display the square root of a²
        print("square root of b is:", b3)  # display the square root of a²
        print("distance between center and focus (C): (C=√a²-b²) =", c3)  # getting the value of C
        print("Focus:", "F1: 0", ",", 0 - c3)  # getting the value of C
        print("Focus:", "F2:0 ", ",", 0 + c3)  # getting the focus f2
        print("vertex: 0", ",", "0", "±", a3)  # getting the value of vertex
        print("v1: 0", ",", (0 + a3))  # getting the value of v1
        print("v2: 0", ",", (0 - a3))  # getting the value of v2
        print("co-vertex: 0", "±", b3, "0")  # getting the value of co - vertex
        print("b1:", (0 + b3), ",", "0")  # getting the value of co - vertex b1
        print("b2:", (0 - b3), ",", "0")  # getting the value of co - vertex b2
        print("latus rectum:", "b²/a", "=", lt)  # getting the value of latus rectum
        print("LR1:", 0 - lt, ",", 0 - c3)  # getting the value of  LR1
        print("LR2:", 0 + lt, ",", 0 - c3)  # getting the value of  LR2
        print("LR3:", 0 - lt, ",", 0 + c3)  # getting the value of  LR3
# Determine if input is a circle
elif a == c and b == 0 and d != 0 and e != 0 and f != 0:
    print("The input is a circle.")
    print("General form of a circle")
    # General form of the Circle
    print(a, "x² + ", c, "y² + ", d, "x + ", e, "y + ", f, " = 0 \n")

    # Divide all input by the value of x²
    a1 = a / a  # This variable will contain the value of x²
    c1 = c / a  # This variable will contain the value of y²
    d1 = d / a  # This variable will contain the value of x
    e1 = e / a  # This variable will contain the value of y
    f1 = f / a  # This variable will contain the value of f

    # Transpose the value of f1
    f2 = f1 * -1

    # Completing the square
    d2 = d1 / 2  # Divide by 2 then multi by itself
    e2 = e1 / 2  # Divide by 2 then multi by itself

    d3 = d2 * d2  # Multiply by itself to complete the square
    e3 = e2 * e2  # Multiply by itself to complete the square
    # Let's add it to the right side to make it equal
    f3 = f2 + d3 + e3
    print("Standard form of a Circle")  # print Standard form of a Circle
    print("(x + ", d2, ")² + ", "(y + ", e2, ")² = ", f3 ** 2)
    d4 = d2 * 1     # if the value of d2 or h is positive/negative  convert the value into negative/positive
    e4 = e2 * 1     # if the value of e2 or k is positive/negative  convert the value into negative/positive
    print("center:", "(", d4, ")", "(", e4, ")")  # display the value of center
    print("radius:", math.sqrt(f3))  # display the value of radius
    print("diameter:", f3 * 2)  # display the value of diameter

elif a == c and b == 0 and d == 0 and e == 0 and f != 0:
    print("The input is a circle.")
    print("General form of a circle")
    # General form of the Circle
    print(a, "x² + ", c, "y² + ", f, " = 0 \n")

    # Divide all input by the value of x²
    a1 = a / a  # x²
    c1 = c / a  # y²
    f1 = f / a  # f
    # Transpose the value of f1
    f2 = f1 * -1
    print("Standard form of a Circle")  # print Standard form of a Circle
    print("( x )² + ", "( y )² = ", f2 ** 2)  # print Standard form of a Circle
    f3 = math.sqrt(f2 ** 2) # getting the square root of R
    print("center:", "( 0 )", "( 0 )")  # display the value of center
    print("radius:", math.sqrt(f3))  # display the value of radius
    print("diameter:", f3 * 2)  # display the value of diameter

# If none of the above conditions are met, input is not a line, circle, parabola, ellipse, or hyperbola
else:
    print("The input is not a line, circle, parabola, ellipse, or hyperbola.")
