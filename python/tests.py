import math
import matplotlib.pyplot as plt
from datetime import datetime, time


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

def time_to_float(dt):
    """Convert a datetime or time object to a float in range [0, 1)."""
    if isinstance(dt, datetime):
        t = dt.time()
    elif isinstance(dt, time):
        t = dt
    else:
        raise ValueError("Input must be a datetime or time object")

    # Total seconds in a day
    total_seconds = 24 * 60 * 60
    # Seconds since midnight
    seconds_since_midnight = t.hour * 3600 + t.minute * 60 + t.second + t.microsecond / 1_000_000
    # Normalize
    return seconds_since_midnight / total_seconds


def time_str_to_float(time_str):
    t = datetime.strptime(time_str, "%H:%M").time()
    return time_to_float(t)


def find_sun_angle(obj_height, shadow_len):
    return math.atan(obj_height / shadow_len)


def find_declination(day):
    return math.radians(-23.44 * math.cos(math.radians((360/365) * (day + 10))))


def find_solar_pos(day, time):
    lat = find_declination(day)
    lon = math.pi - time_str_to_float(time) * math.pi*2

    return (lat, lon)



print([math.degrees(p) for p in find_solar_pos(75, "5:00")])


"""
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
"""