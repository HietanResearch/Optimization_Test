import pulp

prob = pulp.LpProblem('PuLP_with_CPLEX', sense = pulp.LpMaximize)

x1 = pulp.LpVariable('x1', cat = 'Continuous')
x2 = pulp.LpVariable('x2', cat = 'Continuous')

prob += 2 * x1 + 3 * x2

prob += x1 + 3 * x2 <= 9, 'Const1'
prob += x1 + x2 <= 4, 'Const2'
prob += 2 * x1 + x2 <= 6, 'Const3'

print(prob)

solver = pulp.CPLEX_CMD(msg = 1)

status = prob.solve(solver)

print()
print('Status :', pulp.LpStatus[status])
print('Objective Value :', pulp.value(prob.objective))
print('(x1, x2) = (' + str(pulp.value(x1)) + ', ' + str(pulp.value(x2)) + ')')
