def floyd_warshall(W):
    n = len(W)
    D = [row[:] for row in W]  # Copy the input matrix to initialize D

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update the shortest path distance if a shorter path is found
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

    return D


# Example usage with a weighted graph represented as a matrix
W = [
    [0, 12, 7, 10, 14],
    [4, 0, 13, 11, 12],
    [10, 1, 0, 4, 7],
    [14, 2, 13, 0, 2],
    [4, 15, 11, 15, 0]
]

result = floyd_warshall(W)
for row in result:
    print(row)