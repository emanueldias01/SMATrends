from crew.crew_trends import crew

def main():
    theme = input("Escolha o tema: ")

    theme_input = {"tema" : theme}

    output = crew.kickoff(theme_input)

    print(output)


if __name__ == "__main__":
    main()