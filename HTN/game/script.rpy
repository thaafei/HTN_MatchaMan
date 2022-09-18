# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Here we are defining global variables, including characters and counters, for this game
define MM = Character("Mr. Holmes")
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
    MC "Pleasant Valley Prepatory..."

    scene bg sunset2
    MC "A school known for its flawless reputation and distinguished staff..."

    scene bg blackscreen
    MC "But what happens when something goes wrong?"

    play sound "glass.ogg"

    scene bg outside
    MC "Well, you know what they say... The most unlikely places are the darkest of them all."
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
        show SC
        menu:
            "What's your name?":
                jump Classmate_Intro1
            "Well, go on.":
                jump Classmate_Intro2
    label Classmate_Intro1:
        SC "My name is Kevin. I'm a classmate of...you know, them."
        jump Classmate_P2
        
    label Classmate_Intro2:
        SC "Oh, you want me to just start talking? Well, fine. I'm Kevin. I'm a classmate of...you know, them."
        jump Classmate_P2
    
    label Classmate_P2:
        show SC Sad
        SC "Well, I guess I was."
        menu: 
            "Were you friends?":
                jump Classmate_P2_1
            "What was your relationship like?":
                jump Classmate_P2_2
    label Classmate_P2_1:
        show SC Angry
        SC "Something like that."
        jump Classmate_P3

    label Classmate_P2_2:
        show SC Angry
        SC "We...used to be well acquainted."
        jump Classmate_P3

    label Classmate_P3:
        show SC 
        menu:
            "What do you remember about that night?" :
                jump Classmate_P3_1
            "What were you doing that night?":
                jump Classmate_P3_2
    label Classmate_P3_1:
        SC "I was in Mr. Holmes class last  period, and headed to the local bubble tea place after class."
        jump Classmate_P4

    label Classmate_P3_2:
        SC "I was just studying at the local bubble tea place after my last class with Mr. Holmes."
        jump Classmate_P4
    
    label Classmate_P4:
        SC "That grumpy janitor was there again, so everyone wanted to leave the school quickly."
        menu:
            "What can you tell me about the teacher?":
                jump Classmate_P4_1
            "What can you tell me about the janitor?":
                jump Classmate_P4_2

    label Classmate_P4_1:
        SC "Apparently he just...appeared in town one day and he's been here since. I've never seen him without his green tea."
        jump Classmate_Last
    label Classmate_P4_2:
        SC "He's been working this job for as long as anyone can remember. Don't know why, though— he hates it here, hate us kids specifically"
        jump Classmate_Last
    label Classmate_Last:
        MC "After I finish talking to the student, I assess my choices"
        menu:
            "Talk to The Teacher.":
                jump Teacher_Begin
            "Talk to The Janitor.":
                jump Janitor_Begin
            "Make your decision.":
                jump End_Choice

    label End_Choice:
        scene bg schoolsunset_1
        MC "Well, that was a long day of interrogations."
        MC "After everything, though, I feel like I know who the guilty party is."
        menu:
            "The Teacher":
                jump Teacher_Ending
            "The Janitor":
                jump Janitor_Ending
            "The Classmate":
                jump Classmate_Ending
    label Teacher_Ending:
        return
    label Janitor_Ending:
        return
    label Classmate_Ending:
        return
    
    # This ends the game.

    return
