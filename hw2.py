import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Microsoft JhengHei'  

word_count = {}

with open("hw2_data.txt", "r") as file:
    for line in file:
        word = line.strip()
        if word: 
            word_count[word] = word_count.get(word, 0) + 1

# 1. 總共有多少個不重複的英文字
unique_words = len(word_count)
print(f"1.不重複的英文字總數：{unique_words}")

# 2. 每一個英文字出現次數
print("2.每個英文字出現次數：")
for word, count in word_count.items():
    print(f"{word}: {count}")

# 3. 畫出直方圖，由多到少列出
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

labels = [item[0] for item in sorted_words]
counts = [item[1] for item in sorted_words]

plt.figure(figsize=(12, 6))
bars = plt.bar(labels, counts)
plt.bar(labels, counts)
plt.xlabel("英文字")
plt.ylabel("出現次數")

plt.ylim(0, int(max(counts) * 1.1)) 
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(count),
             ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

