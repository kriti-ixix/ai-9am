l1 = [1, 5, 10, 7, 18, 20, 25]
l1.sort()

first = 0
last = len(l1) - 1
element = 5

while first <= last:
    mid = (first + last) // 2
    
    print("Current value:", l1[mid])
    
    if l1[mid] == element:
        print("Found", element, "at", mid, "position")
        break
    else:
        if l1[mid] > element:
            last = mid - 1
            
        elif l1[mid] < element:
            first = mid + 1