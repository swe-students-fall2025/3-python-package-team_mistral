from .funfacts import fun_fact
from .smalltalk import smallTalk
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(prog="conversations")
    parser.add_argument("--category", default="general")
    parser.add_argument("--rarity", default="common")

    parser.add_argument("--question", action="store_true")
    parser.add_argument("--comment", action="store_true")
    
    parser.add_argument("--kind")
    parser.add_argument("--name")

    args = parser.parse_args()

    #add your function parsing strateg here for CLI

    print(fun_fact(category=args.category, rarity=args.rarity))
   
    if args.question or args.comment: 
        print(smallTalk(args.question))

if __name__ == "__main__":
    main()
