class Stack(object):
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, o):
        self.stack.append(o)

    def pop(self):
        return self.stack.pop()

    def seak(self):
        return self.stack[-1]


class Solution(object):
    table = {')': '(', ']': '[', '}': '{'}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for c in s:
            if stack.empty() or c not in self.table or stack.seak() != self.table[c]:
                stack.push(c)
            else:
                stack.pop()
        return stack.empty()

    def valid(self, text):
        left_c = right_c = 0
        for x in ('(' + text):
            if x == '(':
                left_c += 1
            else:
                right_c += 1
        return right_c <= left_c

    def swap(self, text, swap_text=""):
        if len(swap_text) == self.length and self.isValid("(" + swap_text + ")"):
            self.texts.append("(" + swap_text + ")")
            return
        labels = set()
        for i in range(len(text)):
            if text[i] in labels or not self.valid(swap_text):
                continue
            labels.add(text[i])
            self.swap(text[:i] + text[i+1:], swap_text+text[i])

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        text = "()" * (n-1)
        self.length = len(text)
        self.texts = []
        self.swap(text)
        return self.texts
