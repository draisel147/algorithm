def optimal_bst(P):
    n = len(P)
    C = [[0] * (n + 1) for _ in range(n + 2)]
    R = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        C[i][i - 1] = 0
        C[i][i] = P[i - 1]
        R[i][i] = i
        R[i][i - 1] = 0

    C[n + 1][n] = 0
    R[n + 1][n] = 0

    for d in range(1, n):
        for i in range(1, n - d + 1):
            j = i + d
            minval = float('inf')
            for k in range(i, j + 1):
                if C[i][k - 1] + C[k + 1][j] < minval:
                    minval = C[i][k - 1] + C[k + 1][j]
                    kmin = k
            R[i][j] = kmin
            sum_p = sum(P[i - 1:j])
            C[i][j] = minval + sum_p

    return C[1][n], R

# การใช้งานตัวอย่าง:
P = [0.1, 0.2, 0.4, 0.3]
avg_comparisons, optimal_tree = optimal_bst(P)
print("จำนวนการเปรียบเทียบเฉลี่ย:", avg_comparisons)
print("โครงสร้างต้นไม้ BST ที่เหมาะที่สุด (R):")
for row in optimal_tree:
    print(row)