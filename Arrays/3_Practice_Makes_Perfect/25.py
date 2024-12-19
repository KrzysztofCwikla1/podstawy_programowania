import matplotlib.pyplot as plt

x = []
y = []

for i in range(-100, 101):  #generates x values from -100 to 101
    x += [i]  

for n in x:
    y += [n ** 2 - 3]       #calculates y values for every x where y=x^2-3

print("x:", x)
print("y:", y)

plt.plot(x, y)
plt.title("Graph of y = x^2 - 3")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()