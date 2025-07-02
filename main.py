import requests, book, character, movie, potion, spell, json
from google.cloud import storage

req = requests.get('https://api.potterdb.com/v1/books')

print(req.json())

# 1. Ver a lista de livros
# 2. Escolher o livro com o ID e Salvar em um arquivo JSON
# 3. Salvar o JSON no Bucket Google Cloud Storage
# 4. Printar lista de JSON do Bucket Google Cloud Storage


while True:
    print("What we're gonna storage today?\n")
    print("1. Books\n2. Characters\n3. Movies\n4. Potions\n5. Spells")
    match input("Choose an option: "):
        case "1":
            req = book.get_books()
            print(json.dumps(req, indent=4))

            print("\n\nChoose a book ID to get more details")
            book_id = input("Enter the book ID to Save on Cloud Storage: ")
            req = book.get_book_by_id(book_id)
            print(json.dumps(req, indent=4))
            break
        case "2":
            req = character.get_characters()
            print(json.dumps(req, indent=4))
            break
        case "3":
            req = movie.get_movies()
            print(json.dumps(req, indent=4))
            break
        case "4":
            req = potion.get_potions()
            print(json.dumps(req, indent=4))
            break
        case "5":
            req = spell.get_spells()
            print(json.dumps(req, indent=4))
        case _:
            print("Invalid option, please try again.")
    

