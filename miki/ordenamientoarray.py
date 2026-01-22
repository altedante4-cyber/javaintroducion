arr = [1, 2, 3, 4, 5, 6]
d = 2

n = len(arr)
for  i in range(d):

    first = arr[0]

    for j in range(n - 1):

        arr[j] = arr[j + 1]

    arr[n - 1] = first


print(arr) # lo que hace es mover los elementos dos posicion por que se lo indicamos con el d