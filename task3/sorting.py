"""
Наиболее быстрым методом является поразрядная сортировка.
В худшем случае (когда все числа отсортированы в обратном порядке) 
сложность выполнения остается линейной O(n), когда как
остальные методы сравнительной сортировки имеют в этом же случае O(n * logn) и O(n^2)

Поразрядная сортировка использует сортировку подсчетом как подпроцесс
Сортировка подсчетом происходит циклически в зависимости от количества цифр в
числе, у которого значение в массиве является максимальным.

В итоге временная сложность поразрядной сортировки остается линейной
O(d * (n + k)), где d - количество подпроцессов сортировок подсчетом, а 
n + k - временная сложность сортировки подсчетом, где
n - количество элементов в массиве, а k - значение максимального числа в массиве
"""

def countingSortForRadix(inputArray, placeValue):
    countArray = [0] * 10
    inputSize = len(inputArray)

    for i in range(inputSize): 
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1
        
    return outputArray

def radixSort(inputArray):
    maxEl = max(inputArray)

    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1
    
    placeVal = 1

    outputArray = inputArray
    while D > 0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10  
        D -= 1

    return outputArray
    
input = [2,20,61,997,1,619]
print(input)
sorted = radixSort(input)
print(sorted)
