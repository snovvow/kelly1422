from itertools import combinations      # 또는 from itertools import permutations 을 사용하면 순열

L, C = map(int, input().split())
passwords = sorted(list(input().split()))
combs = list(combinations(passwords, L))
vowel = 'aeiou'

for comb in combs:
    no_vowel, no_conso = 0, 0
    for c in comb:
        if c in vowel:
            no_vowel += 1
        else:
            no_conso += 1
    if no_vowel >= 1 and no_conso >= 2:
        print(''.join(comb))