def decode_message(s: str, p: str) -> bool:
    # Initialize a 2D DP table with False
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    dp[0][0] = True  # An empty pattern matches an empty message

    for i in range(1, len(p) + 1):
        if p[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
        else:
            break  

    for i in range(1, len(p) + 1):
        for j in range(1, len(s) + 1):
            if p[i - 1] == '*':

                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[i - 1] == '?' or p[i - 1] == s[j - 1]:

                dp[i][j] = dp[i - 1][j - 1]
