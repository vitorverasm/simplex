# -*- coding: utf-8 -*-


class SimplexMethod():
    def __init__(self, canonical_form_problem):
        self.problem = canonical_form_problem
        self.result = self.problem.x
        self.result_cost = self.problem.get_cost()

    def run(self):
        self.problem.start_basis()
        basic_feasible_solution = self.problem.x
        self.problem.get_reduced_costs()
