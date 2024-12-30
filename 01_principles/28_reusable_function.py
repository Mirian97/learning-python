emojis = {
    ":)": "😊",
    ":(": "😔",
    ":/": "😕",
    ":D": "😄",
    "o/": "🙋"
}
message = input("> ")

def emoji_converter(message: str):
    splitted_message = message.split(" ")
    output = ""
    for word in splitted_message:
        formatted_word = emojis.get(word, word)
        output += f"{formatted_word} "
    return(output)

print(emoji_converter(message))