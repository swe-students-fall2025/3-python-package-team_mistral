from .funfacts import fun_fact
from .smalltalk import smallTalk
from .banter import banter  
from .pickuplines import pickUpLine

import argparse

def main() -> None:
    parser = argparse.ArgumentParser(prog="conversations")
    
    #funfacts.py
    parser.add_argument("--fact", action="store_true", help="print a fun fact")
    parser.add_argument("--category", default="general", help="fun fact category (general, science, history, animals)")
    parser.add_argument("--rarity", default="common", help="fun fact rarity (common, rare)")

    # smalltalk.py
    parser.add_argument("--smalltalk", action="store_true")
    parser.add_argument("--question", action="store_true")
    parser.add_argument("--comment", action="store_true")
    
    # pickuplines.py
    parser.add_argument("--kind", choices=["classic", "poetic", "funny", "nerdy"])
    parser.add_argument("--name", default = "")

    # banter.py
    parser.add_argument("--intensity", choices=["mild", "medium", "intense"])  
    parser.add_argument("--banter", action="store_true") 

    args = parser.parse_args()

    if args.fact:
        print(fun_fact(category=args.category, rarity=args.rarity))
   
    if args.smalltalk: 
        print(smallTalk(args.question))

    if args.banter:  
        intensity = args.intensity if args.intensity else "medium"
        name = args.name if args.name else ""
        print(banter(intensity, name))
        
    if args.pickup and args.kind:
        print(pickUpLine(args.kind, args.name))

if __name__ == "__main__":
    main()
