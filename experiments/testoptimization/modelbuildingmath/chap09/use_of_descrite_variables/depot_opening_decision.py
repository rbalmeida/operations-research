from __future__ import print_function
from ortools.linear_solver import pywraplp

DEMAND = 3000

def DepotOpeningDecision():
    """ Discrete Variables to decide which depot should be opened """

    # Depot OpenCost   Capacity    Transportation Cost    Description
    # 1; 1000; 500 , 10. A Depot outside the city. Lower opening cost, higher transport cost
    # 2, 500, 1000,  15. A Depot outside the city. Lower opening cost, higher transport cost
    # 3, 4000, 2000, 5. A depot inside the city.

    # Instantiate a Glop solver
    solver = pywraplp.Solver('Depot opening decision', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # create two variables
    open_depot1 = solver.IntVar(0, 1, 'open_depot1')
    open_depot2 = solver.IntVar(0, 1, 'open_depot2')
    open_depot3 = solver.IntVar(0, 1, 'open_depot3')

    ship_from_depot1 = solver.IntVar(0, 500, 'ship_from_depot1')
    ship_from_depot2 = solver.IntVar(0, 1000, 'ship_from_depot2')
    ship_from_depot3 = solver.IntVar(0, 2000, 'ship_from_depot3')

    # Constraint 0 : Open Depot Budget
    solver.Add(1000*open_depot1 + 500*open_depot2 + 4000*open_depot3 <= 5000)

    # Capacity Constraints
    # solver.Add(ship_from_depot1 <= 500)
    # solver.Add(ship_from_depot2 <= 1000)
    # solver.Add(ship_from_depot3 <= 500)

    # Opening and demand Constraints
    solver.Add(ship_from_depot1 + ship_from_depot2 + ship_from_depot3 == DEMAND)

    solver.Add(ship_from_depot1 - 500*open_depot1 <= 0)
    solver.Add(ship_from_depot2 - 1000*open_depot2 <= 0)
    solver.Add(ship_from_depot3 - 2000*open_depot3 <= 0)
    # initiall ideia was to add ship_from_depot1*open_depot1 but that is not allowed as it is not a
    # linear funciton, which is the pre req for these models. (check the mathematical concept of this, e.g book [1] chapter 3)

    # Minimize Cost
    solver.Minimize(ship_from_depot1*10 + ship_from_depot2*15 + ship_from_depot3*5 +
                    open_depot1*1000 + open_depot2*500 + open_depot3*4000)

    # solve
    solver.Solve()
    opt_solution = ship_from_depot1.solution_value()*10 + ship_from_depot2.solution_value()*15 + ship_from_depot3.solution_value()*5 \
                   + open_depot1.solution_value()*1000 + open_depot2.solution_value()*500 + open_depot3.solution_value()*4000

    print('Open Depots: 1:[{}]  2:[{}] 3:[{}]'.format(open_depot1.solution_value(),
                                                      open_depot2.solution_value(),
                                                      open_depot3.solution_value()))

    print('Shipping: 1:[{}]  2:[{}] 3:[{}]'.format(ship_from_depot1.solution_value(),
                                                      ship_from_depot2.solution_value(),
                                                      ship_from_depot3.solution_value()))

    print('Total Opening Cost: {}'.format(open_depot1.solution_value()*1000 +
                                          open_depot2.solution_value()*500 +
                                          open_depot3.solution_value()*4000))

    print('Total Shipping Cost: {}'.format( ship_from_depot1.solution_value()*10 +
                                            ship_from_depot2.solution_value()*15 +
                                            ship_from_depot3.solution_value()*5))

    print('Total Cost: {}'.format(opt_solution))

DepotOpeningDecision()

# Example inspired in book Model Building in Mathematical Programming, chapter 9