from codet5 import *

code = """### COCI 2023 #3 - AN2DL

def preprocess(matrix, n, m, r, s):
    row_max = [[0] * (m-s+1) for _ in range(n)]
    for i in range(n):
        q = []
        for j in range(m):
            while q and (q[0] < j - s + 1):
                q.pop(0)
            while q and matrix[i][q[-1]] < matrix[i][j]:
                q.pop()
            q.append(j)
            if j >= s - 1:
                row_max[i][j-s+1] = matrix[i][q[0]]

    max_submatrix = [[0] * (m-s+1) for _ in range(n-r+1)]
    for j in range(m-s+1):
        q = []
        for i in range(n):
            while q and (q[0] < i - r + 1):
                q.pop(0)
            while q and row_max[q[-1]][j] < row_max[i][j]:
                q.pop()
            q.append(i)
            if i >= r - 1:
                max_submatrix[i-r+1][j] = row_max[q[0]][j]
    
    return max_submatrix

def print_max_submatrix(preprocessed, n, m, r, s):
    for i in range(n - r + 1):
        for j in range(m - s + 1):
            print(preprocessed[i][j], end=' ')
        print()

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
r, s = map(int, input().split())

max_submatrix = preprocess(matrix, n, m, r, s)
print_max_submatrix(max_submatrix, n, m, r, s)"""

if __name__ == '__main__':
    model = CodeT5().summarize_by_line(code)

    print(model)