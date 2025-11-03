from .funfacts import fun_fact
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(prog="conversations")
    parser.add_argument("--category", default="general")
    parser.add_argument("--rarity", default="common")
    args = parser.parse_args()

    #add your function parsing strateg here for CLI

    print(fun_fact(category=args.category, rarity=args.rarity))

if __name__ == "__main__":
    main()
