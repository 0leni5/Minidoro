from timer import Timer as T

def main():
    m = input("Enter the length of one study session (min): ")
    b = input("Enter the length of the break (min): ")
    t = T(int(m), int(b)) #create timer object
    t.studytimer() #start timer

if __name__ == "__main__":
    main()