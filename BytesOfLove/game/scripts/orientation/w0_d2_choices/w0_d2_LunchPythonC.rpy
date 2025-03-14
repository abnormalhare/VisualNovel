label w0_d2_LunchPythonC:
    mc "\"Hey Python and C++, what did you guys get for lunch?\""
    show python at left with easeinleft
    p angry "\"...\""
    mc "\"Look, I’m sorry about what happened earlier.\""
    mc "\"Do you think we can move past this and start over?\""
    
    p @ angry talk "\"I guess it would be nice if we all got along.\""
    p @ angry talk "\"What do you think, C++?\""

    show cpp at right with easeinright
    c @ talk "\"I don’t care, do whatever you want.\""

    p pocket @ pocket happy "\"It’s settled then.\""
    p @ pocket happy "\"No hard feelings, we’re all friends here.\""

    mc "\"Great. What did you get for lunch?\""

    p @ pocket happy "\"I got a beef burrito and some plantains for lunch.\""
    p @ pocket happy "\"It looks really good, and I am starving!\""

    mc "\"Yeah me too, I didn’t even get to eat breakfast.\""

    c @ talk "\"Why not? You’re so stupid you don’t know how to cook?\""
    c @ talk "{i}Sighs{/i} \"Sorry that was mean, why didn’t you get breakfast??\""

    mc "\"My morning was a mess.\""
    mc "\"I am from an area about 4 hours away from here and so I had to stay in a hotel.\""
    mc "\"And last night I was up way too late.\""
    mc "\"And as you can guess I didn’t wake up on time.\""

    c @ talk "\"And that was why you barely made it to the room on time?\""

    mc "\"Yeah, and that wasn’t even the worst part.\""
    mc "\"I rushed out the door and got to my car in like 3 minutes.\""
    mc "\"But when I started driving, I realized I didn’t even know where the school was.\""

    p @ pocket happy "\"Yeah, I ran into the same problem.\""
    p @ pocket happy "\"I have never been to Bytesborough before today.\""

    mc "\"Then I eventually got here and I realized I missed the start of orientation.\""
    mc "\"Luckily there was a professor there who told me where I was supposed to go.\""
    mc "\"And that’s how I ended up in the breakout room.\""

    c talk "\"You met a professor?\""
    c "\"I don’t think there are any professors on campus right now.\""
    c "\"Since classes haven’t started, they have no reason to be here.\""
    show cpp

    p @ pocket happy "\"You’re right. Come to think of it, I haven't seen any professors either.\""

    mc "\"Huh, I didn’t think of that.\""
    mc "\"She was definitely older than us and seemed really knowledgeable.\""

    c @ talk "\"You better not be trying to get ahead of me before the semester even starts.\""

    mc "\"Don’t worry, I don’t have to try, I’m probably ahead of you already.\""
    mc "\"Anyway, what did you guys think about JavaScript?\""

    p @ pocket happy "\"She seemed really nice.\""

    c @ talk "\"She just does too much.\""
    c @ talk "\"She was always saying ‘slay’, or ‘queen’.\""
    
    menu w0_d2_JSAnnoying:
        c @ talk "\"Talk about being chronically online...\""

        "Make fun of JavaScript":
            mc "\"Yeah, she is pretty annoying.\""
            # Add camera pan
            mc "\"Look over there, she’s sitting alone.\""
            mc "\"It makes sense when you think about it.\""
            mc "\"I wouldn’t want to sit with her either.\""

        "Defend JavaScript":
            mc "\"I mean she can be a little much.\""
            mc "\"But I wouldn’t go as far as to say she is annoying.\""
            # Add camera pan
            mc "\"Look, she is sitting alone over there.\""
            mc "\"Do you guys want to go sit with her?\""
    
    p pocket happy "\"I think we should go sit with her.\""
    p "\"She is probably feeling lonely.\""
    p "\"And we shouldn’t be mean to someone who could be our new friend.\""
    show python pocket

    show js with dissolve
    jump w0_d2_LunchApology
