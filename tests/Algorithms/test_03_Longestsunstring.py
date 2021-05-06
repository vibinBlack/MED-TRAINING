def atLeastK(freq, k) :

	for i in range(26) :

		if (freq[i] != 0 and freq[i] < k) :
			return False;
	
	return True;

def findlength(string,k) :
	n=len(string)
	maxLen = 0;

	freq = [0]*26;

	for i in range(n) :
		freq = [0]*26;

		for j in range(i,n) :
			freq[ord(string[j]) - ord('a')] += 1;

			if (atLeastK(freq, k)) :
				maxLen = max(maxLen, j - i + 1);
		
	return maxLen;



def test_case1():
	assert findlength("ababbc",2) == 5

def test_case2():
	assert findlength("ababbc", 6) == 0

def test_case3():
	assert findlength("string", 2) == 0

def test_case4():
	assert findlength("ababbc", 1) == 6
	
	

