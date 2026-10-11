class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dict = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "({[":
                stack.append(char)
            elif stack and stack[-1] == par_dict[char]:
                stack.pop()
            else:
                return False

        return (len(stack) == 0)

