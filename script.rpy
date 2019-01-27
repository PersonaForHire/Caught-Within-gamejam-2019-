define owo = Character("Owolman")
define negaowo = Character("Owolman?")
define main = Character("[name]")
define vog = Character("")
define owomom = Character("Owomom")
define superultramegagod =("creator")

label start:
    python:
        name =renpy.input("Enter your name")
        name = name.strip()
        if not name:
            name="I guess no name for u"
    play sound "eatshit.mp3"

    scene bg hallway_spooky
    show owo man_cropped_variation at right
    main "Oh I dont like this"
    owo "Come on, this might be our only way of getting out of here"
    main "I know but.... "
    vog "With this little exchange the worried pair travesed the hallway and reached the door on the other side"
    "They pushed the door open and entered the realm of the long-forgotten throne"
    
    scene bg bathroom_distorted
    
    vog "There is an eerie miasma like atmosphere that immediately sends a chill down our parties’ spines"
    "Our two unwilling participants stepped into the room as careful as if they had just entered the lair of a starving beast they were put in a state of extreme unease."
    "The mist begins to increasingly gather at our protagonists’ feet the farther they go in. They stop for a second looking at each other with the eyes of men who have not known such fear before."
    "Gathering their courage, they ventured further into the room. "
    "They reach where the fog is thickest, they can barely see each other now, the world they were just getting acquainted with now visibly lost to them, a feeling of isolation and loneliness washes over them"
    "This abject feeling of foreboding cripples them. Standing there silent and shaking in fear they see another form emerge from the mist. "
   
    show negaowo broker
    
    vog "The figure cast in a shroud made from a mix of dense fog and mystery made himself known to our not so intrepid heroes"
    "The new creature before them slowly approached them and stared at them with dead eyes"
    
    menu:
        
        "Confront that fucker":
            jump goodname
        
        "Run its the only way":
            jump bathroomenemy
            
    label bathroomenemy:
        vog "Your instincts tell you the only way to survive is to run, faster and harder than you ever have before."
        "You try to move but your body won't let you"
        "You begin to feel weak and collapse, that figure still loaming over you. "
        
        scene bg deathscreen with fade
        play sound "youdied.ogg"
        vog "Too bad my dude"
        return
        
    label goodname:
        
        vog "[name] realizing that this could be the end anyway decided to go out fighting. "
        "Gathering up what remained of their courage [name] stepped towards the unknown creature, seeing this the creatures eyes widened, taking a step back and vanishing into the mist. "
        main "Huh that wasnt so tough now was it Owo?"
        owo "Are u kidding me that was absolutly terrifying. Anyway it seems to be as scared of us as we are of it."
        main "Ya we shouldnt have to worry about that thing for a while at the very least."
        vog "As the two converse the fog began disapateing rapidly. When the fog cleared a sound resenated through the house"
        owo "That sounds like it come from the front door"
        vog "The two raced back to the front door"
        
        scene bg hall_distorted with fade
        owo "It looks like the door is unlocked now"
        main "Thank god. I thought we would be trapped in here forever"
        owo "*reaches out and opens the door*"
        
        scene bg blind with fade
        
        owo "Jeez why is it so bright"
        main "MY EYES!!!!!!!"
        
        scene bg final with fade
        main "Where are we?"
        owomom "A place where that thing can never reach u"
        main "Who said that?"
        show owomom left
        owo "MOM?!?!?!?"
        main "What the fuck is going on?"
        vog "I dont even know anymore"
        main "OK WHO SAID THAT?"
        vog "....................."
        "........................."
        "........................."
        "Yo"
        "Whats up?"
        "Its ya boi"
        "uh..."
        "Mika"
        show owomom left at left
        show vog dog at right
        main "You know what f this"
        main "Im out *walks out of game*"
        owo "Well what do we do now?"
        vog "I guess the games done"
        owo "Wait seriously its just going to end like this"
        "....."
        "Thats bullhshit"
        "What no moral or anything?"
        owomom "Ok the moral of the story is home is a nightmareish hellscape that no person can escape"
        owo "..........."
        
        scene bg all
        superultramegagod "Hey thanks for playing this trash fire and thanks to all the people who put up with us while we were high on energy drinks makeing this"
    return