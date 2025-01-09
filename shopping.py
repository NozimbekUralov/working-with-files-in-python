
def main() -> None:
    DB_URL = "shopping_list.txt"
    print("To stop press: 'Ctrl+c'")
    while True:
        try:
            with open(DB_URL, "a") as file:
                product = input("Enter product name: ")
                file.write(f"{product}\n")
            
            with open(DB_URL, "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line, end="")

        except KeyboardInterrupt:
            exit()

if __name__ == "__main__":
    main()