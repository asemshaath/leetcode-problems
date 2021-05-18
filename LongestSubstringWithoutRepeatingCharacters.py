def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set()

        left = 0
        right = 0
        lettersCount = 0

        while right < len(s):
        
            if s[right] not in letters:
                letters.add(s[right])
                right += 1
                
                if lettersCount <= len(letters):
                    lettersCount = len(letters)
                    
            else:
                letters.remove(s[left])
                left += 1
                
        return lettersCount
