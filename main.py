def euclideanDistance(point1, point2):
  return ((point2[1] - point1[1])**2 + (point2[0] - point1[0])**2)**0.5

num_points = int(input("How many points do you want to calculate? "))
points = [(int(input(f"Enter the x-coordinate of point {i+1}: ")), 
          int(input(f"Enter the y-coordinate of point {i+1}: "))) 
         for i in range(num_points)]


distances = []
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    if (i * j) % (len(points) - 1) == 0: 
      dist = euclideanDistance(points[i], points[j])
      distances.append(dist)

min_distance = min(distances)
print("Minimum mesafe:", min_distance)
