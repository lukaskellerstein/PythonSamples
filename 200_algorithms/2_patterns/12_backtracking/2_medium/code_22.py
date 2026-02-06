
# -----------------------
# Generate Parentheses (LeetCode 22)
# -----------------------

# Difficulty: Medium

# Problem: Given n pairs of parentheses, write a function to generate all
# combinations of well-formed parentheses.

# -----------------------

# For n=3, generate all valid combinations of 3 pairs of parentheses.
n = 3

# ----------------------------------------------------
# Backtracking solution
#
# time complexity = O(4^n / sqrt(n)) - nth Catalan number of valid sequences
# space complexity = O(n) - recursion depth is 2n
# ----------------------------------------------------


def generate_parenthesis(n):
    res = []
    path = []

    def backtrack(open_count, close_count):
        if len(path) == 2 * n:
            res.append("".join(path))
            return

        # Can add '(' if we haven't used all n opening parens
        if open_count < n:
            path.append("(")
            backtrack(open_count + 1, close_count)
            path.pop()

        # Can add ')' only if it won't exceed the number of '(' placed so far
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count + 1)
            path.pop()

    backtrack(0, 0)
    return res


# Example
print(generate_parenthesis(n))
# ['((()))', '(()())', '(())()', '()(())', '()()()']


# ----------------------------------------------------
# Brute Force solution (generate all, then filter)
#
# time complexity = O(n * 2^(2n)) - generate all 2^(2n) sequences, validate each
# space complexity = O(n) - recursion depth
# ----------------------------------------------------


def generate_parenthesis_brute_force(n):
    res = []

    def generate(seq):
        if len(seq) == 2 * n:
            if is_valid(seq):
                res.append(seq)
            return
        generate(seq + "(")
        generate(seq + ")")

    def is_valid(seq):
        balance = 0
        for ch in seq:
            if ch == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    generate("")
    return res


# Example
print(generate_parenthesis_brute_force(n))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
