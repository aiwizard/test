import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('First plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.set_dpi(300)
fig.savefig('first_plot.png')
plt.show()
