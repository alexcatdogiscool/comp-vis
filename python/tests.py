import math
import matplotlib.pyplot as plt


def mercator(lat, lon):
    """take lat, lon, return x,y"""

    x = lon
    y = math.log(math.tan(math.pi/4 + lat/2))

    return (x,y)



def draw_circle(lat0, lon0, radius, theta):
    d = radius  # angular distance

    lat = math.asin(
        math.sin(lat0) * math.cos(d) +
        math.cos(lat0) * math.sin(d) * math.cos(theta)
    )

    lon = lon0 + math.atan2(
        math.sin(theta) * math.sin(d) * math.cos(lat0),
        math.cos(d) - math.sin(lat0) * math.sin(lat)
    )

    return (lat, lon)

def find_sun_angle(obj_height, shadow_len):
    return math.atan(obj_height / shadow_len)

def find_declination(day):
    return -0.4092792 * math.cos(((2*math.pi) / 356) * (day + 10))



num_points = 100
circle = []# x, y mapped coords
for i in range(num_points):
    t = i * (math.tau / num_points)
    circle.append(mercator(*draw_circle(0, 2.5, 1.4, t)))

xs, ys = zip(*circle)


plt.figure()
#plt.plot(xs, ys)
plt.scatter(xs, ys)

plt.xlim(-math.pi, math.pi)
plt.ylim(-3.2, 3.2)

#plt.gca().set_aspect('equal')

plt.show()