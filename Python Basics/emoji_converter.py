message = input('>>>>')
word = message.split(' ') #split() method is used to break a sentence and turn it into list here one space is the boundry.
emoji = {
    ':)':'😃',
    ':(':'😔',
    ':D':'😁'
}
for chars in word:
    while True:
        if chars not in emoji:
            output_msg = chars
            print(output_msg, end=" ")
            break
        elif chars in emoji:
            output_emoji = emoji.get(chars)
            print(output_emoji, end=" ")
            break

# Second method for same code

message = input('>>>>')
words = message.split(' ') #split() method is used to break a sentence and turn it into list here one space is the boundry.
emoji = {
    ':)':'😃',
    ':(':'😔',
    ':D':'😁'
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "   #.get(word, word) it means that it will search emoji with word and if the word will be missing then insted of returning none it will return the same word
print(output)




