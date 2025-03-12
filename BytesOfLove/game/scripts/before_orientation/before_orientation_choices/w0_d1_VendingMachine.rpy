label w0_d1_VendingMachine:
    mc "I think I’ll go downstairs to the vending machine, I could really go for a Snickers and Doritos right now."
    mc "And, I will save some money. You never know when you’ll need it."
    mc "I am pretty hungry though, maybe I should eat something more to fuel my body and mind."

    scene vending_machine
    #scene test
    "{i}*You walk downstairs to find a vending machine*{/i}"
    "{i}*On your way to the vending machines you see someone*{/i}"
    
    show rust at right with fade
    r @ talk "\"Hey there! I’m Rust! Do you go to UB?\""

    menu w0_d1_Rust:
        "Be mean":

            $ r_rep = reputation(r_rep, -affection_change)
            mc "\"Yeah, I do, my name is [mc].\""
            r talk "\"Cool cool. What’s your major?\""

            show rust confused
            mc "\"Wouldn’t you like to know...\""

            r "{i}*hushed*{/i} \"Damn, I was just wondering.\""
            r talk "\"I’m computer engineering, in case you wanted to know my major.\""

            show rust angry
            mc "\"Oh thanks, I didn't.\""
            r "\"Jeez... you don’t have to be mean about it, man.\""
            mc "\"Whatever.\""

            hide rust with dissolve
            "{i}*Rust leaves*{/i}"

        "Be nice":
            $ r_rep = reputation(r_rep, affection_change)

            mc "\"Yeah I do, my name is [mc]. What’s your major?\""

            r @ talk "{i}*Smiles*{/i} \"I’m computer engineering. What about you?\""

            mc "\"Oh, I’m in computer science!\""
            mc "\"We both need to take Programming 1, right?\""
            mc "\"Are you going to be doing it this semester?\""

            r talk "\"Yes, that's what I am planning on doing.\""
            r "\"I have some programming experience from highschool, but I’m excited to learn more.\""
            r "\"We can definitely work on projects and study together! It’ll be pretty cool.\""

            show rust
            mc "\"Absolutely! We’ll probably be spending a lot of time together.\""

            r talk "\"Yeah, I’m excited to get to know you better.\""
            r "\"Well anyway, I have to get back to my room so I can get a good night's sleep.\""
            r "\"You should probably do the same.\""
            r "\"It was nice to meet you, see you in class!\""

            hide rust with dissolve
            "{i}*Rust leaves*{/i}"

    "{i}*You stand at the vending machine, thinking about what you want*{/i}"
    $ byte = bytecoin(byte, -5)
    mc "Hmm, they don’t have Doritos, I guess I’m only getting a Snickers tonight."
    "{i}*You get a snickers bar and heads back up to your room*{/i}"

jump w0_d1_End