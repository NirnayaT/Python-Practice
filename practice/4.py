dict={
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

titles=[]
prices=[]
categories=[]
authors=[]
for data in dict["store"]["book"]:
        title=data["title"]
        price=data["price"]
        category=data["category"]
        author=data["author"]
        
        titles.append(title)
        prices.append(price)
        categories.append(category)
        authors.append(author)
    
for i in range(len(titles)):
    print(f"\nThe {titles[i]} is {prices[i]} fall under this {categories[i]} by author {authors[i]}.\n")

