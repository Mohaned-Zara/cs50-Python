def main():
    sent = input("Input a Sentence: ")
    done=convert(sent)
    print(done)

def convert(text):
    text=text.replace(":)", "🙂")
    text=text.replace(":(", "🙁")
    return text

main()
