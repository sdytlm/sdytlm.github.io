class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        hash_map = {0:0} # <目录深度， 当前字符串长度>
        maxlen = 0

        # splitlines以'\n'划分
        for line in input.splitlines():
            # 有几个\t 就是第几层目录
            depth = line.count('\t')
            name = line.lstrip('\t')
            # 找到文件
            if '.' in name:
                maxlen = max(maxlen, hash_map[depth]+len(name))
            else:
                # "1": "/"
                hash_map[depth+1] = hash_map[depth]+len(name)+1
        return maxlen
