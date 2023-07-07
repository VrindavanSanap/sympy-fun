import random
import matplotlib.pyplot as plt
directions = [-1,1]
curr_loc = 0
a = [curr_loc ]
steps = 30000

for i in range(steps):
  curr_loc += random.choice(directions) 
  a.append(curr_loc)

plt.plot(a)
plt.show()
