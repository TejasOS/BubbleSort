def bubbleSort(arrToBeSorted):

    # We don't need this variable, but the maximum number of times we would need to iterate through would be n-1 times (e.g. 7, 5, 1 would require 2 iterations)
    for _ in range(len(arrToBeSorted) - 1):
        numSwitch = 0  # Count number of switches we've made
        # We want to swap elements, but because we are accessing an element and the next element, we only need n -1
        for j in range(len(arrToBeSorted) - 1):
            if (arrToBeSorted[j+1] < arrToBeSorted[j]):
                toBeSwapped = arrToBeSorted[j]  # Swap the elements
                arrToBeSorted[j] = arrToBeSorted[j+1]
                arrToBeSorted[j+1] = toBeSwapped
                numSwitch += 1
                print("Bubble")  # We know that a swap was made in the array
        if (numSwitch == 0):  # We want to see if the array can be sorted anymore or not
            print("Done")  # Print done if we are done sorting
            return arrToBeSorted
        numSwitch = 0  # Reset num of switches
    return arrToBeSorted


print(bubbleSort([1, 2, 3]))
