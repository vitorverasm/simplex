import numpy as np

class Simplex():
    def __init__(self):
        self.A = np.array([[1, 1, 1, 1, 0, 0], [2, 1, -1, 0, 1, 0], [3, 2, -1, 0, 0, 1]])
        self.b = np.transpose(np.array([40, 20, 30]))
        self.c = np.transpose(np.array([-2, -3, -1, 0, 0, 0]))
        self.base = np.array([2, 3, 4])
        self.j = 10000
        self.m = self.b.shape[0]
        self.n = self.c.shape[0]
        self.basic_index = np.zeros((1, self.m))
        self.B = np.zeros((self.m, self.m))
        self.x = np.zeros((self.n, 1))
        self.xb = np.zeros((1, self.m))
        self.u = 0
        self.z = 0
        self.cb = np.zeros((1, self.n))

    def run(self):
        self.c = np.expand_dims(self.c, axis=0)

        #Passo 1
        # print('A = \n', self.A)
        # print('m = \n', self.m)
        # print('n = \n', self.n)

        self.B = self.A[:, self.base]
        # print('B = \n',self.B)
        # print('c = \n', self.c)

        #Passo 2
        c=0
        while 1:
            print(c+1)
            c+= 1
            self.xb = np.dot(np.linalg.inv(self.B), self.b) #X da Base
            self.z = self.c - np.dot(np.dot(self.c[:, self.base], np.linalg.inv(self.B)), self.A)
            # print('xb = \n', self.xb)
            # print('B = \n', self.B)
            #print('z = \n', self.z.shape)
            negIndexx, negIndexy = np.where(self.z < 0)
            if(len(negIndexy)> 0):
                self.j = negIndexy[0]
            else:
                print('Valor Ótimo encontrado! \n', self.x)
                break
            #print('J = \n', self.j)
            #print('z = \n', self.z[0, self.j])

            #Passo 3
            self.u = np.dot(np.linalg.inv(self.B), self.A[:,self.j])
            #print('u= ', self.u)
            posIndex = np.where(self.u > 0)
            print("IndexPositivo", posIndex[0][0])
            #Passo 4
            if (len(posIndex) > 0):
                var = []
                for i in posIndex:
                    var.append(self.xb[i]/self.u[i])
                theta = min(var)
                index = np.where(var == theta)
                print(theta, index[0][0])
                l = posIndex[0][0]
            else:
                print('O custo ótimo é -infinito')
                break

            #Passo 5
            if c == 0:
                self.u = np.expand_dims(self.u, axis=0)
                self.xb = np.expand_dims(self.xb, axis=0)
                theta = np.expand_dims(theta, axis=0)
            print('shape xb', self.xb.shape)
            print('shape u', self.u.shape)
            print('shape theta', theta.shape)

            self.xb = self.xb - self.u.T * theta
            self.base[l] = self.j
            self.B = self.A[:, self.base]
            self.x[self.j] = theta
