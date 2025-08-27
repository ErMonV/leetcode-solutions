# graphs/number_of_islands.py
from typing import List

class Solution:
    """
    LeetCode 200: Number of Islands
    Dado un grid de '1' (tierra) y '0' (agua), cuenta cuántas islas hay.
    Una isla es un conjunto de '1's conectados ortogonalmente (arriba/abajo/izq/der).

    Enfoque (DFS iterativo, marcando visitados in-place):
    - Recorremos la matriz.
    - Cada vez que vemos un '1', incrementamos el contador de islas
      y lanzamos un DFS para "inundar" (marcar como '0') toda la isla conectada.
    - Marcamos in-place para no usar memoria extra de 'visited'.

    Complejidad:
    - Tiempo: O(R * C) — cada celda se visita a lo sumo una vez.
    - Espacio: O(min(R, C)) por el stack de DFS (iterativo con lista como pila).
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(sr: int, sc: int) -> None:
            stack = [(sr, sc)]
            while stack:
                r, c = stack.pop()
                # Fuera de rango o agua ya marcada
                if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                    continue
                # Marcar como visitado (inundar)
                grid[r][c] = '0'
                # Explorar vecinos ortogonales
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands


if __name__ == "__main__":
    # Ejemplo rápido para correr localmente
    sample = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    print(Solution().numIslands(sample))  # Esperado: 1

    sample2 = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    print(Solution().numIslands(sample2))  # Esperado: 3
