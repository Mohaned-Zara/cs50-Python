import sys
import pyfiglet
import random

def main():
    figlet = pyfiglet.Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())

    elif len(sys.argv) == 3:
        option, font_name = sys.argv[1], sys.argv[2]
        
        if option not in ("-f", "--font"):
            sys.exit("Error: First argument must be -f or --font")
        
        if font_name not in figlet.getFonts():
            sys.exit("Error: Font not found")
    
        font = font_name
    else:
        sys.exit("Usage: python figlet.py [-f FONTNAME]")
    
    figlet.setFont(font=font)
    
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()