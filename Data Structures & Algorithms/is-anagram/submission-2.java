class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            sMap.merge(s.charAt(i),1,Integer::sum);
            tMap.merge(t.charAt(i),1,Integer::sum);
        }
        return sMap.equals(tMap);
    }
}
