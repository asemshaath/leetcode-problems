class Solution {
    public int firstUniqChar(String s) {
        
        HashMap<Character, Integer> letters = new HashMap<Character, Integer>();

        for(int i = 0; i < s.length(); i++){

            char a = s.charAt(i);
            letters.put(a, letters.getOrDefault(a, 0) + 1);
        }


        for (int i = 0; i < s.length(); i++){

            if (letters.get(s.charAt(i)) == 1)
                return i;

        }

        return -1;
    }
}
