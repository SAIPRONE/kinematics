# -*- coding: utf-8 -*-
"""
@author: saibrone
"""
import numpy as np
import random

# Dimension of problem (6 DOF)
dim = 6

class FruitFly:
    def __init__(self):
        self.position = np.array([random.uniform(-np.pi, np.pi) for _ in range(dim)])
        self.smell = None

    def evaluate(self, end_effector_func, desired_position):
        current_position = end_effector_func(self.position)
        self.smell = np.linalg.norm(desired_position - current_position)

    def fly(self, best_position):
        self.position = np.array([random.gauss(mu, 1) for mu in best_position])

def FOA(end_effector_func, desired_position, pop_size, max_iter):
    population = [FruitFly() for _ in range(pop_size)]
    for fly in population:
        fly.evaluate(end_effector_func, desired_position)

    best_fly = min(population, key=lambda x: x.smell)

    for _ in range(max_iter):
        for fly in population:
            fly.fly(best_fly.position)
            fly.evaluate(end_effector_func, desired_position)

        current_best = min(population, key=lambda x: x.smell)
        if current_best.smell < best_fly.smell:
            best_fly = current_best

    return best_fly.position, best_fly.smell
def end_effector_func(theta):
    # Denavit-Hartenberg parameters
    # For a generic 6 DOF robot these would need to be replaced with the actual values
    d = [0, 0, 0, 0, 0, 0]
    a = [0, 0, 0, 0, 0, 0]
    alpha = [0, 0, 0, 0, 0, 0]

    # Compute transformation matrices
    T = []
    for i in range(6):
        A = [[np.cos(theta[i]), -np.sin(theta[i])*np.cos(alpha[i]), np.sin(theta[i])*np.sin(alpha[i]), a[i]*np.cos(theta[i])],
             [np.sin(theta[i]), np.cos(theta[i])*np.cos(alpha[i]), -np.cos(theta[i])*np.sin(alpha[i]), a[i]*np.sin(theta[i])],
             [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
             [0, 0, 0, 1]]
        T.append(np.array(A))

    # Compute end effector position
    T_total = np.linalg.multi_dot(T)
    position = T_total[:3, 3]
    return position

