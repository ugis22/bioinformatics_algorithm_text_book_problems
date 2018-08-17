def distance(a,b):
	distance = 0
	
	for i in range(len(a)):
		if a[i] != b[i]:
			distance += 1
	return distance


def neighbors(pattern, d):
	nucleotides = ['A', 'C', 'G', 'T']
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return nucleotides

	neighborhood = set()
	suffixneigh = neighbors(pattern[1:], d)

	for text in suffixneigh:
		if distance(pattern[1:], text) < d:
			for j in nucleotides:
				neighborhood.add(j+text)
		else:
			neighborhood.add(pattern[0]+text)
	return neighborhood

def motifenumeration(dna, k, d):
	patterns = set()
	kmers =[]

	for pattern in dna:
		for i in range(len(pattern) + k -1):
			kmers.append(neighbors(pattern[i:i+k], d))


	
	for kmer in kmers:
		mydict = {}
		for pattern in dna:
			for i in range(len(pattern)-k+1):
				if distance(kmer, pattern[i:i+k]) <= d:
					mydict.setdefault(pattern, []).append(kmer)
		if len(mydict.keys()) == len(dna):
			patterns.add(kmer)
	return patterns


