# Find the minimum number of characters to be deleted in two strings to
# get the same string.

# This solution optimizes the space complexity of the solution in
# DeletionDistanceDP.py by keeping only those memo values that are
# required in each iteration and discarding unneeded memo values.

# Complexity: O(mn) time. O(min(m, n)) space.


def deletion_distance(a, b):
    m, n = len(a), len(b)

    # Ensure n <= m to reduce space complexity.
    if n > m:
        a, b = b, a
        m, n = n, m

    prev_memo = [0] * (n + 1)

    for i in range(m + 1):
        curr_memo = [0] * (n + 1)

        for j in range(n + 1):
            if i == 0:
                curr_memo[j] = j
            elif j == 0:
                curr_memo[j] = i
            elif a[i - 1] == b[j - 1]:
                curr_memo[j] = prev_memo[j - 1]
            else:
                curr_memo[j] = 1 + min(prev_memo[j], curr_memo[j - 1])

        prev_memo = curr_memo

    return curr_memo[n]
