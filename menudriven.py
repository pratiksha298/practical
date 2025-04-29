import random

def swap_numbers():
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

def generate_random_number():
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    rand_num = random.randint(lower, upper)
    print(f"Generated random number between {lower} and {upper}: {rand_num}")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Swap two numbers")
        print("2. Generate a random number")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            swap_numbers()
        elif choice == '2':
            generate_random_number()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
