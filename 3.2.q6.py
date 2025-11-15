print("press 1 to telecone calling into English")
print("press 2 to telecone calling into Hindi")
print("press 3 to telecone calling into Gujarati")


lang = int(input("Enter your choice (1-3): "))

match lang:
    case 1:
        print("English")
    case 2:
        print("Hindi")
    case 3:
        print("Gujarati")
