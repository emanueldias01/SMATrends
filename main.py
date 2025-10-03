from crew.crew_trends import crew
import os

with open("key.txt", "r") as file:
    line = file.readline().strip()

os.environ["OPENAI_API_KEY"] = line

def main():
    theme = input("Escolha o tema: ")

    theme_input = {"tema" : theme}

    output = crew.kickoff(theme_input)

    print(output)


if __name__ == "__main__":
    main()