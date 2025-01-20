class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n  # Inicialmente, todas as crianças recebem 1 bala

        # Passagem da esquerda para a direita
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Passagem da direita para a esquerda (acumulando o resultado final)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
