from .funfacts import fun_fact
from .smalltalk import smallTalk
from .banter import banter  

import argparse

def main() -> None:
    parser = argparse.ArgumentParser(prog="conversations")
    parser.add_argument("--category", default="general")
    parser.add_argument("--rarity", default="common")

    parser.add_argument("--question", action="store_true")
    parser.add_argument("--comment", action="store_true")
    
    parser.add_argument("--kind", choices=["classic", "poetic", "funny", "nerdy"])
    parser.add_argument("--name", default = "")

    # banter.py
    parser.add_argument("--intensity", choices=["mild", "medium", "intense"])  
    parser.add_argument("--banter", action="store_true") 

    args = parser.parse_args()

    #add your function parsing strategy here for CLI

    print(fun_fact(category=args.category, rarity=args.rarity))
   
    if args.question or args.comment: 
        print(smallTalk(args.question))

    if args.banter:  
        intensity = args.intensity if args.intensity else "medium"
        name = args.name if args.name else ""
        print(banter(intensity, name))

if __name__ == "__main__":
    main()
