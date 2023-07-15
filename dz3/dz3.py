import csv
import json

with open("books.csv", newline='') as file:
    reader = csv.reader(file)
    header = next(reader)
    books = []
    for row in reader:
        books.append(dict(zip(header, row)))

with open('users.json') as f:
    users = json.load(f)

books_for_person = len(books) // len(users)
books_mod = len(books) % len(users)
to_json = []
for i in range(len(users)):
    if i < books_mod:
        books_to_json = []
        for j in range(i * (books_for_person + 1), i * (books_for_person + 1) + books_for_person + 1) :
            books_to_json.append({'title': books[j]["Title"], 'author': books[j]["Author"], \
                                  'pages': books[j]["Pages"], 'genre': books[j]["Genre"]})
    elif i == books_mod:
        books_to_json = []
        for j in range(i * (books_for_person + 1), i * (books_for_person +1 ) + books_for_person) :
            books_to_json.append({'title': books[j]["Title"], 'author': books[j]["Author"], \
                                  'pages': books[j]["Pages"], 'genre': books[j]["Genre"]})
    elif i > books_mod:
        books_to_json = []
        for j in range(i * books_for_person, i * books_for_person + books_for_person) :
            books_to_json.append({'title': books[j]["Title"], 'author': books[j]["Author"], \
                                  'pages': books[j]["Pages"], 'genre': books[j]["Genre"]})

    to_json.append({'name': users[i]["name"], 'gender': users[i]["gender"], \
                    'address': users[i]["address"],'age': users[i]["age"], 'books': books_to_json})
    
with open('result.json', 'w') as f:
    f.write(json.dumps(to_json))