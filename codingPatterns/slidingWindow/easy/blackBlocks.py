class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        minRec = float("inf")

        for i in range(n - k + 1):
            count = 0
            for j in range(i, i + k):
                if blocks[j] == "W":
                    count += 1
            minRec = min(minRec, count)
        return minRec


# WBBWWBBWBW 7
