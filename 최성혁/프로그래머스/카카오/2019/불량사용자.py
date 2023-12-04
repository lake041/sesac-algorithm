from itertools import product

def solution(user_id, banned_id):
    def is_match(u_id, b_id):
        return all(ui == bi or bi == '*' for ui, bi in zip(u_id, b_id))

    answer = set()
    candidates = [set()]

    for b_id in banned_id:
        new_candidates = []
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue

            if is_match(u_id, b_id):
                new_candidates.extend({*c, u_id} for c in candidates if u_id not in c)

        candidates = new_candidates

    for c in candidates:
        answer.add(tuple(sorted(c)))

    return len(answer)

