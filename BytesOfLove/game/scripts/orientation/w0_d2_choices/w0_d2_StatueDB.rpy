label w0_d2_StatueDB:
    $ c_rep = reputation(c_rep, -affection_change)
    $ p_rep = reputation(p_rep, -affection_change)
    $ js_rep = reputation(js_rep, -affection_change)
    show python pocket
    show cpp
    show js

    mc "{i}Distracted{/i} \"Wait, guys. Look at that girl over there.\""
    mc "\"She is actually so hot, should I go talk to her?\""

    p angry @ angry talk "\"What are you even talking about, [mc]?\""

    js @ talk "\"Yeah, what is wrong with you?\""
    js @ talk "\"Were you even listening to the conversation we were having?\""

    mc "\"What? Of course I was!\""

    menu w0_d2_GuessingConvo:
        c @ talk"\"Okay, then what were we talking about?\""

        "\"The political and economic state of the world\"":
            jump w0_d2_StatueDBContinue

        "\"Breaking Bad\"":
            jump w0_d2_StatueDBContinue

        "\"The Seahawks should have ran the ball\"":
            jump w0_d2_StatueDBContinue

label w0_d2_StatueDBContinue:
    c "\"See? That wasn’t even close to what we were talking about.\""

    js @ talk "\"I bet you didn’t know what we were talking about because you were too busy staring at that girl!\""
    js @ talk "\"You are sooo into her!\""

    mc "\"Woah, woah, woah. You’re getting mad at me?\""
    mc "\"Look at her, she’s a 10!\""
    mc "\"When do you get to see girls THAT cute?\""

    menu w0_d2_CuteGroup:
        p @ angry talk "\"What? Aren’t we cute enough?\""

        "Admit the girls are cute":
            mc "\"Well I am not going to sit here and say that you guys aren’t cute...\""
        
        "Deny that they're cute":
            $ c_rep = reputation(c_rep, -affection_change)
            $ p_rep = reputation(p_rep, -affection_change)
            $ js_rep = reputation(js_rep, -affection_change)
            
            mc "\"No way! I don’t think that! That’s crazy! I mean-\""
            mc "\"This feels like a trap!\""
            mc "\"I was just looking at that girl, it wasn’t related to you three.\""

            p @ angry talk "\"Okay, I see how it is...\""

            mc "\"No, I meant-\""
    
    c @ angry talk "\"Well I don’t care who you think is or isn’t cute!\""
    c @ angry talk "\"That’s no reason to be ignoring us.\""

    js @ talk "\"Yeah, sorry our conversation isn’t interesting enough for you.\""

    mc "\"No, that’s not what I was saying-\""
    
    hide python
    hide cpp
    hide js
    show bsl
    bsl @ talk "\"Hey you guys are being really loud.\""
    bsl @ talk "\"Could you try to keep it down?\""

    mc "\"Sorry...\""

    jump w0_d2_AfterStatue