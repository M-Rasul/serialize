def serialize(numbers):
    numbers.sort()
    groups = []
    current_group = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] == current_group[-1] + 1:
            current_group.append(numbers[i])
        else:
            groups.append(current_group)
            current_group = [numbers[i]]
    groups.append(current_group)
    serialized = ""
    for group in groups:
        if len(group) == 1:
            serialized += str(group[0]) + "-"
        else:
            serialized += str(group[0]) + "-" + str(group[-1]) + "-"
    return serialized[:-1]  # remove last "-"


def deserialize(serialized):
    parts = serialized.split("-")
    numbers = []
    for part in parts:
        if len(part) == 1:
            numbers.append(int(part))
        else:
            start, end = map(int, part.split())
            numbers.extend(range(start, end+1))
    return numbers