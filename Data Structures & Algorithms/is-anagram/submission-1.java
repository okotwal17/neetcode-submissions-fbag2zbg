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
        for(HashMap.Entry<Character, Integer> entry : sMap.entrySet()){
            if(!(entry.getValue().equals(tMap.get(entry.getKey())))){
                System.out.println("Entry Key is " + entry.getKey());
                System.out.println("Entry value is " + entry.getValue());
                System.out.println("tMap value is " + tMap.get(entry.getKey()));
                return false;
            }
        }
        return true;
    }
}
