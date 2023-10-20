import matplotlib.pyplot as plt

from random_walk import RandomWalk

points_ = input("Enter number of points:" )


if points_ == '':
    points_ = 5000
    rw = RandomWalk(num_points=points_)
else:
    rw = RandomWalk(num_points = int(points_))

rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,10))

points_number = range(rw.num_points)

ax.plot(rw.x_values, rw.y_values, color='Purple', linewidth = 0.5)


#Show points to start and end points
ax.scatter(0 , 0, c='Green', edgecolors='none', s=int(points_)/20)
ax.scatter(rw.x_values[-1] , rw.y_values[-1], c='Blue', edgecolors='none', s=int(points_)/20)

ax.set_aspect('equal')

#Remove axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()