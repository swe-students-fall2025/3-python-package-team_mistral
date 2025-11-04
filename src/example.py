from conversations.funfacts import fun_fact
from conversations.smalltalk import smallTalk
from conversations.banter import banter  
from conversations.pickuplines import pickUpLine

def demo_conversations():
    keep_going = True
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
            break

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
    demo_conversations()


if __name__ == "__main__":
    main()