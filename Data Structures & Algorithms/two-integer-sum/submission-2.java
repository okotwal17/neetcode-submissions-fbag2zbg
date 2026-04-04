class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            if(map.containsKey(difference)){
                int val = map.get(difference);
                if(val>i){
                    
                    solution[0] = i;
                    solution[1] = val;
                    return solution;
                } else {
                    solution[0] = val;
                    solution[1] = i;
                    return solution;
                }
            } else {
                map.put(nums[i],i);
            }
        }
        return solution;
    }
}
