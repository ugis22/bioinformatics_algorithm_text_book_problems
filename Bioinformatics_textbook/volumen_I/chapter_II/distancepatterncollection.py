import numpy as np

with open('rosalind_ba2h.txt') as file:
	i = 0
	dna = []

	for line in file.read().splitlines():
		if i == 0:
			pattern = line.strip()
		else:
			dna.append(line)
		i += 1
file.close()

dna = dna[0].split()

def number_to_symbol(index):
	symbols_list = {
		0 : 'A',
		1 : 'C',
		2 : 'G',
		3 : 'T',
	}
	return symbols_list[index]


def numbertopattern(index, k):
	if k == 1:
		return number_to_symbol(index)
	prefix_index = index // 4
	rest = index % 4
	symbol = number_to_symbol(rest)
	prefix_pattern = numbertopattern(prefix_index, k-1)
	return prefix_pattern + symbol	


def distance_ha(a,b):
	distance = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			distance += 1
	return distance

def hamming_distance(pattern, dna):
	k = len(pattern)
	distance = 0

	for string in dna:
		hamming = np.inf
		for i in range(len(string)-k+1):
			pattern_prima = string[i:i+k]
			a = distance_ha(pattern, pattern_prima)
			if hamming > a:
				hamming = a
		distance += hamming
	return distance

a = hamming_distance(pattern, dna)
print(a)

