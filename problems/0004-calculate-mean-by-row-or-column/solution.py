def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	means = []
	if mode == 'column':
		for i in range(len(matrix[0])):
			s = 0
			t = 0
			for j in matrix:
				s+=j[i]
				t+=1
			means.append(s/t)
	else:
		for i in matrix:
			means.append(sum(i)/len(matrix[0]))

	return means