def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n = len(vectors[0])
    k = len(vectors)

    def cov(a,b):
        sums = []
        for i in range(len(a)):
            sums.append((a[i] - sum(a)/len(a))*(b[i]-sum(b)/len(b)))
        return sum(sums)/(n-1)

    out = []

    for i in range(k):
        row = []
        for j in range(k):
            row.append(cov(vectors[i],vectors[j]))
        out.append(row)

    return out
