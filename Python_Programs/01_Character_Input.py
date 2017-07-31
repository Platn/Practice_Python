def main():
    userName = input("What is your name? ")
    userAge = input("How old are you? ")

    message = "Your name is %s and you are %s years old\n" % (userName, userAge)    
    print(message) # Storing and printing the message is easier for repeat later

    
    # Print out both variables using the '%' and then insert their positions
    repeat = int(input("Please insert a random number: "))
    print(message * repeat)    
    wait = input("Press <Enter> key to exit...")
    # Not able to find a quick solution for any key press
    
main()
