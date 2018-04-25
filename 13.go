func romanToInt(s string) int {
	dict := map[uint8]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	length := len(s)
	i := length - 1
	num := 0
	for ; i > 0; {
		if dict[s[i-1]] < dict[s[i]] {
			num += dict[s[i]] - dict[s[i-1]]
			i -= 2
		} else {
			num += dict[s[i]]
			i -= 1
		}
	}

	if i == 0 {
		num += dict[s[i]]
	}

	return num
}
