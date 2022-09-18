# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Here we are defining global variables, including characters and counters, for this game
define MM = Character("Teacher")
define MC = Character("[povname]")
define SC = Character("Kevin Ng")
define JC = Character("Spencer Johnson")

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

# Matcha man / teacher 
image MM = "MM.png"
image MM Sad = "MM Sad.png"
image MM Reveal = "MM Reveal.png"

# Janitor
image JC = "JC.png"
image JC Angry = "JC Angry.png"
image JC Annoyed = "JC Annoyed.png"

#Classmate
image SC = "SC.png"
image SC Sad = "SC Sad.png"
image SC Angry = "SC Angry.png"


# The game starts here.

label start:
    #Gets the user input for name
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Williana Wonkas"

    scene bg cat

    show JC Annoyed 
    MM "This is MM"
    hide JC Annoyed 

    show MM Sad
    MC "This is MM Sad"
    hide MM Sad
    
    show MM Reveal
    SC "This is MM Reveal"
    hide MM Reveal

    python:
        choice_test = renpy.input("Make a choice",length=32)
        choice_test.strip().lower()

        if not choice_test:
            bad_ending += 1
        else:
            good_ending += 1

    #choice("Make a choice")

    #if bad_ending >= 1:
    #    MM "This is the bad ending"
    #else:
    #    MC "This is the good ending"

    # This ends the game.

    return
