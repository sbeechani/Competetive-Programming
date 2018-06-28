import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    // implement a trie and use it to efficiently store string
    

    static class Trie {
        
        Node mroot;
        
        Trie(){
           mroot = new Node(); 
        }
        
        
        private static class Node
        {
         boolean isend = false;
         private Node[] child = new Node[26];
        }
        
        public boolean addWord(String word) {
            Node root = mroot;
            int l = word.length();
            for (int i=0;i<l;i++)
            {
                int j = (int)word.charAt(i)-'a';
                if(root.child[j]!=null){
                    root = root.child[j];
                }
                else{
                    root.child[j]=new Node();
                    root = root.child[j];
                }
                    
            }
            if(root.isend == false){
                 root.isend = true;
                return true;
            }
            return false;
        }
    }


















    // tests

    @Test
    public void trieTest() {
        final Trie trie = new Trie();

        boolean result = trie.addWord("catch");
        assertTrue(result);

        result = trie.addWord("cakes");
        assertTrue(result);

        result = trie.addWord("cake");
        assertTrue(result);

        result = trie.addWord("cake");
        assertFalse(result);

        result = trie.addWord("caked");
        assertTrue(result);

        result = trie.addWord("catch");
        assertFalse(result);

        result = trie.addWord("");
        assertTrue(result);

        result = trie.addWord("");
        assertFalse(result);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}