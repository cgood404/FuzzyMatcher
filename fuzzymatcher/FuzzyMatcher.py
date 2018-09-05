class FuzzyMatcher:
    def __init__(self, accuracy):
        self.accuracy = accuracy

    # returns the Levenshtein Distance between two strings
    def levendist(self, s: str, t: str) -> int:
        if s == '':
            return len(t)
        if t == '':
            return len(s)

        if s[-1] == t[-1]:
            cost = 0
        else:
            cost = 1

        i, j, k = (s[:-1], t), (s, t[:-1]), (s[:-1], t[:-1])
        if i not in self.memory:
            self.memory[i] = self.levendist(*i)
        if j not in self.memory:
            self.memory[j] = self.levendist(*j)
        if k not in self.memory:
            self.memory[k] = self.levendist(*k)

        minimum = min(self.memory[i] + 1,
                      self.memory[j] + 1,
                      self.memory[k] + cost)
        return minimum

    def match(self, s: str, t: str) -> float:
        self.memory = {}
        maxlen = max(len(s), len(t))
        if maxlen == 0:
            return 1.0
        return ((maxlen - self.levendist(s.lower(), t.lower())) / maxlen) > self.accuracy
