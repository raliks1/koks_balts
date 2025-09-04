import random

def math_game():
    score = 0
    rounds = 5
    print("Welcome to the Math Game!")
    for i in range(rounds):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(['+', '-', '*'])
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        else:
            answer = a * b
        user_input = input(f"Round {i+1}: What is {a} {op} {b}? ")
        try:
            if int(user_input) == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The answer was {answer}.")
        except ValueError:
            print("Please enter a valid number.")
    print(f"Game over! Your score: {score}/{rounds}")

if __name__ == "__main__":
    math_game()