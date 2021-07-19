def emoji_converter(message):
    words = message.split(' ')  # split() method is used to break a sentence and turn it into list here one space is the boundry.
    emoji = {
        ':)': '😃',
        ':(': '😔',
        ':D': '😁'
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input('>>>>')
print(emoji_converter(message))


