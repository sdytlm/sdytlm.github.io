# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.array = []
        
        def fill(nl):
            for ni in nl:
                # 找到一个integer
                if ni.isInteger():
                    self.array.append(ni.getInteger())
                else:
                    # 找到一个List[NestedInteger]
                    fill(ni.getList())
        
        fill(nestedList)
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        i = self.index
        self.index += 1
        return self.array[i]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index<len(self.array)
