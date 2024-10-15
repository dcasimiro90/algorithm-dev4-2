def main():
    number = int(input("Enter a number: "))
    if number <= 1:
        print(f"{number} is not a prime number.")
        return
    i = 2
    while i * i <= number:
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return
        i += 1

    print(f"{number} is a prime number.")

if __name__ == "__main__":
    main()