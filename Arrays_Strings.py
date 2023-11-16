# a function that reverses a string in place
def reverse_string(string):
    string = list(string)
    i = 0  # the first index in the array
    j = len(string) - 1
    while i < j:
        temp = string[i]
        string[i] = string[j]
        string[j] = temp
        i += 1
        j -= 1
    new_str = ''.join(string)
    return new_str

def find_max_min(array):
    if(array):
        max = array[0]
        min = max
        length = len(array)-1
        index = 0
    else:
        print("error!!")
        return
    while index <= length:
        if array[index] > max:
            max = array[index]
        if array[index] < min:
            min = array[index]
        index+=1
    return max,min

def remove_duplicates(array):
    index = 1
    length = len(array) -1
    if length == 1:
        return array
    while index < length :
        if (array[index] == array[index-1]):
            array.pop(index)
            length = len(array)
        else :
            index+=1
    return array



if __name__ == "__main__":
    # a test for the reverse string function
    print(reverse_string("String"))
    print(reverse_string("Ahmad Kais"))
    print(reverse_string("Hello Fursa !"))
    print(reverse_string(reverse_string("Hello Fursa !")))

    # a test for the second function that finds max and min in array
    print(find_max_min([0,1,2,3,4,5,6,7,8,9]))
    print(find_max_min([10,9,8,7,6,5,4]))
    print(find_max_min([-5,10,-1,-10]))

    # a test for the third function
    print(remove_duplicates([0,0,1,1,2,2,2,2,2,3]))
    print(remove_duplicates([0,1,3,3,3]))
    print(remove_duplicates([1,1,1,1,1,1,1]))
    print(remove_duplicates([1]))

