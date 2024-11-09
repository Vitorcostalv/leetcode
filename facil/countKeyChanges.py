class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        key_changes = 0
      
        previous_key = s[0].lower()
        
        for i in range(1, len(s)):
            current_key = s[i].lower() 
            if current_key != previous_key:
                key_changes += 1 
                previous_key = current_key  
                
        return key_changes
