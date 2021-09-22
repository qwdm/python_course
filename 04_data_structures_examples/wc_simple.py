# упрощенный подсчет частотности
s = "first second first third second first"

words = s.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

for word, count in word_counts.items():
    print(word, count)
