n, k, T = input().split()
words = []
for i in range(int(n)):
    word = input()
    if word.startswith(T):
        words.append(word)
words.sort()
print(words[int(k) - 1])