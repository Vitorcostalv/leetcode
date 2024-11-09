class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def buscar(length):
            """
            Função auxiliar que retorna o índice inicial de uma substring duplicada
            do comprimento especificado. Retorna -1 se não existir tal substring.
            """
            conjunto_hash = set()
            # Base e módulo para o hash rolling
            base = 26
            mod = 2**63 - 1
            hash_value = 0
            
            # Calcula o hash da primeira substring de comprimento `length`
            for i in range(length):
                hash_value = (hash_value * base + ord(s[i]) - ord('a')) % mod
            conjunto_hash.add(hash_value)
            
            # Pré-calcula base^length % mod para atualizar o hash rolling
            base_len = pow(base, length, mod)
            
            # Aplica o hash rolling sobre o resto da string
            for i in range(1, len(s) - length + 1):
                # Remove o caractere antigo e adiciona o novo no hash rolling
                hash_value = (hash_value * base - (ord(s[i - 1]) - ord('a')) * base_len + ord(s[i + length - 1]) - ord('a')) % mod
                
                if hash_value in conjunto_hash:
                    return i
                conjunto_hash.add(hash_value)
            
            return -1

        esquerda, direita = 1, len(s) - 1
        resultado = ""
        
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            inicio = buscar(meio)
            
            if inicio != -1:
                resultado = s[inicio:inicio + meio]
                esquerda = meio + 1  # Tenta encontrar uma substring duplicada mais longa
            else:
                direita = meio - 1  # Reduz o comprimento pois não encontrou duplicata para `meio`

        return resultado
