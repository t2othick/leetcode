package main

import "fmt"

func strStr(haystack string, needle string) int {
	haystackLen := len(haystack)
	needleLen := len(needle)

	if needleLen == 0 {
		return 0
	}
	if needleLen > haystackLen || (needleLen == haystackLen && needle != haystack) {
		return -1
	}

	for i := 0; i <= haystackLen - needleLen; i++ {
		for j, k := i, 0; k < needleLen; {
			if haystack[j] == needle[k] {
				if k == needleLen - 1 {
					return i
				}
				j ++
				k ++
			} else {
				break
			}
		}
	}

	return -1
}

func main() {
	fmt.Println("res: ", strStr("abcd", "abcde"))
}