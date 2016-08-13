class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            for i in uglies:
                yield i*prime

        merged = heapq.merge(*map(gen,[2,3,5]))
        while len(uglies)<n:
            val = next(merged)
            if val != uglies[-1]:
                uglies.append(val)
        return uglies[-1]
        
