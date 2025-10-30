import random

__version__ = "0.1.0"

def banter(name):
    insults = [
        f"{name}, you look like you're easy to draw",
        f"{name}, the closest you’ll come to a brainstorm is a light drizzle",
        f"Hey {name}, You look like a “before” picture.",
        f"{name}, I envy everyone who hasn’t met you",
        f"Wow {name}, if ignorance is bliss, you must be ecstatic at all times.",
        f"{name}, you’ll go far someday. And I hope you stay there."
        f"{name}, if I gave you a penny for your thoughts, I’d get change back",
        f"{name}, you look like something I drew with my left hand.",
    ]
    
    return random.choice(insults)
