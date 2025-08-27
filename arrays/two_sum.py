"""
LeetCode 1: Two Sum
Tema: Arrays / Hash Map
Dificultad: Easy
Link: https://leetcode.com/problems/two-sum/

Estrategia:
- Uso un diccionario (hash map) para guardar los números vistos y sus índices.
- En cada iteración verifico si el complemento ya existe en el diccionario.

Complejidad:
- Tiempo: O(n)
- Espacio: O(n)
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
