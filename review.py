data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))  #印出列印的進度

print(data[0])   #印出第0筆是什麼
print(len(data)) #印出data清單的總數