
def main() -> None:
    DB_URL = "contacts.txt"
    print("To stop press: 'Ctrl+c'")
    while True:
        try:
            with open(DB_URL, "a") as file:
                name = input("Enter your name: ")
                phone = input("Enter your phone number: ")

                file.write(f"{name}: {phone}\n")
            
            with open(DB_URL, "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line, end="")

        except KeyboardInterrupt:
            exit()

if __name__ == "__main__":
    main()