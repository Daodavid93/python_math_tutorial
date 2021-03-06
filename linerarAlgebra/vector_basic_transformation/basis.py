import numpy as np
import matplotlib.pyplot as plt


def append_line(fitst_points, second_points,plt):
    x1 = fitst_points[0]
    y1 = fitst_points[1]

    x2 = second_points[0]
    y2 = second_points[1]
    tg = (y2 - y1) / (x2 - x1)
    x = np.linspace(x1, x2, 10)
    f = lambda z: y1 + tg * z
    y = [f(i) for i in x]
    line2, = ax.plot(x, y, label='Using set_dashes()', color='red')
    line2.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break



def get_projection_array(x, y):
    x = np.linspace(0, x, 10)
    y = [y for i in range(10)]
    return [x, y]


def scalar_mutiplication(x, y):
    return x.T.dot(y)


def get_cordinate(v, basic, tp="array"):
    x_component = scalar_mutiplication(v, basic[:, 0])
    y_component = scalar_mutiplication(v, basic[:, 1])
    if tp == "array":
        return np.array([[x_component],
                         [y_component]])
    else:
        return x_component[0], y_component[0]


def append_vector_plot(x, y, plt, color):
    z = get_projection_array(x, y)
    line1, = ax.plot(z[0], z[1], label='Using set_dashes()', color='green')
    line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    z = get_projection_array(y, x)
    line2, = ax.plot(z[1], z[0], label='Using set_dashes()', color='green')
    line2.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    ax.arrow(0, 0, x, y, head_width=0.3, head_length=0.2, fc=color, ec=color)


basis = np.array([[1, 0],
                  [0, 1]])

v1 = np.array([[1],
               [1]])
# dashes=[30, 5, 10, 5]

x, y = get_cordinate(v1, basis, "cm")
ax = plt.axes()
ax.arrow(0, 0, 10, 0, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e1 axes
ax.arrow(0, 0, 0, 10, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e2 axes
plt.xlim(-10, 10)  # show measure
plt.ylim(-10, 10)

append_vector_plot(x, y, plt, 'blue')

'''
let to create other base
'''

e1 = [1, 1]
e2 = [-1, 1]
T = np.array([e1, e2])
# to find the cordinate of x to basic e1 e2

x, y = get_cordinate(v1, T, "cm")

z = T.dot([[x],
           [y]])

append_vector_plot(z[0, 0], z[1, 0], plt, 'red')
append_line([2,4],[5,7],plt)
plt.show()

"""
let to create other basic

"""
"""
let's to make something deep 
to proof codinates on basic to another

"""
