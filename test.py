from fuzzymatcher import FuzzyMatcher as fm
def main():
    matcher = fm.FuzzyMatcher()

    s = "kitten"
    t = "mitten"

    print(matcher.levendist2(s, t))

if __name__ == "__main__":
    main()