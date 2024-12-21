def main():
    x = get_int("What's x? ")
    print(f"X is {x} ") 

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

            

main()