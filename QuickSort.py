def QuickSort(array, start, end):
    if end <= start:
        return

    pivot = partition(array, start, end)
    QuickSort(array, start, pivot - 1)
    QuickSort(array, pivot + 1, end)


def partition(array, start, end):
    pivot = array[end]  # por convención empezamos con un pivote al final
    # empezamos con un i apuntando fuera del array
    i = start - 1

    # Hay que iterar sobre todo el array variando j
    for j in range(start, end):
        # Hay que comparar el elemento j del arreglo con el pivote
        if array[j] < pivot:
            # primero avanzo y luego
            # hago un swap (i -> j)
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    # En este punto ya recorrimos todo el arreglo una vez
    # Y ya casi se encuentra la posición en donde queda el pivote

    # Avanzo en uno
    i += 1
    # Cambiamos el elemento i por el pivote
    # hago un swap (i -> j)
    temp = array[i]
    array[i] = array[end]
    array[end] = temp

    # Este es el índice donde debe de ir el pivote en el arreglo
    return i


# Prueba
array = [8, 2, 4, 7, 1, 3, 9, 6, 5]
print(QuickSort(array, 0, len(array) - 1))
print(array)
