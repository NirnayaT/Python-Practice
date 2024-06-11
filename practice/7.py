data = {
    "store": {
        "book": [
            {
                "category": "fiction",
                "author": "J. K. Rowling",
                "title": "Harry Potter and the Philosopher's",
                "price": 29.99
            },
            {
                "category": "science",
                "author": "Stephen Hawking",
                "title": "A Brief History of Time",
                "price": 15.99
            },
            {
                "category": "fiction",
                "author": "George Orwell",
                "title": "1984",
                "price": 19.99
            }
        ]
    }
}

category_dict = {}
author_dict = {}
title_dict = {}
price_dict = {}

for book in data["store"]["book"]:
    category_dict[book["title"]] = book["category"]
    author_dict[book["title"]] = book["author"]
    title_dict[book["title"]] = book["title"]
    price_dict[book["title"]] = book["price"]

print("Category Dictionary:")
print(category_dict)
print("\nAuthor Dictionary:")
print(author_dict)
print("\nTitle Dictionary:")
print(title_dict)
print("\nPrice Dictionary:")
print(price_dict)
