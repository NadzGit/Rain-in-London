define t = Character("Tahsan")
define h = Character("Haris")
define j = Character("Josh")

label start:
    scene cafe 

    t "Life is all about choices, isn't it? Coffee or tea. Take the bus or walk. And now... Josh or Haris."

    scene joshvsharis

    t "They're so different, yet... both make me feel alive in ways I didn’t think possible."

    menu:
        "Tell me about Josh.":
            jump joshbranch
        "Tell me about Haris.":
            jump harisbranch

    


label joshbranch:
    scene raincentrallondon

    show joshsmile:
        xalign 0.3
    j "C'mon, Tahsan! It's just a little rain. We’re not made of sugar!"

    show tahsansmile:
        xalign 0.7
        
    t "You’re impossible, you know that?"

    show tahsansmile:
        xalign 0.7 
        linear 1.0 xalign -0.3

    show joshsmile:
        xalign 0.3
        linear 0.5 xalign -0.3

    pause 1.0
    hide tahsansmile
    hide joshsmile


    scene bigben

    show tahsansmile:
        xalign 0.7
    show joshsmile:
        xalign 0.3
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

    show harisneutral:
        xalign 0.3
    
    show tahsansmile:
        xalign 0.7
        
    h "I like this. Just sitting here... no noise, no distractions."

    t "You’ve always liked the quiet moments."

    h "Because that’s when people’s real selves come through. Like you... right now, you're thinking about something, aren't you?"

    pause 1.0
    
    t "...It’s complicated."

    show harissmile:
        xalign 0.3
    
    h "It doesn’t have to be. Sometimes, the right choice is the one that brings you peace."

    menu: 
        "I feel safe with you, Haris.":
            jump harisending
        "I need time to think.":
            jump maindecisionpoint

label maindecisionpoint:
    scene apartment

    t "Josh makes me feel alive—spontaneous, free. But Haris... he’s my safe place, my calm in the storm. How do I choose between two parts of myself?"

    menu:
        "Choose Josh.":
            jump joshending
        "Choose Haris.":
            jump harisending
        "Choose both":
            jump polyending
        "Stay alone":
            jump neutralending
    
    

label joshending:
    scene morning

    show joshblush:
        xalign 0.3

    show tahsanblush:
        xalign 0.7

    j "Told you we'd make it through the storm."

    t "I guess I don’t mind getting caught in the rain... with you."

    show tahsanblush:
        xalign 0.7 
        linear 1.0 xalign -0.3

    show joshblush:
        xalign 0.3
        linear 0.5 xalign -0.3

    pause 1.0
    hide tahsansmile
    hide joshsmile

    scene joshending with fade

    pause 6.0

    return


label harisending:
    scene park_sunset

    show harissmile:
        xalign 0.3
    
    show tahsansmile:
        xalign 0.7
    
    h "You made the right choice, you know. You don’t have to say anything. I just... know."
    t "I’m glad you’re here."

    hide harissmile
    hide tahsansmile

    scene harisending with fade

    pause 6.0

    return 

label polyending:
    scene chickenshop

    show joshangry:
        xalign 0.2
    
    show harissmile:
        xalign 0.8
    
    show tahsansad:
        xalign 0.5

    t "I... I care about both of you. I don’t want to choose."
    j "So, what? We’re just supposed to share you?"
    h "If that’s what makes you happy, Tahsan, then I’m willing to try."
    t "I think it could work. As long as we’re honest with each other."
    show joshneutral:
        xalign 0.2
    hide
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

    scene neutralending with fade#

    pause 6.0
    return