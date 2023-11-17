''' bubble sort : aggregate analysis , we iterate over each element in the
array looking and we "bubble" the maximum element to the end of the aray since the search
starts from the beginning of the array the cost is n-1+n-2+...+1 = (n)n/2 = O(n^2)

merge sort merging two arrays costs  O(n+m)
the depth of the tree of splitting in half is log(n) the length of the array is n then its n(log(n)

c(n) = 2c(n/2)+ n

quick sort : on each iteration we find the correct place of the pivot but when we do the partition
the cases vary in the worst case we choose the pivot to be the maximum or the minimum in each iteration and partition
then all we are doing is the same as bubble sort we bubble the max to the end so in this case the running time
is O(n^2)in case we choose the pivot as the median then we split the array in the next iteration into two half
now the depth of the recursion tree is log(n) and the cost for quick sort is nlog(n)

the factorial function O(n) the depth of the stack is n we make at maximum n calls for the function before
returning

the permutations function space is O(n) assuming the length of the string is n and the time complexity
is n!

'''