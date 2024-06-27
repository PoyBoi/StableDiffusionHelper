import os
# import tqdm

def process_files(folder_path, words_list, charName):
    # for filename in tqdm(os.listdir(folder_path), desc="Processing Caption Files"):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                words = content.split(", ")
                # print("\n", words)

            # Create a new list without the words to delete
            updated_words = [word for word in words if word not in words_list]

            # Add UniqueWord to the first of the list if not exist
            if words[0] != charName.lower() or words[0] != charName:
                # print(words[0].lower())
                updated_words.insert(0, charName)

            # Join the updated words back into a string
            updated_content = ', '.join(updated_words)
            # print("\nUpdated:", updated_content)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

# process_files(folder_loc, words_to_delete_list, charName)