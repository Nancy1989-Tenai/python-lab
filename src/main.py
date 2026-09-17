from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    # Prompt user for a number
    num = float(input("Enter a number: "))
    
    # Calculate and display results
    print(f"\nResults for {num}:")
    print(f"Square: {square(num)}")
    
    if is_even(int(num)):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    
    print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(num)}°F")
    
    # Add greeting functionality
    name = input("\nEnter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()
