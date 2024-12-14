l_nums = []
r_nums = []

with open('input', 'r') as file:
    for line in file:
        _line = line.strip()
        left, right = ' '.join(_line.split()).split()

        left = int(left)
        right = int(right)

        l_nums.append(left)
        r_nums.append(right)

    l_nums.sort()
    r_nums.sort()

    distances = []

    for index, l in enumerate(l_nums):
        r = r_nums[index]
        cur_distance = l - r

        distances.append(abs(cur_distance))

    print(sum(distances))

