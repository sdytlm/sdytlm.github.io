class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row = len(board)
        col = len(board[0])
        trie = Trie()
        # 把words里的单词插入TRIE
        for word in words:
            trie.insert(word)

        # 用来记录这个坐标是否被访问
        visited = [[False] * col for x in range(row)]
        # 用来控制方向
        dz = zip([1,0,-1,0],[0,1,0,-1])
        ret = []

        # 深度优先遍历board
        def dfs(word,node,x,y):
            node = node.children.get(board[x][y])
            # 这个坐标不是TRIE中当前node的资节点
            if node is None:
                return
            visited[x][y] = True
            # 深度遍历board，直到某个坐标不在Trie中
            for z in dz:
                nx, ny = x+z[0], y+z[1]
                if nx >=0 and nx <row and ny >= 0 and ny < col and not visited[nx][ny]:
                    dfs(word+board[nx][ny], node,nx,ny)
            # 若发现word
            if node.isWord == True:
                ret.append(word)
                trie.delete(word)
            visited[x][y] = False
        
        # 主函数开始
        for x in range(row):
            for y in range(col):
                dfs(board[x][y], trie.root,x,y)
        return sorted(ret)


class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def delete(self, word):
        node = self.root
        queue = [] # <letter:node> 记录要删除哪些node
        for letter in word:
            queue.append((letter,node))
            child = node.children.get(letter)
            # 要删除的word不在tri中
            if child is None:
                return False
            node = child
        # 要删除的word在tri中，但不是一个词
        if node.isWord == False:
            return False
        # 要删除的word找到，且这个节点有儿子
        if len(node.children):
            node.isWord = False
        else:
        # 最复杂的情况，要删除的节点没有字节点，需要按照queue的轨迹依次往上删除
            for letter, node in reversed(queue):
                del node.children[letter]
                # 要一直删除直到某个节点有儿子，或者他是词
                if len(node.children) or node.isWord:
                    break
        return True
