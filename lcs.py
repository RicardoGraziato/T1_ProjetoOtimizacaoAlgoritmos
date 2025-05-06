import time

def lcs_dynamic(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    iteracoes = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            iteracoes += 1
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n], iteracoes, dp

def get_lcs_string(dp, s1, s2):
    i, j = len(s1), len(s2)
    lcs = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

if __name__ == "__main__":
    s1 = "ABCD VWXYZ"
    s2 = "ABC EXEMPLO"

    start_time = time.time()
    length, iteracoes, dp = lcs_dynamic(s1, s2)
    elapsed_time = time.time() - start_time

    lcs_string = get_lcs_string(dp, s1, s2)

    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    print(f"LCS: {lcs_string}")
    print(f"Comprimento da LCS: {length}")
    print(f"Iterações: {iteracoes}")
    print(f"Tempo de execução: {elapsed_time:.6f} segundos")
