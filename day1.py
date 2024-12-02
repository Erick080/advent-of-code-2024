import os

arr_ids1 = []
arr_ids2 = []

def part_1() -> int:
    sum_distance = 0

    for i in range(0, len(arr_ids1)):
        distance = arr_ids1[i] - arr_ids2[i]
        if distance < 0: 
            distance *= -1
        sum_distance += distance
    
    return sum_distance

def part_2() -> int:
    similarity_score = 0
    for id_1 in arr_ids1:
        similarity = 0
        for id_2 in arr_ids2:
            if (id_1 < id_2):
                break
            elif (id_1 == id_2):
                similarity += 1
            else:
                continue
        similarity_score += (id_1 * similarity)

    return similarity_score

    
with open(os.path.join("inputs", "day1_input.txt"), "r") as input:
    for line in input:
        ids = line.split("   ")
        arr_ids1.append(int(ids[0]))
        arr_ids2.append(int(ids[1]))

arr_ids1.sort()
arr_ids2.sort()

print(f"(part 1) total distance = {part_1()}")
print(f"(part 2) similarity score = {part_2()}")

