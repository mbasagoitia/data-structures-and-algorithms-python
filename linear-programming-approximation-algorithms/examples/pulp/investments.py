from pulp import *
# Create a linear programming model and set it to maximize its objective
# Read this example here: https://coin-or.github.io/pulp/CaseStudies/a_blending_problem.html
lpModel = LpProblem('InvestmentProblem', LpMaximize)
# Create a variable called x1 and set its bounds to be between 0 and infinity
x1 = LpVariable('x1', 0, None) 
x2 = LpVariable('x2', 0, None)
x3 = LpVariable('x3', 0, None)
x4 = LpVariable('x4', 0, None)
x5 = LpVariable('x5', 0, None)
x6 = LpVariable('x6', 0, None)
# 1. Next create variables x2.. x6
# 2. Set the objective function: here is an example of how to do it. Use the 
#    actual objective function you worked out
lpModel += 25*x1 + 20*x2 + 3*x3 + 1.5*x4 + 3*x5 + 4.5*x6
# 3. Add the constraints like so. Remember there is no need to set xi >= 0 since we
#    already did that when declaring the variables xi.
lpModel += 129*x1 + 286*x2 + 72.29*x3 + 38*x4 + 52*x5 + 148*x6 <= 10000
lpModel += 129*x1 + 286*x2 <= 6666.67
lpModel += 72.29*x3 + 38*x4 <= 6666.67
lpModel += 52*x5 + 148*x6 <= 6666.67
lpModel += 129*x1 + 286*x2 >= 1666.67
lpModel += 72.29*x3 + 38*x4 >= 1666.67
lpModel += 52*x5 + 148*x6 >= 1666.67
lpModel += 129*x1 + 286*x2 + 72.29*x3 + 38*x4 + 52*x5 + 148*x6 <= 15 * (1.9*x1 + 8.1*x2 + 1.5*x3 + 5*x4 + 2.5*x5 + 5.2*x6)
# 4. We have provided the code to solve the model and print the solutions.
# your code here
# The problem is solved using PuLP's choice of Solver
lpModel.solve()
# Each of the variables is printed with it's resolved optimum value
for v in lpModel.variables():
    print(v.name, "=", v.varValue)
    
# The optimised objective function value is printed to the screen
print("Objective value = ", value(lpModel.objective))
raise NotImplementedError