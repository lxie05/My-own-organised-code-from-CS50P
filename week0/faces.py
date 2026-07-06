def main():

    emoji = input()
    convert(emoji)

def convert(emoji):
    emoji = emoji.replace(':)', '🙂')
    emoji = emoji.replace(':(', '🙁')
    print (emoji)

main()
