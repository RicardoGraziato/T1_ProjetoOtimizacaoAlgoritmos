import time

def lcs_recursive(s1, s2, m, n, iterations=0):
    if m == 0 or n == 0:
        return 0, iterations
    if s1[m-1] == s2[n-1]:
        length, iterations = lcs_recursive(s1, s2, m-1, n-1, iterations + 1)
        return 1 + length, iterations
    else:
        length1, iterations = lcs_recursive(s1, s2, m, n-1, iterations + 1)
        length2, iterations = lcs_recursive(s1, s2, m-1, n, iterations + 1)
        return max(length1, length2), iterations

def lcs_dynamic(s1, s2):
    m, n = len(s1), len(s2)
    if m == 0 or n == 0:  
        return 0, 0, []

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

def run_tests():
    test_cases = [
        ("ABCD VWXYZ", "ABC EXEMPLO"),
        ("ABCBDAB", "BDCAB"),
        ("AGGTAB", "GXTXAYB"),
        ("AABBA", "BBAAA"),
        ("alguma coisa", ""),
        ("", "")
    ]

    for s1, s2 in test_cases:
        print(f"\ns1 = '{s1}', s2 = '{s2}'")
        print(f'')

        start = time.time()
        length_dp, iterations_dp, dp_matrix = lcs_dynamic(s1, s2)
        elapsed_dp = time.time() - start
        lcs_str_dp = get_lcs_string(dp_matrix, s1, s2)

        print(f"  LCS: {lcs_str_dp}")
        print(f"  Comprimento: {length_dp}")
        print(f"  Iterações: {iterations_dp}")
        print(f"  Tempo: {elapsed_dp:.6f} s")

        if len(s1) <= 15 and len(s2) <= 15: 
            start = time.time()
            length_rec, iterations_rec = lcs_recursive(s1, s2, len(s1), len(s2))
            elapsed_rec = time.time() - start
            print(f'')
            print(f"Recursivo (Força Bruta):")
            print(f"  Comprimento: {length_rec}")
            print(f"  Iterações: {iterations_rec}")
            print(f"  Tempo: {elapsed_rec:.6f} s")
            print(f'')
            print(f'------------------------------')
        else:
            print("Ignorado para evitar execução longa")

if __name__ == "__main__":
    run_tests()
