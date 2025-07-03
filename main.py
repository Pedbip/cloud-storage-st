import requests, json
from models import book, character, movie, potion, spell, cloud

while True:
    print("What we're gonna storage today?\n")
    print("1. Books\n2. Characters\n3. Movies\n4. Potions\n5. Spells")

    match input("Choose an option: "):
        case "1":
            req = book.get_books()
            # bk = book
            for bk in req["data"]:
                print(f"ID: {bk['id']}, Title: {bk['attributes']['title']}")

            book_id = input("Enter the book ID to Save on Cloud Storage: ")
            req = book.get_book_by_id(book_id)

            file_name = req["data"]["attributes"]["title"] + ".json"
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(req, json_file, ensure_ascii=False, indent=4)
            print(f"Book details saved to {file_name}")

            cloud.upload_archive(bucket_name="teste-bucket-pedbip", source_file_name=file_name, destination_blob_name=f"books/{file_name}")
            cloud.list_blobs_in_folder(bucket_name="teste-bucket-pedbip", folder_prefix="books/")
            break

        case "2":
            req = character.get_characters()
            # char = character
            for char in req["data"]:
                print(f"ID: {char['id']}, Name: {char['attributes']['name']}")

            character_id = input("Enter the character ID to Save on Cloud Storage: ")
            req = character.get_character_by_id(character_id)

            file_name = req["data"]["attributes"]["name"] + ".json"
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(req, json_file, ensure_ascii=False, indent=4)
            print(f"Character details saved to {file_name}")

            cloud.upload_archive(bucket_name="teste-bucket-pedbip", source_file_name=file_name, destination_blob_name=f"characters/{file_name}")
            cloud.list_blobs_in_folder(bucket_name="teste-bucket-pedbip", folder_prefix="characters/")
            break

        case "3":
            req = movie.get_movies()
            # mov = movie
            for mov in req["data"]:
                print(f"ID: {mov['id']}, Title: {mov['attributes']['title']}")

            movie_id = input("Enter the movie ID to Save on Cloud Storage: ")
            req = movie.get_movie_by_id(movie_id)

            file_name = req["data"]["attributes"]["title"] + ".json"
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(req, json_file, ensure_ascii=False, indent=4)
            print(f"Movie details saved to {file_name}")

            cloud.upload_archive(bucket_name="teste-bucket-pedbip", source_file_name=file_name, destination_blob_name=f"movies/{file_name}")
            cloud.list_blobs_in_folder(bucket_name="teste-bucket-pedbip", folder_prefix="movies/")  
            break

        case "4":
            req = potion.get_potions()
            # pot = potion
            for pot in req["data"]:
                print(f"ID: {pot['id']}, Name: {pot['attributes']['name']}")

            potion_id = input("Enter the potion ID to Save on Cloud Storage: ")
            req = potion.get_potion_by_id(potion_id)

            file_name = req["data"]["attributes"]["name"] + ".json"
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(req, json_file, ensure_ascii=False, indent=4)
            print(f"Potion details saved to {file_name}")

            cloud.upload_archive(bucket_name="teste-bucket-pedbip", source_file_name=file_name, destination_blob_name=f"potions/{file_name}")
            cloud.list_blobs_in_folder(bucket_name="teste-bucket-pedbip", folder_prefix="potions/") 
            break

        case "5":
            req = spell.get_spells()
            # sp = spell
            for sp in req["data"]:
                print(f"ID: {sp['id']}, Name: {sp['attributes']['name']}")

            spell_id = input("Enter the spell ID to Save on Cloud Storage: ")
            req = spell.get_spell_by_id(spell_id)

            file_name = req["data"]["attributes"]["name"] + ".json"
            with open(file_name, 'w', encoding='utf-8') as json_file:
                json.dump(req, json_file, ensure_ascii=False, indent=4) 
            print(f"Spell details saved to {file_name}")

            cloud.upload_archive(bucket_name="teste-bucket-pedbip", source_file_name=file_name, destination_blob_name=f"spells/{file_name}")
            cloud.list_blobs_in_folder(bucket_name="teste-bucket-pedbip", folder_prefix="spells/")
            break

        case _:
            print("Invalid option, please try again.")
    

