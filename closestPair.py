import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force_closest_pair(points):
    n = len(points)
    min_dist = float('inf')
    pair = None

    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])

    return pair, min_dist

def closest_pair_strip(strip, d):
    min_dist = d
    pair = None
    n = len(strip)

    for i in range(n):
        for j in range(i + 1, min(i + 8, n)):
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                pair = (strip[i], strip[j])

    return pair, min_dist

def closest_pair_divide_and_conquer(points):
    n = len(points)

    if n <= 3:
        return brute_force_closest_pair(points)

    mid = n // 2
    mid_point = points[mid]

    left_pair, left_dist = closest_pair_divide_and_conquer(points[:mid])
    right_pair, right_dist = closest_pair_divide_and_conquer(points[mid:])
    
    min_dist = min(left_dist, right_dist)
    pair = left_pair if left_dist < right_dist else right_pair

    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < min_dist:
            strip.append(point)

    strip_pair, strip_dist = closest_pair_strip(strip, min_dist)

    if strip_dist < min_dist:
        return strip_pair, strip_dist
    return pair, min_dist

# Example usage
points = [(0, 0), (1, 1), (2, 2), (2, 0), (3, 1), (3, 3), (4, 2)]
points.sort()

closest_pair, distance = closest_pair_divide_and_conquer(points)
print("Closest Pair:", closest_pair)
print("Distance:", distance)
