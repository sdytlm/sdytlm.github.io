class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # degree of each node
        degrees = [0]*numCourses
        # children nodes of each node
        childs = [[] for x in range(numCourses)]
        for i,j in prerequisites:
            degrees[i] += 1
            childs[j].append(i)
        # course set
        courses = [x for x in range(numCourses)]
        flag = True
        ret = []

        while flag and len(courses):
            flag = False
            removeList = []
            # find the node whose outdegree is 0
            for x in courses:
                if degrees[x] == 0:
                    # update the degree of x's childs
                    for child in childs[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    flag = True
            # update courses list and add x in to ret
            for x in removeList:
                ret.append(x)
                courses.remove(x)
        # cannot learn
        if len(courses) != 0:
            return []
        else:
            return ret
