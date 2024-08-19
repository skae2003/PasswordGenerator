import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    while len(password) < 8:
        password += random.choice(characters)
    return password[:length]

def fuzzer(num_tests, output_file):
    with open(output_file, 'w') as file:
        for _ in range(num_tests):
            password = generate_password(8)  # Generate 8 character long passwords
            file.write(password + '\n')
        file.write("q\n")  # Add 'q' as the last line

def main():
  num_tests = 10  # Number of passwords to generate
  output_file = "passwords.txt"  # Output file name
  fuzzer(num_tests, output_file)


if __name__ == "__main__":
  main()
