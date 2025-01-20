using System;

public class Solution
{
    public int MinPatches(int[] nums, int n)
    {
        long currentRange = 1; 
        int patches = 0;      
        int i = 0;            

        while (currentRange <= n)
        {
            if (i < nums.Length && nums[i] <= currentRange)
            {
                // Se o número atual pode ser usado para estender o intervalo
                currentRange += nums[i];
                i++;
            }
            else
            {
                // Adicionar um patch (número igual ao currentRange)
                currentRange += currentRange;
                patches++;
            }
        }

        return patches;
    }
}
