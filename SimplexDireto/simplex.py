import numpy as np

class Simplex():
    def __init__(self):
        self.c = np.transpose(np.array([-10, -12, -12, 0, 0, 0]))
        self.A = np.array([[1, 2, 2, 1, 0, 0], [2, 1, 2, 0, 1, 0], [2, 2, 1, 0, 0, 1]])
        self.b = np.transpose(np.array([20, 20, 20]))
        self.j = 10000
        self.m = self.b.shape[0]
        self.n = self.c.shape[0]
        self.basic_index = np.zeros((1, self.m))
        self.B = np.zeros((self.m, self.m))
        self.x = np.zeros((self.n, 1))
        self.xb = np.zeros((1, self.m))
        self.u = 0

    def run(self):
