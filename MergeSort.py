def mergeSort(nums, n):
    """
    nums: an array of integers
    n: length of the array
    """
    # Esto quiere decir que llegamos a un caso base
    # por lo que los arreglos solo tienen un elemento
    if n < 2:
        return nums  # solo tiene un elemento

    else:
        mid = n // 2

        # tomamos los elementos desde el inicio hasta la mitad
        # por lo que tenemos todos los elementos de la izquierda
        left_nums = nums[0:mid]

        # Hacemos lo mismo pero con los elementos de la derecha
        right_nums = nums[mid:n]

        # Ya que tenemos los dos arreglos separados, hay que hacer la recusión
        L = mergeSort(left_nums, mid)  # L de left
        R = mergeSort(right_nums, n - mid)  # R de right

        # En este punto se tienen que unir ambos arreglos, y por recursión son de un elemento

    return Merge(L, R)


def Merge(L, R):
    """
    Función que devuelve un array ordenado dados dos arrays
    de longitud n y m respectivamente
    """

    # Longitudes de los arrays
    length_left = len(L)
    length_right = len(R)

    # Creamos un array de longitud len(L)+len(R)
    # Por convenciencia se hace con todas sus entradas iguales a cero
    final_array = (length_left + length_right) * [0]

    i = 0  # Avanzo en L
    j = 0  # Avanzo en R
    k = 0  # Posición en donde se pone el nuevo elemento en el array nuevo
    while i < length_left and j < length_right:
        if L[i] <= R[j]:
            final_array[k] = L[i]
            i += 1  # Se mueve el índice en una unidad sobre L
        else:  # L[i] >= R[j]
            final_array[k] = R[j]
            j += 1  # Se mueve el índice en una unidad sobre R

        k += 1  # Si o si se tiene que mover esta Posición

    # Llenamos los lugares que restan en caso de que hayan
    while i < length_left:
        final_array[k] = L[i]
        i += 1
        k += 1

    while j < length_right:
        final_array[k] = R[j]
        j += 1
        k += 1

    return final_array


# Testear el código
nums = [38, 27, 43, 3, 9, 82, 10]
n = len(nums)

print(mergeSort(nums, n))
