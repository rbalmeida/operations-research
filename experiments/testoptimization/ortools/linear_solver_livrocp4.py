from __future__ import print_function
from ortools.linear_solver import pywraplp

def LinearProgrammingExample():
    """ Linear Programming Example """
    # Instantiate a Glop solver
    solver = pywraplp.Solver('LinearProgrammingExample', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # create two variables
    x1 = solver.NumVar(0, solver.infinity(), 'x1')
    x2 = solver.NumVar(0, solver.infinity(), 'x2')

    # Constraint 0 : Raw A:  4x1 + 4x2 <= 75
    constraint0 = solver.Constraint(-solver.infinity(), 75)
    constraint0.SetCoefficient(x1, 4)
    constraint0.SetCoefficient(x2, 4)


    # Constraint 1: Grinding A: 4x1 + 2x2 <= 80
    constraint1 = solver.Constraint(-solver.infinity(), 80)
    constraint1.SetCoefficient(x1, 4)
    constraint1.SetCoefficient(x2, 2)

    # Contraint 2: Polishing A: 2x1 + 5x2  <= 60
    constraint2 = solver.Constraint(-solver.infinity(), 60)
    constraint2.SetCoefficient(x1, 2)
    constraint2.SetCoefficient(x2, 5)

    # Maximize Profit A: 10x1 + 15x2
    objective = solver.Objective()
    objective.SetCoefficient(x1, 10)
    objective.SetCoefficient(x2, 15)
    objective.SetMaximization()

    # solve
    solver.Solve()
    opt_solution = 10 * x1.solution_value() + 15 * x2.solution_value()
    print('Solution: 10*{} + 15*{} => {}'.format(x1.solution_value(), x2.solution_value(), opt_solution))


LinearProgrammingExample()

# Example from book Model Building in Mathematical Programming, chapter 4