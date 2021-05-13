""" Dynamic Programming Algorithm for Minimum Edit Distance

It is a naive recursive Python program to find the minimum number of operations
required to convert s1 to s2.
"""

class MinEditDistance():

    # TODO 1: modify this algorithm into a DP algorithm
    # TODO 2: modify this algorithm such that del/ins/sub can be arbitrary weights
    # TODO 3: add backtracing to this algorithm
    # TODO 4: integrate this algorithm into Elizad (somehow)

    @staticmethod
    def __findEditDistance(s1, s2, m, n):
    
        # If first string is empty, insert all characters of second string.
        if m == 0:
            return n
    
        # If second string is empty, remove all characters of first string.
        if n == 0:
            return m
    
        # If last characters of two strings are same, ignore them and recurse on the remaining strings.
        if s1[m - 1] == s2[n - 1]:
            return MinEditDistance.__findEditDistance(s1, s2, m - 1, n - 1)
    
        # If last characters are not same, consider all three operations on last character of first string,
        # and recursively compute minimum cost for all three operations and take the minimum of three values.
        return 1 + min(MinEditDistance.__findEditDistance(s1, s2, m, n - 1),      # Insert
                       MinEditDistance.__findEditDistance(s1, s2, m - 1, n),      # Remove
                       MinEditDistance.__findEditDistance(s1, s2, m - 1, n - 1))  # Replace

    @staticmethod
    def findEditDistance(s1, s2):
        return MinEditDistance.__findEditDistance(s1, s2, len(s1), len(s2))
