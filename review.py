data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())

print(data) #印出全部的資料



