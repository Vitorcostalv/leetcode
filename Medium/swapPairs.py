class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Passo 1: Criar um nó auxiliar (dummy)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Passo 2: Iterar enquanto houver pelo menos dois nós para trocar
        while current.next and current.next.next:
            # Definir os dois nós a serem trocados
            first = current.next
            second = current.next.next
            
            # Passo 3: Trocar os nós
            first.next = second.next
            second.next = first
            current.next = second
            
            # Passo 4: Mover o ponteiro para o próximo par
            current = first
        
        # Retornar o novo início da lista
        return dummy.next
