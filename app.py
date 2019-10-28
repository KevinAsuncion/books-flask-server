from flask import Flask, jsonify, request
from flask_cors import CORS

# Config
DEBUG = True

# Create app instance

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS

CORS(app, resources={r"/*": {"origins": "*"}})

# Testing Data

BOOKNOTES = [
    {
        "id": 1,
        "title": "Book One",
        "author": "Author Author",
        "content": "<h1>Book One Notes</h1>",
        "rating": 1,
    },
    {
        "id": 2,
        "title": "Book Two",
        "author": "Author Author Two",
        "content": "<h1>Book Two Notes</h1>",
        "rating": 2,
    },
    {
        "id": 3,
        "title": "Book Three",
        "author": "Author Author Three",
        "content": "<h1>Book One Three</h1>",
        "rating": 5,
    },
]


@app.route("/booknotes", methods=["GET", "POST"])
def book_notes():
    response = {"status": "success"}
    if request.method == "POST":
        data = request.get_json()
        BOOKNOTES.append(
            {
                "id": len(BOOKNOTES) + 1,
                "title": data["title"],
                "author": data["author"],
                "content": data["content"],
                "rating": data["rating"],
            }
        )
        response["message"] = "Notes added!"
    else:
        response["book_notes"] = BOOKNOTES
    return jsonify(response)


@app.route("/booknotes/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_one_book(id):
    response = {"status": "success"}

    if request.method == "DELETE":
        remove_one_booknote(id)
        response["message"] = "Deleted book note"
    elif request.method == "PUT":
        booknote = find_one_booknote(id)
        data = request.get_json()
        print(data)
        booknote["title"] = data["title"]
        booknote["author"] = data["author"]
        booknote["content"] = data["content"]
        booknote["rating"] = data["rating"]
        response["message"] = "Updated book note"
    elif request.method == "GET":
        response["booknote"] = find_one_booknote(id)
    return jsonify(response)


def find_one_booknote(id):
    for booknote in BOOKNOTES:
        if booknote["id"] == id:
            return booknote


def remove_one_booknote(id):
    for booknote in BOOKNOTES:
        if booknote["id"] == id:
            BOOKNOTES.remove(booknote)


if __name__ == "__main__":
    app.run()
