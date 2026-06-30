# ==========================
# # Q8
#  (Main Program)
# ==========================

import task4_1 as mymodule

name = input("Enter your name: ")
mymodule.greet(name)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = mymodule.calculate_power(base, exp)
print("Result:", result)