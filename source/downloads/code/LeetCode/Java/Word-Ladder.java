public class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

	HashSet<String> visited = new HashSet<String>();

	visited.add(beginWord);
	wordList.add(endWord);
	int distance = 1;
	while (!visited.contains(endWord)){
	    Set<String> toAdd = new HashSet<String>();
	    for (String each : visited){
		// All strings in visited
		for(int i=0; i<each.length(); i++){
		    char[] chars = each.toCharArray();
		    for (char ch = 'a'; ch <= 'z'; ch++){
			chars[i] = ch;
			String word = new String(chars);
			// find matched
			if(wordList.contains(word)){
			    toAdd.add(word);
			    wordList.remove(word);
			}
		    }
		}
	    }
	    distance ++;
	    if(toAdd.size()==0) return 0;
	    visited = toAdd;
	}
	return distance;
    }
}
