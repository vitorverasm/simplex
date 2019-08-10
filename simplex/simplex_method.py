# -*- coding: utf-8 -*-
import numpy as np


class SimplexMethod():
    def __init__(self, canonical_form_problem):
        self.problem = canonical_form_problem
        self.result = self.problem.x
        self.result_cost = self.problem.get_cost()

    def run(self):
        self.problem.start_basis()
        basic_feasible_solution = self.problem.x
        reduced_costs = self.problem.get_reduced_costs()
        has_negatives = self.has_negative_value(reduced_costs)
        while has_negatives[0]:
            negative_index_chosen = np.random.choice(has_negatives[1], 1)[0]
            j = negative_index_chosen
            B_inv = np.linalg.inv(self.problem.B)
            A_j = self.problem.A[:, j].reshape(self.problem.m, 1)
            u = np.dot(B_inv, A_j)
            if len(np.where(u > 0)[0]) > 0:
                xb = self.problem.x[self.problem.basic_index]
                theta = np.divide(xb, u, out=np.zeros_like(xb), where=u > 0)
                theta_min = np.min(theta[np.nonzero(theta)])
                theta_l_idx = np.where(theta == theta_min)[0][0]
                self.problem.changeBasis(theta_min, theta_l_idx, j, u)
                reduced_costs = self.problem.get_reduced_costs()
                has_negatives = self.has_negative_value(reduced_costs)
            else:
                print('Optimal X:\n{}'.format(self.problem.x))
                print('Optimal Z(cost): -inf')

        print('Optimal X:\n{}'.format(self.problem.x))
        print('Optimal Z(cost): {}'.format(self.problem.get_cost()))

    def has_negative_value(self, array):
        return [len(np.where(array < 0)[0]) > 0, np.where(array < 0)[0]]
