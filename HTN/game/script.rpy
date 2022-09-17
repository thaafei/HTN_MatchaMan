# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MM = Character("Matcha Man")
define MC = Character("[povname]")
define SC = Character("Billy Bob")


# The game starts here.

label start:
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Williana Wonkas"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show eileen happy
    # These display lines of dialogue.
    
    
    MC "How are you?"
    MM "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
