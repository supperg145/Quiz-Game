import random
# General Knowledge Questions
general = {
    "Which planet is known as the 'Red Planet'?": [
        "Mars", "Venus", "Jupiter", "Saturn"
    ],
    "Who painted the famous artwork 'The Starry Night'?": [
        "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"
    ],
    "Which animal is known as the 'King of the Jungle'?": [
        "Lion", "Elephant", "Giraffe", "Tiger"
    ],
    "Who wrote the novel 'To Kill a Mockingbird'?": [
        "Harper Lee", "J.D. Salinger", "F. Scott Fitzgerald", "George Orwell"
    ],
    "What is the chemical symbol for the element Gold?": [
        "Au", "Ag", "Fe", "Hg"
    ],
    "Which country is famous for the landmark 'Machu Picchu'?": [
        "Peru", "Brazil", "Mexico", "Egypt"
    ],
    "What is the capital city of Australia?": [
        "Canberra", "Sydney", "Melbourne", "Brisbane"
    ],
    "Which mountain range is located in North America?": [
        "Rocky Mountains", "Andes Mountains", "Himalayas", "Alps"
    ],
    "What is the currency of Japan?": [
        "Yen", "Euro", "Dollar", "Pound"
    ],
    "Which famous scientist developed the theory of general relativity?": [
        "Albert Einstein", "Isaac Newton", "Nikola Tesla", "Marie Curie"
    ]
}

geography = {
    "Which country is the largest by land area?": [
        "Russia", "Canada", "China", "United States"
    ],
    "Which river is the longest in the world?": [
        "Nile", "Amazon", "Yangtze", "Mississippi"
    ],
    "What is the capital city of France?": [
        "Paris", "Rome", "London", "Madrid"
    ],
    "Which ocean is the largest?": [
        "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"
    ],
    "Which African country is known as the 'Pearl of Africa'?": [
        "Uganda", "Kenya", "Egypt", "Morocco"
    ],
    "Which country is famous for the Great Barrier Reef?": [
        "Australia", "Indonesia", "Thailand", "Brazil"
    ],
    "Which desert is the largest in the world?": [
        "Sahara Desert", "Gobi Desert", "Kalahari Desert", "Atacama Desert"
    ],
    "Which European country is known for its tulips and windmills?": [
        "Netherlands", "Germany", "France", "Spain"
    ],
    "Which mountain is the highest in the world?": [
        "Mount Everest", "K2", "Kangchenjunga", "Mount Kilimanjaro"
    ],
    "What is the capital city of Brazil?": [
        "Brasília", "Rio de Janeiro", "São Paulo", "Buenos Aires"
    ]
}


music = {
"What is the name of the instrument that is played by blowing air through reeds and keys?": [
"Clarinet", "Saxophone", "Oboe", "Bassoon"
],
"Which musical term is used to indicate a gradual decrease in volume?": [
"Diminuendo", "Crescendo", "Fortissimo", "Pianissimo"
],
"Who composed the famous symphony 'Symphony No. 5' in C minor?": [
"Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Franz Schubert"
],
"What is the standard tuning for a guitar's strings, from lowest to highest pitch?": [
"EADGBE", "DGCFAD", "EBGDAE", "BEADGC"
],
"What is the name of the musical technique where a performer or group repeats a section of music?": [
"Repetition", "Syncopation", "Improvisation", "Looping"
],
"Which famous rock band released the album 'Stairway to Heaven'?": [
"Led Zeppelin", "The Beatles", "Pink Floyd", "Queen"
],
"Who is known as the 'King of Pop'?": [
"Michael Jackson", "Elvis Presley", "Stevie Wonder", "Prince"
],
"What is the highest female singing voice range?": [
"Soprano", "Alto", "Tenor", "Bass"
],
"Which musical term is used to indicate a quick, lively tempo?": [
"Allegro", "Adagio", "Andante", "Presto"
],
"What is the name of the percussion instrument that consists of a pair of wooden sticks struck together?": [
"Claves", "Maracas", "Tambourine", "Triangle"
]
}



def main():
    play = True
    while play:
        choice = choose_category()
        score = get_question(choice)
        print_score(score)
        play = ask_play_again()


def get_question(choice):
    score = 0

    for question, answers in choice.items():
        print(question)
        correct = answers[0]  # Assign the correct answer before shuffling
        random.shuffle(answers)
        for answer in answers:
            print(answer)

        while True:
            user_answer = input("Your answer: ").lower()
            if user_answer in [answer.lower() for answer in answers]:
                break
            else:
                print("Invalid input. Please try again.")

        if check_answer(user_answer, correct):
            score += 1

    return score


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False


def choose_category():
    print("Available categories:\n1. General\n2. Geography\n3. Music")
    while True:
        choice = input("Please select a category: ").lower()
        if choice == "general":
            return general
        elif choice == "geography":
            return geography
        elif choice == "music":
            return music
        else:
            print("Invalid input. Please try again.")


def print_score(score):
    if score >= 8:
        print(f"You earned {score} points. You are amazing! Here is a cookie: 🍪")
    elif 5 <= score < 8:
        print(f"You earned {score} points. Keep up the great work!")
    else:
        print(f"You earned {score} points. Better luck next time!")


def ask_play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")




if __name__ == "__main__":
    main()