emojis = {
    ":)": "😊",
    ":(": "😔",
    ":/": "😕",
    ":D": "😄",
    "o/": "🙋"
}

message = input("> ")
splitted_message = message.split(" ")

updated_message = ""

for word in splitted_message:
    formatted_word = emojis.get(word, word)
    updated_message += f"{formatted_word} "
    
print(updated_message)