label w0_d2_LunchJava:
    # I think this should increase JS affection, currently not in script - Lazzy
    show js with dissolve
    mc "\"Hey JavaScript, I’m sorry for how I was acting earlier.\""
    mc "\"That was mean of me.\""

    js @ talk "\"Oh, it’s okay.\""
    js @ talk "\"It was really just a misunderstanding.\""

    mc "\"Okay, whew. I was scared you would still be mad at me.\""

    js talk "\"No, it’s okay.\""
    js "\"I’m not mad.\""
    js "\"Like I said, it was a misunderstanding, I’m not mad.\""
    js "\"Thank you for coming and sitting with me.\""
    js "\"I am really excited to eat this lunch!\""
    js "\"I’ve heard the plantains are to die for.\""
    show js

    mc "\"Yeah me too, I love plantains.\""
    mc "\"And I didn’t get to eat breakfast, so I’m pretty hungry.\""

    js @ talk "\"How come? Breakfast is like the most important meal of the day.\""

    mc "\"My morning was a mess.\""
    mc "\"I am from an area about 4 hours away from here and so I had to stay in a hotel.\""
    mc "\"And last night I was up way too late.\""
    mc "\"And as you can guess I didn’t wake up on time.\""

    js @ talk "\"Did you make it to orientation on time?\""

    mc "\"Yeah, and that wasn’t even the worst part.\""
    mc "\"I rushed out the door and got in my car in like 3 minutes so I could get to orientation on time.\""
    mc "\"But when I started driving, I realized I didn’t even know where the school was.\""

    js @ talk "\"Yeah, I literally experienced something like that too!\""
    js @ talk "\"Even though my mom drove with me, I still have no idea how to get around this town.\""

    mc "\"Then I eventually got here, and I realized I missed the start of orientation.\""
    mc "\"Luckily, there was a professor there who told me where to go.\""
    mc "\"And that’s how I ended up in the breakout room.\""

    js talk "\"You met a professor?\""
    js "\"I don’t think there are any professors on campus right now.\""
    js "\"Classes haven’t started, so they have no reason to be here.\""
    show js

    mc "\"Huh I didn’t think of that.\""
    mc "\"She was definitely older than us and seemed really knowledgeable.\""
    mc "\"She definitely wasn’t a student, she looked too old to be anywhere near our age.\""

    js @ talk "\"Hmm, maybe-\""

    show python pocket at left with dissolve
    show cpp at right with dissolve
    jump w0_d2_LunchApology
    
