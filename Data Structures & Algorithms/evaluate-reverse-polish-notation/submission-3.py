class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:

            if ch == "*" or ch == "/" or ch=="-" or ch=="+":
                lastVal = stack.pop()
                firstVal = stack.pop()

                if ch == "*":
                    stack.append(firstVal * lastVal)
                elif ch == "+":
                    stack.append(firstVal + lastVal)
                elif ch== "-":
                    stack.append(firstVal - lastVal)
                else:
                    stack.append(int(firstVal / lastVal))


            else:
                stack.append(int(ch))

        return int(stack[0])