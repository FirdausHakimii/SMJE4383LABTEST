#question 1 

def arithmetic_sequence_sum(a, d, n):
    # Formula for the sum of an arithmetic sequence: S = n/2 * (2a + (n-1)d)
    sequence_sum = n / 2 * (2 * a + (n - 1) * d)
    return int(sequence_sum)

# Get input from the user
a = int(input("Enter the first term (a) of the arithmetic sequence: "))
d = int(input("Enter the common difference (d) of the arithmetic sequence: "))
n = int(input("Enter the number of terms (n) to sum: "))

# Calculate and print the sum
result = arithmetic_sequence_sum(a, d, n)
print(f"The sum of the first {n} terms of the arithmetic sequence is: {result}")