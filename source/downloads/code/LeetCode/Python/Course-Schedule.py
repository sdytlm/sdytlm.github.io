class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites == None:
            return True
        course = [x for x in range(numCourses)]
        hash_map = [0]*numCourses # out-degree of each node
        children = [[] for x in range(numCourses)] # children set of each node
        # init hash_map and children
        for i,j in prerequisites:
            hash_map[i] += 1
            children[j].append(i)
        
        while len(course) != 0:
            # find the node without outdegree
            remove_list = []
            flag = False
            for x in course:
                # find pre-course
                if hash_map[x] == 0:
                    # update hash_map
                    for child in children[x]:
                        hash_map[child] -= 1
                    flag = True
                    remove_list.append(x)

            if flag == False:
                return False
            
            for x in remove_list:
                course.remove(x)
        return True
