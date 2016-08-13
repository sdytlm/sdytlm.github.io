import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        # merged: priority queue iterative
        merged = heapq.merge(*map(gen,primes))
         
        while len(uglies) < n:
            # current minimal value in merged, after uglies is appended.
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

if __name__ == "__main__":
    sol =Solution()
    sol.nthSuperUglyNumber(12,[2,3,5,7])

