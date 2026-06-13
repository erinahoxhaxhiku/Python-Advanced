from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "title": "Anonim",
        "author": "Kadare",
        "year": 2017,
        "genre": "idk"
    },
    {
        "title": "Prilli i Thyer",
        "author": "Kadare",
        "year": 1980,
        "genre": "Roman"
    },
    {
        "title": "Pallati i Ëndrrave",
        "author": "Kadare",
        "year": 1981,
        "genre": "Roman"
    }
]


@app.get("/")
def home():
    return {"message": "Welcome"}


@app.get("/books")
def get_books():
    return books


@app.get("/newest")
def newest_book():
    newest = max(books, key=lambda book: book["year"])
    return newest