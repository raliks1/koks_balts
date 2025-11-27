import os
os.system('cls')
print("\n")

def main():

 x = int(input(" x? "))
 print("skaitlis kvadrāta ir ", square(x))


def square(n):
    return n + n

if __name__ == "__main__":
    main()

