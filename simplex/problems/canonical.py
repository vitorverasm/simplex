# -*- coding: utf-8 -*-
import numpy as np


class Canonical():
    """
    This class represents the modeling of a LP problem
    in the canonical form.

    - [vector] c: coefficients from Z objective function.
    - [matrix] A: coefficients from problem restrictions.
    - [vector] b: values of the right hand side of the restrictions.
    - [string] description: optional description of the problem
    - [int] m: number of restriction
    - [int] n: number of variables
    """

    def __init__(self, c, A, b, description="Canonical form problem"):
        self.c = np.expand_dims(c, axis=0)
        self.A = A
        self.b = b
        self.description = description
        self.m = b.shape[0]
        self.n = c.shape[0]
        self.basic_index = np.zeros((1, self.m))
        self.nonbasic_index = np.zeros((1, self.n - self.m))
        self.B = np.zeros((self.m, self.m))
        self.x = np.zeros((self.n, 1))
        self.xb = np.zeros((1, self.m))

    def get_cost(self):
        """ Compute the value of the cost function:(c'x). """
        return np.dot(self.c, self.x)[0]

    def start_basis(self):
        """
        This function starts the problem basis structure with
        the following steps:
        1. Choose basic_index (from n variables choose m)
        and store their indexes
        2. Create B containing m columns of A
        (only the columns with index in basic_index, Square matrix)
        3. Calculate xb with the cost of the basic variables
        (xb = Bˆ-1 * b)
        4. Calculate x with values:
        if x_i basic take value from xb_i, otherwise take 0
        """
        xb = np.full((1, self.m), -1.0)
        cb = np.zeros((self.m, 1))
        while len(np.where(xb <= 0)[0]) > 0:
            basic_index = np.sort(np.random.choice(self.n, self.m, False))
            B = self.A[:, basic_index]
            xb = np.dot(np.linalg.inv(B), self.b)

        x = np.zeros((self.n, 1))
        for idx, x_i in np.ndenumerate(basic_index):
            x[x_i] = xb[idx[0]]

        self.basic_index = basic_index
        self.B = B
        self.xb = xb
        self.x = x
        self.cb = self.c[:, basic_index]

    # TODO: BUGADO AQ TO FAZENO AINDA
    def get_reduced_costs(self):
        nonbasic_index = np.setdiff1d(
            np.arange(self.n), self.basic_index).reshape(1, self.m)[0]
        reduced_cost = np.zeros(nonbasic_index.size)
        for idx, nb_idx in np.ndenumerate(nonbasic_index):
            c_j = self.c[0, nb_idx]
            B_inv = np.linalg.inv(self.B)
            A_j = self.A[:, nb_idx].reshape(self.m, 1)
            reduced_cost[idx] = c_j - np.dot(np.dot(self.cb, B_inv), A_j)[0]
        self.nonbasic_index = nonbasic_index
        return reduced_cost

    def changeBasis(self, theta_min, theta_l_idx, j, u):
        new_basis = self.basic_index
        l = new_basis[theta_l_idx]
        new_basis[theta_l_idx] = j
        B = self.A[:, new_basis]

        xb = self.xb.reshape(3, 1) - np.dot(theta_min, u)
        x = self.x
        x[j] = theta_min
        x[l] = 0
        self.basic_index = new_basis
        self.B = B
        self.xb = xb
        self.x = x

    def print_representation(self):
        """ Prints to the console the problem representation. """

        print("#########################\n"+self.description+"\n")
        print("- c: \n{}".format(self.c)+"\n")
        print("- A: \n{}".format(self.A)+"\n")
        print("- b: \n{}".format(self.b)+"\n")
        print("\n#########################")
