from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'Title': 'A cabana do Pai Tomás',
        'Author': 'Harriet Beecher Stowe'
    },
    {
        'id': 2,
        'title': '1984',
        'Author': ' George Orwell '
    },
    {
        'id': 3,
        'title': 'Dom Quixote',
        'Author': 'Miguel de Cervantes'
    },
    {
        'id': 4,
        'title':'Hamlet',
        'Author': 'William Shakespeare'
    }
]

#Consult (all)
@app.route('/books', methods = ['GET'])
def getBooks():
    return jsonify(books)

#Consult(id)
@app.route('/books/<int:id>',methods=['GET'])
def getBookByID(id):
     for book in books:
        if book.get('id') == id:
            return jsonify(book)

#Edit
@app.route('/books/<int:id>',methods=['PUT'])
def editBookByID(id):
    ChangedBook=request.get_json()
    for i, book in enumerate(books):
        if book.get('id') == id:
            books[i].update(ChangedBook)
            return jsonify(books[i])
        
#Create
@app.route('/books', methods=['POST'])
def includeNewBook():
    newBook = request.get_json()
    books.append(newBook)

    return jsonify(books)

#Delete
@app.route('/books/<int:id>', methods=['DELETE'])
def DeleteBook(id):
    for i, book in enumerate(books):
        if book.get('id') == id:
            del books[i]

    return jsonify(books)


app.run(port=5000, host='localhost', debug=True)