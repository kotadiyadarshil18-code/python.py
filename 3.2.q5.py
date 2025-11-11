print("press 1 to order sandwhich")
print("press 2 to order Pizza")
print("press 3 to order Burger")
print("press 4 to order Thin crust pizza")
print("press 5 to order Cheese Burst pizza")
print("press 6 to order Fresh Dough pizza")

num=int(input("Enter a number to orader fast food:"))


match num:
    case 1:
        print("sandwhich")
    case 2:
        print("pizza")
    case 3:
        print("burger")

    case 4:
        print("Thin crust pizza")
    case 5:
        print(" Cheese Burst pizza")
    case 6:
        print("Fresh Dough pizza")



