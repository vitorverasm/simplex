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
        self.c = c
        self.A = A
        self.b = b
        self.description = description
        self.m = b.shape[0]
        self.n = c.shape[0]
        self.x = np.zeros((self.n, 1))  # solucao basica factivel
        self.xb = np.zeros((self.m, 1))

    def startBasis(self):
        print("m:{} e n:{}".format(self.m, self.n))
        basis_index = np.sort(np.random.choice(self.n, self.m, False))
        B = self.A[:, basis_index]
        x = np.zeros((self.n, 1))
        xb = np.dot(np.linalg.inv(B), self.b)
        print("xb:\n{}".format(xb))

    def printRepresentation(self):
        """ Prints to the console the problem representation. """

        print("#########################\n"+self.description+"\n")
        print("- c: \n{}".format(self.c)+"\n")
        print("- A: \n{}".format(self.A)+"\n")
        print("- b: \n{}".format(self.b)+"\n")
        print("\n#########################")
