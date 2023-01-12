"""
Ним-пасьянс
"""

stones = int(input())
while stones > 0:
    take = int(input())
    stones -= take
    print(stones)
