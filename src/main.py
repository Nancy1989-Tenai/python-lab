from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    num = float(input("Enter a number: "))
    print(f"Square: {square(num)}")
    
    if is_even(int(num)):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        
    print(f"Fahrenheit: {celsius_to_fahrenheit(num)}")
    
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()