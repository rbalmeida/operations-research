from __future__ import print_function
from ortools.linear_solver import pywraplp

def ColoringProblem():
    """ Linear Programming Example """
    # Instantiate a Glop solver
    solver = pywraplp.Solver('Graph Coloring MIP', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # create two variables
    # x1 possible colors
    x1_red = solver.IntVar(0, 1, 'x1_red')
    x1_blue = solver.IntVar(0, 1, 'x1_blue')
    x1_green = solver.IntVar(0, 1, 'x1_green')

    # x2 possible colors
    x2_blue = solver.IntVar(0, 1, 'x2_blue')
    x2_green = solver.IntVar(0, 1, 'x2_green')

    # x3 possible colors
    x3_red = solver.IntVar(0, 1, 'x3_red')
    x3_blue = solver.IntVar(0, 1, 'x3_blue')

    # x4 possible colors
    x4_red = solver.IntVar(0, 1, 'x4_red')
    x4_blue = solver.IntVar(0, 1, 'x4_blue')

    # x5 possible colors
    x5_blue = solver.IntVar(0, 1, 'x5_blue')
    x5_green = solver.IntVar(0, 1, 'x5_green')

    # x6 possible colors
    x6_red = solver.IntVar(0, 1, 'x_red')
    x6_green = solver.IntVar(0, 1, 'x6_green')
    x6_teal = solver.IntVar(0, 1, 'x6_teal')

    # x7 possible colors
    x7_red = solver.IntVar(0, 1, 'x7_red')
    x7_blue = solver.IntVar(0, 1, 'x7_blue')

    # Constraint for each pair of adjacent nodes so that does not have same color
    # using only colors on each domain which is common

    # x1 and x2
    solver.Add(x1_blue + x2_blue <= 1)
    solver.Add(x1_green + x2_green <= 1)

    # x1 and x3
    solver.Add(x1_blue + x3_blue <= 1)
    solver.Add(x1_red + x3_red <= 1)

    # x1 and x4
    solver.Add(x1_blue + x4_blue <= 1)
    solver.Add(x1_red + x4_red <= 1)

    # x1 and x7
    solver.Add(x1_blue + x7_blue <= 1)
    solver.Add(x1_red + x7_red <= 1)

    # x2 and x6
    solver.Add(x2_green + x6_green <= 1)

    # x3 and x7
    solver.Add(x3_blue + x7_blue <= 1)
    solver.Add(x3_red + x7_red <= 1)

    # x4 and x5
    solver.Add(x4_blue + x5_blue <= 1)

    # x4 and x7
    solver.Add(x4_blue + x7_blue <= 1)
    solver.Add(x4_red + x7_red <= 1)

    # x5 and x6
    solver.Add(x5_green + x6_green <= 1)

    # x5 and x7
    solver.Add(x5_blue + x7_blue <= 1)

    # constraints so that each node gets a color
    solver.Add(x1_red + x1_blue + x1_green == 1)
    solver.Add(x2_blue + x2_green == 1)
    solver.Add(x3_red + x3_blue == 1)
    solver.Add(x4_red + x4_blue == 1)
    solver.Add(x5_blue + x5_green == 1)
    solver.Add(x6_red + x6_green + x6_teal == 1)
    solver.Add(x7_red + x7_blue == 1)

    # Maximize
    # solver.Minimize(x1_red + x1_blue + x1_green +
    #                 x2_blue + x2_green +
    #                 x3_red + x3_blue +
    #                 x4_red + x4_blue +
    #                 x5_blue + x5_green +
    #                 x6_red + x6_green + x6_teal +
    #                 x7_red + x7_blue)

    # solve
    solver.Solve()
    print('Solution')
    print('x1 : red({}), blue({}), green({})'.format(x1_red.solution_value(), x1_blue.solution_value(), x1_green.solution_value()))
    print('x2 : blue({}), green({})'.format(x2_blue.solution_value(), x2_green.solution_value()))
    print('x3 : red({}), blue({})'.format(x3_red.solution_value(), x3_blue.solution_value()))
    print('x4 : red({}), blue({})'.format(x4_red.solution_value(), x4_blue.solution_value()))
    print('x5 : blue({}), green({})'.format(x5_blue.solution_value(), x5_green.solution_value()))
    print('x6 : red({}), green({}), teal({})'.format(x6_red.solution_value(), x6_green.solution_value(), x6_teal.solution_value()))
    print('x7 : red({}), blue({})'.format(x7_red.solution_value(), x7_blue.solution_value()))



ColoringProblem()

# Constraint Programming, Chapter 4 page 114, coloring problem
# No adjacent same color
# allowed colors per node
# x1 : {red, blue, green}
# x2 : {blue, green}
# x3 : {red, blue}
# x4 : {red, blue}
# x5 : {blue, green}
# x6 : {red, green, teal}
# x7 : {red, blue}
# adjacent list
# x1 : {x2, x3, x4, x7}
# x2 : {x1, x7}
# x3 : {x1, x7}
# x4 : {x1, x5, x7}
# x5 : {x4, x6, x7}
# x6 : {x2, x5}
# x7 : {x1, x3, x4, x5}

# ideas
# colors : {red, blue, green, teal}
# alternative 1, brute force, 16 variables, x1_red, x1_blue, x1_green as a binary variable
# constraints on adjacent nodes and same color, for example x1_blue + x2_blue <= 1
# constraint on variable to get at least one color

# alternative 2: auto generate constraints with node color domain and adjacent list