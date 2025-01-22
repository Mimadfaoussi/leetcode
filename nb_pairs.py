def nb_pairs(N, arr, K):
	i = 0
	nb_p = 0
	while i < N - K:
		j = i
		sum = 0
		while (j < i + K):
			sum = sum + arr[j]
			j += 1
		if sum % 2 == 0:
			nb_p += 1
		i += 1
	print(nb_p)
	if nb_p == 0:
		return (-1)
	return nb_p

if __name__ == "__main__":
	nb_pairs(8, [1,2,2,2,2,2,3,4], 2)
