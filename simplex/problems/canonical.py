class Canonical():
    """
    This class represents the modeling of a LP problem
    in the canonical form.

    - [vector] c: coefficients from Z objective function.
    - [matrix] A: coefficients from problem restrictions.
    - [vector] b: values of the right hand side of the restrictions.
    """

    def __init__(self, c, A, b, description="Canonical form problem"):
        self.c = c
        self.A = A
        self.b = b
        self.description = description

    def printRepresentation(self):
        """ Prints to the console the problem representation. """

        print("#########################\n"+self.description+"\n")
        print("- c: \n{}".format(self.c)+"\n")
        print("- A: \n{}".format(self.A)+"\n")
        print("- b: \n{}".format(self.b)+"\n")
        print("\n#########################")
