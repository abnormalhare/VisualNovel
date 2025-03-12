label w0_d2_StatueJS:
    $ p_rep = reputation(p_rep, 2)
    $ js_rep = reputation(js_rep, 2)
    $ c_rep = reputation(c_rep, -2)
    show js
    show python pocket
    mc "\"I agree with JavaScript and Python, you need to take a chill pill C++.\""
    mc "\"He does look cool, I didn’t realize that was ‘Firewall’ Jackson either.\""

    c angry @ angry talk "\"Ugh whatever.\""
    c @ angry talk "\"You guys need to be more knowledgeable, though, it’s embarrassing.\""

    js @ talk "\"That is ridiculous, why do you even know that?\""

    c @ angry talk "\"Who doesn’t know that?\""
    c @ angry talk "\"Have you ever taken a history class?\""

    js talk "\"Yes I have!\""
    js "\"You are being so mean right now, C++, there’s no need to be nasty!\""
    js "\"I bet you’re just mad because [mc] doesn’t agree with you.\""
    show js

    c handhip @ handhip talk "\"Well [mc] is only agreeing with you because he thinks you’re cute.\""

    mc "{i}Flustered{/i} \"Whoa whoa whoa, I never said that.\""

    show js smirk

    menu w0_d2_CuteJS:
        js "\"Hm, so do you think I’m cute?\""

        "Admit JavaScript is cute":
            $ js_rep = reputation(js_rep, 2)
            mc "{i}Flustered{/i}"
            mc "\"Well... that’s not exactly what I was saying...\""
            mc "\"But, I do think you’re kind of cute.\""
            
            js blush "{i}Blushes{/i} \"Well that makes sense…\""

            c handhip talk "\"Ugh I knew it!\""
            c "\"So typical of boys to only care about looks.\""
            c "\"JavaScript, don’t think you’re right just because this guy agrees with you!\""
            show cpp handhip
            
            js talk "\"And what would you know about being right?\""
            js "\"You’re just mad because he didn’t take your side!\""
            show js smirk

            c @ handhip talk "\"I wouldn’t want someone so superficial to agree with me anyway!\""

            mc "\"Woah, I’m not superficial, I just think--\""

        "Call out JavaScript":
            $ js_rep = reputation(js_rep, -2)
            mc "\"Alright, don’t go fishing for a compliment just because I agreed with you...\""
            mc "\"I agree that Python shouldn’t go around calling statues cool without knowing what they represent.\""
            mc "\"That's it.\""

            js talk "\"So you think I'm ugly!?\""
            show js angry
            mc "\"I-\""
            
            c talk "\"Why are you begging for his attention, JavaScript?\""
            c "\"This isn’t about you, it’s about the statue.\""
            c "\"Or did you forget what you were so mad about already?\""
            show cpp handhip

            js talk "\"Listen, know it all, no one asked you for your input in the first place.\""
            js "\"You’re just mad because he didn’t take your side.\""

            c @ handhip talk "\"At least he doesn’t think I’m ugly...\""

            js -angry @ talk "\"Excuse me!?\""
            
            mc "\"I never said-\""
    
    jump w0_d2_StatueSexist