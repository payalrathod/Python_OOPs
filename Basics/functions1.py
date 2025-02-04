# single parameter
def fucntion(parameter):
    print(parameter + 2)


fucntion(3)

# multiple parameter
strf = "the number"


def funct_name(p1, p2, p3):
    print(p1 + " " + str(p2) + " " + p3)


funct_name(strf, 5, "is an integer")


# default parameters
def deafu(num1=7, num2=8):
    print(num1 * num2)


deafu(3)


# return
def example(n1=4, n2=7):
    return n1 * n2


prodcut = example()
print(prodcut)


# return with expressions
def example1(n1=4, n2=7):
    return n1 * n2


print(example1() + 10)