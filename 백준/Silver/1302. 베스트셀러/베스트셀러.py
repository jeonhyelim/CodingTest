n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1 
    else:
        books[book] += 1 #책 등장 횟수; books
        
target = max(books.values()) #가장 큰 값; target
array = []

for book, number in books.items():
    if number == target:
        array.append(book)
        
print(sorted(array)[0])