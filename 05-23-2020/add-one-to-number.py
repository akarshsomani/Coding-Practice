# https://www.interviewbit.com/problems/add-one-to-number/#

# The complexity used in the algorithm is o(n
)
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        # iterating from last for normal addition of numbers with carry
        # initial carry is considered as 1 because we have to add 1
        l = len(A) -1
        carry = 1
        while(l>=0):

            if(A[l] == 9 and carry == 1):
                A[l] = 0
            else:
                A[l] += 1
                carry = 0
                break
            l -= 1

        # if carry is 1 means the case is similar to all 9's so we have to append 1 at starting
        if carry == 1:
            return [1]+A
        else:
            # This step is to eleminate the starting 0's
            pos = 0
            for i in range(len(A)):
                if(A[i] != 0):
                    pos = i
                    break
            return A[pos:]
            
            
