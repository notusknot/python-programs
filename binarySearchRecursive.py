def binary_search(ListToSearch, l, h, x):
    if l > h:
        return "Not Present"

    mid = (h+l)//2

    if ListToSearch[mid] == x:
        return mid
    elif ListToSearch[mid] > x:
        return binary_search(ListToSearch, l, mid - 1, x)
    
    return binary_search(ListToSearch, mid + 1, h, x)
    

ListToSearch = [ 1, 3, 5, 7, 9, 10, 12, 14, 16, 18 ]
x = 10

result = binary_search(ListToSearch, 0, len(ListToSearch)-1, x)

if result != "Not Present":
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
