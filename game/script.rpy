define t = Character("Tahsan")
define h = Character("Haris")
define j = Character("Josh")




label start:
    scene cafebg


    t "Life is all about choices, isn't it? Coffee or tea. Take the bus or walk. And now... Josh or Haris."

    scene joshvsharis

    t "They're so different, yet... both make me feel alive in ways I didn’t think possible."

    menu:
        "Tell me about Josh.":
            jump joshbranch
        "Tell me about Haris.":
            jump harisbranch

    


label joshbranch:
    
    transform show_left:
        zoom 1.3
        xalign 0.3 yalign 1.0
    
    transform show_right:
        zoom 1.3
        xalign 0.7 yalign 1.0

    scene londoneye

    show joshsmile at show_left
    j "C'mon, Tahsan! It's just a little rain. We’re not made of sugar!"

    show tahsansmile at show_right
        
    t "You’re impossible, you know that?"

    show tahsansmile:
        zoom 1.3 
        xalign 0.7 yalign 1.0
        linear 1.0 xalign -0.8

    show joshsmile:
        zoom 1.3
        xalign 0.3 yalign 1.0
        linear 0.5 xalign -0.8

    pause 1.0
    hide tahsansmile
    hide joshsmile


    scene bigben

    show tahsansmile:
        zoom 1.3
        xalign 1.8 yalign 1.0
        linear 1.0 xalign 0.7

    show joshsmile:
        zoom 1.3 
        xalign 1.8 yalign 1.0
        linear 1.0 xalign 0.3
    j "You know what I love about this city? It feels alive. Even in the rain."
    t "Yeah... it does."

    j "You make me feel alive too, you know? Being with you—it's like... I forget about the rest of the world."

    menu:
        "I feel the same way, Josh.":
            jump joshending
        "I need time to think.":
            jump maindecisionpoint

label harisbranch:
    scene park

    show harissmile at show_left

    
    show tahsansmile at show_right
        
        
    h "I like this. Just sitting here... no noise, no distractions."

    t "You’ve always liked the quiet moments."

    h "Because that’s when people’s real selves come through. Like you... right now, you're thinking about something, aren't you?"

    hide tahsansmile
    show tahsansad at show_right

    pause 1.0
    
    t "...It’s complicated."

    hide harissmile
    show haristalking at show_left
    
    h "It doesn’t have to be. Sometimes, the right choice is the one that brings you peace."

    menu: 
        "I feel safe with you, Haris.":

            t "I feel safe with you Haris."
            h "Well I'm glad you feel like that, I feel the same way."
            t "No, I mean..."

            hide tahsansad
            show tahsanblush at show_right

            hide haristalking
            show harissmile at show_left

            h "What do you mean Tahsan?"
            t "Well, um..."

            hide harissmile
            show haristalking:
                zoom 1.3
                xalign 0.3 yalign 1.0
                linear 0.5 xalign 0.5
            
            hide tahsanblush
            show tahsanextrablush:
                zoom 1.3
                xalign 0.7 yalign 1.0
                linear 0.5 xalign 0.8
            
            h "Could you mean..."
            h "You like me?..."


            t "!"
            
            
            show haristalking:
                zoom 1.3
                xalign 0.5 yalign 1.0

            h "Me and my emirati passport, hm?"

            t "W-well, that's not it..."
            
            show haristalking:
                zoom 1.3
                xalign 0.5 yalign 1.0
                linear 0.3 xalign 0.7
            h "It's not?"

            show tahsanextrablush:
                xalign 0.9 yalign 1.0

            t "I-I mean..."
            hide tahsanextrablush
            show tahsanblush:
                zoom 1.3
                xalign 0.9 yalign 1.0
                

            t "I like you..."
            t "But the passport's kinda nice too..."

            hide haristalking
            show harissmile at show_left
            h "Haha..."

            hide harissmile
            show haristalking at show_left
            h "Only kidding, I've known you liked me for a while to be honest."

            hide tahsanblush
            show tahsanextrablush:
                zoom 1.3
                xalign 0.9 yalign 1.0
            
            t "You've known??!!"

            h "I saw the way you were eyeing up my emirati passport. I know you want me."

            t "Okay well I wouldn't put it like that..."

            h "Come here big boy."

            h "Let me give you this emirati passport."

            show haristalking:
                zoom 1.3 
                xalign 0.3 yalign 1.0
                linear 1.0 xalign 0.7
            
            t "Hey! Not so fast!"

            show tahsanextrablush:
                zoom 1.3
                xalign 0.9 yalign 1.0
                linear 0.6 xalign -0.8

            pause 3.0
            
            jump harisending
        "I need time to think.":
            t "I..."
            t "I need time to think."

            hide haristalking
            show harissad at show_left
            h "I understand..."

            jump maindecisionpoint

label maindecisionpoint:
    scene apartment

    t "Josh makes me feel alive—spontaneous, free. But Haris... he’s my safe place, my calm in the storm. How do I choose between two parts of myself?"

    menu:
        "Spend time with Josh":
            jump joshbranch
        "Spend time with Haris":
            jump harisbranch
        "Choose Josh.":
            jump joshending
        "Choose Haris.":
            jump harisending
        "Choose both":
            jump polyending
        "Stay alone":
            jump neutralending
    
    

label joshending:
    scene bigben

    show joshsmile:
        zoom 1.3
        xalign 0.3 yalign 1.0

    show tahsansmile:
        zoom 1.3
        xalign 0.7 yalign 1.0
    
    t "I feel the same way, Josh."

    show joshneutral:
        zoom 1.3
        xalign 0.3 yalign 1.0

    j "..."

    pause 1.0

    # play heartbeat
    
    j "Say it properly."

    hide tahsansmile
    show tahsanblush:
        zoom 1.3
        xalign 0.7 yalign 1.0
    
    t "I..."
    t "I-"
    pause 0.8
    t "I like you Josh."

    hide joshneutral

    show joshsmile:
        zoom 1.3
        xalign 0.3 yalign 1.0

    j "I like you too, Tahsan"

    j "I knew we'd make it through the storm."

    
    show tahsanblush:
        zoom 1.3
        xalign 0.7 yalign 1.0
        
    t "I guess I don’t mind getting caught in the rain... with you."
    show tahsansmile:
        zoom 1.3
        xalign 0.7 yalign 1.0
    t "Whatever that means..."

    
    pause 1.0
    hide tahsanblush
    show tahsansmile:
        zoom 1.3
        xalign 0.7 yalign 1.0
        linear 1.0 xalign -0.8

    show joshsmile:
        zoom 1.3 
        xalign 0.3 yalign 1.0
        linear 0.5 xalign -0.8

    pause 1.0
    hide tahsansmile
    hide joshsmile

    scene joshending with fade

    pause 6.0

    return


label harisending:
    scene park_sunset

    show harissmile at show_left
    
    show tahsansmile at show_right
    
    h "You made the right choice, you know. You don’t have to say anything. I just... know."
    t "I’m glad you’re here."

    hide harissmile
    hide tahsansmile


    scene harisending with fade

    pause 6.0

    return 

label polyending:

    transform show_middle:
        zoom 1.3
        xalign 0.5 yalign 1.0


    scene chickenshop

    show joshangry at show_left
    
    show harissmile at show_right
    
    show tahsansad at show_middle

    t "I... I care about both of you. I don’t want to choose."
    j "So, what? We’re just supposed to share you?"
    h "If that’s what makes you happy, Tahsan, then I’m willing to try."
    t "I think it could work. As long as we’re honest with each other."
    j "You guys don't get it. I'm silver."
    j "What's this guy got that I don't?!"
    t "An emirati passport."
    j "{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0} Shit."

    hide harissmile
    show haristalking at show_right
    h "I mean {w=1.5}I could show you the fruits of having an emirati passport if you'd be willing to do this with us~"

    hide joshangry
    show joshblush at show_left
    j "I, I mean {w=1.0} s-sure...{w=1.5} whatever I guess..."
    t "And, josh {w=1.0}you could carry Haris out of iron?"
    hide joshblush
    show joshangry at show_left
    j "Yeah, whatever. Sure."

    hide haristalking
    show harissmile at show_right
    
    hide joshangry
    show joshneutral at show_left
    
    j "This is going to be interesting."
    h "But I’m willing to see where it goes."
    t "Me too."
    hide joshneutral
    hide harissmile
    hide tahsansad
    scene polyending with fade

    pause 6.0
    return

label neutralending:
    scene apartment_night

    t "Maybe I don’t need to choose right now. Maybe it’s okay to take time to figure myself out first."

    scene neutralending with fade

    pause 6.0
    return