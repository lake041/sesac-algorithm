def solution(files):
    answer = []

    parsed_files = []

    for file_idx, file in enumerate(files):
        head, number, _ = file.split(maxsplit=2)
        parsed_files.append((head.lower(), number.zfill(5), str(file_idx).zfill(4)))

    parsed_files.sort()

    for _, _, order in parsed_files:
        answer.append(files[int(order)])

    return answer
