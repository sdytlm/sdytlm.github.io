class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        print nodes
        diff=1
        for i in range(len(nodes)):
            diff -= 1
            if diff < 0:
                return False

            if nodes[i] != '#':
                diff += 2
        print diff
        if diff == 0:
            return True
        else:
            return False
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

