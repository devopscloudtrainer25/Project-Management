from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "🎨 Welcome to the Colorful Calculator!")

num1 = float(input(Fore.YELLOW + "Enter first number: "))
num2 = float(input(Fore.YELLOW + "Enter second number: "))

print(Fore.GREEN + "\nChoose an operation:")
print(Fore.MAGENTA + "1. Addition (+)")
print(Fore.MAGENTA + "2. Subtraction (-)")
print(Fore.MAGENTA + "3. Multiplication (*)")
print(Fore.MAGENTA + "4. Division (/)")

choice = input(Fore.CYAN + "\nEnter your choice (1-4): ")

if choice == "1":
    result = num1 + num2
    print(Fore.GREEN + f"\nResult: {result}")
elif choice == "2":
    result = num1 - num2
    print(Fore.RED + f"\nResult: {result}")
elif choice == "3":
    result = num1 * num2
    print(Fore.BLUE + f"\nResult: {result}")
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(Fore.MAGENTA + f"\nResult: {result}")
    else:
        print(Fore.RED + "\nError: Cannot divide by zero!")
else:
    print(Fore.RED + "\nInvalid choice!")
