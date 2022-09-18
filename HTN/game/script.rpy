# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Here we are defining global variables, including characters and counters, for this game
define MM = Character("Teacher")
define MC = Character("[povname]")
define SC = Character("Kevin Ng")
define JC = Character("Spencer Johnson")

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

# Here we are loading in all the images used in this game
image bg sunset1 = "bg schoolsunset_1.jpg"
image bg sunset2 = "bg schoolsunset_2.jpg"
image bg blackscreen = "bg blackscreen.jpg"
image bg outside = "bg outside.jpg"
image bg classroom = "bg classroom.jpg"


label start:
    #Gets the user input for name

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Williana Wonkas"

    scene bg sunset1
    "Pleasant Valley Prepatory..."

    scene bg sunset2
    "A school known for its flawless reputation and distinguished staff..."

    scene bg blackscreen
    "But what happens when something goes wrong?"

    play sound "glass.ogg"

    scene bg outside
    "Well, you know what they say... The most unlikely places are the darkest of them all."
    play sound "sirens.ogg"

    scene bg outside

    # This is where the game begins
    menu:
        "As the city's best detective, it is your job to interview the death of a student from the local prepatory school.\n
        Who would you like to interrogate first?"

        "The Teacher": 
            jump Teacher_Begin
        "The Janitor":
            jump Janitor_Begin
        "The Classmate":
            jump Classmate_Begin
    
    label Teacher_Begin:
        return
    label Janitor_Begin:
        return
    label Classmate_Begin:
        menu:
            "What's your name?":
                jump Classmate_Intro1
            "Well, go on.":
                jump Classmate_Intro2
    label Classmate_Intro1:
        "My name is Kevin. I'm a classmate of...you know, them."
        "Or I guess I was."
    label Classmate_Intro2:
        "Oh, you want me to just start talking? Well, fine. I'm Kevin. I'm a classmate of...you know, them."
        "Or I guess I was."

    # This ends the game.

    return
