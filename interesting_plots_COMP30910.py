# Interesting plots for MSCP COMP30190
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import math

# Scatter Plot with points
print("Final Year Project Design and Implementation (COMP30910)")
x_axis = [x * x for x in range(2, 6)]
y_axis = [4.08, 22.87, 82.03, 220.78]
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('Size of Sudoku grid, N')
plt.ylabel('Minimum Number of Clues, $N^2(1 - ε)$')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.title('Upper Bound Approximation using POI of C and R')
plt.grid()
plt.savefig('mscp_it_plot_upperbound.png')

# Smooth curve
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = np.array(x_axis)
y_axis = np.array(y_axis)
x_new = np.linspace(x_axis.min(), x_axis.max(),500)

f = interp1d(x_axis, y_axis, kind='quadratic')
y_smooth=f(x_new)

plt.plot (x_new,y_smooth)
plt.scatter (x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('Size of Sudoku grid, N')
plt.ylabel('Minimum Number of Clues, $N^2(1 - ε)$')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.title('Upper Bound Approximation using POI of C and R')
plt.grid()
plt.savefig('mscp_it_plot_upperboundsmooth.png')

# Plotting capacity against probability of erasure, ε
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = [0.74, 0.72, 0.68, 0.65]
y_axis = [0.51, 0.90, 1.28, 1.64]
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Capacity (C)')
plt.title('Capacity (C) against ε')
plt.grid()
plt.savefig('mscp_it_plot_cap_epsilon.png')

# Plotting rate and capacity against probability of erasure, ε
# print("Final Year Project Design and Implementation (COMP30910)")
# plt.clf()
# plt.plot([0.7446898437, 0.7176458017, 0.6795661468, 0.6467488305], [0.5106203126, 0.8950416323, 1.281735413, 1.64044763], label='Rate')
# plt.plot([0.7446898437, 0.7176458017, 0.6795661468, 0.6467488305], [1, 4, 9, 16], label='second plot')
# plt.legend()

# Good lower bound approximation for MSCP
epsilon_approximations = []
for i in range(1, 9):
    # print("i: {}".format(i))
    epsilon_approximations.append(((i**2 - 1) / i**2)**(i - 1))
print("Epsilon Approximations:", epsilon_approximations)
min_num_clues = []
for i in range(1, len(epsilon_approximations) + 1):
    min_num_clues.append( math.floor((i**2 * i**2) * (1 - epsilon_approximations[i - 1])) )
print("Minimum Number of Clues:", min_num_clues)
print("Sudoku of size N x N:", [x**2 * x**2 for x in range(1, 9)])

# Plotting good lower bound approximation for MSCP
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = [x * x for x in range(1, 9)]
y_axis = min_num_clues
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('Size of Sudoku grid, N')
plt.ylabel('Minimum Number of Clues, $N^2(1 - ε)$')
plt.title('Lower Bound Approximation')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_goodlowerbound.png')

# Plotting good lower bound approximation for MSCP smooth
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = np.array(x_axis)
y_axis = np.array(y_axis)
x_new = np.linspace(x_axis.min(), x_axis.max(),500)

f = interp1d(x_axis, y_axis, kind='quadratic')
y_smooth=f(x_new)

plt.plot (x_new,y_smooth)
plt.scatter (x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('Size of Sudoku grid, N')
plt.ylabel('Minimum Number of Clues, $N^2(1 - ε)$')
plt.title('Lower Bound Approximation')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_goodlowerbound_smooth.png')
# round(x, 2)

# Plotting N against ε formula values
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = epsilon_approximations
y_axis = [x * x for x in range(1, 9)]
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Size of Sudoku grid, N')
plt.title('N against ε formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_grideformula.png')

# Plotting N against ε formula values smooth
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = np.array(x_axis)
y_axis = np.array(y_axis)
x_new = np.linspace(x_axis.min(), x_axis.max(),500)

f = interp1d(x_axis, y_axis, kind='quadratic')
y_smooth=f(x_new)

plt.plot (x_new,y_smooth)
plt.scatter (x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Size of Sudoku grid, N')
plt.title('N against ε formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_grideformula_smooth.png')

# Plotting n against ε formula values 
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = epsilon_approximations
y_axis = [y for y in range(1, 9)]
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Size of Sudoku subgrid, n')
plt.title('n against ε formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_subgrideformula.png')

# Plotting n against ε formula values smooth
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = np.array(x_axis)
y_axis = np.array(y_axis)
x_new = np.linspace(x_axis.min(), x_axis.max(),500)

f = interp1d(x_axis, y_axis, kind='quadratic')
y_smooth=f(x_new)

plt.plot (x_new,y_smooth)
plt.scatter (x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Size of Sudoku subgrid, n')
plt.title('n against ε formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_subgrideformula_smooth.png')

# Plotting Capacity against ε formula values
print("Final Year Project Design and Implementation (COMP30910)")
x_axis = epsilon_approximations
y_axis = []
for i in range(1, len(epsilon_approximations) + 1):
    y_axis.append((1 - epsilon_approximations[i - 1]) * math.log((i)**2, 2))
plt.clf()
x_axis = [round(x, 2) for x in x_axis]
y_axis = [round(y, 2) for y in y_axis]
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Capacity (C)')
plt.title('Capacity (C) against ε using ε formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_ceformula.png')

# Plotting Capacity against ε formula values smooth
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = np.array(x_axis)
y_axis = np.array(y_axis)
x_new = np.linspace(x_axis.min(), x_axis.max(),500)

f = interp1d(x_axis, y_axis, kind='quadratic')
y_smooth=f(x_new)

plt.plot (x_new,y_smooth)
plt.scatter (x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Capacity (C)')
plt.title('Capacity (C) against ε using ε formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_ceformula_smooth.png')

# Plotting Minimum Number of Clues against ε
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = [round(e, 2) for e in epsilon_approximations]
y_axis = min_num_clues
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Minimum Number of Clues, $N^2(1 - ε)$')
plt.title('Lower Bound Approximation against ε using formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_goodlowerboundeformula.png')

# 
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = np.array(x_axis)
y_axis = np.array(y_axis)
x_new = np.linspace(x_axis.min(), x_axis.max(),500)

f = interp1d(x_axis, y_axis, kind='quadratic')
y_smooth=f(x_new)

plt.plot (x_new,y_smooth)
plt.scatter (x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('ε')
plt.ylabel('Minimum Number of Clues, $N^2(1 - ε)$')
plt.title('Lower Bound Approximation against ε using formula values')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_goodlowerboundeformula_smooth.png')


# Plotting ε against Minimum Number of Clues
print("Final Year Project Design and Implementation (COMP30910)")
plt.clf()
x_axis = min_num_clues
y_axis = [round(e, 2) for e in epsilon_approximations]
plt.scatter(x_axis, y_axis)
for i_x, i_y in zip(x_axis, y_axis):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.xlabel('Minimum Number of Clues, $N^2(1 - ε)$')
plt.ylabel('ε')
plt.title('ε using formula values against Good Lower Bound Approximation')
# plt.vlines(x_axis, 0, y_axis, linestyle="dashed")
# plt.hlines(y_axis, 0, x_axis, linestyle="dashed")
plt.grid()
plt.savefig('mscp_it_plot_egoodlowerboundformula.png')