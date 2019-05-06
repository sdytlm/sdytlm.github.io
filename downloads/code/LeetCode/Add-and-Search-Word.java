public class WordDictionary {
    // TrieNode class
    public class TrieNode {
	public TrieNode[] children = new TrieNode[26];
	public String item = ""; // this node is a word, if item not null
    }
    private TrieNode root = new TrieNode();
    /** Initialize your data structure here. */
    public WordDictionary() {

    }

    /** Adds a word into the data structure. */
    public void addWord(String word) {
	TrieNode node = root;
	for(char c : word.toCharArray()){
	    if(node.children[c-'a']==null){
		node.children[c-'a'] = new TrieNode();
	    }
	    node = node.children[c-'a'];
	}
	node.item = word;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
	return match(word.toCharArray(), 0, root);
    }

    private boolean match(char[] ch, int k, TrieNode node){
	if(k==ch.length) return !node.item.equals("");
	if (ch[k]!='.')
	    return node.children[ch[k]-'a']!=null && match(ch, k+1, node.children[ch[k]-'a']);
	else{
	    // consider a buntch of '.'
	    for(int i=0; i<node.children.length; i++){
		if (node.children[i] != null && match(ch, k+1, node.children[i]))
		    return true;
	    }
	}
	return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
