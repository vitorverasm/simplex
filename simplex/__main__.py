# -*- coding: utf-8 -*-
import numpy as np
from simplex.problems.canonical import Canonical

if __name__ == '__main__':
    # Definir um problema na forma normal
    c = np.transpose(np.array([-10, -12, -12, 0, 0, 0]))
    A = np.array([[1, 2, 2, 1, 0, 0], [2, 1, 2, 0, 1, 0], [2, 2, 1, 0, 0, 1]])
    b = np.transpose(np.array([20, 20, 20]))

    # Definir instancia do simplex
    canonical_form_problem = Canonical(c, A, b, "Min -10x1 -12x2 -12x3")
    # canonical_form_problem.printRepresentation()
    canonical_form_problem.startBasis()

    # Executar o algoritmo
    # Exibir a saída
