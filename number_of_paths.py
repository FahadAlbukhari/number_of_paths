from __future__ import division
# Python program to count all possible paths
# from top left to bottom right

# Returns count of possible paths to reach cell
# at row number m and column number n from the
# topmost leftmost cell (cell at 1, 1)


def number_of_paths(m, n):
    # Create a 2D table to store
    # results of subproblems
    count = [[0 for x in range(m)] for y in range(n)]
    list = []

    # Count of paths to reach any
    # cell in first column is 1
    for i in range(m):
        try:
            count[i][0] = 1
        except:
            pass

    # Count of paths to reach any
    # cell in first column is 1
    for j in range(n):
        count[0][j] = 1

    # Calculate count of paths for other
    # cells in bottom-up
    # manner using the recursive solution
    for i in range(1, m):
        for j in range(n):
            try:
                count[i][j] = count[i - 1][j] + count[i][j - 1]
            except:
                pass
            x = i / m - j / n
            y = j / n - i / n
            maxv = max(float("{:.2f}".format(x)), float("{:.2f}".format(y)))
            list.append(maxv)
    print list
    print "len of list:",len(list)
    if m <= n:
        return count[m - 1][n - 1]
    elif m > n:
        return count[n - 1][n - 1]


# Driver program to test above function
m = 7
n = 3
print(number_of_paths(m, n))
