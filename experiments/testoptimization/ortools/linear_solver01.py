from __future__ import print_function
from ortools.linear_solver import pywraplp

def LinearProgrammingExample():
    """ Linear Programming Example """
    # Instantiate a Glop solver
    solver = pywraplp.Solver('LinearProgrammingExample', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # create two variables
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    # constraint 0: x + 2y <= 14
    constraint0 = solver.Constraint(-solver.infinity(), 14)
    constraint0.SetCoefficient(x, 1)
    constraint0.SetCoefficient(y, 2)

    # constraint 1: 3x - y >= 0
    constraint1 = solver.Constraint(0, solver.infinity())
    constraint1.SetCoefficient(x, 3)
    constraint1.SetCoefficient(y, -1)

    # constraint 2: x - y <= 2
    constraint2 = solver.Constraint(-solver.infinity(), 2)
    constraint2.SetCoefficient(x, 1)
    constraint2.SetCoefficient(y, -1)

    # Objective function: 3x + 4y
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 4)
    objective.SetMaximization()

    solver.Solve()
    opt_solution = 3 * x.solution_value() + 4 * y.solution_value()

    print('Number of variables = {}'.format(solver.NumVariables()))
    print('Number of constraints = {}'.format(solver.NumConstraints()))
    print('Solution:')
    print('x = {}'.format(x.solution_value()))
    print('y = {}'.format(y.solution_value()))

    print('Optimal Objective Value = {}'.format(opt_solution))


LinearProgrammingExample()