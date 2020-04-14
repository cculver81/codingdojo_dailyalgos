# Given [3,4,5,7,12,13,14,18] return a string noting the continuous ranges ei: "3-5, 7, 12-14, 18"
# Page 61 of the algos book

# First Iteration
# def bookmarkIndexes(arrInput):
#     strOutput = str(arrInput[0])
#     lastConsecutive = arrInput[0]

#     for i in range(1, len(arrInput)-1, 1):
#         if type(arrInput[i]) is not int:
#             pass # validation code not required for assignment
#         elif arrInput[i] < lastConsecutive:
#             pass # validation code not required for assignment
#         elif arrInput[i] == lastConsecutive:
#             continue
#         elif arrInput[i] == lastConsecutive + 1:
#             lastConsecutive = arrInput[i]
#         elif i + 1 == len(arrInput):
#             strOutput = strOutput + '-' + str(arrInput[i]) + ', ' + str(arrInput[i+1])
#         else:
#             strOutput = strOutput + '-' + str(arrInput[i]) + ', ' + str(arrInput[i+1])
#             lastConsecutive = arrInput[i+1]

#     print(strOutput)

# bookmarkIndexes([3,4,5,7,12,13,14,18])



# Second Interation
def bookmarkIndexes(arrInput):
    strOutput = str(arrInput[0])
    lastConsecutive = arrInput[0]

    for i in range(1, len(arrInput), 1):
        if i + 1 == len(arrInput): # len(arrInput) currently = 8
            pass
        else:
            if arrInput[i] == lastConsecutive:
                continue
            elif arrInput[i] == lastConsecutive + 1:
                lastConsecutive = arrInput[i]
            elif arrInput[i] != lastConsecutive + 1:
                strOutput = strOutput + '-' + str(lastConsecutive) + ', ' + str(arrInput[i])
                lastConsecutive = arrInput[i] + 1
            

    print(strOutput)
    return(strOutput)

bookmarkIndexes([3,4,5,7,12,13,14,18])


# strOutput = '3'; '3-5, 7
# lastConsecutive = 3, 4, 5, 7
# i = 1, 2, 3, 4