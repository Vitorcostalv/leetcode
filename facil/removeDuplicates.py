class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Ponteiro para a posição do último elemento único
        unique_index = 0
        
        # Iterar sobre o array começando do segundo elemento
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                # Encontrou um elemento único, move para a próxima posição
                unique_index += 1
                nums[unique_index] = nums[i]
        
        # O número de elementos únicos será unique_index + 1
        return unique_index + 1
