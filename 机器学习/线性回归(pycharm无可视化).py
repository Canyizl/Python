import numpy as np

# y = wx + b
def compute_error_for_line_given_points(b, w, points):
    totalError=0
    for i in range(0,len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w*x + b))** 2
    return totalError / float(len(points))

def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(0,len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((w_current * x) + b_current))
        w_gradient += -(2 / N) * x * (y - ((w_current * x) + b_current))
    new_b = b_current - (b_gradient * learningRate)
    new_w = w_current - (w_gradient * learningRate)
    return [new_b, new_w]

def gradient_descent_runner(points, strating_b, strating_w, learningRate, num_iteration):
    b = strating_b
    w = strating_w
    for i in range(num_iteration):
        b, w = step_gradient(b, w, np.array(points), learningRate)
    return [b, w]

def run():
    points = np.genfromtxt('../data/data.txt', delimiter=' ')
    learning_rate = 0.001
    initial_b = 1
    initial_w = 1
    num_iterations = 8000
    print("Starting at b = {0}， w = {1} , error = {2}".format(initial_b, initial_w, compute_error_for_line_given_points(initial_b, initial_w, points)))
    print('Running')
    [b, w] = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations b = {1}， w = {2} , error = {3}".format(num_iterations, b, w, compute_error_for_line_given_points(b, w, points)))

run()