import java.util.HashSet;
import java.util.Set;
class Solution {
    public int partitionString(String s) {
        Set<Character> seen = new HashSet<>();
        int count = 1;
        
        for (char c: s.toCharArray()) {
            if (seen.contains(c)){
                count++;
                seen.clear();
            }
            seen.add(c);
        }
        return count;

    }
}