
def main() -> None:
    DB_URL = "grades.txt"
    number_of_grades = 0
    grades = []
    with open(DB_URL, "w"):
        print("To stop press: 'Ctrl+c'")

    while True:
        try:
            with open(DB_URL, "a") as file:
                name = input("Enter student name: ")
                grade = input("Enter student grade: ")
                try:
                    grade = int(grade)
                    file.write(f"{name}: {grade}\n")

                    number_of_grades +=1
                    grades.append(grade)

                    print(
                        "O'rtacha baho:\n"
                        f"\t({" + ".join(list(map(str, grades)))}) / {number_of_grades} = {sum(grades)/number_of_grades:.2f}",
                        sep=""
                    )

                except ValueError:
                    print("Invalid Grade.")
            
            with open(DB_URL, "r") as file:
                print("O'quvchilar:")
                lines = file.readlines()
                for line in lines:
                    print("\t", line, end="", sep="")

        except KeyboardInterrupt:
            exit()

if __name__ == "__main__":
    main()