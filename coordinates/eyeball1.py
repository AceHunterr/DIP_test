import math
x = [104.00605827569962, 101.1019729077816,
     104.99933257699013, 107.76771202683449]
y = [78.92935824394226, 79.51172590255737,
     83.10595142841339, 82.7933120727539]
mean_x = (x[0]+x[2])/2
mean_y = (y[0]+y[2])/2
print(mean_x, mean_y)
radius = math.sqrt(math.pow(mean_x-x[1], 2)+math.pow(mean_y-y[1], 2))
print(radius)

# point_x = mean_x+radius*math.cos(0.017453)
# point_y = mean_y+radius*math.sin(0.017453)

# print(point_x, point_y)
X = []
Y = []
i = 270
while(i <= 360):
    j = math.radians(i)
    point_x = mean_x+radius*math.cos(j)
    point_y = mean_y+radius*math.sin(j)
    X.append(point_x)
    Y.append(point_y)
    i += 1
i = 0
while(i < 270):
    j = math.radians(i)
    point_x = mean_x+radius*math.cos(j)
    point_y = mean_y+radius*math.sin(j)
    X.append(point_x)
    Y.append(point_y)
    i += 1
# print(X)
# print(Y)
L = len(X)
L1 = len(Y)
print(L, L1)
i = 0
while(i < L):
    print('{ x:', X[i], ', y:', Y[i], '},')
    i = i+1
