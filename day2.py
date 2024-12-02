import os

reports = []

def is_safe(array) -> bool:
    decreasing = False

    i = 0
    while i < (len(array)):
        if i == len(array) - 1:
            return True

        diff = int(array[i]) - int(array[i+1])
        
        if diff > 0 and diff <= 3:
            if i == 0 or decreasing:  
                decreasing = True
                i+=1
                continue
            else:
                break

        elif diff < 0 and diff >= -3:
            if i == 0 or not decreasing:
                decreasing = False
                i += 1
                continue
            else:
                break

        else:
            break
    
    return False

def solution(tolerate = False) -> int:
    with open(os.path.join("inputs", "day2_input.txt"), "r") as input:
        safe_count = 0
        for line in input:
                safe = False
                reports = line.split(" ")

                if is_safe(reports):
                    safe = True
                    safe_count += 1
                
                if tolerate and not safe:
                    j = 0
                    while (j < len(reports)):
                        arrayAux = reports[:j]
                        if j < len(reports) - 1:
                            arrayAux += reports[j+1:]

                        if is_safe(arrayAux):
                            safe_count += 1
                            break
                        j += 1
            
    return safe_count       

print(f"(part 1) safe count = {solution()}")
print(f"(part 2) safe count = {solution(True)}")