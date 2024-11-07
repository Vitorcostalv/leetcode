class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Função auxiliar para contar o número de nós na lista
        def countNodes(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count
        
        # Função auxiliar para reverter 'k' nós
        def reverseKNodes(start, k):
            prev = None
            current = start
            for _ in range(k):
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev  # Retorna a nova cabeça do grupo revertido
        
        # Verificar se há nós suficientes para reverter
        nodeCount = countNodes(head)
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        
        while nodeCount >= k:
            # Identificar o início e o final do grupo
            groupStart = groupPrev.next
            groupEnd = groupStart
            for _ in range(k - 1):
                groupEnd = groupEnd.next
            
            # Próximo grupo
            nextGroup = groupEnd.next
            
            # Reverter o grupo atual
            groupEnd.next = None
            reversedHead = reverseKNodes(groupStart, k)
            
            # Conectar o grupo revertido com o restante da lista
            groupPrev.next = reversedHead
            groupStart.next = nextGroup
            
            # Atualizar ponteiros para o próximo grupo
            groupPrev = groupStart
            nodeCount -= k
        
        return dummy.next
