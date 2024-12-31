unsorted = [4,2,56,1,56,23,32,11,3,45,56]
target = sorted(unsorted)
n = len(unsorted)
swaps = 0
print(unsorted)
print(target)

for i in range(n):
    if(unsorted[i]!=target[i]):
        swaps+=1
        print(unsorted)
        temp_index = unsorted.index(unsorted[i])
        target_temp_index = unsorted.index(target[i])
        unsorted[target_temp_index] = unsorted[i]
        unsorted[temp_index] = target[i]

print(unsorted)
print(swaps)

        