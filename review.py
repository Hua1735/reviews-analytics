data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		print(len(data))  #印出列印的進度

print(data[0])   #印出第0筆是什麼
print(len(data)) #印出data清單的總數