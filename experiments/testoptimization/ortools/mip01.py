from __future__ import print_function
from ortools.linear_solver import pywraplp

def LinearProgrammingExample():
    """ Linear Programming Example """
    # Instantiate a Glop solver
    solver = pywraplp.Solver('LinearProgrammingExample', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # create two variables
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')

    # Constraint 0 : Raw A:  4x1 + 4x2 <= 75
    solver.Add(4*x1 + 4*x2 <= 75)

    # Constraint 1: Grinding A: 4x1 + 2x2 <= 80
    solver.Add(4*x1 + 2*x2 <= 80)

    # Constraint 2: Polishing A: 2x1 + 5x2  <= 60
    solver.Add(2*x1 + 5*x2 <= 60)

    # Maximize Profit A: 10x1 + 15x2
    solver.Maximize(10*x1 + 15*x2)

    # solve
    solver.Solve()
    opt_solution = 10 * x1.solution_value() + 15 * x2.solution_value()
    print('Solution: 10*{} + 15*{} => {}'.format(x1.solution_value(), x2.solution_value(), opt_solution))


LinearProgrammingExample()

# Example from book Model Building in Mathematical Programming, chapter 4