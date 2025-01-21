def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers) 

#Example usage
numbers = [10,20,30,40,50]
avg = calculate_average(numbers)
print(f"Average:{avg}")
numbers = []
avg = calculate_average(numbers)
print(f"Average:{avg}") 