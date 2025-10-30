#TODO

import random

def banter(name): 

    insults = [
        f"{name}, you're so bright, you make the sun look like a nightlight!",
        f"Nice try, {name}. I've seen better attempts from a broken calculator.",
        f"{name}, you're proof that even participation trophies have standards.",
        f"Hey {name}, I'd agree with you but then we'd both be wrong.",
        f"{name}, you're like a software update—nobody asked for you, but here you are anyway.",
        f"Wow {name}, that idea is almost as good as pineapple on pizza.",
        f"{name}, you're the reason the gene pool needs a lifeguard.",
        f"Keep talking, {name}. I always yawn when I'm interested.",
        f"{name}; you just have bad luck thinking.",
        f"I'd challenge you to a battle of wits, {name}, but I see you came unarmed."
    ]
    
    return random.choice(insults)