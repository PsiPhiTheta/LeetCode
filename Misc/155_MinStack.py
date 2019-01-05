class MinStack(object):

    def __init__(self):
        self.mystack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.mystack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.mystack.pop()

    def top(self):
        """
        :rtype: int
        """
        n = len(self.mystack)
        return self.mystack[n-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.mystack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
