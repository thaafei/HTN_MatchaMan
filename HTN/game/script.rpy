# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Here we are defining global variables, including characters and counters, for this game
define MM = Character("Matcha Man")
define MC = Character("[povname]")
define SC = Character("Billy Bob")

define good_ending = 0
define bad_ending = 0

init python:
    def choice(player_prompt):
        choice_test = renpy.input(player_prompt,length=32)
        choice_test.strip()

        if not choice_test:
            bad_ending += 1
        else:
            good_ending += 1

# Here we are loading in all the images used in this game
image bg bbt = "bg bbt.jpg"
image bg cat = "bg cat.png"
image MM normal = "MM normal.png"
image MC normal = "MC normal.png"
image SC normal = "SC normal.png"

# The game starts here.

label start:
    #Gets the user input for name
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Williana Wonkas"

    scene bg cat

    show MM normal
    MM "This is MM"
    hide MM normal

    show MC normal
    MC "This is MC"
    hide MC normal
    
    show SC normal
    SC "This is SC"
    hide SC normal

    python:
        choice_test = renpy.input("Make a choice",length=32)
        choice_test.strip().lower()

        if not choice_test:
            bad_ending += 1
        else:
            good_ending += 1

    choice("Make a choice")

    if bad_ending >= 1:
        MM "This is the bad ending"
    else:
        MC "This is the good ending"

    # This ends the game.

    return
