import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Passo 1: Verificar se a lista está vazia
        if not lists:
            return None
        
        # Passo 2: Criar um min-heap
        heap = []
        
        # Passo 3: Inicializar o heap com o primeiro nó de cada lista, se não estiver vazia
        for i in range(len(lists)):
            if lists[i]:
                # Inserindo o valor do nó, o índice da lista e o próprio nó no heap
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # Passo 4: Criar um nó cabeça (dummy) para ajudar a construir a lista resultante
        dummy = ListNode()
        current = dummy
        
        # Passo 5: Processar o heap até que esteja vazio
        while heap:
            # Extrair o menor elemento do heap
            val, i, node = heapq.heappop(heap)
            
            # Conectar o nó extraído ao final da lista resultante
            current.next = node
            current = current.next
            
            # Avançar para o próximo nó na lista do índice i
            if node.next:
                # Inserir o próximo nó no heap
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        # Retornar a lista resultante, ignorando o nó cabeça
        return dummy.next
