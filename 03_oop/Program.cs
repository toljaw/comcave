﻿int[] array1 = new int[20];
int[] array2 = new int[20];
int summe1 = 0;
int summe2 = 0;
float mittelwert1 = 0f;
float mittelwert2 = 0f;

for (int i = 0; i < array1.Length; i++)
{
    array1[i] = 5 * (i + 1);
    array2[i] = array1[i] * 2;
    summe1 += array1[i];
    summe2 += array2[i];
    mittelwert1 = summe1 / (i + 1);
    mittelwert2 = summe2 / (i + 1);
    Console.WriteLine($"Element aus array1: {array1[i]}");
    Console.WriteLine($"array1: Summe: {summe1}, Mittelwert: {mittelwert1}");
    Console.WriteLine();
    Console.WriteLine($"Element aus array2: {array2[i]}");
    Console.WriteLine($"array2: Summe: {summe2}, Mittelwert: {mittelwert2}");
    Console.WriteLine("-----------------------------");
    Console.WriteLine();
}

