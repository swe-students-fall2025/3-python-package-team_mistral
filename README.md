![CI / CD](https://github.com/swe-students-fall2025/3-python-package-team_mistral/actions/workflows/build.yaml/badge.svg)


# ChatterPy

ChatterPy is a lighthearted Python package that helps spark **fun conversations** by giving you a random **fun fact**, **small talk question**, **compliment**, or even a **pickup line** for when things get quiet.  

## Group Members

[Mahabub Alif](https://github.com/Alif-4)

[Sydney Nadeau](https://github.com/sen5217)

[Susan Wang](https://github.com/sw5556)

[Aden Juda](https://github.com/yungsemitone)

[Serena Wang](https://github.com/serena0615)

## Example Output

When you run these commands, you'll get different outputs:

### Small Talk (Comment)

```bash
python -m chatterpy --smalltalk --comment
```

You might see something like this:

```

Avocado toast is overrated, but I’d still eat it.

```

### Small Talk (Question)

```bash
python -m chatterpy --smalltalk --question
```
You might get:

```

I’ve been meaning to start reading/watching something new — any recommendations?

```

### Pickup Line (No Name)

```bash
python -m chatterpy --pickup --kind poetic
```

You could see:

```

your presence feels like morning sunshine.

```

### Pickup Line (With Name)

```bash
python -m chatterpy --pickup --kind nerdy --name Susan
```

The output might be:

```

Susan, you’re a clean solution in a messy codebase.

```

### Compliment (With Name)

```bash
python -m chatterpy --compliment --name Sydney --intensity medium
```
This might return:

```

Sydney, You always add something unique to your look.

```

### Fun Facts (No parameters)

```bash
python -m chatterpy --fact
```

Could get you:

```

Bananas are berries, but strawberries aren’t.

```

### Fun Facts (With parameters)

```bash
python -m chatterpy --fact --category history --rarity rare
```

Might spit out:

```

Ancient Roman concrete can 'self-heal'.


```

### Banter (No name)

```bash
python -m chatterpy --banter --intensity medium
```

Will say:

```

you look like something I drew with my left hand.

```

### Banter (With name)

```bash
python -m chatterpy --banter --intensity mild --name Aden
```

Will return:

```
Aden, you're like a software update: nobody asked for you.


```



---

## Features

| Function | Description |
| ----------------------------- | -------------------------------------------------------------- |
| `fun_fact(category: str = "general", rarity: str = "common")` | Returns a random fun fact from one of four categories: `general`, `science`, `history`, or `animals`, with varying rarity|
| `smallTalk(question: bool)` | Returns either a fun question (`True`) or a random comment (`False`). |
| `pickUpLine(kind: str, name: str = "")` | Returns a pickup line of a certain type (`classic`, `poetic`, `funny`, `nerdy`). Optionally includes a name at the start. |
| `compliment(name: str, intensity: str)` | Returns a compliment of a specific intesity(`mild`, `medium`, `intense`). Includes a name at the start. |
| `banter(intensity: str, name: str = "")` | Returns a playful roast or joke depending on the chosen intensity (`mild`, `medium`, `intense`). Optionally includes a name to personalize it. |



## Project Structure

```
3-python-package-team_mistral/
├──src/
│   ├───chatterpy/
│       ├── __init__.py
│       ├── __main__.py
│       ├── funfacts.py
│       ├── smalltalk.py
│       ├── pickuplines.py
│       └── banter.py
│       └── compliments.py
│   ├─── example.py
├──tests/
│   ├── test_funfacts.py
│   ├── test_smalltalk.py
│   ├── test_pickuplines.py
│   └── test_compliments.py
│   └── test_banter.py
├── Pipfile
├── pyproject.toml
└── README.md
```

## example.py

[Link to example.py](src/example.py)

example.py is a standalone Python script that demonstrates the functionality of the chatterpy package. It calls each of the package’s functions: fun facts, small talk, banter, pickup lines, and compliments.  

This script is separate from the CLI interface in that it can be run directly with Python, and is intended for demonstration or testing purposes, rather than as a command-line tool for user input.
