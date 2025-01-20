using System;

public class Solution
{
    public int MaximumSwap(int num)
    {
        char[] digitos = num.ToString().ToCharArray();
        int n = digitos.Length;

        int[] ultimo = new int[10];
        for (int i = 0; i < n; i++)
        {
            ultimo[digitos[i] - '0'] = i;
        }

        for (int i = 0; i < n; i++)
        {
            // Verificar se há um dígito maior à direita
            for (int d = 9; d > digitos[i] - '0'; d--)
            {
                if (ultimo[d] > i)
                {
                    char temp = digitos[i];
                    digitos[i] = digitos[ultimo[d]];
                    digitos[ultimo[d]] = temp;
                    return int.Parse(new string(digitos));
                }
            }
        }

        // Se nenhuma troca foi feita, o número já é o máximo
        return num;
    }
}
