class FuzzyMatcher:
    def levendist2(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dist_matrix = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1, m+1):
            dist_matrix[i][0] = i

        for i in range(1, n+1):
            dist_matrix[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                cost = 1
                if s[i] == t[j]:
                    cost = 0
                dist_matrix[i][j] = min(dist_matrix[i-1][j] + 1,
                                        dist_matrix[i][j-1] + 1,
                                        dist_matrix[i-1][j-1] + cost)
        return dist_matrix[m][n]
