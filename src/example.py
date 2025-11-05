from chatterpy.funfacts import fun_fact
from chatterpy.smalltalk import smallTalk
from chatterpy.banter import banter  
from chatterpy.pickuplines import pickUpLine
from chatterpy.compliments import compliment

def demo_chatterpy():
    keep_going = True
    _map = {"mild": 1, "medium": 2, "intense": 3}

    while(keep_going):
        choice = input("Enter a choice for your conversation:\n"
                       "\t1. Banter\n"
                       "\t2. Compliment\n"
                       "\t3. Fun fact\n"
                       "\t4. Pick up line\n"
                       "\t5. Small talk\n")

        if choice == "1":
            intensity = input("Enter an intensity (mild, medium, intense): ")
            name = input("Enter a name: ")
            print(banter(intensity, name))

        elif choice == "2":
            intense = input("Enter an intensity (mild, medium, intense): ").strip().lower()
            intensityNum = _map.get(intense or "medium", 2)
            name = input("Enter a name: ")
            print(compliment(name, intensityNum))

        elif choice == "3":
            category = input("Enter a category (general, science, history, animals): ")
            rarity = input("Enter a rarity (common, rare): ")
            print(fun_fact(category, rarity))

        elif choice == "4": 
            kind = input("Enter what kind of pickup line (classic, poetic, funny, nerdy): ")
            name = input("Enter a name: ")
            print(pickUpLine(kind, name))

        elif choice == "5":
            questionComment = input("Enter question or comment: ").strip().lower() 
            if questionComment == "question": 
                print(smallTalk(True)) 
            else:
                print(smallTalk(False)) 

        else:
            print("Invalid choice! Please enter a number 1 - 5.")   
        
        again = input("Do you want to continue? Y/N: ").strip().lower()
        if again != "y":
            keep_going = False
            print("Goodbye!")

def main():
    demo_chatterpy()


if __name__ == "__main__":
    main()