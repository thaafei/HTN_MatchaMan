# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MM = Character("Matcha Man")
define MC = Character("[povname]")
define SC = Character("Billy Bob")

image eileen happy = "MC normal.png"
image bg room = "bg bbt.jpg"

# The game starts here.

label start:
    #Gets the user input for name
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Williana Wonkas"

    scene bg room
    show eileen happy

    MC "How are you?"
    MM "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
