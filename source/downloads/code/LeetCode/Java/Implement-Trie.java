class TrieNode {
    boolean isEnd;
    TrieNode[] children;
    // Initialize your data structure here.
    public TrieNode() {
        isEnd = true;
        children = new TrieNode[26];
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode cur = root;
        for (int i=0; i<word.length(); i++){
            int index = word.charAt(i)-'a';
            if(cur.children[index]==null){
                cur.children[index] = new TrieNode();
                cur.children[index].isEnd = false;
            }
            cur = cur.children[index];
        }
        cur.isEnd = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        return search(word, 1);
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        return search(prefix, 2);
    }

    public boolean search(String word, int type){
    // Type: 1: search, 2: startsWith
        TrieNode current = root;
        for(int i=0; i<word.length(); i++){
            int index = word.charAt(i)-'a';
            if(current.children[index] == null) return false;
            else
                current = current.children[index];
        
        }
        return type==1 ? current.isEnd : true;    
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
