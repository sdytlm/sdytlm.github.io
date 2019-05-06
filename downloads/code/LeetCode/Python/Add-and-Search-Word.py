class TrieNode(object):
    def __init__ (self):
        self.isWord = False
        self.children = dict()



class WordDictionary(object):

    def __init__(self):

        """
        initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):

        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child == None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

        
    def search(self, word):

        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root,word)

    def find (self, node,word):
        if word == "":
            return node.isWord

        letter = word[0]

        if letter == '.':
            for child in node.children:
                if self.find(node.children[child],word[1:]):
                    return True
        
        child = node.children.get(letter)
        if child == None:
            return False
        else:
            return self.find(child,word[1:])

        return False


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
