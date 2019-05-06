# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        size = len(points)
        if size == 0:
            return 0

        ret = 0
        for x in range(size):
            # hash_map: <pb.y-pa.y/pb.x-pa.x, 出现次数>
            hash_map = {}
            # 和x相同的点
            equalNum = 0 
            for y in range(x+1, size):
                if self.isEqual(points[x],points[y]):
                    equalNum += 1
                else:
                    # 计算斜率
                    k = self.getK(points[x],points[y])
                    if hash_map.get(k) == None:
                        hash_map[k] = 1
                    else:
                        hash_map[k] += 1
            val = 0
            if hash_map:
                val = max(hash_map.values())
            ret = max(ret, val+equalNum+1)
        return ret
    # 判断两个点是否相同
    def isEqual(self, pa, pb):
        return pa.x == pb.x and pa.y == pb.y
    
    # 计算斜率
    def getK(self, pa, pb):
        if pa.x == pb.x:
            return None
        return 1.0* (pb.y-pa.y)/(pb.x-pa.x)
