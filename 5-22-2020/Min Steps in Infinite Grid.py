class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    

    def coverPoints(self, A, B):
        l = len(A)
        dist = 0
        for i in range(l - 1):
            # This will make the case to move from (0,0) to (a,b). Just shifting the point of reference.
            a = abs(A[i+1] - A[i])
            b = abs(B[i+1] - B[i])
            
            # Either we go diagonal or we go straight we have to move at least the max of the stepts of i,j.
            dist += max(a,b)
        return(dist)
            