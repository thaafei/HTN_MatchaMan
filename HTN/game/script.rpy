# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Here we are defining global variables, including characters and counters, for this game
define MM = Character("Mr. Holmes")
define MC = Character("Detective [povname]")
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
image bg bed_night = "bg bed_night.jpg"


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

    play sound "Sound Effects/glass.ogg"

    scene bg outside
    MC "Well, you know what they say... The most unlikely places are the darkest of them all."
    play sound "Sound Effects/sirens.ogg"

    scene bg outside

    # This is where the game begins
    play music "Sound Effects/piano bg.mp3"

    "As the city's best detective, it is your job to investigate the death of a student from the local prepatory school."

    "Jasmine Gray, a senior at Pleasant Valley, disappeared last night and was discovered to have been murdered. "
    "There are no traces of the murderer except for a bit of matcha powder left on the scene, a hallmark of the once infamous Matcha Man killer."
    "He disappeared off the grid years ago: could he have possibly come back?"


    MC "Well, it's time to start the day."
    menu:
        "Who would you like to interrogate first?"

        "The Teacher": 
            jump Teacher_Begin
        "The Janitor":
            jump Janitor_Begin
        "The Classmate":
            jump Classmate_Begin
    
    #Teacher Route
    label Teacher_Begin:
        show MM
        menu: 
            "State your name and occupation.":
                jump Teacher_Intro1
            "What's your name?":
                jump Teacher_Intro2

    label Teacher_Intro1:
        show MM
        MM "Jerry Holmes, and a teacher, obviously."
        jump Teacher_P2
    
    label Teacher_Intro2:
        show MM
        MM "The kids call me Mr.Holmes, I teach their English and Foreign Language Classes."
        jump Teacher_P2
    
    label Teacher_P2:
        show MM
        MC "What can you tell me about that day, did you notice the victim acting strange?"

        MM "Jasmine did seem a litte reserved. From the classroom gossip, it sounds like her boyfriend broke up with her, something about adultery? "

        menu:
            "Tell me about this boyfriend of hers.":
                jump Teacher_P3_1
            "Tell me more about you.":
                jump Teacher_P3_2

    label Teacher_P3_1:
        show MM
        MM "Kevin? He does well enough in school and sports. Although he does have a bit of a hot-temper."
        MC "A hot-temper?"
        MM "Yes, the reason he transferred to our prepatory was because he would frequently get into fights at his old school."
        MC "Hmm.. noted."
        jump Teacher_Last


    label Teacher_P3_2:
        show MM Sad
        MM "I'm devasted, it's a sad day when a student misses a class for a day... now this..."
        MM "Jasmine was always a ray of sunshine, she had an interest in tea as well."
        MM "We would frequently discuss on tea brewing techniques after classes..."
        "........."
        MM "I'm sorry, I need a minute.."
        MC "Of course"
        jump Teacher_Last

    label Teacher_Last:
        hide MM Sad
        hide MM

        MC "After I finish talking to the teacher, I assess my choices."
        menu:
            "Talk to The Teacher again.":
                jump Teacher_Begin
            "Talk to The Classmate":
                jump Classmate_Begin   
            "Talk to The Janitor.":
                jump Janitor_Begin
            "Make your decision.":
                jump End_Choice

#JANITOR ROUTE
    label Janitor_Begin:
        show JC
        menu:
            "Good morning, can I have a minute?":
                jump Janitor_Intro1
            "Hey! I need to talk to you!":
                jump Janitor_Intro2
    label Janitor_Intro1:
        JC "Sure, whaddya need?"
        jump Janitor_P2
    label Janitor_Intro2:
        show JC Angry
        JC "Yo! Watch your tone! *tsk* You and all these kids keep testing my limits! Leaving your bubble tea cups everywhere and giving me attitude..."
        jump Janitor_P2

    label Janitor_P2:
        MC "I'm here to investigate the murder of Jasmine Gray."
        menu:
            "Did you know her?":
                jump Janitor_P3
            "Did you witness any suspicious behaviour on campus before her death?":
                jump Janitor_P3_2
    
    label Janitor_P3:
        show JC Annoyed
        JC "Personally? No. I caught her and her boyfriend in my storage room once a few months back. Awkward. I didn't see them around for some time though."
        jump Janitor_Last

    label Janitor_P3_2:
        show JC Annoyed
        JC "I can't say for sure. But that Holmes guy rubs me the wrong way. Always acting like he's better than everyone even though he has a mental breakdown every time he isn't near his stupid tea tumblr. The guy has issues."
        jump Janitor_Last

    label Janitor_Last:
        show JC
        MC "Hmm, I see. Thanks for the info."
        JC "Yeah, whatever."
        MC "After I finish talking to the Janitor, I assess my choices"
        hide JC
        menu:
            "Talk to The Teacher.":
                jump Teacher_Begin
            "Talk to The Classmate.":
                jump Classmate_Begin
            "Make your decision.":
                jump End_Choice

    #Classmate Route
    label Classmate_Begin:
        show SC
        menu:
            "What's your name?":
                jump Classmate_Intro1
            "Well, go on.":
                jump Classmate_Intro2

    label Classmate_Intro1:
        SC "My name is Kevin. I'm a classmate of Jasmine."
        jump Classmate_P2
        
    label Classmate_Intro2:
        SC "Oh, you want me to just start talking? Well, fine. I'm Kevin. I'm a classmate of Jasmine."
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
        SC "I was in Mr. Holmes class last period."
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
        SC "I don't know much about him, only that I've never seen him without his green tea."
        jump Classmate_Last

    label Classmate_P4_2:
        SC "He's been working this job for as long as anyone can remember. Don't know why, though— he hates it here, hate us kids specifically."
        SC "Says it's because we always leave our bubble tea cups around."
        jump Classmate_Last

    label Classmate_Last:
        hide SC
        MC "After I finish talking to the student, I assess my choices."
        menu:
            "Talk to The Classmate again.":
                jump Classmate_Begin
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
        scene bg bed_night
        MC "After the Janitor Spencer was convicted for the murder using my evidence, I felt at ease. The city was safe."
        MC "When I returned home, however, something seemed to overwhelm me. The smell of...matcha."
        MC "It must be a trick. Surely."
        MC "But when I turend around, I saw it— the letter, and the tell tale dust of matcha powder right on top."
        "{i}YOU'RE NEXT{/i}"
        scene bg blackscreen
        "BAD ENDING"

    label Classmate_Ending:
        scene bg bed_night
        MC "After the classmate Kevin was convicted for the murder using my evidence, I felt at ease. The city was safe."
        MC "When I returned home, however, something seemed to overwhelm me. The smell of...matcha."
        MC "It must be a trick. Surely."
        MC "But when I turned around, I saw it— the letter, and the tell tale dust of matcha powder right on top."
        "{i}YOU'RE NEXT{/i}"
        scene bg blackscreen
        "BAD ENDING"
    
    # This ends the game.

    return
