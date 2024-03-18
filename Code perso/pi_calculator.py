total_points = 0
points_in_circle = 0

res = 500000000
true_res = int(res**0.5)

for y in range(true_res):
    y_true = -1 + (1/true_res) + (2*y/true_res)
    for x in range(true_res):
        x_true = -1 + (1/true_res) + (2*x/true_res)
        total_points += 1
        if (x_true)**2 + (y_true)**2 <= 1:
            points_in_circle += 1

print(points_in_circle, total_points, (points_in_circle/total_points)*4)