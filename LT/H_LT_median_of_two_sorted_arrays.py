'''
    There are two sorted arrays nums1 and nums2 of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).
    You may assume nums1 and nums2 cannot be both empty.
'''

def findMedianSortedArrays(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 == 0:
        if len2 % 2 == 0:
            return (nums2[int(len2 / 2 - 1)] + nums2[int(len2 / 2)]) / 2
        else:
            return nums2[int(len2 / 2)]
    elif len2 == 0:
        if len1 % 2 == 0:
            return (nums1[int(len1 / 2 -1)] + nums1[int(len1 / 2)]) / 2
        else:
            return nums1[int(len1 /2)]
    else:
        '''
        # This part we will have to consider very carefully
        # We could implement something easy to begin with which will be of oreder O(n+m)
        # for this we implement a merge sort algorithm
        def mergeLists(l1, l2):
            len1 = len(l1)
            len2 = len(l2)
            res = [None] * (len1 + len2)
            i, j, k = 0, 0, 0
            while i < len1 and j < len2:
                if l1[i] < l2[j]:
                    res[k] = l1[i]
                    k += 1
                    i += 1
                else:
                    res[k] = l2[j]
                    k += 1
                    j += 1

            while i < len1:
                res[k] = l1[i]
                k += 1
                i += 1

            while j < len2:
                res[k] = l2[j]
                k += 1
                k += 1
            return res
        combined = mergeLists(nums1, nums2)
        lenc = len(combined)
        if lenc % 2 == 0:
            return (combinded[int(lenc / 2 -1)] + combinde[int(lenc / 2)]) / 2
        else:
            return combined[int(lenc / 2)]
        '''
        # We will now need to think of a way to do this in O(log(n*m)) time.

        # There is a great article at http://www.drdobbs.com/parallel/finding-the-median-of-two-sorted-arrays/240169222?pgno=2
        # which explains a method we will try and implement here in Python
        
        median = 0
        i = 0
        j = 0

        def maximum(a, b) :
            return a if a > b else b

        # def to find minimum
        def minimum(a, b) :
            return a if a < b else b

        # def to find median
        # of two sorted arrays
        def findMedianSortedArrays(a, n, b, m) :

            global median, i, j
            min_index = 0
            max_index = n

            while (min_index <= max_index) :

                i = int((min_index + max_index) / 2)
                j = int(((n + m + 1) / 2) - i)

                # if i = n, it means that
                # Elements from a[] in the
                # second half is an empty
                # set. and if j = 0, it
                # means that Elements from
                # b[] in the first half is
                # an empty set. so it is
                # necessary to check that,
                # because we compare elements
                # from these two groups.
                # Searching on right
                if (i < n and j > 0 and b[j - 1] > a[i]) :
                    min_index = i + 1

                # if i = 0, it means that
                # Elements from a[] in the
                # first half is an empty
                # set and if j = m, it means
                # that Elements from b[] in
                # the second half is an empty
                # set. so it is necessary to
                # check that, because we compare
                # elements from these two groups.
                # searching on left
                elif (i > 0 and j < m and b[j] < a[i - 1]) :
                    max_index = i - 1

                # we have found the
                # desired halves.
                else :

                    # this condition happens when
                    # we don't have any elements
                    # in the first half from a[]
                    # so we returning the last
                    # element in b[] from the
                    # first half.
                    if (i == 0) :
                        median = b[j - 1]

                    # and this condition happens
                    # when we don't have any
                    # elements in the first half
                    # from b[] so we returning the
                    # last element in a[] from the
                    # first half.
                    elif (j == 0) :
                        median = a[i - 1]
                    else :
                        median = maximum(a[i - 1], b[j - 1])
                    break



            # calculating the median.
            # If number of elements
            # is odd there is
            # one middle element.
            if ((n + m) % 2 == 1) :
                return median

            # Elements from a[] in the
            # second half is an empty set.
            if (i == n) :
                return ((median + b[j]) / 2.0)

            # Elements from b[] in the
            # second half is an empty set.
            if (j == m) :
                return ((median + a[i]) / 2.0)

            return ((median + minimum(a[i], b[j])) / 2.0)
        
        if len1 < len2:
            return findMedianSortedArrays(nums1, len1, nums2, len2)
        else:
            return findMedianSortedArrays(nums2, len2, nums1, len1)


print('Test nums1 empty')
nums1 = []
nums2 = [1,2,3,4,5,6]
print(findMedianSortedArrays(nums1, nums2))

nums1 = [1, 1, 1, 1, 1, 2, 3, 4, 9, 9]
nums2 = [2, 3, 4, 5, 6, 7, 8]

print(findMedianSortedArrays(nums1, nums2))







