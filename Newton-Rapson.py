# Newton-Rapson

def f(x, x_0 = 2):
    return x**2 - x_0

def f_prime(x):
    return 2*x

# Precision
accuracy = 1E-20

# Solving for (e.g. square toor of x_0, ...)
x_0 = 2

# Initial guess
x_n = 5

prev_accuracy = 0

while True:
    x_n1 = x_n - f(x_n)/f_prime(x_n)
    if abs(x_n - x_n1) < accuracy:
        break

    # Avoid starving due to unreachable accuracy
    if prev_accuracy >0 and abs(x_n - x_n1) >= prev_accuracy:
        break
    
    prev_accuracy = abs(x_n - x_n1)
    
    x_n = x_n1
    print(x_n, (x_0**(1/2) - x_n))

print(x_n)
if abs(x_n - x_n1) > accuracy:
    print("  accuracy: ",  str(accuracy), "not reached!")
                               
