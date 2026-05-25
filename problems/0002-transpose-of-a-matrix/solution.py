def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    l = []
    t = len(a[0])
    for i in range(t):
        k = []
        for j in a:
            k.append(j[i])
        l.append(k)
    return l
    