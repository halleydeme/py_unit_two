# Use this file to calculate the amount of compound interest. Follow the instructions on the
# Variables and Expressions sheet carefully.
p = 10000
n = 12
r = .08
t = 10
A = p * (1 + r/n) ** (n*t)

print( "The amount of compound interest is", A)