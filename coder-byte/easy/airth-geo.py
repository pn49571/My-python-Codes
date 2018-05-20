'''This challenge requires you to determine if the integers in an array follow either an arithmetic or geometric sequence. An arithmetic sequence is one where the difference between each successive pair of integers is constant, for example in the array [2, 4, 6, 8] the difference between the integers is always 2. A geometric sequence is one where each element in the array is the product of the previous integer multiplied by some constant or ratio, for example in the array [3, 9, 27, 81] each element is a result of the previous element multiplied by 3 '''


def ArithGeo(arr):

    # this function will loop through the provided array
    # checking to see if the difference provided matches
    # every element-pair difference in the array
    def arrayDiffs(diff, arr, subtract):

        # loop starting from i=2 and check if every difference is the same
        for i in range(2, len(arr)):

            # store the temporary difference
            if subtract:
                tempDiff = arr[i] - arr[i-1]
            else:
                tempDiff = arr[i] / arr[i-1]

                # if differences do not match return False
            if (tempDiff != diff):
                return False

            # if we reach the end of the array and all differences matched
            elif (i == len(arr)-1 and tempDiff == diff):
                return True

    # store the first difference for a potential arithmetic sequence
    diffArith = arr[1] - arr[0]

    # store the first difference for a potential geometric sequence
    diffGeo = arr[1] / arr[0]

    # check the whole array for an arithmetic sequence
    isArithSeq = arrayDiffs(diffArith, arr, True)

    if isArithSeq:
        return "Arithmetic"
    # if not an arithmetic sequence, check for geometric sequence
    else:
        isGeoSeq = arrayDiffs(diffGeo, arr, False)
        if isGeoSeq:
            return "Geometric"
        else:
            return -1


print ArithGeo([3, 9, 27, 81])
