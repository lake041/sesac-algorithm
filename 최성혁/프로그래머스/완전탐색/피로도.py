from itertools import permutations

def solution(k, dungeons):
    dungeon_orders = []

    for order_permutation in permutations(range(len(dungeons)), len(dungeons)):
        remaining_k = k
        visited_dungeons = 0

        for dungeon_index in order_permutation:
            required_k, used_k = dungeons[dungeon_index]

            if remaining_k >= required_k:
                visited_dungeons += 1
                remaining_k -= used_k

        dungeon_orders.append(visited_dungeons)

    return max(dungeon_orders)
