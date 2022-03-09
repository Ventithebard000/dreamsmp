define D = Character(_('<DREAM>'), color="#32cd32")
define G = Character(_('<GEORGE>'), color="#6495ed")
define S = Character(_('<SAPNAP>'), color="#e32636")
define d = Character(_('<???>'), color="#32cd32")
define g = Character(_('<???>'), color="#6495ed")
define s = Character(_('<???>'), color="#e32636")
define pov = Character(_('<[povname]>'), color="#ffff76")
define XD = Character(_('<XD>'), color="#add8e6")
define DS = Character(_('<DREAM> & <SAPNAP>'), color="#ceed13")
define GS = Character(_('<GEORGE> & <SAPNAP>'), color="#e016ff")
define DG = Character(_('<DREAM> & <GEORGE>'), color="#20ffbf")
define DT = Character(_('<DREAM TEAM>'), color="#ff18b7")
define YG = Character(_('<[povname]> & <GEORGE>'), color="#3dfee8")
define YS = Character(_('<[povname]> & <SAPNAP>'), color="#fea93d")
define YD = Character(_('<[povname]> & <DREAM>'), color="#c2fe3d")
define xd = Character(_('<???>'), color="#add8e6")

$ flash = Fade(0.5, 0, 0.5, color="#FFFFFF")


image phone = "phone.png"
image phone2 = "phone2.png"
image chest = "chest.png"
image gapple = "gapple.png"


image dream neutral = "dreamneutral.png"
image dream wary = "dreamwary.png"
image dream grin 1 = "dreamgrin1.png"
image dream grin 2 = "dreamgrin2.png"
image dream annoyed = "dreamannoyed.png"
image dream angry = "dreamangry.png"
image dream serious = "dreamserious.png"
image dream shock = "dreamshock.png"
image dream sigh = "dreamsigh.png"
image dream pained 1 = "dreampained1.png"
image dream pained 2 = "dreampained2.png"
image dream cry 1 = "dreamcry1.png"
image dream cry 2 = "dreamcry2.png"
image dream disappointed = "dreamdisappointed.png"


image george neutral = "georgeneutral.png"
image george grin 1 = "georgegrin1.png"
image george grin 2 = "georgegrin2.png"
image george sigh = "georgesigh.png"
image george serious = "georgeserious.png"
image george wary = "georgewary.png"
image george pained 1 = "georgepained1.png"
image george pained 2 = "georgepained2.png"
image george angry = "georgeangry.png"
image george annoyed = "georgeannoyed.png"
image george cry 1 = "georgecry1.png"
image george cry 2 = "georgecry2.png"
image george shock = "georgeshock.png"
image george disappointed = "georgedisappointed.png"
image george grin 2 blush = "georgegrin2blush.png"
image george embarrassed = "georgeembarrassed.png"


image sapnap neutral = "sapnapneutral.png"
image sapnap grin 1 = "sapnapgrin1.png"
image sapnap annoyed = "sapnapannoyed.png"
image sapnap wary = "sapnapwary.png"
image sapnap serious = "sapnapserious.png"
image sapnap grin 2 = "sapnapgrin2.png"
image sapnap sigh = "sapnapsigh.png"
image sapnap angry = "sapnapangry.png"
image sapnap pained 1 = "sapnappained1.png"
image sapnap pained 2 = "sapnappained2.png"
image sapnap shock = "sapnapshock.png"
image sapnap cry 1 = "sapnapcry1.png"
image sapnap cry 2 = "sapnapcry2.png"
image sapnap disappointed = "sapnapdisappointed.png"
image sapnap flushed 1 = "sapnapflush.png"
image sapnap flushed 2 = "sapnapflush2.png"


image XD neutral = "XDneutral.png"
image XD grin = "XDgrin.png"
image XD wary 1 = "XDwary1.png"
image XD wary 2 = "XDwary2.png"


image portal:
    "portal1.png"
    time 0.5
    "portal2.png"
    time 1.0
    "portal1.png"
    time 1.5
    "portal2.png"
    time 2.0
    "portal1.png"
    time 2.5
    "portal2.png"
    time 3.0
    "portal1.png"
    time 3.5
    "portal2.png"
    time 4.0



image error:
    "tverror1.png"
    time 0.3
    "tverror2.png"
    time 0.5
    "tverror3.png"
    time 1.0
    "tverror1.png"
    time 1.3
    "tverror2.png"
    time 1.5
    "tverror1.png"
    time 1.9
    "tverror4.png"
    time 2.3
    "tverror5.png"
    time 2.5
    "tverror4.png"
    time 2.9


define fastdissolve = Dissolve(0.5)
define slowdissolve = Dissolve(3.0)
define wipeleftfast = CropMove(0.5, "wipeleft")
define wipeupfast = CropMove(0.3, "wipeup")
define wipedownfast = CropMove(0.1, "wipedown")


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.8 xmaximum 300 at alpha_dissolve # This is the timer bar.

init:
    $ timer_range = 0
    $ timer_jump = 0



init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]



default book = False


init python:
    def purge_saves():
        saves = renpy.list_slots()
        for save in saves:
            renpy.unlink_save(save)
        renpy.take_screenshot()
        renpy.save("1-1", save_name)
        return


# screen debug_variables():
#   zorder 3000
#   vbox:
#     text "ending_count [ending_count]"
#     text "persistent.trueroute [persistent.trueroute]"


init python:
    if not persistent.trueroute:
        persistent.trueroute = None


label start:
    init:
        $ bad_choices = None
        $ ending_count = 0
        if persistent.seen_ending_1 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_2 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_3 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_4 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_5 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_6 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_7 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_8 == True:
            $ ending_count = ending_count + 1
        if persistent.seen_ending_7 == True and persistent.seen_ending_8 == True:
            $ bad_choices = True
        $ george_points = 0
        $ dream_points = 0
        $ sapnap_points = 0
        $ george_romantic = 0
        $ george_platonic = 0
        $ george_bad = 0
        $ sapnap_romantic = 0
        $ sapnap_platonic = 0
        $ sapnap_bad = 0
        $ dream_romantic = 0
        $ dream_platonic = 0
        $ dream_bad = 0

    stop music fadeout 1.0
    # show screen debug_variables
    scene cg1
    $ mouse_parallax.set ((-20, -5, "l0"))
    $ showp ("cg1")
    with fade
    "{b}8:59 PM.{/b}"
    "You stretched in your seat,{w=0.3} in the process of getting ready for a match of Hypixel with your friends when you've gotten a notification on your phone."
    "It was an alert from Twitch.{w=0.3} Your favorite streamers are online!"
    "You finish setting up and proceeded to wait for your friends in the lobby."
    "Thinking that they were taking quite a long while,{w=0.3} you decided to put the stream up on your phone."
    $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
    $ showp ("cg1", "phone")
    show phone
    with dissolve
    D "Hi!{w=0.3} Hello!{w=0.3} Welcome to the stream,{w=0.3} guys."
    D "I'm here with George and Sapnap,{w=0.3} say 'Hi'."
    G "Hi!"
    S "Helloooo!"
    D "We'll be doing another Minecraft Challenge for this stream!{w=0.3} This challenge,{w=0.3} we coded it so that we..."
    "Suddenly,{w=0.3} their voices began to fade out as your eyelids started to feel heavy."
    "You try to fight against the urge to shut your eyes but it was proven futile as you felt your body fall back from your seat,{w=0.3} completely blacking out."
    $ scenep ()
    with dissolve
    scene cg1
    scene black
    with fade
    play sound "audio/fall.mp3" volume 0.3
    "{b}{i}Thud!!{/i}{/b}"
    "You let out a groan as you felt your back collide with the ground."
    "You assumed that you had landed on your apartment floor until you heard three different voices from above you."
    d "That was a really harsh fall.{w=0.3} Do you think they're okay?"
    play sound "audio/sapnap idk.mp3"
    s "I don't know,{w=0.3} Dream.{w=0.3} Why don't you try landing a 140-block fall with no MLG?"
    "{i}Dream?{/i}{w=0.3} That name sounded familiar.{w=0.3} That sound effect ringing in your ear was just as familiar,{w=0.3} too."
    "You began to stir awake and attempt to open your eyes."
    g "Wait-{w=0.3} Guys,{w=0.3} shh!!{w=0.3} They're waking up,{w=0.3} I think!"
    scene cg2
    $ mouse_parallax.set ((-20, -5, "l0"))
    $ showp ("cg2")
    with dissolve
    play music "audio/Twin Musicom - Italian Morning.mp3" fadein 1.0 volume 0.5
    "You were met with three familiar faces looking down at you in concern."
    d "Hey!{w=0.3} Are you okay?"
    $ scenep ()
    with dissolve
    d "Here,{w=0.3} let me help you up..."
    scene flower
    with dissolve
    "You were brought up to your feet by the tall male in front of you,{w=0.3} your arms immediately flailing about as you try to regain your balance."
    "You then began to pat the dirt off of your pants as you come to the realization that you were surrounded by {i}three of your favorite Content Creators.{/i}"
    show dream wary
    with dissolve
    d "You're probably {i}so{/i} confused right now.{w=0.3} Um..."
    show dream neutral
    with dissolve
    D "I go by Dream.{w=0.3} What's yours?"
    hide dream neutral with dissolve


label a:
    $ povname = renpy.input("What is your name?")
    if povname == "Pissbaby":
        show dream grin 1 with dissolve
        D "Haha,{w=0.3} funny.{w=0.3} Seriously,{w=0.3} what's your name?"
        hide dream grin 1 with dissolve
        jump a
    if povname == "pissbaby":
        show dream grin 1 with dissolve
        D "Haha,{w=0.3} funny.{w=0.3} Seriously,{w=0.3} what's your name?"
        hide dream grin 1 with dissolve
        jump a
    if povname == "Fish":
        show george grin 1 with dissolve
        g "What was that?{w=0.3} Were you boxed like a fish?{w=0.3} What's your {i}actual{/i} name?"
        hide george grin 1 with dissolve
        jump a
    if povname == "fish":
        show george grin 1 with dissolve
        g "What was that?{w=0.3} Were you boxed like a fish?{w=0.3} What's your {i}actual{/i} name?"
        hide george grin 1 with dissolve
        jump a
    if povname == "Snapmap":
        show sapnap annoyed with dissolve
        s "Are you trying to annoy me?{w=0.3} What's your name,{w=0.3} like,{w=0.3} seriously."
        hide sapnap annoyed with dissolve
        jump a
    if povname == "snapmap":
        show sapnap annoyed with dissolve
        s "Are you trying to annoy me?{w=0.3} What's your name,{w=0.3} like,{w=0.3} seriously."
        hide sapnap annoyed with dissolve
        jump a

    if povname == "peg":
        show dream wary at left
        with dissolve
        D ".{w=0.3}.{w=0.3}.{w=0.3}"
        show george shock at right, bounce
        with dissolve
        g "Wait!"
        g "Is Dream g-{w=0.3}{nw}"
        hide dream wary
        hide george shock
        with dissolve
        jump a

    if povname == "Peg":
        show dream wary at left
        with dissolve
        D ".{w=0.3}.{w=0.3}.{w=0.3}"
        show george shock at right, bounce
        with dissolve
        g "Wait!"
        g "Is Dream g-{w=0.3}{nw}"
        hide dream wary
        hide george shock
        with dissolve
        jump a


    else:
     "You introduced yourself."

     jump b

label b:
     show dream grin 2 with dissolve
     "Dream grins."
     play sound "audio/dream hi.mp3"
     D "[povname]!{w=0.3} Nice to meet you."

     "Dream was then pushed over to the side by a brunet who had a bandana tied around his forehead.{w=0.3} He seemed to be a really energetic person."
     play sound "audio/fall.mp3" volume 0.3
     show dream serious at left
     with move
     show sapnap grin 1 at right, shake
     with dissolve
     play sound "audio/sapnap hi.mp3"
     S "Hi there,{w=0.3} [povname]!{w=0.3} I'm Sapnap."
     show dream angry at left
     with dissolve
     D "Sapnap,{w=0.3} you didn't have to shove me!"
     show sapnap annoyed at right
     with dissolve
     S "You just weren't quick enough to move out of the way!"
     "You bashfully nodded and waved back to the two as they both began to bicker.{w=0.3} You heard a sigh coming from your right and looked towards a shorter brunet."
     hide dream angry
     hide sapnap annoyed
     with dissolve
     show george sigh with dissolve
     G "I'm really sorry for these two.{w=0.3} This is all completely normal."
     show george neutral with dissolve
     play sound "audio/george hi.mp3"
     G "I'm George.{w=0.3} Pleasured to meet you,{w=0.3} [povname]."
     "George then cleared his throat loudly enough for the other two to hear."
     show george serious with dissolve
     G "So,{w=0.3} what's our plan now?"
     G "Obviously we're stuck in a Minecraft world,{w=0.3} but we can't stay here {i}forever.{/i}"
     show dream annoyed at left
     show sapnap annoyed at right
     with dissolve
     "Flustered,{w=0.3} Dream and Sapnap had fixed themselves and focused on the situation at hand."
     show sapnap wary at right
     with dissolve
     S "How do you think we can get out of this?{w=0.3} Any ideas?"
     "It seemed that they have discussed this before you had arrived,{w=0.3} confirming that everyone was from the real world and was not a bot built into the game's code."
     "Seeing you fall from,{w=0.3} apparently,{w=0.3} 140 blocks high also served as enough evidence that you,{w=0.3} too,{w=0.3} were real to them."
     "A moment of silence had passed for a while as all four of you try to think of a solution."
     show dream shock at left
     with dissolve
     D "...{color=#55FF55}Free the end{/color}?"
     "Everyone turned to Dream."
     show george wary at center, bounce
     G "The {i}what?{/i}"
     show dream serious at left
     with dissolve
     D "The End.{w=0.3} We find the Stronghold,{w=0.3} beat the Ender Dragon,{w=0.3} and {color=#55FF55}free the end{/color}.{w=0.3} Just like how we usually do our challenges."
     D "I'm not sure if this will help us get back,{w=0.3} but it's worth a try.{w=0.3} Right?"
     show sapnap serious at right
     with dissolve
     S "But then this is {i}us{/i},{w=0.3} Dream."
     S "We're not our characters anymore,{w=0.3} we're {i}actual{/i} people stuck in their places."
     S "We can't just die and respawn.{w=0.3} 0 hearts and we disappear."
     D "How are you so sure about that?"
     D "We don't know if that's true."
     "Sapnap,{w=0.3} out of the blue,{w=0.3} proceeded to punch George."
     play sound "audio/fall.mp3" volume 0.3
     show george pained 1 at shake
     with dissolve
     show george pained 2
     with dissolve
     "A glimpse of George's health had appeared on top of his head for a split second with his last heart split in half."
     show dream wary at left
     with dissolve
     "Dream's face faltered at this."
     show george angry with dissolve
     G "Of all people,{w=0.3} Sapnap,{w=0.3} you really had to choose-"
     S "So,{w=0.3} if we're going to finish this game, we {i}all{/i} have to be careful."
     "You nodded along,{w=0.3} gazing up to see that you had half of your entire health bar down due to your fall earlier."
     show dream sigh at left
     with dissolve
     D "Alright,{w=0.3} then let's split up since it's almost nighttime."
     show dream neutral at left
     with dissolve
     D "I'll go mine for ores."
     D "George,{w=0.3} you go get us as many wood as you can."
     D "Sapnap,{w=0.3} find us a proper place to reside in for now."
     hide dream neutral with dissolve
     hide sapnap serious with dissolve
     hide george angry with dissolve
     "As three of them went their separate ways,{w=0.3} you were left on your own.{w=0.3} You wanted to help out,{w=0.3} too,{w=0.3} so you decided to..."
     $ renpy.music.stop(fadeout=2.0)
     menu:
         "Get Wood":
             $ george_points += 2
             $ george_romantic += 5
             $ george_platonic += 5
             $ george_bad += 5
             jump george1

         "Wander Around":
             $ sapnap_points += 2
             $ sapnap_romantic += 5
             $ sapnap_platonic += 5
             $ sapnap_bad += 5
             jump sapnap1

         "Mine Down" if persistent.trueroute == True:
             $ dream_points += 2
             $ dream_romantic += 5
             $ dream_platonic += 5
             $ dream_bad += 5
             jump dream1


     label george1:
         $ renpy.fix_rollback()
         play music "audio/Twin Musicom - Rhodesia MkII.mp3" fadein 5.0 volume 0.5
         scene forest1
         with dissolve
         "You decided to walk towards the path George had taken,{w=0.3} one leading deeper into the forest biome."
         show george shock
         with dissolve
         G "[povname]!"
         show george neutral with dissolve
         G "So you decided to catch up with me."
         "You nodded as you went to the opposite side of the tree he was getting materials from,{w=0.3} starting to break it down."
         show george grin 2 with dissolve
         G "I'm so glad you went with me.{w=0.3} This way,{w=0.3} we could get more supplies a lot faster."
         hide george grin 2 with dissolve
         "You smiled at him as you went to another tree to gather more materials."
         "After a bit of silence passed between you two,{w=0.3} George spoke up once more."
         show george neutral with dissolve
         G "So,{w=0.3} you play Minecraft.{w=0.3} I'm pretty sure you know of us."
         G "Is there anything you like to do in particular that got you into it?"
         hide george neutral with dissolve
         menu:
             "I'm quite interested in coding, actually.":
                 jump georgeromantic1
             "I just happened to like the game.":
                 jump georgeplatonic1
             "Let's just focus on getting more wood.":
                 jump georgebad1
         label georgeromantic1:
             $ renpy.fix_rollback()
             "You haven't exactly had any experience in doing it,{w=0.3} per say,{w=0.3} but you {i}would{/i} like to tackle it some day."
             "And Minecraft seemed like a good start for you.{w=0.3} A blank slate for different mods you can create."
             scene georgecg1 with dissolve:
                 xpos 0.9 ypos 1.5 xanchor 0.66 yanchor 0.93 zoom 2.0
                 linear 15 yanchor 0.59
             pause(1.0)
             scene georgecg1
             $ mouse_parallax.set ((-20, -5, "l0"))
             $ showp ("georgecg1")
             with dissolve
             G "Coding,{w=0.3} huh?{w=0.3} Cool!"
             G "Maybe once we're out of here,{w=0.3} I can try teaching you the basics.{w=0.3} I know quite a lot about it."
             $ scenep ()
             with dissolve
             "Hearing him sound so excited,{w=0.3} it makes you look forward to getting out of here together even more.{w=0.3} You bit your lip in an attempt to fight the flush that had tried to rise to your cheeks."
             $ george_romantic += 10
             jump george1b
         label georgeplatonic1:
             $ renpy.fix_rollback()
             "Your friends have simply showed you the game,{w=0.3} and you found yourself interested in the various minigames you could play with them."
             "The summer wouldn't be as exciting if it meant not hanging out with them for the most of it."
             show george grin 2 with dissolve
             G "Yeah,{w=0.3} especially when you have friends to mess around with,{w=0.3} too."
             show george neutral with dissolve
             G "Without those two,{w=0.3} I wouldn’t know where I'd be."
             "You can hear the fondness in his voice and looked at him from where you stood.{w=0.3} He looked back at you with an easy smile on his face."
             $ george_platonic += 10
             jump george1b
         label georgebad1:
             $ renpy.fix_rollback()
             "You'd rather focus on the task at hand rather than to participate in small talk."
             "Besides,{w=0.3} it'd mean that you could get back to the real world quicker the faster everyone reunites after this."
             show george wary with dissolve
             G "..."
             show george serious with dissolve
             play sound "audio/george hum.mp3"
             G "Not much of a talker,{w=0.3} hmm?"
             hide george serious with dissolve
             "You paid him no mind as you continue to obtain more wood."
             $ george_bad += 10
             jump george1b

             label george1b:
                scene forest1
                with dissolve
                "Once you feel like the amount of materials you've gotten was enough,{w=0.3} you peer back and see George waiting for you to finish up."
                show george grin 1 with dissolve
                G "Let's head back,{w=0.3} yeah?"
                "You nodded as you both make your way back when Sapnap had called out."
                show george shock at center, bounce
                with dissolve
                S "Guys!{w=0.3} I found a Ruined Portal!"
                "The both of your heads snapped towards the direction of where Sapnap's voice resonated and bounded over to his area."
                play sound "audio/walking.mp3"
                scene black
                with wipeleft
                scene ruinedportal1
                with wipeleft
                jump c


     label sapnap1:
         $ renpy.fix_rollback()
         play music "audio/Twin Musicom - Rhodesia MkII.mp3" fadein 5.0 volume 0.5
         scene forest2
         with dissolve
         "You decided to walk a bit towards the side you had last seen Sapnap.{w=0.3} Not too long after,{w=0.3} you spot the familiar flare of his bandana as he turned around to the sound of your footsteps approaching him."
         show sapnap grin 1 with dissolve
         S "Oh!{w=0.3} So you decided to venture out with me?"
         "You rolled your eyes playfully as you ran up to his side.{w=0.3} Finding a suitable place to stay wouldn't be that hard,{w=0.3} right?"
         show sapnap grin 2 with dissolve
         "Sapnap continued to ramble about various topics as you did most of the observation."
         "From the corner of your eye,{w=0.3} You spotted a village.{w=0.3} You exclaimed to catch the brunet's attention as you pointed at the spot."
         show sapnap shock with dissolve
         S "Nice one,{w=0.3} [povname]!"
         show sapnap grin 1 with dissolve
         S "I was so busy babbling about that I didn't even get to notice."
         hide sapnap grin 1 with dissolve
         play sound "audio/dig.mp3"
         "He then mined off a block of dirt."
         show sapnap neutral at center, bounce
         with dissolve
         S "So that we can return here later on!"
         show sapnap grin 2 with dissolve
         S "Let’s continue walking around and see if we can find something even more interesting."
         hide sapnap grin 2 with dissolve
         "You nodded and continued down the path the both of you were taking."
         scene plains
         with dissolve
         "As you made your way around,{w=0.3} Sapnap spoke up."
         show sapnap neutral with dissolve
         S "So,{w=0.3} what do you think?"
         "You glanced at him,{w=0.3} confused.{w=0.3} Sapnap just laughed as he placed his arms behind his head."
         play sound "audio/sapnap chuckle.mp3"
         show sapnap grin 2 with dissolve
         S "I'm guessing you didn't hear me.{w=0.3} Don't worry!{w=0.3} I swear,{w=0.3} I'm kind enough to repeat myself."
         show sapnap neutral with dissolve
         S "I was wondering,{w=0.3} what would be the first thing you'd like to do the moment you get out of here?"
         hide sapnap neutral with dissolve
         menu:
             "Take a break from the computer, have a hangout in real life.":
                 jump sapnapplatonic1
             "I'd rather stay here.":
                 jump sapnapbad1
             "Go for a walk on the beach, take some time to wind-down.":
                 jump sapnapromantic1


         label sapnapromantic1:
             $ renpy.fix_rollback()
             "You realized you've been in front of the computer so much lately that you haven't appreciated the outside world as much as you should've."
             "Maybe being aware that you might get stuck here helped remind you of that."
             scene sapnapcg1 with dissolve:
                 xpos 0.8 ypos 1.5 xanchor 0.66 yanchor 0.93 zoom 2.0
                 linear 15 yanchor 0.59
             pause(1.0)
             scene sapnapcg1
             $ mouse_parallax.set ((-20, -5, "l0"))
             $ showp ("sapnapcg1")
             with dissolve
             S "Huh,{w=0.3} I guess I've gotten used to people telling me they'd rather stay online all the time."
             S "Maybe,{w=0.3} once we get out,{w=0.3} you’d like some company on your walk?"
             $ scenep ()
             with dissolve
             "You let out a teasing hum,{w=0.3} not particularly taking up his offer but not flat-out rejecting it either.{w=0.3} You let out a tiny giggle when you see the tiniest pout form on the brunet's face."
             "The pout quickly forms into a smile,{w=0.3} though."
             "He gently grabs ahold of your hand as he led the both of you down the path."
             $ sapnap_romantic += 10
             jump sapnap1b
         label sapnapplatonic1:
             $ renpy.fix_rollback()
             "All you've been doing all summer break was to play Minecraft and watch them do dumb challenges."
             "Maybe it was time to just calm down,{w=0.3} call a few friends over.{w=0.3} Relish in some fun physical activities that you used to do."
             show sapnap neutral with dissolve
             S "I like the sound of that.{w=0.3} Keeping your friends close,{w=0.3} shoving them when they do a really funny joke…"
             show sapnap grin 2 with dissolve
             S "Yeah,{w=0.3} I think I’d like to do that too."
             "He gives you a grin as you both continued on the path you followed."
             $ sapnap_platonic += 10
             jump sapnap1b
         label sapnapbad1:
             $ renpy.fix_rollback()
             "Nothing was exciting in the real world,{w=0.3} anyway.{w=0.3} You were even able to meet your favorite people because of this world,{w=0.3} too."
             "Why bother leaving?"
             show sapnap annoyed with dissolve
             S "Hmm."
             "Your response clearly intrigued him."
             show sapnap grin 1 with dissolve
             S "Well,{w=0.3} I've always wanted to see the impact of a Creeper explosion up close!{w=0.3} Maybe burn a different village,{w=0.3} too."
             "He wickedly grins at you as he takes your hand,{w=0.3} leading you down the path even quicker as walking turned into jogging."
             $ sapnap_bad += 10
             jump sapnap1b

             label sapnap1b:
                 scene ruinedportal1
                 with dissolve
                 "As you reached the end,{w=0.3} the biome turning from a grassy field to one of a jungle,{w=0.3} the both of you had spotted a ruined Nether portal."
                 "Your eyebrows raise in surprise as Sapnap turned around,{w=0.3} his hands cupped around his mouth as he called out."
                 show sapnap angry at center, bounce
                 with dissolve
                 S "Guys!{w=0.3} We found a Ruined Portal!"
                 hide sapnap angry with dissolve
                 "As his voice echoed through out the dark oak forest,{w=0.3} the two other members had made their way towards the both of you to regroup."
                 jump c

     label dream1:
         $ renpy.fix_rollback()
         play music "audio/Twin Musicom - With a Stamp.mp3" fadein 5.0 volume 0.5
         scene cave
         with dissolve
         "You didn't feel like following any of the two who were on surface level,{w=0.3} so you decided to walk over to the small cave that Dream had created."
         "You began climbing down silently until you accidentally kicked a pebble down the pathway,{w=0.3} the sound bouncing off from the walls catching the attention of the blonde."
         show dream shock at center, bounce
         with dissolve
         "He turned around quickly,{w=0.3} in a defensive stance,{w=0.3} before realizing that it was you.{w=0.3} He heaved a relieved sigh."
         show dream sigh at center, bounce
         D "It was just you,{w=0.3} [povname].{w=0.3} You scared me."
         show dream neutral with dissolve
         D "You sure you don’t want to stay up there?{w=0.3} I don’t have a torch with me,{w=0.3} so it's gonna be kinda dark."
         "You shook your head no,{w=0.3} to which he shrugged at."
         hide dream neutral with dissolve
         scene cave2
         with dissolve
         "He continued to mine for more iron ore as you mined the occasional coal ore that would pop up on the way.{w=0.3} Sometimes,{w=0.3} even a block of gold ore would pop up and the both of you would gasp in glee!"
         "As the both of you continued your way down the cave,{w=0.3} Dream suddenly halted his actions.{w=0.3} You peered up at him,{w=0.3} confused."
         show dream wary with dissolve
         D "Don't you feel.{w=0.3}.{w=0.3}.{w=0.3} scared about this?{w=0.3} How we're just suddenly stuck in this realm?"
         D "I know I don't usually show the other two,{w=0.3} but I've been pretty freaked out this entire time."
         hide dream wary with dissolve
         menu:
             "{color=#e60000}I'm sure everyone feels the same way.{/color}" if bad_choices == True:
                 jump dreambad1
             "You're... scared?":
                 jump dreamromantic1
             "I'm pretty freaked out, too.":
                 jump dreamplatonic1
         label dreamromantic1:
             $ renpy.fix_rollback()
             play sound "audio/dream giggle.mp3"
             "Dream chuckled at your response."
             show dream grin 2 with dissolve
             D "It's funny,{w=0.3} right?{w=0.3} Scared of the one game I've come to love for all these years."
             D "I know the mechanics like the back of my hand,{w=0.3} but here I am hesitating like an idiot."
             scene dreamcg1 with dissolve:
                 xpos 0.8 ypos 1.5 xanchor 0.66 yanchor 0.93 zoom 2.0
                 linear 15 yanchor 0.59
             pause(1.0)
             scene dreamcg1
             $ mouse_parallax.set ((-20, -5, "l0"))
             $ showp ("dreamcg1")
             with dissolve
             D  "You don't think I'm like.{w=0.3}.{w=0.3}.{w=0.3} weak,{w=0.3} or anything?"
             "You responded with an expression on your face that seemed as if you were offended."
             play sound "audio/dream giggle.mp3"
             "Dream laughed it off,{w=0.3} waving his hand in dismissal."
             D "I appreciate your worry for me,{w=0.3} [povname].{w=0.3} Thank you."
             $ scenep ()
             with dissolve
             $ dream_romantic += 10
             jump dream1b
         label dreamplatonic1:
             $ renpy.fix_rollback()
             "Dream's eyebrows raise."
             show dream shock with dissolve
             D "You too?"
             "You nodded,{w=0.3} and he tries to give you the most comforting smile he could muster."
             show dream neutral with dissolve
             D "Well,{w=0.3} that makes the both of us.{w=0.3} But,{w=0.3} I can reassure you that we'll all get out of here together."
             "Upon hearing that,{w=0.3} you smiled back up at him as you began to feel a lot more relieved than before."
             $ dream_platonic += 10
             jump dream1b
         label dreambad1:
             $ renpy.fix_rollback()
             "Dream's gaze was stuck to one block.{w=0.3} He seemed far away even though physically he was just right in front of you."
             show dream disappointed with dissolve
             D "Yeah,{w=0.3} you're probably right."
             hide dream disappointed with dissolve
             "Although confused,{w=0.3} you felt as if there were walls that stood in your way that effectively blocked you off from the blonde."
             $ dream_bad += 100
             jump dream1b

             label dream1b:
                 scene cave2
                 with dissolve
                 "You motioned your hand in front of you for him to continue your cooperated mining a little bit longer before finally settling on the amount of materials obtained."
                 show dream neutral with dissolve
                 D "This is enough.{w=0.3} Let's head back up and reunite with the other two."
                 "You nodded,{w=0.3} following his stride as he led the both of you out of the man-made tunnel."
                 scene cave
                 with dissolve
                 "As the both of you reached the surface,{w=0.3} you heard Sapnap's voice echo throughout the nearby forest."
                 show dream shock at center, bounce
                 with dissolve
                 S "Guys!{w=0.3} I found a Ruined Portal!"
                 play sound "audio/walking.mp3"
                 scene black
                 with wipeleft
                 scene ruinedportal1
                 with wipeleft
                 jump c

     label c:
         stop music fadeout 1.0
         pause(1.0)
         play music "audio/Twin Musicom - Life in Romance.mp3" fadein 5.0 volume 0.5
         scene ruinedportal1
         show dream grin 1 at center, bounce
         with dissolve
         D "Nice find!"
         hide dream grin 1 with dissolve
         "As everyone reunited,{w=0.3} they had huddled around the Ruined Portal."
         show dream neutral at left
         with dissolve
         show george neutral at right
         with dissolve
         "Dream and George had exchanged the materials they have obtained,{w=0.3} successfully creating a crafting table."
         "Dream creates enough stone axes and pickaxes for everyone to be able to defend themselves when needed."
         hide george neutral with dissolve
         "George then stashes the crafting table in his inventory."
         show dream serious at left
         with dissolve
         D "Now,{w=0.3} let's see what the chest has in store for us."
         show sapnap serious at right
         with dissolve
         "He motions for Sapnap to take the lead."
         "The brunet bounds over to the chest buried in between the netherrack,{w=0.3} opening the lock up and revealing the items locked in."
         hide dream serious
         hide sapnap serious
         with dissolve
         show chest with dissolve
         D "So?"
         D "What do we got?"
         S "Um,{w=0.3} a Gapple."
         S "There's also a flint and steel,{w=0.3} a few golden ingots,{w=0.3} an enchanted golden helmet,{w=0.3} and some Obsidian blocks."
         hide chest with dissolve
         show sapnap neutral at right
         with dissolve
         "Sapnap then quickly sweeps a hand into the chest before anyone could speak up."
         show sapnap grin 2 at right, shake
         with dissolve
         S "I call dibs on the flint and steel!"
         show george annoyed at left
         with dissolve
         "George rolls his eyes before approaching the chest."
         show george neutral at left, bounce
         G "Then,{w=0.3} I'll grab the helmet."
         hide sapnap grin 2
         hide george neutral
         with dissolve
         show dream serious with dissolve
         "Dream was the last to approach the chest,{w=0.3} bringing out the two remaining items."
         "He holds them both in his hands,{w=0.3} as if to 'weigh' his choices."
         show dream neutral at center, bounce
         D "Here,{w=0.3} [povname]."
         "He tosses the Golden Apple to you."
         "You glanced at it for a second before looking back up towards the blonde.{w=0.3} He simply smiled back at you."
         show dream grin 2 with dissolve
         D "You'll need it more than I do."
         show dream neutral with dissolve
         D "Besides,{w=0.3} these'll be handy later on."
         hide dream neutral with dissolve
         scene ruinedportal2
         with dissolve
         stop music fadeout 1.0
         "You were about to speak up when the sound of groaning was heard all around you."
         play music "audio/Twin Musicom - The Coal Mine.mp3" fadein 5.0 volume 0.5
         "The three of you had lost track of time as night came upon all of you.{w=0.3} Numerous mobs have begun to spawn."
         show george wary at center, bounce
         with dissolve
         G "Guys?!"
         hide george wary with dissolve
         show sapnap angry at center, bounce
         with dissolve
         S "There's a Village down here!"
         S "Find a one-block hole,{w=0.3} that's my marker!"
         hide sapnap angry with dissolve
         "Upon hearing this,{w=0.3} Dream had already sprinted ahead;{w=0.3} leaving everyone else to follow his lead."
         "As you all ran,{w=0.3} you heard a yelp from someone behind you."
         show george wary at bounce
         with dissolve
         G "AH!"
         show sapnap angry at right, bounce
         with dissolve
         stop music fadeout 1.0
         S "GEORGE!"
         hide george wary
         hide sapnap angry
         with dissolve

         label dummychoice1:
             play music "audio/Twin Musicom - Savoy Theatre.mp3" fadein 5.0 volume 0.5
             show ruinedportal2
             with dissolve
             play sound "audio/zombie gurgle.mp3"
             "George was wrestling with a zombie.{w=0.3} Sapnap also turned his head around and immediately wielded his axe."
             play sound "audio/creeper hiss.mp3"
             "As you looked behind the younger brunet,{w=0.3} you spotted a Creeper approaching his way."

             label menu1:
                 $ time = 5
                 $ timer_range = 5
                 $ timer_jump = 'dummyending1'
                 show screen countdown
                 menu:
                     "Defend George":
                         hide screen countdown
                         $ george_points += 1
                         $ george_romantic += 3
                         $ george_platonic += 3
                         $ george_bad += 3
                         jump george2

                     "Defend Sapnap":
                         hide screen countdown
                         $ sapnap_points += 1
                         $ sapnap_romantic += 3
                         $ sapnap_platonic += 3
                         $ sapnap_bad += 3
                         jump sapnap2


         label george2:
             $ renpy.fix_rollback()
             "You were much closer to George,{w=0.3} so you sprinted towards him whilst Sapnap turned around to the hissing of the mob behind him."
             "You wielded your axe up and high before striking down a crit onto the Zombie that had grabbed ahold of George."
             play sound "audio/zombie death.mp3"
             pause(1.0)
             play sound "audio/exp.mp3"
             "Doing it three more times,{w=0.3} the mob then disappeared into smoke and a few orbs of EXP."
             "George, seemingly out of breath,{w=0.3} appreciates your help."
             show george sigh with dissolve
             G "Thanks,{w=0.3} [povname]."
             hide george sigh with dissolve
             jump d



         label sapnap2:
             $ renpy.fix_rollback()
             "You called out for Sapnap to take a big stride to the side as you struck the Creeper behind him.{w=0.3} You nodded at him to continue his way to George."
             play sound "audio/creeper hit.mp3"
             pause(1.0)
             play sound "audio/exp.mp3"
             "As the Creeper began to flash white,{w=0.3} you hit the mob one more time.{w=0.3} It recedes into dust as a few orbs of EXP had taken its place."
             "When you turn around,{w=0.3} you see Sapnap pushing George off in front of him in an attempt to get him to move."
             "He passes by you as you turn back to run with them towards the Village."
             show sapnap neutral with dissolve
             S "Thanks for having my back,{w=0.3} [povname]!"
             hide sapnap neutral with dissolve
             jump d


         label dummyending1:
             "You couldn't seem to decide,{w=0.3} and before you knew it,{w=0.3} the Creeper had blown up the entire area the three of you had been in."
             play sound "audio/creeper boom.mp3"
             scene white
             pause(2.0)
             stop music fadeout 1.0
             pause(2.0)
             scene gameover
             with fade
             play music "audio/bensound-betterdays.mp3" volume 0.3
             pause(2.0)
             show XD neutral at center, bounce
             with dissolve
             XD "It seems that you've ran out of time!"
             show XD grin at center, bounce
             XD "Bummer.{w=0.3} Would you like to try again?"
             hide XD grin with dissolve
             menu:
                 "Retry":
                     stop music fadeout 1.0
                     scene white
                     with dissolve
                     pause(1.0)
                     jump dummychoice1
                 "Return to Main Menu":
                     show XD grin at center, bounce
                     with dissolve
                     XD "That sucks,{w=0.3} but understandable!"
                     XD "We'll see you soon!"
                     return


         label d:
             scene village1
             with wipeleftfast
             "Dream turns around."
             show dream serious at center, bounce
             with dissolve
             D "Are you guys okay?!"
             hide dream serious with dissolve
             "All three of you nodded in response."
             show dream angry at center, bounce
             with dissolve
             D "Alright,{w=0.3} then come on!{w=0.3} We're almost there!"
             hide dream angry with dissolve
             play sound "audio/walking.mp3"
             scene black
             with wipeleftfast
             scene village3
             with wipeleftfast
             "You all hobbled over to the nearby Village."
             show dream serious with dissolve
             "Dream had shoved a random door open and ushered all of you inside,{w=0.3} breaking any lever or button nearby the entrance to ensure that no other mob could get in."
             "He really didn't have to,{w=0.3} but it was better safe than sorry."
             stop music fadeout 1.0
             scene village4
             with fastdissolve
             pause(1.0)
             show dream sigh at center, bounce
             with dissolve
             play music "audio/Twin Musicom - Mikhail Tal.mp3" fadein 5.0 volume 0.5
             "Dream then sighed as everyone attempted to catch their breath."
             show dream wary with dissolve
             D "Anyone hurt badly,{w=0.3} or anything?"
             hide dream wary with dissolve
             show george serious at left, bounce
             show sapnap serious at right, bounce
             with dissolve
             "You,{w=0.3} George,{w=0.3} and Sapnap glanced at each other for a minute before shaking your heads altogether."
             hide george serious
             hide sapnap serious
             with dissolve
             show dream neutral with dissolve
             "Dream sighs in relief before glancing at the Iron Golem doing its job to protect its Village through the window."
             hide dream neutral with dissolve
             show george shock with dissolve
             G "Well,{w=0.3} it seems like we're in a library."
             show george neutral at center, bounce
             with dissolve
             G "Might as well make the most of our time here and rest up until daylight comes back."
             show dream neutral at left, bounce
             show sapnap neutral at right, bounce
             with dissolve
             "Dream and Sapnap nodded at this."
             hide george neutral
             hide dream neutral
             hide sapnap neutral
             with dissolve
             "Dream continued to stay nearby the door, keeping watch of the mobs outside.{w=0.3} Sapnap had decided to sit by the staircase to the upper floor of the Library.{w=0.3} George had already gone up to check out the many books on the shelves."
             "You took this as a time to breathe and venture around."
             menu:
              "I wanna learn more about the End." if persistent.trueroute == True:
                 $ dream_points += 2
                 $ dream_romantic += 8
                 $ dream_platonic += 8
                 $ dream_bad += 8
                 jump dream2
              "I wanna know more about books.":
                  $ george_points += 2
                  $ george_romantic += 5
                  $ george_platonic += 5
                  $ george_bad += 5
                  jump george3

              "I wanna talk more about biomes.":
                  $ sapnap_points += 2
                  $ sapnap_romantic += 5
                  $ sapnap_platonic += 5
                  $ sapnap_bad += 5
                  jump sapnap3




             label george3:
                 $ renpy.fix_rollback()
                 scene libraryshelf
                 with dissolve
                 "You decided to head upstairs.{w=0.3} You wanted to see what the Library had in store for you."
                 "Hearing your footsteps approaching,{w=0.3} George sees you standing at the top of the stairs."
                 show george neutral with dissolve
                 G "[povname]."
                 "He smiles at you as he puts a book back in the shelf.{w=0.3} You questioned him as to why he did that,{w=0.3} as he seemed quite interested in it."
                 show george grin 2 at center, bounce
                 G "Oh- it's,{w=0.3} um.{w=0.3} It was nothing,{w=0.3} really."
                 "You don't buy it one bit,{w=0.3} but you let it slide."
                 hide george grin 2 with dissolve
                 "You stood next to him as you peered at the multiple books with Enchantment Table language engraved on their spines.{w=0.3} Your fingers brush against the leather before George clears his throat."
                 show george grin 1 with dissolve
                 G "So,{w=0.3} books.{w=0.3} You like books too?"
                 hide george grin 1 with dissolve
                 menu:
                     "Not really. They bore me.":
                         jump georgebad2
                     "I enjoy reading a lot.":
                         jump georgeromantic2
                     "It takes my mind off of some things.":
                         jump georgeplatonic2

                 label georgeromantic2:
                     $ renpy.fix_rollback()
                     "You like the way books open up a different world for you to discover and conform to."
                     "You smile at (probably) the countless books you've decided were your favorite ones,{w=0.3} whether they were just a standalone or a long series."
                     scene georgecg2 with dissolve:
                         xpos 0.9 ypos 1.6 xanchor 0.66 yanchor 0.93 zoom 2.0
                         linear 15 yanchor 0.59
                     pause(1.0)
                     scene georgecg2
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("georgecg2")
                     with dissolve
                     "George smiles."
                     G "You think that too,{w=0.3} huh?"
                     G "It's just kinda like here,{w=0.3} too.{w=0.3} Opening portals,{w=0.3} finding different parts of its universe,{w=0.3} understanding its lore..."
                     "He then catches himself from rambling further,{w=0.3} his face tinging pink."
                     G "Sorry,{w=0.3} I think I've said too much."
                     $ scenep ()
                     with dissolve
                     "You reassure him that he hadn't.{w=0.3} You tell him that you enjoy hearing him talk about the things he's interested in."
                     "He looks a bit shocked at your response before settling on a smile."
                     G "You're great company,{w=0.3} [povname]."
                     $ george_romantic += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

                 label georgeplatonic2:
                     $ renpy.fix_rollback()
                     "Some things take too much of a toll in the real world,{w=0.3} so you turn to the compiled pages and immerse yourself into it."
                     "George nods along."
                     show george neutral with dissolve
                     G "Things {i}can{/i} get out of hand,{w=0.3} don't they?"
                     show george grin 2 at center, bounce
                     G "If you'd like,{w=0.3} I'd give you recommendations once we're out of here."
                     show george grin 1 with dissolve
                     G "Dream and Sapnap aren't exactly into the genres I like,{w=0.3} so maybe you'd like them."
                     "You smiled at him,{w=0.3} and he smiled back."
                     hide george grin 1 with dissolve
                     $ george_platonic += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

                 label georgebad2:
                     $ renpy.fix_rollback()
                     "You just can't seem to get into what people like about novels.{w=0.3} They're just pieces of papers with some made-up story stringed along into it."
                     "George seemed to frown at this, {w=0.3} but when you took a proper look at him,{w=0.3} traces of the negative expression had faded in mere seconds."
                     show george sigh with dissolve
                     G "Yeah, I think they're stupid too..."
                     "He sounded as if he were biting something back.{w=0.3} You wanted to pry,{w=0.3} but decided against it."
                     hide george sigh with dissolve
                     $ george_bad += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

             label sapnap3:
                 $ renpy.fix_rollback()
                 "The recent events had tired you out.{w=0.3} Your legs feeling wobbly,{w=0.3} you decided to take a seat next to Sapnap."
                 "He glances at you."
                 show sapnap grin 2 at center, bounce
                 with dissolve
                 S "Tiring day,{w=0.3} huh?"
                 "You nodded as you bunched your arms on your knees and rested your head on top of them."
                 hide sapnap grin 2 with dissolve
                 "Sapnap leans against the side of the staircase, {w=0.3}heaving out a sigh.{w=0.3} You looked at him and it seemed as if gears were turning in his mind."
                 pause(1.0)
                 show sapnap wary with dissolve
                 S "So.{w=0.3}.{w=0.3}.{w=0.3} Biomes?"
                 "Your eyebrows furrow at him in confusion as he attempted to bring up a random topic to talk about.{w=0.3} He flails his hands around."
                 show sapnap annoyed at center, bounce
                 S "No,{w=0.3} see,{w=0.3} what I meant was-"
                 show sapnap neutral at center, bounce
                 S "Was there any place you labeled as your 'go-to' here?{w=0.3} Any favorite biome?"
                 hide sapnap neutral with dissolve
                 menu:
                     "Nether.":
                         jump sapnapplatonic2
                     "Plains or Desert biomes.":
                         jump sapnapromantic2
                     "The End.":
                         jump sapnapbad2

                 label sapnapromantic2:
                     $ renpy.fix_rollback()
                     "You liked the calmer and surface-level biomes.{w=0.3} Although it'd be covered with mobs in the night,{w=0.3} you're still able to adapt and find new ways to advance until dawn."
                     "This piques Sapnap's interest."
                     scene sapnapcg2 with dissolve:
                         xpos 0.9 ypos 1.6 xanchor 0.66 yanchor 0.93 zoom 2.0
                         linear 15 yanchor 0.59
                     pause(1.0)
                     scene sapnapcg2
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("sapnapcg2")
                     with dissolve
                     S "Huh."
                     S "Well,{w=0.3} you know what they say.{w=0.3} \"Opposites Attract.\""
                     "He teasingly says this,{w=0.3} and you let out an unamused huff in return.{w=0.3} He laughs at this."
                     $ scenep ()
                     with dissolve
                     S "I'm kidding,{w=0.3} I'm kidding.{w=0.3} You're cool,{w=0.3} [povname]."
                     S "Normally I'd like to go to riskier areas,{w=0.3} but yeah,{w=0.3} I like to relax from time to time too."
                     S "I should try learning a thing or two from you."
                     "You simply smiled at him.{w=0.3} You knew he'd like something more of a challenge,{w=0.3} but hearing him appreciate what you preferred was nice."
                     $ sapnap_romantic += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

                 label sapnapplatonic2:
                     $ renpy.fix_rollback()
                     "Seeing the bright,{w=0.3} orange biome makes you a bit nervy,{w=0.3} but it also makes you bristle with excitement."
                     "With mobs contrasting from the Overworld,{w=0.3} you'd appreicate a slightly challenging setting."
                     pause(1.0)
                     show sapnap grin 1 with dissolve
                     "Sapnap seems to beam at this."
                     show sapnap grin 2 at center, bounce
                     S "The Nether is {i}so{/i} cool!{w=0.3} I totally agree!"
                     show sapnap grin 1 at center, bounce
                     S "It isn't {i}that{/i} hard,{w=0.3} but it isn't that easy either.{w=0.3} A perfect balance."
                     "You agree,{w=0.3} it gives you the thrill that's {i}just{/i} right."
                     play sound "audio/sapnap chuckle.mp3"
                     "Sapnap gives you a chuckle."
                     show sapnap neutral at center, bounce
                     S "Once we're out,{w=0.3} let's have a race.{w=0.3} First to find a fortress wins."
                     "Not being one who'd back down from a challenge,{w=0.3} you accepted the offer."
                     $ sapnap_platonic += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

                 label sapnapbad2:
                     $ renpy.fix_rollback()
                     "You didn't really fancy much of the other biomes.{w=0.3} You thought them as bland and would rather finish the game head on."
                     show sapnap shock with dissolve
                     "Sapnap gapes at you in surprise."
                     show sapnap wary at center, bounce
                     S "Oh!"
                     "Sapnap seems to take your response in consideration."
                     pause(1.0)
                     show sapnap grin 2 at center, bounce
                     S "I like the end,{w=0.3} too!"
                     hide sapnap grin 2 with dissolve
                     "He doesn't say anything else other than that,{w=0.3} but you can feel that the atmosphere between the two of you had shifted."
                     $ sapnap_bad += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

             label dream2:
                 $ renpy.fix_rollback()
                 scene librarynight
                 with dissolve
                 "You approach Dream,{w=0.3} who was situated nearby the door."
                 show dream neutral with dissolve
                 "He glances at you and nods,{w=0.3} taking note of your presence with a smile."
                 D "[povname]."
                 "You nod back with the same expression,{w=0.3} seated on the opposite side from him whilst glancing out of the window."
                 hide dream neutral with dissolve
                 "You both watched the Iron Golem protect its Village,{w=0.3} flinging the many spider and skeleton mobs up into the air and causing damage to them."
                 "You decided to ask a question."
                 pause(1.0)
                 show dream shock at center, bounce
                 with dissolve
                 D "The end?"
                 show dream annoyed at center, bounce
                 D "Well.{w=0.3}.{w=0.3}.{w=0.3}"
                 hide dream wary with dissolve
                 "Dream looked a bit off into the distance."
                 show dream serious at center, bounce
                 with dissolve
                 D "Well,{w=0.3} it would make sense,{w=0.3} right?{w=0.3} It's how you'd normally beat the game."
                 D "Getting iron,{w=0.3} walking around the Nether,{w=0.3} finding a Fortress,{w=0.3} obtain Ender Eyes,{w=0.3} locate the Stronghold,{w=0.3} defeat the Ender Dragon..."
                 hide dream serious with dissolve
                 "He trails off before meeting your gaze.{w=0.3} It seems clouded,{w=0.3} but you can't decipher what it was."
                 show dream wary with dissolve
                 D "If you were in my place,{w=0.3} [povname],{w=0.3} what would you do?"
                 "You pondered.{w=0.3} He was a guy who had a lot of people have high expectations on him."
                 hide dream wary with dissolve
                 menu:
                     "Ask others for advice.":
                         jump dreamplatonic2
                     "{color=#e60000}Rethink {i}everything.{/i}{/color}" if bad_choices == True:
                         jump dreambad2
                     "Believe in myself.":
                         jump dreamromantic2

                 label dreamromantic2:
                     $ renpy.fix_rollback()
                     "Dream blinks at you for a second before gazing outside the window with a smile.{w=0.3} He lets out a low chuckle."
                     play sound "audio/dream giggle.mp3"
                     show dream grin 1 with dissolve
                     D "You're right.{w=0.3} I can do this-{w=0.3} {i}We{/i} can do this."
                     D "The Dream Team has been doing these kinds of things {i}all{/i} the time."
                     scene dreamcg2 with dissolve:
                         xpos 0.9 ypos 1.4 xanchor 0.66 yanchor 0.93 zoom 2.0
                         linear 15 yanchor 0.59
                     pause(1.0)
                     scene dreamcg2
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("dreamcg2")
                     with dissolve
                     D "We'll be okay,{w=0.3} right?"
                     "You nodded.{w=0.3} If all he needed was reassurance,{w=0.3} you'd be willing to give it.{w=0.3} The last thing you'd want to see is him beating himself up over the tiniest thing that had gone wrong."
                     "Like baby steps,{w=0.3} all of you would be able to weave your way through all of this."
                     $ scenep ()
                     with dissolve
                     "As you thought of this,{w=0.3} you've come to notice the purple glint in one of his eyes as they were hit by a ray of sunlight."
                     $ dream_romantic += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

                 label dreamplatonic2:
                     $ renpy.fix_rollback()
                     "Dream hummed at your suggestion."
                     show dream neutral with dissolve
                     D "I could do that too,{w=0.3} yeah."
                     show dream grin 2 at center, bounce
                     D "They aren't my friends for nothing!"
                     "He smiled at you,{w=0.3} thankful for reminding him of that option."
                     hide dream grin 2 with dissolve
                     "It's evident that he's spent a lot of time thinking over many,{w=0.3} {i}many{/i} things.{w=0.3} You thought that it'd be better if he'd discuss it with everyone else so that he wouldn't have to weigh everything on himself."
                     $ dream_platonic += 10
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

                 label dreambad2:
                     $ renpy.fix_rollback()
                     "Dream's expression darkened as he lowered his head."
                     show dream annoyed with dissolve
                     pause(1.0)
                     D "Yeah."
                     show dream disappointed with dissolve
                     D "Yeah,{w=0.3} you're right."
                     hide dream disappointed with dissolve
                     $ dream_bad += 20
                     stop music fadeout 1.0
                     pause(1.0)
                     scene libraryday
                     with dissolve
                     jump e

         label e:
             $ renpy.fix_rollback()
             scene libraryday
             play music "audio/Twin Musicom - Old Bossa.mp3" fadein 5.0 volume 0.5
             show dream grin 1 at center, bounce
             with dissolve
             D "Guys!"
             show sapnap shock at right, bounce
             show george shock at left, bounce
             with dissolve
             show dream neutral with dissolve
             D "Sun's out!{w=0.3} Let's go and loot this place."
             hide dream neutral
             hide george shock
             hide sapnap shock
             with dissolve
             scene village5
             with dissolve
             "Everyone assembled themselves nearby the entrance of the Library."
             show dream serious at left
             with dissolve
             D "Main focus is to find more iron.{w=0.3} If you guys found enough,{w=0.3} craft a shield for each of you."
             show dream neutral at left
             with dissolve
             D "I'll look for a furnace and smelt the ones I've mined.{w=0.3} I'll keep an eye out for more,{w=0.3} too."
             show george neutral at right, bounce
             with dissolve
             G "And look for food,{w=0.3} too.{w=0.3} We'll be needing more of it later on."
             hide dream neutral
             hide george neutral
             with dissolve
             "Everyone nods and headed off in various directions."
             scene villagehouse
             with dissolve
             play sound "audio/villager.mp3"
             "You enter a nearby house to be greeted by a Villager,{w=0.3} who stares at you for a moment before leaving the structure."
             "You shook your head at the random encounter before climbing up the stairs to see a chest in the corner."
             scene villageloot
             with dissolve
             show chest2 with dissolve
             "Opening it,{w=0.3} you were greeted by 4 piece of bread,{w=0.3} 2 Iron Ingots,{w=0.3} and an Apple."
             "Smiling,{w=0.3} you stash all of them into your inventory before heading out."
             hide chest 2 with dissolve
             scene village5
             with dissolve
             "You met up with Sapnap and George as they both emerged from a nearby house."
             show george grin 2 at left, bounce
             with dissolve
             "George approaches you.{w=0.3} He gives you a shield and an Iron pickaxe to replace your stone one.{w=0.3} You noted that he was able to make enough for everyone."
             show george neutral at left
             with dissolve
             show dream neutral at right
             with dissolve
             "Turning around to the sound of footsteps approaching,{w=0.3} you see Dream returning with more iron ingots and a bunch of buckets in his hands."
             "George also made his way to the blonde,{w=0.3} handing him his share of the new Iron assets."
             show dream grin 2 at right, bounce
             "Dream nodded at him in thanks."
             D "Nice!"
             show dream neutral at right, bounce
             D "Alright,{w=0.3} Sapnap?"
             show sapnap shock at center, bounce
             with dissolve
             S "?"
             show dream neutral at right, bounce
             D "How many Obsidian blocks were in the chest?"
             show sapnap annoyed
             with dissolve
             "Sapnap pondered for a bit."
             show sapnap neutral at center, bounce
             S "I think there were two."
             "Dream glances down at the buckets he had with him and handed a few over to George."
             show dream grin 1 at right, bounce
             D "Alright,{w=0.3} George,{w=0.3} you go and get water.{w=0.3} I'll go ahead and get some lava.{w=0.3} Sapnap-{w=1.0}{nw}"
             show sapnap grin 1 at bounce
             S "I'll stay here and light the new portal up."
             show dream grin 2 at right, bounce
             D "You stay here and light the new portal up."
             hide george neutral
             hide dream grin 2
             hide sapnap grin 1
             with dissolve
             "Dream bounds off to the opposite direction,{w=0.3} while George walks to the nearby brook.{w=0.3} Sapnap walks down the path towards the Ruined Portal area."
             menu:
                 "Who do you wanna catch up to?"

                 "Follow George":
                     $ george_points += 2
                     $ george_romantic += 3
                     $ george_platonic += 3
                     $ george_bad += 3
                     jump george4

                 "Follow Dream" if persistent.trueroute == True:
                     $ dream_points += 2
                     $ dream_romantic += 3
                     $ dream_platonic += 3
                     $ dream_bad += 3
                     jump dream3

                 "Follow Sapnap":
                     $ sapnap_points += 2
                     $ sapnap_romantic += 3
                     $ sapnap_platonic += 3
                     $ sapnap_bad += 3
                     jump sapnap4




                     label george4:
                         $ renpy.fix_rollback()
                         pause(0.5)
                         scene brook
                         with fastdissolve
                         "You sped up a bit and caught up with George."
                         show george grin 2 with dissolve
                         "He smiles at you as you both fall into step."
                         hide george grin 2 with dissolve
                         "As you approach the small body of water,{w=0.3} George crouches down and scoops up enough water into the bucket."
                         show george neutral with dissolve
                         G "You seem really easy to talk to, [povname]."
                         show george grin 1 at center, bounce
                         G "How are you with your friends on your end?"
                         hide george grin 1 with dissolve
                         menu:
                             "They're... fine.":
                                 jump georgebad3
                             "They're a great bunch.":
                                 jump georgeplatonic3
                             "They mean the world to me.":
                                 jump georgeromantic3

                         label georgeromantic3:
                             $ renpy.fix_rollback()
                             "You smile as you thought of your friend group.{w=0.3} They always knew how to brighten up your day when it gets too much."
                             "You would do anything it takes to make them just as happy."
                             "George smiles at this."
                             scene georgecg3 with dissolve:
                                 xpos 0.7 ypos 1.7 xanchor 0.66 yanchor 0.93 zoom 2.0
                                 linear 15 yanchor 0.59
                             pause(1.0)
                             scene georgecg3
                             $ mouse_parallax.set ((-20, -5, "l0"))
                             $ showp ("georgecg3")
                             with dissolve
                             G "I feel the exact same."
                             G "I'd give them everything I have if it meant having smiles on their faces,{w=0.3} too."
                             $ scenep ()
                             with dissolve
                             "You can hear the fondness dripping from his voice.{w=0.3} The other two seem to be very dear to him,{w=0.3} you concluded."
                             $ george_romantic += 10
                             jump george4b

                         label georgeplatonic3:
                             $ renpy.fix_rollback()
                             "You've hung out with your friends a lot.{w=0.3} They make you laugh without having to try hard."
                             "Sometimes,{w=0.3} they even drag you into unnecessary trouble.{w=0.3} You inwardly roll your eyes at the fond memories."
                             show george grin 1 with dissolve
                             "George chuckles at this."
                             play sound "audio/george giggle.mp3"
                             G "Yeah,{w=0.3} I get that too."
                             G "They'd get you into all sorts of situations,{w=0.3} good and bad."
                             show george grin 2 at center, bounce
                             G "But,{w=0.3} I guess what's important is that you're all there for each other."
                             hide george grin 2 with dissolve
                             "The amusement echoes out in his voice.{w=0.3} You agree with his statement."
                             $ george_platonic += 10
                             jump george4b

                         label georgebad3:
                             $ renpy.fix_rollback()
                             "You wouldn't prefer to be alone,{w=0.3} but you wouldn't prefer to be around them a lot either.{w=0.3} People come and go."
                             show george serious with dissolve
                             "George hums passively at your curt tone."
                             play sound "audio/george hum.mp3"
                             G "Hmm."
                             G "Not as easy as I thought."
                             hide george serious with dissolve
                             "His tone sounded more guarded than before,{w=0.3} but you paid no mind to it."
                             $ george_bad += 10
                             jump george4b
                     label george4b:
                         $ renpy.fix_rollback()
                         scene brook
                         with dissolve
                         show george grin 1 with dissolve
                         G "Let's head back."
                         "You nodded before walking right behind him,{w=0.3} following the path back towards the Ruined Portal."
                         scene ruinedportal1
                         with dissolve
                         jump f


                     label sapnap4:
                         $ renpy.fix_rollback()
                         pause(0.5)
                         scene ruinedportal1
                         with fastdissolve
                         "You decided to walk down the path,{w=0.3} following Sapnap to the Portal."
                         show sapnap neutral at center, bounce
                         with dissolve
                         "He nods at you whilst you take a seat on a nearby grass block,{w=0.3} mirroring him."
                         hide sapnap neutral with dissolve
                         "You both sat in silence for a bit as you waited for the others to return."
                         "After a while,{w=0.3} Sapnap speaks up.{w=0.3} His face seemed serious and it made you worry quite a bit as you're much used to the cheery expression that had stayed much more constant on his features."
                         show sapnap annoyed at center, bounce
                         with dissolve
                         S "So."
                         show sapnap wary at center, bounce
                         S "What are you looking forward to?{w=0.3} Like,{w=0.3} what do you wanna get out of this?"
                         "You take in his question and ponder for a bit."
                         hide sapnap wary with dissolve
                         menu:
                             "The experience would be useful.":
                                 jump sapnapromantic3
                             "Something other than {i}normal.{/i}":
                                 jump sapnapbad3
                             "I don't know, really.":
                                 jump sapnapplatonic3

                         label sapnapromantic3:
                             $ renpy.fix_rollback()
                             "It wasn't as if you enjoyed the idea of being stuck in some sort of virtual reality,{w=0.3} but sometimes you liked to look on the brighter side of things."
                             "Besides,{w=0.3} this could come in handy for future situations,{w=0.3} with it exercising your patience and all."
                             "Sapnap seemed to be in thought."
                             scene sapnapcg3 with dissolve:
                                 xpos 0.7 ypos 1.7 xanchor 0.66 yanchor 0.93 zoom 2.0
                                 linear 15 yanchor 0.59
                             pause(1.0)
                             scene sapnapcg3
                             $ mouse_parallax.set ((-20, -5, "l0"))
                             $ showp ("sapnapcg3")
                             with dissolve
                             S "As much as I love Minecraft and all,{w=0.3} being stuck here sucks."
                             S "I just wanna go back home and be in my bed,{w=0.3} stay on call with the other two."
                             S "But,{w=0.3} you're right.{w=0.3} Maybe I should just think more positively about this,{w=0.3} rather than to think against it the entire time we'll be here."
                             $ scenep ()
                             with dissolve
                             "You agreed.{w=0.3} You can't stay upset forever or else you wouldn't reach a clearer solution."
                             "You received a calmer look from the brunet."
                             $ sapnap_romantic += 10
                             jump sapnap4b

                         label sapnapplatonic3:
                             $ renpy.fix_rollback()
                             "You sway your legs back and forth as you couldn't bring up a proper answer."
                             "You decided to settle on shrugging your shoulders.{w=0.3} You didn't really want to expect much of anything."
                             show sapnap sigh with dissolve
                             "Sapnap sighs at this,{w=0.3} though it wasn't in a negative light."
                             S "Yeah,{w=0.3} I don't know either too."
                             show sapnap neutral at center, bounce
                             S "I shouldn't get {i}way{/i} ahead of myself with these kinds of things.{w=0.3} We'll deal with problems the moment they come,{w=0.3} right?"
                             "You nodded.{w=0.3} THere isn't any point in shaking yourself up for a possible situation that won't even happen after a while.{w=0.3} Some things are better dealt as it comes your way."
                             show sapnap grin 2 at center, bounce
                             "Sapnap inhales deeply in an attempt to calm himself before having a tiny smile on his face."
                             hide sapnap grin 2 with dissolve
                             $ sapnap_platonic += 10
                             jump sapnap4b

                         label sapnapbad3:
                             $ renpy.fix_rollback()
                             "There were millions of things to try out here in this universe.{w=0.3} You couldn't wait to try it."
                             "It was better than real life,{w=0.3} you thought."
                             show sapnap wary with dissolve
                             "Sapnap looks at you in bewilderment."
                             S "You'd really wanna stay here...?{w=0.3} Like,{w=0.3} forever?"
                             "Your glance drifts off to the side.{w=0.3} You didn't exactly mean {i}forever{/i},{w=0.3} but you wouldn't mind just existing here either."
                             show sapnap annoyed with dissolve
                             "Sapnap had his eyebrows furrowed slightly.{w=0.3} He seemed to be upset at this."
                             $ sapnap_bad += 10
                             jump sapnap4b

                         label sapnap4b:
                             $ renpy.fix_rollback()
                             scene ruinedportal1
                             with dissolve
                             "He continues to toss his flint and steel up one more time until you both turned towards the sound of footsteps that were arriving at your area."
                             jump f


                     label dream3:
                         $ renpy.fix_rollback()
                         "You sprint after the masked male,{w=0.3} a smile lighting up his features as you fall into step with him."
                         show dream neutral with dissolve
                         "He hands you one of the buckets as you walked along the fine trail between the forest biome and the desert biome."
                         hide dream neutral with dissolve
                         pause(0.5)
                         scene desert
                         with fastdissolve
                         "From afar,{w=0.3} Dream spots a lava pool nearby.{w=0.3} He beckons at you to follow him off the path."
                         scene lava
                         with dissolve
                         "The both of you had crouched near the pool,{w=0.3} cautious enough to not burn yourselves,{w=0.3} and proceeded to scoop up the needed material."
                         show dream annoyed with dissolve
                         "Dream was the first to break the silence between you both,{w=0.3} sitting nearby the pool as he was the first to finish."
                         D "So,{w=0.3} um.{w=0.3}.{w=0.3}.{w=0.3}"
                         show dream wary at center, bounce
                         D "What do you think of the unknown?"
                         D "Don't you think it's.{w=0.3}.{w=0.3}.{w=0.3} terrifying?"
                         hide dream wary with dissolve
                         menu:
                             "I don't think it is.":
                                 jump dreamromantic3
                             "{color=#e60000}Oh, for sure.{/color}" if bad_choices == True:
                                 jump dreambad3
                             "It's quite intimidating.":
                                 jump dreamplatonic3


                         label dreamromantic3:
                             $ renpy.fix_rollback()
                             "Dream tilts his head."
                             scene dreamcg3 with dissolve:
                                  xpos 1.0 ypos 1.6 xanchor 0.66 yanchor 0.93 zoom 2.0
                                  linear 15 yanchor 0.59
                             pause(1.0)
                             scene dreamcg3
                             $ mouse_parallax.set ((-20, -5, "l0"))
                             $ showp ("dreamcg3")
                             with dissolve
                             D "How so?"
                             pause(0.5)
                             "You explain to him that there's no need to fear the things that you don't know.{w=0.3} All you can do is brace yourself and adapt to the changes you'll just have to face."
                             "Dream takes your words into account,{w=0.3} bopping his head as he comprehends the information."
                             "After a second or two,{w=0.3} his face breaks into a smile."
                             $ scenep ()
                             with dissolve
                             D "Yeah,{w=0.3} you're right."
                             D "Thanks,{w=0.3} [povname].{w=0.3} I guess it's just the whole 'virtual reality' thing jarring me.{w=0.3} That really eases my mind."
                             scene lava
                             with dissolve
                             "You mirror his expression with your own comforting smile,{w=0.3} glad to have helped him out even a little bit."
                             scene desert
                             with dissolve
                             $ dream_romantic += 10
                             jump dream3b

                         label dreamplatonic3:
                             $ renpy.fix_rollback()
                             show dream grin 2 at center, bounce
                             with dissolve
                             play sound "audio/dream giggle.mp3"
                             "Dream chuckled as you stammered your response."
                             "You didn't want to lie-{w=0.3} everything so far had overwhelmed you from time to time.{w=0.3} It wouldn't be a surprise if there would be a point where you'd like to just stop everything for a while and just {i}breathe.{/i}"
                             "Dream sighed as his laughter died down,{w=0.3} a weary smile resting on his lips."
                             show dream neutral with dissolve
                             D "I feel the same,{w=0.3} too."
                             show dream grin 1 at center, bounce
                             D "I'm glad you didn't let anything stop you from helping us out,{w=0.3} though."
                             show dream grin 2 at center, bounce
                             D "You're really cool, [povname]."
                             hide dream grin 2 with dissolve
                             "He ruffles your hair before placing both of his hands on one of the buckets you both filled."
                             show dream grin 2 at center, bounce
                             with dissolve
                             play sound "audio/dream giggle.mp3"
                             "You complained at the messy result,{w=0.3} to which he laughed at."
                             hide dream grin 2 with dissolve
                             scene desert
                             with dissolve
                             $ dream_platonic += 10
                             jump dream3b

                         label dreambad3:
                             $ renpy.fix_rollback()
                             show dream wary with dissolve
                             "Dream frowns at the way you visibly shivered at the mention of the topic."
                             "He immediately apologizes for this."
                             show dream annoyed with dissolve
                             D "Sorry."
                             D "Let's just drop this."
                             hide dream annoyed with dissolve
                             scene desert
                             with dissolve
                             $ dream_bad += 20
                             jump dream3b


                         label dream3b:
                             $ renpy.fix_rollback()
                             scene desert
                             show dream neutral with dissolve
                             "Dream stands up from the pool.{w=0.3} You follow his lead and meet his gaze."
                             show dream grin 2 at center, bounce
                             "You both nodded at each other,{w=0.3} a quiet confirmation that you both had the same thing in mind."
                             hide dream grin 2 with dissolve
                             "You both then headed back to the Ruined Portal."
                             scene ruinedportal1
                             with dissolve
                             jump f

             label f:
                 $ renpy.fix_rollback()
                 scene ruinedportal1
                 show dream grin 1 with dissolve
                 D "You guys got the stuff?"
                 show george neutral at left, bounce
                 show sapnap neutral at right, bounce
                 with dissolve
                 "Everyone raises their needed item,{w=0.3} confirming that they all had what they needed."
                 show dream grin 2 at center, bounce
                 "Dream smiles at this before beginning to call George to his side to help complete the portal altogether."
                 hide dream grin 2
                 hide george neutral
                 hide sapnap neutral
                 with dissolve
                 "You stood by the side as the three other members had grouped up together to speed up the portal-building process."
                 "Once they were all finished,{w=0.3} Sapnap flicked the stone in his possession and flared the new Nether Portal to life."
                 scene netherportal1
                 with dissolve
                 pause(1.0)
                 show dream grin 1 at center, bounce
                 show george grin 1 at left, bounce
                 show sapnap grin 1 at right, bounce
                 with dissolve
                 "The four of you grinned at the success of your first half of the plan.{w=0.3} Sapnap then glances around to everyone else."
                 show sapnap grin 1 at right, bounce
                 S "So,{w=0.3} is everyone ready?"
                 "Dream points to George."
                 show dream neutral at center, bounce
                 D "Wear your helmet,{w=0.3} George."
                 show george shock at left, bounce
                 G "Oh!{w=0.3} Yeah."
                 hide george shock with dissolve
                 "George quickly applies the helmet and gave out a thumbs up."
                 show george grin 2 at left, bounce
                 with dissolve
                 G "We're ready!"
                 show sapnap neutral at right, bounce
                 "Sapnap nods and you all usher over to the line of blocks right before the portal."
                 hide sapnap neutral
                 hide george grin 2
                 hide dream neutral
                 with dissolve
                 "You inhale deeply and exhale slowly,{w=0.3} an attempt to calm your nerves before entering the portal.{w=0.3} You peer over to the side to see the other three doing the same."
                 show dream serious with dissolve
                 "Dream then began to count."
                 show dream serious at center, bounce
                 D "On three.{w=0.3} One..."
                 show george serious at left
                 with dissolve
                 G "Two..."
                 show sapnap angry at right, bounce
                 with dissolve
                 S "{i}Three!{/i}"
                 "As Sapnap shouted,{w=0.3} all four of you had jumped into the Portal at the same time."
                 stop music fadeout 1.0
                 scene portal
                 with dissolve
                 play sound "audio/nether.mp3" volume 0.2
                 pause(3.0)
                 play music "audio/Twin Musicom - Dial M.mp3" fadein 5.0 volume 0.5
                 scene nether2
                 with dissolve
                 "After feeling light for a split second as you thread through two different worlds,{w=0.3} you feel gravity pulling you down as you entered a warmer surrounding."
                 "You decided to take a step down from the Obsidian platform.{w=0.3} With the disorientation catching up to you,{w=0.3} you had fallen onto your knees and clutched your head."
                 play sound "audio/fall.mp3" volume 0.3
                 show nether2 with hpunch:
                     zoom 1.5
                 "Teleporting from one world to another isn't exactly as fun as it seemed."
                 scene nether2
                 with dissolve
                 show dream pained 2
                 show george pained 2 at left
                 show sapnap pained 2 at right
                 with dissolve
                 "The other three had simultaneously groaned as they landed."
                 show sapnap annoyed at right, bounce
                 S "Yeah,{w=0.3} hopefully we're {i}never{/i} doing this again."
                 show george wary at left, bounce
                 G "I second that."
                 hide dream pained 2
                 hide george wary
                 hide sapnap annoyed
                 with dissolve
                 "Shaking his head,{w=0.3} Dream stood up and batted away the Netherrack dust that had gotten all over him from the fall.{w=0.3} You and the other two had followed his lead and did the same."
                 "Dream gazes around the view of endlessly dripping lava,{w=0.3} trying to let the scene sink in."
                 show dream wary at center, bounce
                 with dissolve
                 D "The Nether.{w=0.3}.{w=0.3}.{w=0.3}"
                 hide dream wary with dissolve
                 "You can hear the dread in Dream's voice,{w=0.3} and you were about to approach him about it before he turned around with a stern look on his face."
                 show dream serious with dissolve
                 D "Gather a bunch of Netherrack.{w=0.3} We'll all need it."
                 show george serious at left, bounce
                 show sapnap serious at right, bounce
                 with dissolve
                 "You all nodded and split off,{w=0.3} and you bounded off to the side creating a small strip mine to easily gather a big amount of the nearby material."
                 hide dream serious
                 hide george serious
                 hide sapnap serious
                 with dissolve
                 scene nether2 with dissolve:
                      xpos 1.0 ypos 0.9 xanchor 0.66 yanchor 0.77 zoom 2.0
                      ease 2 yanchor 0.62
                 pause(1.0)
                 "As you mined away,{w=0.3} you heard a loud gasp echo from outside the cave."
                 play sound "audio/george gasp 2.mp3"
                 G "GUYS!"
                 G "The Fortress!{w=0.3} It's right here!"
                 scene nether2 with dissolve
                 "You raise your eyebrows in surprise.{w=0.3} It was just near spawn?{w=0.3} That's so lucky!"
                 "You hurriedly mine a bit more Netherrack before running outside,{w=0.3} catching up to Sapnap who had evidently done the exact same."
                 scene nether1 with dissolve
                 show george shock at center, bounce
                 with dissolve
                 show sapnap grin 1 at right, bounce
                 with dissolve
                 S "Nice find,{w=0.3} Gogy!"
                 show dream grin 2 at left, bounce
                 with dissolve
                 show george annoyed at center, bounce
                 "George seemingly cringes at the nickname but was cut off from reacting due to the fact that Dream had ruffled his hair."
                 hide george annoyed
                 hide dream grin 2
                 hide sapnap grin 1
                 with dissolve
                 "Everyone follows George's lead towards the structure."
                 scene nether1 with dissolve:
                      xpos 1.0 ypos 0.5 xanchor 0.66 yanchor 0.77 zoom 2.3
                      ease 2 yanchor 0.62
                 pause(1.0)
                 "As your group approaches the Netherbrick walls,{w=0.3} everyone took turns in using their bundles of Netherrack to maneuver up to an entrance."
                 stop music fadeout 1.0
                 pause (1.0)
                 scene fortress1
                 with fastdissolve
                 show george pained 2 at center, shake
                 with hpunch
                 play music "audio/Twin Musicom - Fall of the Solar King.mp3" fadein 5.0 volume 0.5
                 play sound "audio/george gasp 1.mp3"
                 pause(1.0)
                 play sound "audio/shield.mp3"
                 "As you helped each other up the ledge,{w=0.3} George gasps as a Wither Skeleton attacked him.{w=0.3} He had managed to bring up his shield in time to block it."
                 show dream angry at left, bounce
                 show sapnap angry at right, bounce
                 with dissolve
                 DS "{i}GEORGE!{/i}"
                 show george angry at center, bounce
                 G "I'm fine!{w=0.3} Let's just {i}go!{/i}"
                 hide george angry
                 hide dream angry
                 hide sapnap angry
                 with dissolve
                 "He shoves the mob back as everyone darted off to the opposite direction."
                 scene fortress2
                 with fastdissolve
                 show dream angry at left, bounce
                 show sapnap serious at right, bounce
                 with dissolve
                 "Dream points towards a nearby Blaze spawner,{w=0.3} calling Sapnap to his side."
                 hide dream angry
                 hide sapnap serious
                 with dissolve
                 show george wary at center, bounce
                 with dissolve
                 "As they both began to farm for the needed Blaze Rods,{w=0.3} George was busy defending the area from the other mobs that have followed you."
                 hide george wary with dissolve
                 stop music fadeout 1.0
                 pause(1.0)
                 label dummychoice2:
                     play music "audio/Twin Musicom - Seven Lives to Live.mp3" fadein 5.0 volume 0.5
                     show fortress2
                     with dissolve
                     "The two different mobs began to multiply as time passed,{w=0.3} and you knew you had to help out somehow."
                     label menu2:
                         $ time = 5
                         $ timer_range = 5
                         $ timer_jump = 'dummyending2'
                         show screen countdown
                         menu:

                            "Assist Dream" if persistent.trueroute == True:
                                 hide screen countdown
                                 $ dream_points += 2
                                 $ dream_romantic += 5
                                 $ dream_platonic += 5
                                 $ dream_bad += 5
                                 jump dream4

                            "Assist George":
                                hide screen countdown
                                $ george_points += 2
                                $ george_romantic += 5
                                $ george_platonic += 5
                                $ george_bad += 5
                                jump george5

                            "Assist Sapnap":
                                 hide screen countdown
                                 $ sapnap_points += 2
                                 $ sapnap_romantic += 5
                                 $ sapnap_platonic += 5
                                 $ sapnap_bad += 5
                                 jump sapnap5



                     label george5:
                         $ renpy.fix_rollback()
                         "You bounded over to George as quick as you can,{w=0.3} swinging your axe at nearby Wither Skeletons before shoving the others away with your own shield."
                         "George looks at you in surprise."
                         scene georgecg4 with dissolve:
                              xpos 0.8 ypos 1.65 xanchor 0.66 yanchor 0.93 zoom 2.0
                              linear 15 yanchor 0.59
                         pause(1.0)
                         scene georgecg4
                         $ mouse_parallax.set ((-20, -5, "l0"))
                         $ showp ("georgecg4")
                         with dissolve
                         G "[povname]!{w=0.3} You-"
                         $ scenep ()
                         with dissolve
                         "But he was cut off when two more Skeletons had bumped against him.{w=0.3} You reprimanded him,{w=0.3} saying that it isn't the right time to complain about your split-second choices."
                         "He silently nodded,{w=0.3} working on defending the other two as they handled each other's sides."
                         jump g


                     label sapnap5:
                         $ renpy.fix_rollback()
                         "You quickly situated yourself near Sapnap,{w=0.3} fending away a Blaze that attempted to get too close to him."
                         "He notices your presence and shoots you a grin."
                         scene sapnapcg4 with dissolve:
                              xpos 0.9 ypos 1.7 xanchor 0.66 yanchor 0.93 zoom 2.0
                              linear 15 yanchor 0.59
                         pause(1.0)
                         scene sapnapcg4
                         $ mouse_parallax.set ((-20, -5, "l0"))
                         $ showp ("sapnapcg4")
                         with dissolve
                         S "Thanks,{w=0.3} [povname]!"
                         $ scenep ()
                         with dissolve
                         "You nodded your head in acknowledgement of his gratitude,{w=0.3} continuing to protect him and slaying more of the blazing mobs whilst at the same time obtaining the rods that drop."
                         jump g


                     label dream4:
                         $ renpy.fix_rollback()
                         "You grunted as you swung your axe from side to side in an attempt to reach Dream.{w=0.3} You deflected a Blaze's hit last second before finally reaching his area."
                         "He looks at you with an angered expression."
                         scene dreamcg4 with dissolve:
                             xpos 0.75 ypos 1.6 xanchor 0.66 yanchor 0.93 zoom 2.0
                             linear 15 yanchor 0.59
                         pause(1.0)
                         scene dreamcg4
                         $ mouse_parallax.set ((-20, -5, "l0"))
                         $ showp ("dreamcg4")
                         with dissolve
                         D "[povname]!{w=0.3} What are you doing?!"
                         D "You didn't have to-"
                         $ scenep ()
                         with dissolve
                         play sound "audio/blaze death.mp3"
                         scene white
                         pause (1.0)
                         scene fortress2
                         with dissolve
                         "He was cut off as you landed a critical hit on the Blaze that had attempted to get him,{w=0.3} reducing into pixels and a blaze rod."
                         play sound "audio/exp.mp3"
                         "You obtained the needed item and EXP as you fixated a glare at the male."
                         show dream annoyed at center, bounce
                         with dissolve
                         "He puts on a sheepish look."
                         show dream wary at center, bounce
                         D "I owe you one."
                         "You nodded and continued to fend off as much Blazes as you can."
                         hide dream wary with dissolve
                         "Dream continues to do the same,{w=0.3} slaying down the mobs until he figured it was enough."
                         jump g


                     label dummyending2:
                          "You couldn't choose which side you should help out on.{w=0.3} Before you knew it,{w=0.3} the number of mobs have multiplied to the point of overwhelming all four of you."
                          scene black
                          with dissolve
                          stop music fadeout 1.0
                          pause(2.0)
                          scene gameover
                          with fade
                          play music "audio/bensound-betterdays.mp3" volume 0.3
                          pause(2.0)
                          show XD neutral at center, bounce
                          with dissolve
                          XD "It seems that you've ran out of time!"
                          show XD grin at center, bounce
                          XD "Bummer.{w=0.3} Would you like to try again?"
                          hide XD grin with dissolve
                          menu:
                              "Retry":
                                  stop music fadeout 1.0
                                  scene white
                                  with dissolve
                                  pause(1.0)
                                  jump dummychoice2
                              "Return to Main Menu":
                                  show XD grin at center, bounce
                                  with dissolve
                                  XD "That sucks,{w=0.3} but understandable!"
                                  XD "We'll see you soon!"
                                  return

                 label g:
                     $ renpy.fix_rollback()
                     show fortress2
                     with dissolve
                     show dream angry at center, bounce
                     with dissolve
                     D "We have enough!{w=0.3} Let's go!"
                     hide dream angry with dissolve
                     play sound "audio/walking.mp3"
                     scene black
                     with wipeleftfast
                     scene nether3
                     with wipeleftfast
                     "You all fought your way through the Fortress grounds and went to the nearby Netherrack field."
                     "As you dashed through the terrain,{w=0.3} you noticed Dream and the others weren't heading for the portal."
                     "You wracked your brain as you wondered why,{w=0.3} but remembered that you needed the easiest and quickest way that you all could think of for obtaining Ender Pearls."
                     "And that was through Piglin Trading."
                     play sound "audio/walking.mp3"
                     scene black
                     with wipeleftfast
                     scene nether4
                     with wipeleftfast
                     "You all look for a biome that had enough mobs that were available for trading."
                     show dream serious with dissolve
                     "Dream hollers over to you guys to dig up a hole to surround at least two or three Piglins."
                     hide dream serious with dissolve
                     "George passes his golden helmet over to Dream as he tosses Gold Ingots towards the hog-like humanoids,{w=0.3} leading them to the hole you all made."
                     "With no gold to pass the Piglins' tastes,{w=0.3} the others have begun to run towards everyone else."
                     stop music fadeout 1.0
                     pause(1.0)
                     label dummychoice3:
                         play music "audio/Twin Musicom - Savoy Theatre.mp3" fadein 5.0 volume 0.5
                         show nether4 with dissolve
                         show sapnap serious at right
                         with dissolve
                         "Sapnap was on one end of the pit fighting against two Ghasts that have simultaneously spawned."
                         show george serious at left
                         with dissolve
                         "George was on the other end fending off other Piglins and a few Wither Skeletons that had followed your group."
                         show sapnap angry at right, bounce
                         S "Dream,{w=0.3} make it quick!"
                         show dream angry at center, bounce
                         with dissolve
                         D "I'm trying!"
                         show george angry at left, bounce
                         G "{i}Dream!{/i}"
                         hide george angry
                         hide dream angry
                         hide sapnap angry
                         with dissolve

                         label menu3:
                             $ time = 5
                             $ timer_range = 5
                             $ timer_jump = 'dummyending3'
                             show screen countdown
                             menu:

                                 "Trade with Piglins" if persistent.trueroute == True:
                                      hide screen countdown
                                      $ dream_points += 2
                                      $ dream_romantic += 10
                                      $ dream_platonic += 10
                                      $ dream_bad += 10
                                      jump dream5

                                 "Fend off Piglins":
                                     hide screen countdown
                                     $ george_points += 2
                                     $ george_romantic += 10
                                     $ george_platonic += 10
                                     $ george_bad += 10
                                     jump george6

                                 "Fight Ghasts":
                                      hide screen countdown
                                      $ sapnap_points += 2
                                      $ sapnap_romantic += 10
                                      $ sapnap_platonic += 10
                                      $ sapnap_bad += 10
                                      jump sapnap6

                         label george6:
                             $ renpy.fix_rollback()
                             scene nether3
                             with fastdissolve
                             "Making up your mind,{w=0.3} you take long strides towards the older male who seemed to have a tiny bit of trouble fighting off the mobs."
                             "You tell George that you can handle the skeletons and have him run around the area as much as he can to stall time for Dream to make the sufficient amount of trades."
                             show george grin 1 at center, bounce
                             with dissolve
                             G "Sounds like a plan, [povname]!"
                             hide george grin 1 with dissolve
                             "He then began to run around and lead the other Piglins away as you exchanged hits with the Wither Skeletons in front of you."
                             jump h


                         label sapnap6:
                             $ renpy.fix_rollback()
                             scene netherghast1
                             with fastdissolve
                             "Making up your mind,{w=0.3} you decided to rush towards Sapnap's side."
                             "One of the Ghasts have launched a fireball right towards the brunet.{w=0.3} You managed to be quicker enough to swing it back wiith your axe."
                             "The fireball missed the levitating mob,{w=0.3} but Sapnap thanked you nonetheless."
                             show sapnap grin 2 at center, bounce
                             with dissolve
                             S "Knew I could count on you, [povname]!"
                             hide sapnap grin 2 with dissolve
                             "You grinned as you both focused on one Ghast each.{w=0.3} It took you 4 tries to hit the mob back,{w=0.3} while it took Sapnap 2."
                             pause(1.0)
                             show nether4
                             with fastdissolve
                             show sapnap grin 1 at center, bounce
                             with dissolve
                             "After defeating both of them,{w=0.3} you gave each other a quick high-five."
                             scene netherghast2
                             with fastdissolve
                             pause (1.0)
                             show sapnap shock at center, bounce
                             with dissolve
                             "But,{w=0.3} shortly after,{w=0.3} you both saw that more Ghasts were coming your way."
                             hide sapnap shock with dissolve
                             jump h


                         label dream5:
                             $ renpy.fix_rollback()
                             "Making up your mind,{w=0.3} you hopped down into the pit with Dream."
                             scene netherpiglin3
                             with fastdissolve
                             show dream shock at center, bounce
                             with dissolve
                             "He looks at you,{w=0.3} bewildered,{w=0.3} but immediately understood your intentions."
                             show dream serious at center, bounce
                             "He splits off the number of Gold Ingots he had in his inventory and gave the other half to you.{w=0.3} Quickly,{w=0.3} you started to initiate in the trading process."
                             play sound "audio/piglin trade.mp3"
                             hide dream serious with dissolve
                             "You simply waited as you took turns with the mob,{w=0.3} giving up gold for different items."
                             "The items you've seen so far have been a Water Bottle,{w=0.3} a few Iron Nuggets,{w=0.3} Obsidian blocks.{w=0.3}.{w=0.3}.{w=0.3}"
                             "And then you saw 3 Ender Pearls on the ground."
                             show netherpiglin3 with hpunch:
                                 zoom 1.5
                             "Quickly,{w=0.3} you nabbed it before throwing another Gold Ingot at the mob before it began to attack you."
                             play sound "audio/piglin trade.mp3"
                             scene netherpiglin3 with dissolve
                             "Anticipating another,{w=0.3} you immediately lunged at the drop of a set of 4."
                             show netherpiglin3 with hpunch:
                                 zoom 1.5
                             pause(1.0)
                             scene netherpiglin3
                             with dissolve
                             show dream wary with dissolve
                             D "Have you gotten enough?"
                             show dream serious at center, bounce
                             D "I've gotten a set of 2 and a set of 4."
                             hide dream serious with dissolve
                             "You were unsure,{w=0.3} so you continued to attempt to trade one more time to ease yourself.{w=0.3} In doing so,{w=0.3} you've lost track of your surroundings."
                             jump h


                         label dummyending3:
                             "You couldn't choose which side you should help out on.{w=0.3} Before you knew it,{w=0.3} the number of mobs have multiplied to the point of overwhelming all four of you."
                             scene black
                             with dissolve
                             stop music fadeout 1.0
                             pause(2.0)
                             scene gameover
                             with fade
                             play music "audio/bensound-betterdays.mp3" volume 0.3
                             pause(2.0)
                             show XD neutral at center, bounce
                             with dissolve
                             XD "It seems that you've ran out of time!"
                             show XD grin at center, bounce
                             XD "Bummer.{w=0.3} Would you like to try again?"
                             hide XD grin with dissolve
                             menu:
                                 "Retry":
                                     stop music fadeout 1.0
                                     scene white
                                     with dissolve
                                     pause(1.0)
                                     jump dummychoice3
                                 "Return to Main Menu":
                                     show XD grin at center, bounce
                                     with dissolve
                                     XD "That sucks,{w=0.3} but understandable!"
                                     XD "We'll see you soon!"
                                     return

                     label h:
                         $ renpy.fix_rollback()
                         scene nether4
                         with dissolve
                         "Everything began to overhelm you,{w=0.3} from the amount of mobs surrounding all of you to the huge amount of pressure you're feeling right now."
                         "Sapnap began to call out,{w=0.3} peeved tone seeping out of his voice."
                         show sapnap angry at center, bounce
                         with dissolve
                         S "{i}DREAM!{/i}"
                         hide sapnap angry with dissolve
                         show dream annoyed with dissolve
                         "Dream rolled his eyes."
                         show dream angry at center, bounce
                         D "Let's go!{w=0.3} This way!"
                         hide dream angry with dissolve
                         "He was visibly irritated as he was pressured,{w=0.3} but hopefully everyone would shrug it off."
                         play sound "audio/walking.mp3"
                         scene black
                         with wipeleftfast
                         scene nether2
                         with wipeleftfast
                         scene black
                         with wipeleftfast
                         scene netherportal2
                         with wipeleftfast
                         "You all bolted towards the right direction to the Portal,{w=0.3} the one you finally recognize,{w=0.3} and gasped in relief when you spotted the familiar purple particles flaring into the air."
                         show dream serious with dissolve
                         "Dream reaches it first,{w=0.3} not entering the vortex and instead opted out to take a swing at an apporaching aggressive Piglin mob."
                         show dream angry at center, bounce
                         D "Get in!{w=0.3} {i}NOW!{/i}"
                         hide dream angry with dissolve
                         "Without a second thought,{w=0.3} Sapnap and George had entered the Portal,{w=0.3} their bodies slowly disappearing into the Overworld the longer they stayed in."
                         scene nether2
                         with fastdissolve
                         "You glanced back at Dream and hesitated.{w=0.3} You didn't want to leave him behind."
                         "Dream frowned at you."
                         show dream angry at center, bounce
                         with dissolve
                         D "{i}GO!{/i}"
                         "When you didn't budge,{w=0.3} Dream had instead pushed you through the portal."
                         stop music fadeout 1.0
                         scene portal
                         with dissolve
                         play sound "audio/nether.mp3" volume 0.2
                         pause(3.0)
                         scene netherportal1
                         with dissolve
                         play sound "audio/fall.mp3" volume 0.3
                         show netherportal1 with hpunch:
                             zoom 1.5
                         pause(1.0)
                         scene netherportal1
                         with slowdissolve
                         play music "audio/Twin Musicom - Push Me 10 Minutes.mp3" fadein 5.0 volume 0.5
                         "When you came to,{w=0.3} your first reaction was to frantically check your surroundings for your other companions."
                         S "We're here,{w=0.3} [povname].{w=0.3} We're here."
                         scene jungle
                         with dissolve
                         show sapnap wary at right, bounce
                         with dissolve
                         show george sigh at left
                         with dissolve
                         "From behind you,{w=0.3} you hear Sapnap and George seemingly out of breath.{w=0.3} The older of the two was lying on his back,{w=0.3} whilst the other was seated on a nearby grass block and wiping the sweat from his chin."
                         show george wary at left
                         with dissolve
                         "George's voice wavered when he spoke up."
                         show george wary at left, bounce
                         G "Where's Dream?"
                         "Your heart sank when you had to explain what had happened before you teleported back into the Overworld."
                         show george wary at left, bounce
                         show sapnap wary at right, bounce
                         "They both frowned at this."
                         show sapnap annoyed at right, bounce
                         S "Of course he would.{w=0.3}.{w=0.3}.{w=0.3}"
                         show george angry at left, bounce
                         G "We have to go back,{w=0.3} see if he's still there!{w=0.3} We need to help him!"
                         scene netherportal1
                         with fastdissolve
                         play sound "audio/nether.mp3" volume 0.2
                         "Before their argument could get any bigger,{w=0.3} Dream had suddenly appeared into the Overworld."
                         play sound "audio/fall.mp3" volume 0.3
                         show dream pained 2 at center, shake
                         with dissolve
                         "He landed onto the grass with a harsh thud."
                         show george shock at left, bounce
                         show sapnap shock at right, bounce
                         with dissolve
                         GS "Dream!"
                         "You all rushed over to his side,{w=0.3} to which he waved off.{w=0.3} Both Sapnap and George helped him up onto his feet."
                         show dream sigh at center, bounce
                         D "I'm fine,{w=0.3} I'm fine."
                         show dream wary at center, bounce
                         D "Health check,{w=0.3} guys?"
                         show george wary at left, bounce
                         show sapnap wary at right, bounce
                         "You all warily nodded before looking up to your own health bars."
                         show george serious at left, bounce
                         "George says that he has 4 left."
                         show sapnap serious at right, bounce
                         "You and Sapnap have the same amount of 3."
                         show dream serious at center, bounce
                         "Dream only had half a heart."
                         show george annoyed at left, bounce
                         show sapnap wary at right, bounce
                         "Sapnap frowned as George crossed his arms."
                         show george angry at left, bounce
                         G "What happened to being {i}careful{/i},{w=0.3} Dream?"
                         show dream disappointed at center, bounce
                         play sound "audio/dream ugh.mp3"
                         "Dream waves him off as he pulled out a piece of bread to replenish his hunger and to regen."
                         show dream annoyed at center, bounce
                         D "All that matters is that we're fine."
                         show dream annoyed at center, bounce
                         D "It was our first,{w=0.3} and hopefully {i}last{/i},{w=0.3} time in the Nether.{w=0.3} Of course it'd end up messy."
                         "You were about to hand him your Golden Apple,{w=0.3} but he noticed and stopped you from doing so."
                         show dream serious at center, bounce
                         D "I told you.{w=0.3} You'll need it more than I do."
                         "You frowned,{w=0.3} but didn't push.{w=0.3} You stashed it back into your inventory as Sapnap approached him to craft Eyes of Ender."
                         hide dream serious
                         hide sapnap annoyed
                         hide george angry
                         with dissolve
                         "As they successfully crafted a few,{w=0.3} Dream flicked one up.{w=0.3} It slowly rises and leans towards one direction before ultimately plunging to the ground."
                         "The blonde catches it right before it lands and double checks if it snapped into two."
                         show dream serious with dissolve
                         D "Well,{w=0.3} we have our lead.{w=0.3} Let's go."
                         hide dream serious with dissolve
                         "You all then fell into step with each other."
                         scene walking
                         with dissolve
                         "The walk was quiet,{w=0.3} save for the occasional clinking of the Ender Eyes that came from Dream."
                         "It was a bit too quiet for your liking."
                         menu:
                             "Check up on who?"

                             "\"Dream, are you okay?\"" if persistent.trueroute == True:
                                 $ dream_points += 2
                                 $ dream_romantic += 3
                                 $ dream_platonic += 3
                                 $ dream_bad += 3
                                 jump dream6

                             "\"Are you good, Sapnap?\"":
                                 $ sapnap_points += 2
                                 $ sapnap_romantic += 3
                                 $ sapnap_platonic += 3
                                 $ sapnap_bad += 3
                                 jump sapnap7

                             "\"Any injuries, George?\"":
                                 $ george_points += 2
                                 $ george_romantic += 3
                                 $ george_platonic += 3
                                 $ george_bad += 3
                                 jump george7

                         label george7:
                             $ renpy.fix_rollback()
                             scene walking2
                             with dissolve
                             "You slowed your pace down to match with George's,{w=0.3} who was situated on the very end of your little line of 'Follow the Leader'."
                             show george shock at center, bounce
                             with dissolve
                             "The colorblind male had been munching on his share of bread,{w=0.3} effectively replenishing his health.{w=0.3} He nods as he swallows his recent bite."
                             show george neutral at center, bounce
                             G "I'm all good,{w=0.3} [povname].{w=0.3} Thanks for asking."
                             show george grin 1 at center, bounce
                             G "Do you need anything?"
                             show george wary at center, bounce
                             G "The only food I've seen you wield was the Gapple from way earlier."
                             "You shook your head,{w=0.3} letting him know that you have your own stash of foods."
                             hide george wary with dissolve
                             "A little bit of silence filled the space between you two before George spoke up this time."
                             show george annoyed with dissolve
                             G "So.{w=0.3}.{w=0.3}.{w=0.3}"
                             show george shock at center, bounce
                             G "Do you have any questions?{w=0.3} Like,{w=0.3} in general?"
                             show george neutral at center, bounce
                             G "I just figured that since you've been with us this entire time,{w=0.3} might as well get to know each other a bit more."
                             hide george neutral with dissolve
                             menu:
                                 "What else would you like to do outside of this?":
                                     jump georgeromantic4
                                 "I'm not really interested in talking.":
                                     jump georgebad4
                                 "What even got you guys into this mess?":
                                     jump georgeplatonic4


                             label georgeromantic4:
                                 $ renpy.fix_rollback()
                                 "You now knew that he likes coding and reading books.{w=0.3} Maybe there's more that he'd like to do?"
                                 show george annoyed at center, bounce
                                 with dissolve
                                 "George blinked for a second,{w=0.3} before humming in thought."
                                 play sound "audio/george hum.mp3"
                                 G "Something I like to do other than the ones I've told you.{w=0.3}.{w=0.3}.{w=0.3}?"
                                 pause(1.0)
                                 show george grin 1 at center, bounce
                                 G "Well,{w=0.3} I'm quite into chess!{w=0.3} I play it from time to time with the other two."
                                 "You nodded your head."
                                 "Interesting,{w=0.3} it wasn't really a game you were {i}too{/i} interested in.{w=0.3} It fascinates you when you watch people play,{w=0.3} but the mechanics are quite confusing."
                                 "He notices this,{w=0.3} and he lets out the softest laughter."
                                 show george grin 2 at center, bounce
                                 G "Haha,{w=0.3} if you aren't into it,{w=0.3} that's okay!"
                                 show george neutral at center, bounce
                                 G "But,{w=0.3} if you really wanna learn it,{w=0.3} I can teach you."
                                 show george grin 2 blush at center, bounce
                                 play sound "audio/george giggle.mp3"
                                 G "Maybe even have a little chess.{w=0.3}.{w=0.3}.{w=0.3} date?{w=0.3} If you'd like that?"
                                 "His cheeks tint pink,{w=0.3} and you bashfully smiled back.{w=0.3} You'll have to keep that offer in mind."
                                 scene strongholdarea
                                 with dissolve
                                 $ george_romantic += 10
                                 jump i

                             label georgeplatonic4:
                                 $ renpy.fix_rollback()
                                 "It was a question that had stayed in your mind ever since you fell into the realm.{w=0.3} How did all of this even start?"
                                 "George seemed to not anticipate this question,{w=0.3} since his cheeks and ears were tinged with rosy pink."
                                 show george embarrassed with dissolve
                                 G "About that.{w=0.3}.{w=0.3}.{w=0.3}"
                                 show george grin 2 blush at center, bounce
                                 G "It was kind of my fault.{w=0.3}.{w=0.3}.{w=0.3}?"
                                 show george wary at center, bounce
                                 G "It was an error in the code that we were trying out right then.{w=0.3} I activated it before Dream told me to,{w=0.3} just to check if it would work properly,{w=0.3} and all of a sudden,{w=0.3} we woke up in this world."
                                 show george disappointed with dissolve
                                 G "Maybe I shouldn't have tested it."
                                 hide george disappointed with dissolve
                                 "He sheepishly answered,{w=0.3} regret lacing his voice.{w=0.3} You reassure him that whatever he had done wasn't his fault."
                                 "It was just a weird glitch in the system that had transported all of you into the game.{w=0.3} No person can actually pull that off {i}intentionally{/i}."
                                 show george shock at center, bounce
                                 with dissolve
                                 show george neutral at center, bounce
                                 "George looks at you properly before giving you a small smile as he understood your intentions."
                                 hide george neutral with dissolve
                                 "He thanks you,{w=0.3} but his voice was as low as a whisper."
                                 scene strongholdarea
                                 with dissolve
                                 $ george_platonic += 10
                                 jump i

                             label georgebad4:
                                 $ renpy.fix_rollback()
                                 "George looked crestfallen at your response.{w=0.3} He had thought that you two were getting along just fine."
                                 show george wary at center, bounce
                                 with dissolve
                                 G "Oh."
                                 show george wary at center, bounce
                                 G "Sorry,{w=0.3} I must've assumed.{w=0.3}.{w=0.3}.{w=0.3}"
                                 show george annoyed at center, bounce
                                 G "I'll drop it."
                                 hide george annoyed with dissolve
                                 "You look away,{w=0.3} feeling awkward."
                                 scene strongholdarea
                                 with dissolve
                                 $ george_bad += 10
                                 jump i

                         label sapnap7:
                             $ renpy.fix_rollback()
                             scene walking2
                             with dissolve
                             "He was nearer to you,{w=0.3} being in the middle of the small line of 'Follow the Leader'."
                             "You checked up on him as he finished up an apple."
                             show sapnap shock at center, bounce
                             with dissolve
                             S "Oh!{w=0.3} [povname]."
                             show sapnap grin 2 at center, bounce
                             S "Yeah,{w=0.3} I'm all good now."
                             show sapnap wary at center, bounce
                             S "What about you?{w=0.3} Are you okay?"
                             hide sapnap wary with dissolve
                             "You nodded your head,{w=0.3} earning a smile from the brunet."
                             show sapnap neutral at center, shake
                             with dissolve
                             "He stretches his arms out wide,{w=0.3} the popping of his joints quite audible."
                             show sapnap grin 1 at center, bounce
                             S "That was quite terrifying,{w=0.3} huh?"
                             hide sapnap grin 1 with dissolve
                             menu:
                                 "No, it wasn't.":
                                     jump sapnapbad4
                                 "Yeah, it was.":
                                     jump sapnapplatonic4
                                 "I was scared for you.":
                                     jump sapnapromantic4

                             label sapnapromantic4:
                                 $ renpy.fix_rollback()
                                 show sapnap flushed 1 at center, bounce
                                 with dissolve
                                 "Sapnap was surprised to hear that."
                                 show sapnap flushed 1 at center, bounce
                                 S "Me?"
                                 show sapnap flushed 1 at center, bounce
                                 S "You were worried for me?"
                                 hide sapnap flushed 1 with dissolve
                                 "You nodded.{w=0.3} It was a terrible experience in your opinion,{w=0.3} as there were too many close calls."
                                 "You were glad that you were able to be of aid to him from time to time and keep him away from danger as much as you could."
                                 show sapnap flushed 1 at center, bounce
                                 with dissolve
                                 S ".{w=0.3}.{w=0.3}.{w=0.3}"
                                 show sapnap flushed 1 at center, bounce
                                 S "Oh."
                                 "He looks at you with a goofy grin."
                                 show sapnap grin 1 at center, bounce
                                 S "So you were {i}worried{/i} for me,{w=0.3} huh,{w=0.3} [povname]?"
                                 "He had that annoying and teasing tone as he leaned in close to your face.{w=0.3} Deeming him as {i}too close for comfort{/i},{w=0.3} you shove his face away."
                                 play sound "audio/fall.mp3" volume 0.3
                                 show sapnap flushed 2 at center, shake
                                 with dissolve
                                 play sound "audio/sapnap chuckle.mp3"
                                 "He lets out a hearty chuckle at your reaction."
                                 show sapnap flushed 2 at center, bounce
                                 S "You're {i}adorable{/i},{w=0.3} [povname]."
                                 show sapnap neutral at center, bounce
                                 S "I'm flattered for your concern.{w=0.3} Thank you."
                                 hide sapnap neutral with dissolve
                                 "You let out a huff,{w=0.3} but it wasn't out of annoyance.{w=0.3} You roll your eyes as you focused on the path you guys were taking."
                                 scene strongholdarea
                                 with dissolve
                                 $ sapnap_romantic += 10
                                 jump i

                             label sapnapplatonic4:
                                 $ renpy.fix_rollback()
                                 "You wouldn't want to admit that it {i}scared{/i} you,{w=0.3} per say.{w=0.3} But you had to agree that it {i}was{/i} too close for comfort."
                                 show sapnap neutral at center, bounce
                                 with dissolve
                                 "Sapnap gives you a smile."
                                 show sapnap flushed 2 at center, bounce
                                 S "I'm glad you had our back, [povname]."
                                 hide sapnap flushed 2 with dissolve
                                 "You grinned back at him,{w=0.3} feeling at ease that you could be of use to them."
                                 scene strongholdarea
                                 with dissolve
                                 $ sapnap_platonic += 10
                                 jump i

                             label sapnapbad4:
                                 $ renpy.fix_rollback()
                                 "It wasn't that hard nor scary.{w=0.3} You'd rather have something {i}way{/i} more challenging."
                                 show sapnap wary at center, bounce
                                 with dissolve
                                 "Sapnap looks at you,{w=0.3} befuddled."
                                 show sapnap wary at center, bounce
                                 S "Does nothing ever scare you?"
                                 "You simply shrugged."
                                 hide sapnap wary with dissolve
                                 "He scoffed at your reply."
                                 scene strongholdarea
                                 with dissolve
                                 $ sapnap_bad += 10
                                 jump i

                         label dream6:
                             $ renpy.fix_rollback()
                             scene walking2
                             with dissolve
                             "You sped up your pace to catch up to the front of the small line of 'Follow the Leader'."
                             show dream annoyed with dissolve
                             "Dream seemed to ignore your question at first."
                             hide dream annoyed with dissolve
                             "You repeated your question."
                             "Dream stopped for a moment to bring out another eye,{w=0.3} flinging it up to the sky."
                             show dream disappointed at center, shake
                             with dissolve
                             D ".{w=0.3}.{w=0.3}.{w=0.3}"
                             show dream wary with dissolve
                             D "Why didn't you listen to me earlier?"
                             hide dream wary with dissolve
                             "His eyebrows were furrowed in frustration as he caught the item,{w=0.3} resuming his long strides towards the new direction."
                             show dream serious with dissolve
                             D "I told you to follow the other two out of the Nether."
                             show dream wary at center, bounce
                             D "[povname],{w=0.3} you could've gotten {i}hurt.{/i}"
                             hide dream wary with dissolve
                             menu:
                                 "I wanted to help you.":
                                     jump dreamromantic4
                                 "I'm sorry I worried you.":
                                     jump dreamplatonic4
                                 "{color=#e60000}Well, {i}I'm{/i} sorry.{/color}" if bad_choices == True:
                                     jump dreambad4

                             label dreamromantic4:
                                 $ renpy.fix_rollback()
                                 show dream angry at center, shake
                                 with dissolve
                                 D "But you-"
                                 "Dream exclaims,{w=0.3} but he stops himself."
                                 show dream disappointed at center, shake
                                 "He closes his eyes and inhales deeply to try and calm himself down."
                                 hide dream disappointed with dissolve
                                 pause(1.0)
                                 show dream wary at center, bounce
                                 with dissolve
                                 "He locks his gaze with you after a short while."
                                 show dream disappointed at center, bounce
                                 play sound "audio/dream ugh.mp3"
                                 D "Sorry.{w=0.3} I didn't mean to sound so.{w=0.3}.{w=0.3}.{w=0.3}"
                                 show dream wary at center, bounce
                                 D "I know you can handle yourself.{w=0.3} I'm just.{w=0.3}.{w=0.3}.{w=0.3} worried out of my mind,{w=0.3} I guess."
                                 hide dream wary with dissolve
                                 "Dream had the other two to look after,{w=0.3} too.{w=0.3} You couldn't blame him for being paranoid for everyone;{w=0.3} especially since there was an additional member."
                                 "You apologized too,{w=0.3} for acting impulsively.{w=0.3} The both of you knew that you weren't exactly on the same level as everyone else was,{w=0.3} let alone {i}know{/i} you."
                                 show dream annoyed with dissolve
                                 D ".{w=0.3}.{w=0.3}.{w=0.3}"
                                 show dream wary at center, bounce
                                 D "I care about you, [povname]."
                                 hide dream wary with fastdissolve
                                 "You looked at him.{w=0.3} He didn't look back at you when he says this."
                                 "If you squinted,{w=0.3} you could've sworn that there was a dust of rosy pink on his cheeks,{w=0.3} but he started walking on a much faster pace leaving you to catch up to him."
                                 $ dream_romantic += 10
                                 jump dream6b

                             label dreamplatonic4:
                                 $ renpy.fix_rollback()
                                 show dream sigh at center, bounce
                                 with dissolve
                                 D ".{w=0.3}.{w=0.3}.{w=0.3}"
                                 show dream wary at center, bounce
                                 D "Just.{w=0.3}.{w=0.3}.{w=0.3} don't do that again,{w=0.3} okay?"
                                 hide dream wary with dissolve
                                 "You couldn't promise him that,{w=0.3} but you decided to nod your head to ease his nerves."
                                 show dream neutral at center, bounce
                                 with dissolve
                                 "He smiles at you in thanks."
                                 show dream grin 1 at center, bounce
                                 D "You did amazing under all that pressure,{w=0.3} by the way."
                                 hide dream grin 1 with dissolve
                                 "Surprised,{w=0.3} you stopped in your tracks as you thanked him."
                                 show dream grin 2 at center, bounce
                                 with dissolve
                                 "He lets out a laugh as you were rendered speechless."
                                 hide dream grin 2 with dissolve
                                 $ dream_platonic += 10
                                 jump dream6b

                             label dreambad4:
                                 $ renpy.fix_rollback()
                                 show dream disappointed at center, bounce
                                 with dissolve
                                 D "Unbelievable."
                                 hide dream disappointed with dissolve
                                 play sound "audio/dream ugh.mp3"
                                 "Dream scoffed,{w=0.3} shaking his head as he looked away from you.{w=0.3} He seemed upset by your response."
                                 $ dream_bad += 20
                                 jump dream6b


                             label dream6b:
                                 $ renpy.fix_rollback()
                                 "You stayed in place for a bit longer as you remembered what you had in your inventory.{w=0.3} You combined both of the Blaze Rods and Ender Pearls you had to create some more Ender Eyes."
                                 "You then began to run back up to Dream's side,{w=0.3} giving the key items over to him."
                                 scene strongholdarea
                                 with dissolve
                                 show dream neutral at center, bounce
                                 with dissolve
                                 "He nods at you in gratitude before flinging another one to check where you all need to go."
                                 hide dream neutral with dissolve
                                 "The eye then slowly sunk towards the ground,{w=0.3} through the grass block,{w=0.3} before bouncing back up to the surface."
                                 jump i

                     label i:
                         $ renpy.fix_rollback()
                         scene strongholdarea
                         "Everyone stopped walking when Dream halted in his tracks."
                         show dream shock at center, bounce
                         with dissolve
                         D "It's down here."
                         hide dream shock with dissolve
                         "He announces as he whipped out his pickaxe,{w=0.3} beginning to mine away through the ground."
                         "George and Sapnap had gone to do the same thing on either side of him,{w=0.3} so you decided to follow through and mimic their actions in front of the hole Dream made."
                         scene black
                         with wipeup
                         play sound "audio/dig5.mp3"
                         "You continued to dig deeper,{w=0.3} not even paying attention until you realized you've dug through the Stronghold's ceiling and fell through."
                         scene strongholdthreeway
                         with wipeupfast
                         play sound "audio/fall.mp3" volume 0.3
                         show strongholdthreeway with hpunch:
                             zoom 1.5
                         pause(1.0)
                         scene strongholdthreeway
                         with dissolve
                         DT "{i}[povname]!{/i}"
                         play sound "audio/water mlg.mp3"
                         "You dealt a bit of damage to yourself thanks to your clumsiness.{w=0.3} Dream had safely landed with a Water MLG and so did George,{w=0.3} although he let his water spread around for a bit for Sapnap to land safely in."
                         show george wary at center, bounce
                         with dissolve
                         G "You're gonna give us a heart attack,{w=0.3} [povname]!{w=0.3} Be careful next time!"
                         "You let out a sheepish chuckle as you pulled out an apple from your inventory and proceeded to munch on it to regen."
                         hide george wary with dissolve
                         "You all took a better look at which part of the Stronghold you guys were located in.{w=0.3} You all realized you were in the middle of it,{w=0.3} with three pathways."
                         "The End Portal,{w=0.3} the Library,{w=0.3} and a way to another hallway."
                         "Sapnap lets out a huff."
                         show sapnap shock at center, bounce
                         with dissolve
                         S "Huh.{w=0.3} Lucky."
                         hide sapnap shock with dissolve
                         "You patted off the remaining dirt off of your clothes as Dream began going towards the Portal Room,{w=0.3} getting rid of the Silverfish spawner before starting on filling in the gaps of the Portal itself."
                         show sapnap annoyed at right, bounce
                         with dissolve
                         show george serious at left, bounce
                         with dissolve
                         "Sapnap scratches his head before heading off to the empty hallway that lead to an iron door."
                         show sapnap wary at right, bounce
                         S "I'll go over here and check if there's any stuff I can grab before we enter."
                         hide sapnap wary with dissolve
                         show george neutral at left, bounce
                         G "Same.{w=0.3} I'll check over here."
                         hide george neutral with dissolve
                         "You were then left to your own devices yet again."
                         menu:
                             "Go with whom?"

                             "Go towards the Library":
                                 $ george_points += 2
                                 $ george_romantic += 5
                                 $ george_platonic += 5
                                 $ george_bad += 5
                                 jump george8
                             "Go down the hall":
                                 $ sapnap_points += 2
                                 $ sapnap_romantic += 5
                                 $ sapnap_platonic += 5
                                 $ sapnap_bad += 5
                                 jump sapnap8
                             "Fill in the Ender Portal" if persistent.trueroute == True:
                                 $ dream_points += 2
                                 $ dream_romantic += 5
                                 $ dream_platonic += 5
                                 $ dream_bad += 5
                                 jump dream7


                         label george8:
                             stop music fadeout 1.0
                             $ renpy.fix_rollback()
                             "You took the left path,{w=0.3} entering the Iron door and following the older male."
                             play sound "audio/walking.mp3"
                             scene black
                             with wipeleftfast
                             scene strongholdlibrary
                             with wipeleftfast
                             play music "audio/Twin Musicom - Rhodesia MkII.mp3" fadein 5.0 volume 0.5
                             "As you entered the room,{w=0.3} you were greeted by tall rows of bookshelves filled to the brim."
                             "Hearing the {i}clink!{/i} of the Iron door closing behind you,{w=0.3} George called out from the corner of the room."
                             G "I'm right here!"
                             scene strongholdlibrary with dissolve:
                                   xpos 0.8 ypos 0.8 xanchor 0.66 yanchor 0.77 zoom 2.0
                                   ease 2 yanchor 0.62
                             pause(1.0)
                             "You followed the sound of his voice,{w=0.3} leading you to him as he closed a chest.{w=0.3} He proceeded to sit on it."
                             show george grin 2 at center, bounce
                             with dissolve
                             G "Just a compass and a few blank pages;{w=0.3} nothing useful."
                             show george shock at center, bounce
                             "He mutters out a little 'Oh,{w=0.3} yeah.'{w=0.3} and proceeded to bring out his crafting table,{w=0.3} seemingly creating a bow along with some arrows."
                             hide george shock with dissolve
                             "A moment of silence had seeped into your conversation before he called out to you."
                             G "[povname]?"
                             scene georgecg5plat with dissolve:
                                   xpos 0.9 ypos 0.7 xanchor 0.66 yanchor 0.77 zoom 2.5
                                   ease 2 yanchor 0.62
                             pause(1.0)
                             "You look to him.{w=0.3} He seemed a bit nervous and flustered."
                             G "I figured that maybe this'll be the last time we'll be able to talk in a.{w=0.3}.{w=0.3}.{w=0.3} calmer matter,{w=0.3} let's say."
                             G "So,{w=0.3} Ijust want to admit something."
                             G "[povname],{w=0.3} I think you're.{w=0.3}.{w=0.3}.{w=0.3} {i}really{/i} amazing."
                             G "I hope I don't,{w=0.3} like,{w=0.3} overwhelm you or anything.{w=0.3} I just wanted to let you know that."
                             menu:
                                 "\"I like you too.\"":
                                     jump georgeromantic5
                                 "\"Thank you for the dono.\"":
                                     jump georgeplatonic5
                                 "\"You're... okay.\"":
                                     jump georgebad5

                             label georgeromantic5:
                                 $ renpy.fix_rollback()
                                 G "Oh!"
                                 scene georgecg5rom with dissolve:
                                        xpos 0.9 ypos 0.7 xanchor 0.66 yanchor 0.62 zoom 2.5
                                 pause(1.0)
                                 "He smiles sweetly at you."
                                 scene georgecg5rom
                                 $ mouse_parallax.set ((-20, -5, "l0"))
                                 $ showp ("georgecg5rom")
                                 with dissolve
                                 G ".{w=0.3}.{w=0.3}.{w=0.3}I'm glad the feelings are mutual."
                                 $ scenep ()
                                 with dissolve
                                 pause(1.0)
                                 scene strongholdlibrary
                                 with dissolve
                                 "You feel a slight blush rise to your cheeks as he affirmed your growing feelings towards him."
                                 $ george_romantic += 10
                                 jump george8b

                             label georgeplatonic5:
                                 $ renpy.fix_rollback()
                                 scene georgecg5plat
                                 $ mouse_parallax.set ((-20, -5, "l0"))
                                 $ showp ("georgecg5plat")
                                 with dissolve
                                 G "Pft.{w=0.3}.{w=0.3}.{w=0.3}!!"
                                 G "Oh my god-"
                                 "He throws his head back in laughter at your response."
                                 play sound "audio/george giggle.mp3"
                                 G "That's such a dumb joke.{w=0.3}.{w=0.3}.{w=0.3}!"
                                 $ scenep ()
                                 with dissolve
                                 "You both snickered at the reference you've made.{w=0.3} George looks at you properly."
                                 G "Yeah,{w=0.3} I'm really glad we're friends,{w=0.3} [povname]."
                                 scene strongholdlibrary
                                 with dissolve
                                 "You simply grinned at him.{w=0.3} He mirrors your expression."
                                 $ george_platonic += 10
                                 jump george8b

                             label georgebad5:
                                 $ renpy.fix_rollback()
                                 scene strongholdlibrary
                                 with dissolve
                                 show george sigh at center, bounce
                                 with dissolve
                                 "George sighs in relief."
                                 show george neutral at center, bounce
                                 G "I'm glad you aren't exactly.{w=0.3}.{w=0.3}.{w=0.3} annoyed with me or anything."
                                 $ george_bad += 10
                                 jump george8b


                         label george8b:
                             $ renpy.fix_rollback()
                             scene strongholdlibrary
                             "He hops off of the chest."
                             show george grin 1 at center, bounce
                             with dissolve
                             G "Let's head back?"
                             show george neutral at center, bounce
                             G "I'm pretty sure Sapnap's calmed his nerves and Dream's finished up the Portal by now."
                             "You nodded and followed his lead out of the chamber."
                             play sound "audio/walking.mp3"
                             scene black
                             with wipeleftfast
                             scene strongholdendportal2
                             with wipeleftfast
                             jump j


                         label sapnap8:
                             stop music fadeout 1.0
                             $ renpy.fix_rollback()
                             "You jogged over to Sapnap's side."
                             show sapnap grin 2 at center, bounce
                             with dissolve
                             "He shoots you a grin,{w=0.3} appreciating your company."
                             play sound "audio/walking.mp3"
                             scene black
                             with wipeleftfast
                             scene strongholdhallway
                             with wipeleftfast
                             play music "audio/Twin Musicom - Rhodesia MkII.mp3" fadein 5.0 volume 0.5
                             "You both walk down the empty corridor and find a chest in between a bunch of slabs."
                             show sapnap shock at center, bounce
                             with dissolve
                             S "!!"
                             show sapnap grin 1 at center, bounce
                             S "Bingo."
                             hide sapnap grin 1 with dissolve
                             "He opens up the chest excitedly to find a bunch of rails,{w=0.3} coal,{w=0.3} and 3 pieces of bread."
                             show sapnap sigh at center, bounce
                             with dissolve
                             "Sapnap stashed the bread before closing its lid and leaning onto the chest.{w=0.3} He seemed unsettled."
                             show sapnap wary at center, bounce
                             S "You think we can.{w=0.3}.{w=0.3}.{w=0.3} take a breather?{w=0.3} Stay here for a second?"
                             show sapnap annoyed at center, bounce
                             S "Everything's just {i}so{/i} overwhelming,{w=0.3} I need to catch myself for a bit."
                             hide sapnap annoyed with dissolve
                             "You nodded,{w=0.3} sitting on the slab next to the chest."
                             scene strongholdhallway with dissolve:
                                   xpos 0.8 ypos 0.8 xanchor 0.66 yanchor 0.77 zoom 2.0
                                   ease 2 yanchor 0.62
                             pause(1.0)
                             "You hear Sapnap heave a long sigh."
                             S "[povname]?"
                             "You turn to him,{w=0.3} his face unsure."
                             show sapnap wary at center, bounce
                             with dissolve
                             S "I hope you don't mind me,{w=0.3} like,{w=0.3} rambling?{w=0.3} Sort of?"
                             show sapnap disappointed at center, bounce
                             S "I don't normally.{w=0.3}.{w=0.3}.{w=0.3} I mean,{w=0.3} I could say I'm usually affectionate with my friends.{w=0.3} But,{w=0.3} that's off-topic-{w=0.3}{nw}"
                             "Sapnap inhales deeply before correcting himself."
                             hide sapnap disappointed with dissolve
                             scene sapnapcg5plat with dissolve:
                                   xpos 0.8 ypos 0.6 xanchor 0.66 yanchor 0.77 zoom 2.5
                                   ease 2 yanchor 0.62
                             pause(1.0)
                             S "What I mean is-{w=0.5}{nw}"
                             S "[povname],{w=0.3} I think you're {i}really{/i} cool.{w=0.3} I don't normally say these things out loud,{w=0.3} but I just thought I'd let you know."
                             menu:
                                 "\"I like you too.\"":
                                     jump sapnapromantic5
                                 "\"You're cool too, Sapnap.\"":
                                     jump sapnapplatonic5
                                 "\"Thanks... You too, I guess.\"":
                                     jump sapnapbad5

                             label sapnapromantic5:
                                 $ renpy.fix_rollback()
                                 "Sapnap looks at you with wide eyes,{w=0.3} his face flushed."
                                 S "Huh!"
                                 scene sapnapcg5rom with dissolve:
                                     xpos 0.8 ypos 0.6 xanchor 0.66 yanchor 0.62 zoom 2.5
                                 pause(1.0)
                                 "And then his face breaks out into a grin."
                                 scene sapnapcg5rom
                                 $ mouse_parallax.set ((-20, -5, "l0"))
                                 $ showp ("sapnapcg5rom")
                                 with dissolve
                                 S "That's cool.{w=0.3} That's really.{w=0.3}.{w=0.3}.{w=0.3} {i}really{/i} cool."
                                 $ scenep ()
                                 with dissolve
                                 pause(1.0)
                                 scene strongholdhallway
                                 with dissolve
                                 "It seems that he was rendered quite speechless,{w=0.3} as he was reduced to only a goofy smile on his face.{w=0.3} He stands up and gives you a hug."
                                 show strongholdhallway with hpunch
                                 "Surprised,{w=0.3} you slowly hugged him back.{w=0.3} After a bit,{w=0.3} you both pull away from each other."
                                 show sapnap flushed 2 at center, bounce
                                 with dissolve
                                 "Sapnap's face was flushed,{w=0.3} but his smile was still permanent."
                                 hide sapnap flushed 2 with dissolve
                                 $ sapnap_romantic += 10
                                 jump sapnap8b

                             label sapnapplatonic5:
                                 $ renpy.fix_rollback()
                                 scene sapnapcg5plat
                                 $ mouse_parallax.set ((-20, -5, "l0"))
                                 $ showp ("sapnapcg5plat")
                                 with dissolve
                                 "Sapnap lets out a soft giggle."
                                 S "I'm glad we're on the same page,{w=0.3} then."
                                 $ scenep ()
                                 with dissolve
                                 pause(1.0)
                                 scene strongholdhallway
                                 with dissolve
                                 scene strongholdhallway with hpunch
                                 "He reaches over and ruffles your hair playfully,{w=0.3} to which you swatted his hand at."
                                 show sapnap grin 2 at center, bounce
                                 with dissolve
                                 play sound "audio/sapnap chuckle.mp3"
                                 "He lets out a chuckle."
                                 hide sapnap grin 2 with dissolve
                                 $ sapnap_platonic += 10
                                 jump sapnap8b

                             label sapnapbad5:
                                 $ renpy.fix_rollback()
                                 scene strongholdhallway
                                 with dissolve
                                 "Sapnap leans away as he huffs out a breath."
                                 show sapnap disappointed at center, bounce
                                 with dissolve
                                 S "Yeah-{w=0.3} Let's just-{w=0.3}"
                                 show sapnap annoyed at center, bounce
                                 S "Let's pretend that went better."
                                 hide sapnap annoyed with dissolve
                                 $ sapnap_bad += 10
                                 jump sapnap8b


                         label sapnap8b:
                             $ renpy.fix_rollback()
                             scene strongholdhallway
                             "Sapnap then steps away and stretches his arms out."
                             show sapnap grin 1 at center, bounce
                             with dissolve
                             S "Let's head back,{w=0.3} yeah?"
                             show sapnap neutral at center, bounce
                             S "George is probably back from the Library by now,{w=0.3} and Dream's definitely done with filling up the Portal."
                             hide sapnap neutral with dissolve
                             "You agreed and followed him back towards the Portal Room."
                             play sound "audio/walking.mp3"
                             scene black
                             with wipeleftfast
                             scene strongholdendportal2
                             with wipeleftfast
                             jump j


                         label dream7:
                             stop music fadeout 1.0
                             $ renpy.fix_rollback()
                             "You follow the blonde through the Portal Room."
                             scene strongholdportalentrance
                             with dissolve
                             scene strongholdendportal1
                             with dissolve
                             play music "audio/Twin Musicom - With a Stamp.mp3" fadein 5.0 volume 0.5
                             show dream neutral at center, bounce
                             with dissolve
                             "He notices this and tosses you a few Ender Eyes before slowly (and carefully) completing one side of it."
                             hide dream neutral with dissolve
                             "As you steadily fill in the spaces with the spheres,{w=0.3} you hear him sigh."
                             "You looked up and see that he had placed both of his arms on the rim of the Portal."
                             show dream sigh at center, bounce
                             with dissolve
                             D "This has been.{w=0.3}.{w=0.3}.{w=0.3} {i}so{/i} crazy."
                             hide dream sigh with dissolve
                             "You gave him a weary smile.{w=0.3} It was understandable;{w=0.3} you all literally spent only one night taking a breather.{w=0.3} Everything else happened in a span of hours,{w=0.3} events happening one right after the other."
                             show dream neutral at center, bounce
                             with dissolve
                             "Dream looks at you before shaking his head,{w=0.3} your smile being infectious."
                             show dream neutral at center, bounce
                             D "Yet,{w=0.3} through all this,{w=0.3} you're still able to push through and smile like that."
                             show dream grin 2 at center, bounce
                             D "How do you do it?"
                             hide dream grin 2 with dissolve
                             "Stunned by the sudden deep question,{w=0.3} you opted to stay silent and continue to fill in more of the holes."
                             scene strongholdendportal2
                             with fastdissolve
                             "All the eyes were then placed properly and resulted with the Portal's vortex appearing with a loud thrum."
                             D "[povname]."
                             "You looked up and met his gaze."
                             scene dreamcg5plat with dissolve:
                                   xpos 0.8 ypos 0.5 xanchor 0.66 yanchor 0.77 zoom 2.5
                                   ease 2 yanchor 0.62
                             pause(1.0)
                             D "You're {i}incredible{/i}."
                             D "And I {i}genuinely{/i} mean it."
                             "He says this as a soft smile stays on his face.{w=0.3} He doesn't look away from you."
                             menu:
                                 "\"I like you too.\"":
                                     jump dreamromantic5
                                 "\"And you're great, too.\"":
                                     jump dreamplatonic5
                                 "{color=#e60000}\"Yeah, thanks.\"{/color}" if bad_choices == True:
                                     jump dreambad5

                             label dreamromantic5:
                                 $ renpy.fix_rollback()
                                 scene dreamcg5rom with dissolve:
                                     xpos 0.8 ypos 0.5 xanchor 0.66 yanchor 0.62 zoom 2.5
                                 pause(1.0)
                                 "Dream's smile grows as he hears the words come out of your mouth."
                                 scene dreamcg5rom
                                 $ mouse_parallax.set ((-20, -5, "l0"))
                                 $ showp ("dreamcg5rom")
                                 with dissolve
                                 "With how much affection had dripped from his voice,{w=0.3} and how flushed his face seemed to be,{w=0.3} it confirms that your feelings are reciprocated."
                                 D "I'm glad to have met you,{w=0.3} [povname].{w=0.3} Really."
                                 "You let out a pleased huff,{w=0.3} letting him know that you thought the same as well."
                                 $ scenep()
                                 with dissolve
                                 D "I swear to you,{w=0.3} once we get out of here,{w=0.3} we'll work things out."
                                 D "We'll plan things."
                                 D "I promise."
                                 scene strongholdendportal2
                                 with dissolve
                                 "You nodded,{w=0.3} placing your full trust in him."
                                 "It was exhilarating to have your feelings out like that,{w=0.3} and to have it reciprocated too."
                                 "You grinned a bit to yourself,{w=0.3} your heart beating happily."
                                 $ dream_romantic += 10
                                 jump dream7b

                             label dreamplatonic5:
                                 $ renpy.fix_rollback()
                                 scene dreamcg5plat
                                 $ mouse_parallax.set ((-20, -5, "l0"))
                                 $ showp ("dreamcg5plat")
                                 with dissolve
                                 "Dream's smile grows wide,{w=0.3} causing his eyes to close.{w=0.3} He seemed to be calmer than before."
                                 $ scenep()
                                 with dissolve
                                 D "I'm grateful for you,{w=0.3} [povname]."
                                 scene strongholdendportal2
                                 with dissolve
                                 "You let him know of your own gratitude as well,{w=0.3} receiving a hearty chuckle from the blonde."
                                 $ dream_platonic += 10
                                 jump dream7b

                             label dreambad5:
                                 $ renpy.fix_rollback()
                                 scene strongholdendportal2
                                 with dissolve
                                 show dream grin 2 at center, bounce
                                 with dissolve
                                 "Dream's smile fumbles a bit,{w=0.3} but it still stays.{w=0.3} He seemed to struggle to maintan the expression on his face,{w=0.3} though."
                                 hide dream grin 2 with dissolve
                                 $ dream_bad += 20
                                 jump dream7b


                         label dream7b:
                             $ renpy.fix_rollback()
                             scene strongholdendportal2
                             "You both stepped away from the Portal as you heard footsteps from the hall outside."
                             jump j


                         label j:
                             stop music fadeout 1.0
                             scene strongholdendportal2
                             "As everyone started to regroup,{w=0.3} the quiet humming of the finished End Portal echoes out."
                             "Nervously,{w=0.3} Sapnap speaks."
                             show sapnap wary at center, bounce
                             with dissolve
                             S "Uh,{w=0.3} any encouraging words before we hop in?"
                             hide sapnap way with dissolve
                             menu:
                                 "Turn to George":
                                     $ george_points += 2
                                     $ george_romantic += 10
                                     $ george_platonic += 10
                                     $ george_bad += 10
                                     jump george9

                                 "Turn to Dream" if persistent.trueroute == True:
                                     $ dream_points += 2
                                     $ dream_romantic += 10
                                     $ dream_platonic += 10
                                     $ dream_bad += 10
                                     jump dream8

                                 "Turn to Sapnap":
                                     $ sapnap_points += 2
                                     $ sapnap_romantic += 10
                                     $ sapnap_platonic += 10
                                     $ sapnap_bad += 10
                                     jump sapnap9


                             label george9:
                                 $ renpy.fix_rollback()
                                 show george embarrassed at center, bounce
                                 with dissolve
                                 "When George meets your gaze,{w=0.3} his face was slightly tinted pink."
                                 show george embarrassed at center, bounce
                                 G "M-me?{w=0.3} You want me to.{w=0.3}.{w=0.3}.{w=0.3}"
                                 hide george embarrassed with dissolve
                                 "All three of you had simply encouraged him with smiles on your faces."
                                 show george sigh at center, bounce
                                 with dissolve
                                 "George sighs,{w=0.3} shaking his head a bit before looking back at you all with a smile of his own."
                                 show george neutral at center, bounce
                                 G "Alright then."
                                 show george wary at center, bounce
                                 G "I know most of this was my fault,"
                                 show george sigh at center, bounce
                                 G "but there's no time to dwell on that now."
                                 show george grin 1 at center, bounce
                                 G "What matters is that we're close to what's probably the solution,{w=0.3} and that we'll all be able to escape this realm and return back home."
                                 hide george grin 1 with dissolve
                                 jump k


                             label sapnap9:
                                 $ renpy.fix_rollback()
                                 show sapnap shock at center, bounce
                                 with dissolve
                                 "When you met gazes,{w=0.3} Sapnap dumbly points at himself."
                                 show sapnap shock at center, bounce
                                 S "Me?"
                                 "You laughed at him as the other two had simply nodded."
                                 show sapnap grin 2 at center, bounce
                                 play sound "audio/sapnap chuckle.mp3"
                                 "Sapnap laughs along for a bit as he cheekily scratches the back of his head."
                                 show sapnap annoyed at center, bounce
                                 S "Well,{w=0.3} uhm.{w=0.3}.{w=0.3}.{w=0.3}"
                                 show sapnap neutral at center, bounce
                                 S "We don't know how things will go in the End,{w=0.3} but I sure hope that we'll all make it back."
                                 show sapnap grin 2 at center, bounce
                                 S "Actually,{w=0.3} no,{w=0.3} I'm {i}sure{/i} we'll make it back!"
                                 hide sapnap grin 2 with dissolve
                                 jump k


                             label dream8:
                                 $ renpy.fix_rollback()
                                 show dream sigh at center, bounce
                                 with dissolve
                                 "When you locked gazes with Dream,{w=0.3} he huffs as if he knew it was coming."
                                 show dream neutral at center, bounce
                                 "With confidence,{w=0.3} Dream began to speak up."
                                 show dream grin 1 at center, bounce
                                 D "Alright,{w=0.3} alright."
                                 show dream grin 2 at center, bounce
                                 D "We've gone through this before.{w=0.3} Countless times,{w=0.3} actually."
                                 "Dream glances at the other two,{w=0.3} grinning,{w=0.3} before reducing back to a calming smile as his gaze lands on you."
                                 show dream neutral at center, bounce
                                 D "And I trust you to be able to keep up,{w=0.3} yeah?"
                                 "You nodded,{w=0.3} giving off a determinded vibe."
                                 hide dream neutral with dissolve
                                 jump k


                         label k:
                             $ renpy.fix_rollback()
                             "Everyone had given each other affirming glances,{w=0.3} reassuring one another that they're ready before staring down towards the black vortex."
                             scene strongholdendportal2 with dissolve:
                                   xpos 0.8 ypos 0.7 xanchor 0.66 yanchor 0.77 zoom 2.0
                                   ease 2 yanchor 0.62
                             pause(1.0)
                             "You gripped on the axe and shield you were wielding,{w=0.3} your nerves making you feel all jittery."
                             G ".{w=0.3}.{w=0.3}.{w=0.3}"
                             G "On three?"
                             "Sapnap shakily breathes."
                             S ".{w=0.3}.{w=0.3}.{w=0.3}One."
                             G "Two."
                             "And everyone began to run up."
                             D "{i}Three!{/i}"
                             play sound "audio/nether.mp3" volume 0.2
                             scene black
                             with wipeupfast
                             scene end
                             with wipeupfast
                             play music "audio/Twin Musicom - Fall of the Solar King.mp3" fadein 5.0 volume 0.5
                             "You braced yourself as the discomfort of teleporting began to set in."
                             play sound "audio/fall.mp3" volume 0.3
                             show end with hpunch:
                                 zoom 1.5
                             "You covered your mouth as you landed onto the Obsidian platform,{w=0.3} trying to get ahold of yourself."
                             scene end
                             with dissolve
                             show george pained 2 with dissolve
                             "George shakes his head as he checks on everyone right after landing."
                             show george wary at center, bounce
                             G "[povname]!{w=0.3} Are you okay?"
                             "You waved him off,{w=0.3} coughing as you do so."
                             hide george wary with dissolve
                             "It doesn't particularly convince him,{w=0.3} but he trusts you enough to regain your balance yourself."
                             show dream serious at left, bounce
                             show sapnap serious at right, bounce
                             with dissolve
                             "Dream and Sapnap seemed to have gotten used to the feeling of teleporting as they appeared fine."
                             hide dream serious
                             hide sapnap serious
                             with dissolve
                             "You struggled to get back on your feet as they began to build their way towards the center of the island where the dragon was situated."
                             show end with hpunch
                             "You got yourself on your feet and caught up to them."
                             scene end1
                             with fastdissolve
                             show george angry at left, bounce
                             with dissolve
                             G "Go ahead and push towards the dragon!{w=0.3} I'll take care of the Ender Crystals!"
                             show sapnap grin 1 at right, bounce
                             with dissolve
                             S "Make every shot count,{w=0.3} George!"
                             show george grin 2 at left, bounce
                             G "Of course!"
                             hide sapnap grin 1
                             hide george grin 2
                             with dissolve
                             "He runs off to the sides as he already begun aiming at the top of the pillars."
                             show dream serious at center, bounce
                             with dissolve
                             "Dream turns to you."
                             show dream serious at center, bounce
                             D "Me and Sapnap will go ahead land attacks on the Ender Dragon."
                             show dream serious at center, bounce
                             D "You steer clear from her,{w=0.3} alright?{w=0.3} Kill some Endermen and grab the pearls they drop so that you can filter them to us or use them for yourself if you have to flee."
                             hide dream serious with dissolve
                             "You obliged,{w=0.3} staying in the outer ring of the island as the two childhood friends rushed towards the middle."
                             scene endenderman
                             with fastdissolve
                             "You dared to make eye contact with the tall,{w=0.3} void-like mobs to aggravate them."
                             play sound "audio/enderman aggro.mp3"
                             pause(1.0)
                             play sound "audio/shield.mp3"
                             "It proved effective as they began to open their mouths,{w=0.3} their irritating buzzing getting louder as they launch themselves at your shield."
                             "You shoved them away and attempted to land hits on them whilst taking caution of any of their attacks that manage to get too near to you."
                             scene endenderman with dissolve:
                                   xpos 1.2 ypos 0.7 xanchor 0.66 yanchor 0.77 zoom 2.0
                                   ease 2 yanchor 0.62
                             pause(1.0)
                             "After taking at least two hits from the mob,{w=0.3} you counted the amount of Ender Pearls you've gained whilst eating some bread to regenerate your health."
                             scene endenderman with dissolve
                             scene end1
                             with fastdissolve
                             "Seeing that you've gotten quite alot,{w=0.3} you quickly jumped into the middle to throw some to Dream and Sapnap."
                             show sapnap grin 2 at center, bounce
                             with dissolve
                             S "Thanks,{w=0.3} [povname]!"
                             hide sapnap grin 2 with dissolve
                             play sound "audio/water mlg.mp3"
                             "Sapnap manages to catch all of it,{w=0.3} tossing the other half towards the blonde who had just landed his Water MLG."
                             scene end1 with dissolve:
                                    xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                                    ease 2 yanchor 0.62
                             pause(1.0)
                             "After a few more minutes of combat,{w=0.3} it seemed that the Ender Dragon's health had depleted until halfway.{w=0.3} George had done his job of shooting all the healing crystals."
                             scene end1
                             with dissolve
                             "You were busy looking around for the older male when the dragon had launched a fireball near you."
                             show end1 with hpunch
                             "You had only heard a soft thudding sound,{w=0.3} and before you knew it,{w=0.3} you were surrounded by purple particles that began to burn you."
                             play sound "audio/fall.mp3"
                             show tverror5:
                                 alpha 0.5
                             with fastdissolve
                             pause(0.2)
                             hide tverror5 with fastdissolve
                             show dream angry at center, bounce
                             with dissolve
                             D "[povname]!"
                             show dream angry at center, bounce
                             D "Use an Ender Pearl!{w=0.3} Get out of there!"
                             hide dream angry with dissolve
                             "You fumble over the items in your inventory,{w=0.3} finally stumbling over the sphere-like object,{w=0.3} and throwing it away to somewhere safer."
                             scene end1 with dissolve:
                                 xpos 0.7 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 3.0
                                 ease 2 yanchor 0.62
                             pause(1.0)
                             "Your breath was shaky and in short puffs as you teleported.{w=0.3} You looked up to your health bar to see you had two and a half hearts left."
                             S "[povname],{w=0.3} are you okay?!"
                             "You wanted to reassure them that you're fine,{w=0.3} even a wave of your hand,{w=0.3} but the required effort to do as such was too much for you and ended up making you feel a lot more lightheaded."
                             D "George,{w=0.3} we need you!"
                             show george wary with dissolve
                             "Being the nearest one to you,{w=0.3} George glances back to you worriedly."
                             "You shook your head in an attempt to tell him to go help the others."
                             show george serious with dissolve
                             "George furrowed his eyebrows together before turning away and ran towards the middle."
                             scene end1
                             with fastdissolve
                             show george angry at center, bounce
                             with dissolve
                             G "I'm right here!"
                             show dream angry at left, bounce
                             with dissolve
                             D "We need your help in keeping the dragon away from [povname]!"
                             show george angry at center, bounce
                             G "Got it!"
                             hide george angry
                             hide dream angry
                             with dissolve
                             "Right.{w=0.3} Dream was the sole person out of everyone in your group to have experienced being on half a heart,{w=0.3} and you were close."
                             "To say it hurt was sugar-coating it.{w=0.3} You felt excruciating pain as your heart tried to make up for the blood that you've lost from the recent situation."
                             "As you breathed heavily,{w=0.3} you fiddled around for the Golden Apple that had stayed in your inventory the entire time."
                             "The last time you glanced at the dragon's health bar,{w=0.3} it was nearly finished.{w=0.3} Just a few critical hits and it would be over."
                             show gapple at center, bounce
                             with dissolve
                             "You sighed as you took your time,{w=0.3} finally being able to fish it out from all of your belongings."
                             hide gapple with dissolve
                             play sound "audio/enderdragon roar 2.mp3"
                             scene enddragon
                             with hpunch
                             "You were about to eat it when you heard a bellowing noise from above-{w=0.3} the Ender Dragon was coming right at you."
                             show dream angry at center, bounce
                             show george angry at left, bounce
                             show sapnap angry at right, bounce
                             with dissolve
                             DT "{i}[povname]!{/i}"
                             hide dream angry
                             hide george angry
                             hide sapnap angry
                             with dissolve
                             "You froze up and shut your eyes tight as you braced yourself for what was about to happen."
                             stop music fadeout 1.0
                             scene black
                             with wipedownfast
                             jump routecount

     label routecount:
         if george_points > max(sapnap_points, dream_points):
             jump georgeendings

         elif sapnap_points > max(george_points, dream_points):
              jump sapnapendings

         elif dream_points > max(george_points, sapnap_points):
              jump dreamendings


         label georgeendings:
             if george_romantic > max(george_platonic, george_bad):
                 jump georgeromanticending
             elif george_platonic > max(george_romantic, george_bad):
                 jump georgeplatonicending
             elif george_bad > max(george_romantic, george_platonic):
                 jump georgebadending


                 label georgeromanticending:
                     $ persistent.seen_ending_1 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     play music "audio/bensound-adventure.mp3" fadein 5.0 volume 0.5
                     scene georgecggood1 with dissolve:
                         xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                     pause(2.0)
                     scene georgecggood1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("georgecggood1")
                     with dissolve
                     "George,{w=0.3} who had his bow up,{w=0.3} and fired his last arrow at the dragon that had been only one hit away."
                     play sound "audio/enderdragon death.mp3"
                     "The dragon screeches as it levitates up,{w=0.3} light protruding its body as it slowly disintegrates into specks of particles and EXP points."
                     $ scenep ()
                     with dissolve
                     "And right then,{w=0.3} a sound effect echoes about from George himself."
                     play sound "audio/exp.mp3"
                     "{i}GeorgeNotFound has made the advancement {color=#55FF55}(Free the end){/color}"
                     scene endexitportal1
                     with slowdissolve
                     "Everything was silent,{w=0.3} before all three of them began to whoop loudly."
                     show dream grin 1 at left, bounce
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     D "Oh my God,{w=0.3} George,{w=0.3} you did it!"
                     show sapnap grin 2 at right, bounce
                     S "YEEEEAAAH!{w=0.3} THAT'S OUR BOY!!"
                     hide dream grin 1
                     hide sapnap grin 2
                     with dissolve
                     "George was then lifted into the air by the two,{w=0.3} the male himself laughing loudly as they all cheered."
                     scene endexitportal1 with dissolve:
                         xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                         ease 2 yanchor 0.62
                     pause(2.0)
                     "After a whole while of being stunned,{w=0.3} you let out your share of giggles."
                     show george shock at center, bounce
                     show sapnap shock at right, bounce
                     show dream shock at left, bounce
                     with dissolve
                     "The boys turned around as they heard you laugh."
                     pause(0.5)
                     show dream grin 1 at left, bounce
                     show sapnap grin 1 at right, bounce
                     pause(1.0)
                     show dream grin 2 at left, bounce
                     show sapnap grin 2 at right, bounce
                     "The two childhood friends had glanced at each other with a glint of mischief in their eyes,{w=0.3} before running towards you with George still on their shoulders."
                     show george wary at center, bounce
                     G "Woah,{w=0.3} guys!{w=0.3} Let me down!"
                     scene endexitportal1
                     with dissolve
                     "The two had simply laughed at him before letting him get off as they stopped right in front of you."
                     show dream neutral with dissolve
                     "Dream helped you up to your feet,{w=0.3} giving you the Golden Apple you dropped to heal up."
                     hide dream neutral with dissolve
                     "You nodded at him in thanks,{w=0.3} feeling a whole lot better as you took a bite out of it,{w=0.3} and turned to see Sapnap pushing a blushing George towards you."
                     show george annoyed with dissolve
                     show george shock at center, bounce
                     "When he was right in front of you,{w=0.3} you had simply thanked him for being brave and saving your life."
                     show george grin 2 blush at center, bounce
                     G "I'm.{w=0.3}.{w=0.3}.{w=0.3} really glad you're okay,{w=0.3} [povname]."
                     "He wasn't one who can easily convey his emotions through words,{w=0.3} you figured."
                     "You gave out a soft laugh as you cupped his cheek,{w=0.3} letting him have a bite of your Golden Apple."
                     show george shock at center, bounce
                     G "O-{w=0.3}Oh!"
                     show george grin 2 blush at center, bounce
                     G "Thanks,{w=0.3} [povname]."
                     show dream grin 2 at left, bounce
                     with dissolve
                     "Dream laughed at the exchange,{w=0.3} his hands on his stomach as he cackled."
                     show george annoyed at center, bounce
                     "George sent him a glare,{w=0.3} going to the point of even rolling his eyes at the male's reaction towards you two."
                     show dream grin 1 at left, bounce
                     D "Alright,{w=0.3} you two are cute,{w=0.3} we get it."
                     show dream neutral at left, bounce
                     D "Come on,{w=0.3} let's go home."
                     hide george annoyed
                     hide dream neutral
                     with dissolve
                     "You nodded,{w=0.3} and all four of you had walked up to the middle."
                     show dream grin 2 at left, bounce
                     show sapnap grin 2 at right, bounce
                     with dissolve
                     "Dream and Sapnap had hugged each other sideways as they made their way to the portal,{w=0.3} their antics making you stifle a small giggle."
                     scene endexitportal2
                     with dissolve
                     "You hoped that once you all jump in,{w=0.3} you will all: 1. Be able to come back home safely,{w=0.3} and 2. Remember everything that had happened."
                     "You were so nervous,{w=0.3} but this was so far your only choice:{w=0.3} to jump into the unknown."
                     show endexitportal2 with vpunch:
                         zoom 1.5
                     "You felt someone grab ahold of your hand."
                     scene endexitportal2
                     with dissolve
                     show george neutral with dissolve
                     "Your gaze trailed from the portal to see that it was George himself."
                     show george grin 2 blush at center, bounce
                     "He had a soft,{w=0.3} reassuring smile on his face as he squeezed your hand."
                     hide george grin 2 blush with dissolve
                     "You were sure that he was nervous,{w=0.3} too."
                     show dream grin 1 with dissolve
                     D "On three?"
                     hide dream grin 1 with dissolve
                     "Everyone grinned at him."
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     S "One!"
                     show dream grin 2 at left, bounce
                     with dissolve
                     D "Two!"
                     hide dream grin 2
                     hide sapnap grin 1
                     with dissolve
                     show george grin 2 at center, bounce
                     with dissolve
                     YG "{i}Three!!{/i}"
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                         zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}GeorgeNotFound went live: Fixing my chair.{/i}"
                     "GeorgeNotFound.{w=0.3} {i}George{/i}."
                     "Minecraft.{w=0.3} The realm."
                     "You quickly pressed on the notification,{w=0.3} the stream's audio booming out of your phone's speakers."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     G "Sorry,{w=0.3} guys!"
                     G "I know we were supposed to be doing a Minecraft Challenge right now,{w=0.3} but our connections did some sort of blip,{w=0.3} and now my chair is wrecked."
                     "The chat roars in laughter,{w=0.3} finding it hilarious that he had fallen off of his chair to the point of breaking it."
                     G "Wow,{w=0.3} chat.{w=0.3} You guys aren't feeling nice tonight,{w=0.3} huh."
                     "Your heart beat rising,{w=0.3} you impulsively sent a dono to try and catch his attention."
                     "He stops holding the pieces that belonged to his chair to check the donation."
                     G "Okay,{w=0.3} who just dono'ed 'Thank you for the dono'?{w=0.3} You think you're soooo funny, huh-{w=0.3}{nw}"
                     "George stopped himself when he had read your username."
                     G "[povname].{w=0.3}.{w=0.3}.{w=0.3}?"
                     G "Hold on,{w=0.3} DM me on Twitter.{w=0.3} Do you have the same user?"
                     "You had to be quick-{w=0.3} You knew how fast people can be at taking names and usernames and impersonating people."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     "You immediately transfer to Twitter,{w=0.3} the stream turning into a picture-in-picture form and situating itself at the bottom corner of your phone,{w=0.3} and sent him a message."
                     pov "{i}George!{/i}"
                     pov "{i}It's me.{w=0.3} Do you remember everything?{/i}"
                     pov "{i}The Minecraft realm,{w=0.3} the Library,{w=0.3} the Golden Apple?{/i}"
                     "Your heartrate picks up as you anxiously wait for a response.{w=0.3} You hope you were quick enough."
                     "You heard his quick typing noises from his stream as the chat zoomed by with your name combined with a bunch of question marks,{w=0.3} asking who you were."
                     $ scenep ()
                     with dissolve
                     "And then,{w=0.3} suddenly,{w=0.3} someone joined the call."
                     play sound "audio/teamspeak.mp3"
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     G "Dream!"
                     D "George-{w=0.3} What the hell are you doing?!"
                     G "It's [povname]!"
                     D "What do you mean it's [povname]-"
                     D "Mute your mic on stream,{w=0.3} you idiot!-{w=0.3}{nw}"
                     "The audio from both Dream and George's mic have been silenced."
                     "And then suddenly,{w=0.3} you have a notification beep from Twitter."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     G "{i}[povname]!{//i}"
                     G "{i}of course I remember. :]{/i}"
                     G "{i}Dream's helping me book a flight for you right now.{w=0.3} would next next week be okay?{/i}"
                     "You flushed.{w=0.3} Already?"
                     "But it wasn't as if you didn't want to be by his side-{w=0.3} You already missed being next to him."
                     "The next message came in,{w=0.3} and it was like you both had a connected braincell."
                     G "{i}wait{/i}"
                     G "{i}oh my god{/i}"
                     G "{i}waitwaitwait{/i}"
                     G "{i}was that too quick???????{/i}"
                     G "{i}oh my god im so sorry{/i}"
                     pov "{i}george!!{w=0.3} it's okay.{/i}"
                     pov "{i}i'm free,{w=0.3} so it's okay.{/i}"
                     pov "{i}:]{/i}"
                     pause(1.0)
                     G "{i}.{w=0.3}.{w=0.3}.{w=0.3}{/i}"
                     G "{i}is this real{/i}"
                     G "{i}oh my god{/i}"
                     G "{i}wait please dont look at my stream for like 5 seconds{/i}"
                     $ scenep ()
                     with dissolve
                     scene cg1
                     with dissolve
                     "Huh.{w=0.3} Curiously,{w=0.3} you peeked at the stream window on the bottom corner."
                     scene georgegoodendrom with dissolve:
                          xpos 0.9 ypos 0.3 xanchor 0.66 yanchor 0.77 zoom 3.3
                          ease 2 yanchor 0.62
                     pause(1.0)
                     "George was jumping around in happiness,{w=0.3} arms in the air,{w=0.3} before returning back to the mic seemingly telling the other male of your decision."
                     scene georgegoodendrom
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("georgegoodendrom")
                     with dissolve
                     "You laughed to yourself,{w=0.3} your cheeks hurting from how much you were smiling that entire time."
                     $ scenep ()
                     with dissolve
                     "You couldn't wait to see him again."
                     scene georgegoodendrom
                     pause(1.0)
                     stop music fadeout 1.0
                     scene georgeromanticend
                     with fade
                     pause(3.0)
                     jump endingcount



                 label georgeplatonicending:
                     $ persistent.seen_ending_2 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     play music "audio/bensound-adventure.mp3" fadein 5.0 volume 0.5
                     scene georgecggood1 with dissolve:
                         xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                     pause(2.0)
                     scene georgecggood1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("georgecggood1")
                     with dissolve
                     "George,{w=0.3} who had his bow up,{w=0.3} and fired his last arrow at the dragon that had been only one hit away."
                     play sound "audio/enderdragon death.mp3"
                     "The dragon screeches as it levitates up,{w=0.3} light protruding its body as it slowly disintegrates into specks of particles and EXP points."
                     $ scenep ()
                     with dissolve
                     "And right then,{w=0.3} a sound effect echoes about from George himself."
                     play sound "audio/exp.mp3"
                     "{i}GeorgeNotFound has made the advancement {color=#55FF55}(Free the end){/color}"
                     scene endexitportal1
                     with slowdissolve
                     "Everything was silent,{w=0.3} before all three of them began to whoop loudly."
                     show dream grin 1 at left, bounce
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     D "Oh my God,{w=0.3} George,{w=0.3} you did it!"
                     show sapnap grin 2 at right, bounce
                     S "YEEEEAAAH!{w=0.3} THAT'S OUR BOY!!"
                     hide dream grin 1
                     hide sapnap grin 2
                     with dissolve
                     "George was then lifted into the air by the two,{w=0.3} the male himself laughing loudly as they all cheered."
                     scene endexitportal1 with dissolve:
                         xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                         ease 2 yanchor 0.62
                     pause(2.0)
                     "After a whole while of being stunned,{w=0.3} you let out your share of giggles."
                     show george shock at center, bounce
                     show sapnap shock at right, bounce
                     show dream shock at left, bounce
                     with dissolve
                     "The boys turned around as they heard you laugh."
                     pause(0.5)
                     show dream neutral at left, bounce
                     show sapnap neutral at right, bounce
                     show george neutral at center, bounce
                     "Their faces softened as they lowered the older male down,{w=0.3} approaching you."
                     hide dream neutral
                     hide sapnap neutral
                     hide george neutral
                     with dissolve
                     "Dream and Sapnap helped you up to your feet,{w=0.3} and George passes you the Golden Apple you dropped."
                     show george grin 1 with dissolve
                     G "Be careful with your things next time,{w=0.3} okay,{w=0.3} [povname]?"
                     "He smiles at you as you nodded,{w=0.3} your face flushing at your clumsiness last minute that had caused you to be endangered in the first place."
                     show george grin 2 with dissolve
                     "You mutter a small thanks whilst proceeding to nibble at the fruit,{w=0.3} to which his smile grew sweeter at."
                     hide george grin 2 with dissolve
                     show dream grin 1 at left, bounce
                     with dissolve
                     D "Alright,{w=0.3} let's go home,{w=0.3} guys."
                     show sapnap grin 2 at right, bounce
                     with dissolve
                     show dream grin 2 at left, bounce
                     "Dream hollers out.{w=0.3} Sapnap approaches him,{w=0.3} slinging his arm around him in some weird side hug.{w=0.3} They both laughed as they made their way towards the middle."
                     hide sapnap grin 2
                     hide dream grin 2
                     with dissolve
                     "You,{w=0.3} on the other hand,{w=0.3} had taken slow strides beside George."
                     show george shock with dissolve
                     "He seemed to have noticed that you felt nervous."
                     show george neutral at center, bounce
                     G "Hey."
                     show george neutral at center, bounce
                     G "It'll be okay.{w=0.3} We'll be back home once we enter the portal."
                     "His tone was soft,{w=0.3} comforting.{w=0.3} You were thankful for him understanding your feelings as you both made your way to the portal."
                     hide george neutral with dissolve
                     scene endexitportal2
                     with dissolve
                     "You all stared down at the black,{w=0.3} swirling vortex;{w=0.3} with particles swirling around mixing with hints of teal."
                     show dream grin 1 with dissolve
                     D "On three?"
                     hide dream grin 1 with dissolve
                     "Everyone grinned at him."
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     S "One!"
                     show dream grin 2 at left, bounce
                     with dissolve
                     D "Two!"
                     hide dream grin 2
                     hide sapnap grin 1
                     with dissolve
                     show george grin 2 at center, bounce
                     with dissolve
                     YG "{i}Three!!{/i}"
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                         zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}GeorgeNotFound went live: Fixing my chair.{/i}"
                     "GeorgeNotFound.{w=0.3} {i}George{/i}."
                     "Minecraft.{w=0.3} The realm."
                     "You quickly pressed on the notification,{w=0.3} the stream's audio booming out of your phone's speakers."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     G "Sorry,{w=0.3} guys!"
                     G "I know we were supposed to be doing a Minecraft Challenge right now,{w=0.3} but our connections did some sort of blip,{w=0.3} and now my chair is wrecked."
                     "The chat roars in laughter,{w=0.3} finding it hilarious that he had fallen off of his chair to the point of breaking it."
                     G "Wow,{w=0.3} chat.{w=0.3} You guys aren't feeling nice tonight,{w=0.3} huh."
                     "Your heart beat rising,{w=0.3} you impulsively sent a dono to try and catch his attention."
                     "He stops holding the pieces that belonged to his chair to check the donation."
                     G "Okay,{w=0.3} who just dono'ed 'Thank you for the dono'?{w=0.3} You think you're soooo funny, huh-{w=0.3}{nw}"
                     "George stopped himself when he had read your username."
                     G "[povname].{w=0.3}.{w=0.3}.{w=0.3}?"
                     G "Hold on,{w=0.3} DM me on Twitter.{w=0.3} Do you have the same user?"
                     "You had to be quick-{w=0.3} You knew how fast people can be at taking names and usernames and impersonating people."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     "You immediately transfer to Twitter,{w=0.3} the stream turning into a picture-in-picture form and situating itself at the bottom corner of your phone,{w=0.3} and sent him a message."
                     pov "{i}George!{/i}"
                     pov "{i}It's me.{w=0.3} Do you remember everything?{/i}"
                     pov "{i}The Minecraft realm,{w=0.3} the Library,{w=0.3} the Ender Dragon?{/i}"
                     "Your heartrate picks up as you anxiously wait for a response.{w=0.3} You hope you were quick enough."
                     "You heard his quick typing noises from his stream as the chat zoomed by with your name combined with a bunch of question marks,{w=0.3} asking who you were."
                     $ scenep ()
                     with dissolve
                     "And then,{w=0.3} suddenly,{w=0.3} someone joined the call."
                     play sound "audio/teamspeak.mp3"
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     G "Dream!"
                     D "George-{w=0.3} What the hell are you doing?!"
                     G "It's [povname]!"
                     D "What do you mean it's [povname]-"
                     D "Mute your mic on stream,{w=0.3} you idiot!-{w=0.3}{nw}"
                     "The audio from both Dream and George's mic have been silenced."
                     "And then suddenly,{w=0.3} you have a notification beep from Twitter."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     G "{i}hey!{/i}"
                     G "{i}i remember you,{w=0.3} [povname]. :]{/i}"
                     G "{i}do you wanna hang out on mc later? after i fix my chair?{/i}"
                     G "{i}maybe do a challenge and record it?{/i}"
                     "You hesitated.{w=0.3} Remembering what he said.{w=0.3}.{w=0.3}.{w=0.3}"
                     "Immediately,{w=0.3} he added another response."
                     G "{i}i'll proofread the code this time,{w=0.3} don't worry!{/i}"
                     G "{i}i'll do 2{/i}"
                     G "{i}3 times{/i}"
                     G "{i}i'll even get dream and sapnap to do it!!!{/i}"
                     "You let out an amused chuckle as you typed in a reply."
                     pov "{i}It's okay,{w=0.3} George!{/i}"
                     pov "{i}Of course i'll play with you after your stream. :]{/i}"
                     pause(1.0)
                     G "{i}oh!{/i}"
                     G "{i}oh cool!!{/i}"
                     G "{i}ok!!!{w=0.3} cool!!!{w=0.3} cant wait!!! :]{/i}"
                     $ scenep ()
                     with dissolve
                     "You smiled so widely that your eyes shut,{w=0.3} bringing your phone close to your chest."
                     scene georgegoodendplat with dissolve:
                           xpos 0.9 ypos 0.3 xanchor 0.66 yanchor 0.77 zoom 3.3
                           ease 2 yanchor 0.62
                     pause(2.0)
                     scene georgegoodendplat
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("georgegoodendplat")
                     with dissolve
                     "You can't wait for the challenge."
                     $ scenep ()
                     with dissolve
                     scene georgegoodendplat
                     pause(1.0)
                     stop music fadeout 1.0
                     scene georgeplatonicend
                     with fade
                     pause(3.0)
                     jump endingcount

                 label georgebadending:
                     $ persistent.seen_ending_3 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     scene enddragon
                     with wipeupfast
                     show george pained 1 at center, shake
                     with dissolve
                     show george pained 2
                     with dissolve
                     "George."
                     play music "audio/Twin Musicom - Not Without the Rest.mp3" fadein 5.0 volume 0.5
                     show george grin 2 with dissolve
                     "He had a smile on his face,{w=0.3} but his teeth were clenched."
                     "You let out a breath as you glanced up at his health bar."
                     "{i}No.{w=0.3} No, no, no,{w=0.3} {b}no.{/b}{/i}"
                     "The remaining heart in his health bar had begun to flash white,{w=0.3} before disappearing altogether."
                     show george pained 2 at shake
                     hide george pained with dissolve
                     "You caught him as he fell forward,{w=0.3} right into your arms.{w=0.3} You held him as closely as you can."
                     scene enddragon with hpunch:
                         xpos 1.3 ypos 0.45 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                     pause(2.0)
                     "He felt so {i}light.{/i}{w=0.3} You noticed that there are specks of colors appearing around him-"
                     "They were {i}pixels.{/i}{w=0.3} He was {i}disappearing into the tiniest of particles.{/i}"
                     scene enddragon
                     with dissolve
                     show dream angry at center, shake
                     with dissolve
                     D "{i}GEORGE!{/i}"
                     hide dream angry with fastdissolve
                     "Dream exclaimed before landing a final hit onto the dragon."
                     scene white
                     pause(1.0)
                     scene enddragondeath with dissolve:
                         xpos 0.95 ypos 0.9 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                     pause(2.0)
                     play sound "audio/enderdragon death.mp3"
                     "It lets out a screech as it levitates up,{w=0.3} light portruding its body as it slowly disintegrates into specks of particles and EXP points."
                     scene endexitportal1 with dissolve:
                          xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                          ease 2 yanchor 0.62
                     pause(2.0)
                     "Sapnap had immediately ran to your side."
                     show sapnap cry 1 at right, bounce
                     with dissolve
                     S "George?"
                     show sapnap cry 1 at right, bounce
                     S "George,{w=0.3} {i}stay with us.{/i}{w=0.3} Don't screw around."
                     "George only lets out a weak giggle,{w=0.3} his body beginning to glitch out as he tries to poke Sapnap's cheek lightheartedly."
                     show dream cry 1 at left, bounce
                     with dissolve
                     "Dream hurries to your area,{w=0.3} holding his other hand."
                     G "Come on,{w=0.3} guys."
                     G "It was better me than any one of you."
                     G "I wouldn't want you having to experience any of this."
                     show dream cry 2 at left, shake
                     D "George,{w=0.3} stop being an idiot {i}for once.{/i}"
                     "You began to tear up,{w=0.3} whilst both Dream and Sapnap had begun to weep for their best friend."
                     show sapnap cry 1 at right, bounce
                     S "{i}Stop fooling around,{w=0.3} George.{/i}{w=0.3} You're coming with us."
                     show sapnap cry 2 at right, shake
                     S "You're coming with us.{w=0.3}.{w=0.3}.{w=0.3} Just-{w=0.3} just {i}shut up{/i} and come through the portal by our side."
                     scene georgebadcg1 with dissolve:
                          xpos 0.6 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 2.5
                          ease 2 yanchor 0.62
                     pause(1.0)
                     G "Hey.{w=0.3}.{w=0.3}.{w=0.3}"
                     G "Guys,{w=0.3} you all look way better with smiles on your faces."
                     G "Let's try that,{w=0.3} yeah?{w=0.3} Smile for me?"
                     "Dream lets out a sob,{w=0.3} and Sapnap could only sniffle.{w=0.3} But the two of them tried their hardest to give George what he wanted.{w=0.3} They always did."
                     "They let out the best smile they could ever muster.{w=0.3} George grins back."
                     G "I knew I could always count on you two."
                     "He then turns to you."
                     G ".{w=0.3}.{w=0.3}[povname]."
                     G "I'm sorry to have annoyed or burdened you in any way,{w=0.3} but I have only one last request for you."
                     scene georgebadcg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("georgebadcg1")
                     with dissolve
                     pause(1.0)
                     G ".{w=0.3}.{w=0.3}.{w=0.3}Could you please take care of these two for me?"
                     $ scenep ()
                     with dissolve
                     scene georgebadcg1
                     pause(1.0)
                     scene endexitportal1
                     with dissolve
                     "Before you could even give him a response,{w=0.3} his body collapses into thin air;{w=0.3} the last thing you saw was a pleased smile on his face."
                     show dream cry 2 at left
                     show sapnap cry 2 at right
                     with dissolve
                     "Dream and Sapnap had simultaneously let out loud wails as they began to lower themselves to the ground where their best friend used to be."
                     hide dream cry 2
                     hide sapnap cry 2
                     with dissolve
                     "You sat there,{w=0.3} motionless,{w=0.3} and unable to properly comprehend what had just happened."
                     "You feel numb,{w=0.3} but you also began to shed your own share of tears."
                     scene endexitportal1
                     pause(1.0)
                     "All three of you had stayed there a bit longer,{w=0.3} allowing yourselves to grieve for a while longer."
                     show dream cry 2 at left
                     with dissolve
                     "After a few moments,{w=0.3} Dream took a shaky stance up whilst wiping the tears away from his face.{w=0.3} He reaches out to both you and Sapnap to help you both up to your feet."
                     show sapnap cry 2 at right, shake
                     with dissolve
                     show dream cry 2 at left, bounce
                     D "Come on."
                     show dream cry 1 at left
                     with dissolve
                     D "We have to go."
                     hide dream cry 1
                     hide sapnap cry 2
                     with dissolve
                     "He keeps his grip on both of your sleeves and Sapnap's as he leads all three of you to the Exit Portal."
                     scene endexitportal2
                     with dissolve
                     "It was silent as he pulls the both of you into the vortex."
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                         zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}dreamwastaken went live: my chair broke.{/i}"
                     pause(1.0)
                     "Huh."
                     "You tapped on the notification and tuned into the stream."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     D "Sapnap!{w=0.3} Stop laughing!"
                     D "I didn't laugh at you when you screwed your chair up!"
                     "Sapnap lets out a cackle.{w=0.3} It sounded like he was laughing so hard to the point where he had to clutch at his stomach."
                     S "But I wasn't a moron who,{w=0.3} not only accidentally disconnected his Wi-Fi,{w=0.3} but also leaned back to the point of breaking his own chair!"
                     "The Texan continued to poke fun at his friend.{w=0.3} Dream lets out a scoff."
                     D "Whatever,{w=0.3} Sapnap."
                     D "Chat,{w=0.3} we're delaying the challenge me and Sapnap coded for a bit.{w=0.3} I don't have anything else to sit on."
                     "You let out a chuckle at their interactions.{w=0.3} Their chemistry with each other as a duo had always been entertaining."
                     $ scenep ()
                     with dissolve
                     "Though,{w=0.3} you feel like something was missing here.{w=0.3}.{w=0.3}.{w=0.3}"
                     pause(1.0)
                     scene black
                     with fade
                     "Oh,{w=0.3} yeah!"
                     "Your Hypixel game.{w=0.3} You should really get back online."
                     pause(1.0)
                     stop music fadeout 1.0
                     scene georgebadend
                     with fade
                     pause(3.0)
                     jump endingcount

                 label sapnapendings:
                     if sapnap_romantic > max(sapnap_platonic, sapnap_bad):
                         jump sapnapromanticending
                     elif sapnap_platonic > max(sapnap_romantic, sapnap_bad):
                         jump sapnapplatonicending
                     elif sapnap_bad > max(sapnap_romantic, sapnap_platonic):
                         jump sapnapbadending


                 label sapnapromanticending:
                     $ persistent.seen_ending_4 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     play music "audio/bensound-adventure.mp3" fadein 5.0 volume 0.5
                     scene sapnapcggood1 with dissolve:
                          xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 2.5
                          ease 2 yanchor 0.62
                     pause(2.0)
                     scene sapnapcggood1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("sapnapcggood1")
                     with dissolve
                     "Sapnap,{w=0.3} who wielded his axe,{w=0.3} and managed to land the last hit at the dragon that had been only one hit away."
                     play sound "audio/enderdragon death.mp3"
                     "The dragon screeches as it levitates up,{w=0.3} light protruding its body as it slowly disintegrates into specks of particles and EXP points."
                     $ scenep ()
                     with dissolve
                     "And right then,{w=0.3} a sound effect echoes about from Sapnap himself."
                     play sound "audio/exp.mp3"
                     "{i}Sapnap has made the advancement {color=#55FF55}(Free the end){/color}"
                     scene endexitportal1
                     with slowdissolve
                     "Everything was silent,{w=0.3} before all three of them began to whoop loudly."
                     show dream grin 1 at left, bounce
                     show george grin 1 at right, bounce
                     with dissolve
                     DG "{i}SAPNAP!!{/i}"
                     show george grin 2 at right, bounce
                     G "Oh my God!!"
                     show dream grin 2 at left, bounce
                     D "You did it,{w=0.3} brother!"
                     hide dream grin 1
                     hide george grin 2
                     with dissolve
                     "They both hoisted the younger male onto each of their shoulders as they continued to holler and celebrate."
                     scene endexitportal1 with dissolve:
                           xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                           ease 2 yanchor 0.62
                     show sapnap grin 2 at center, bounce
                     with dissolve
                     "And,{w=0.3} of course,{w=0.3} Sapnap joined in on making the loudest noises he could pull off;{w=0.3} from screaming to chanting out 'Yeah!' multiple times and in beat with the other two."
                     hide sapnap grin 2 with dissolve
                     pause(2.0)
                     "After a whole while of being stunned,{w=0.3} you let out your share of giggles."
                     show george shock at right, bounce
                     show sapnap shock at center, bounce
                     show dream shock at left, bounce
                     with dissolve
                     "The boys turned around as they heard you laugh."
                     pause(0.5)
                     show dream grin 1 at left, bounce
                     show george grin 1 at right, bounce
                     pause(1.0)
                     show dream grin 2 at left, bounce
                     show george grin 2 at right, bounce
                     "The two best friends had shared a mischievous look with one another,{w=0.3} before finally settling on the choice to run over to your area."
                     show sapnap wary at center, bounce
                     "Surprised,{w=0.3} Sapnap gripped tightly onto their clothes as he was still situated on their shoulders."
                     show sapnap wary at center, bounce
                     S "WOAH!"
                     S "Guys,{w=0.3} slow down!{w=0.3} Oh my god-{w=0.3}{nw}"
                     hide george grin 2
                     hide dream grin 2
                     with dissolve
                     "He was silenced when he looked back up and saw you."
                     show sapnap flushed 1 at center, bounce
                     pause(1.0)
                     show sapnap flushed 2 at center, bounce
                     S "[povname]!"
                     hide sapnap flushed 2 with dissolve
                     "He hops off his friends' shoulders and latched onto you instead,{w=0.3} enveloping you in what seemed to be his equivalent of a bear hug."
                     show endexitportal1 with hpunch
                     "You wrap your arms around him,{w=0.3} his laughter ringing in your ear,{w=0.3} but you can tell that he felt relieved to see that you were safe."
                     show george neutral at right, bounce
                     show dream neutral at left, bounce
                     with dissolve
                     "You glanced up to see George smiling down at you two whilst Dream gave you your Golden Apple back."
                     "You tried to reel your arms back from the male,{w=0.3} but he squeezed you a bit tighter."
                     "When he spoke up,{w=0.3} it was a bit of a mumble."
                     S "Let me hold you a bit longer."
                     show dream grin 2 at left, bounce
                     "Flushed,{w=0.3} you looked at Dream,{w=0.3} who simply shook his head as he wore an amused smile."
                     "He glances a bit over to George before clasping a hand over the younger male's shoulder."
                     show dream neutral at left, bounce
                     show george grin 2 at right, bounce
                     D "Sap,{w=0.3} come on,{w=0.3} [povname] needs room to breathe too."
                     hide dream neutral
                     hide george neutral
                     with dissolve
                     show sapnap annoyed with dissolve
                     "It was as if you were dealing with a child,{w=0.3} because Sapnap reluctantly let go of you with a pout on his face."
                     "You laughed at him,{w=0.3} taking a bite from your Golden Apple before nudging it nearer to him."
                     show sapnap shock at center, bounce
                     pause(1.0)
                     show sapnap sigh at center, bounce
                     pause(0.8)
                     show sapnap grin 2 at center, bounce
                     "He sends you a tiny grin."
                     show sapnap grin 2 at center, bounce
                     S "Thanks,{w=0.3} [povname].{w=0.3} You're the best."
                     scene endexitportal1
                     with dissolve
                     "He stands up and grabs your arm to help stabilize you onto your feet."
                     show endexitportal1 with hpunch
                     "Once you were properly standing,{w=0.3} he didn't let go of your arm.{w=0.3} In fact,{w=0.3} he decided to intertwine your fingers together with his."
                     show sapnap flushed 2 at center, bounce
                     with dissolve
                     "You looked at him whilst being aware that your cheeks were flushed.{w=0.3} His hold tightens as he sends you a grin."
                     show george grin 1 at right, bounce
                     with dissolve
                     "George decides to coo at the two of you teasingly."
                     show george grin 2 at right, bounce
                     G "{i}Aww,{/i}{w=0.3} look at lil' Sap{w=0.3}py Nap{w=0.3}py!"
                     show sapnap annoyed at center, bounce
                     S "George,{w=0.3} can you shut up?"
                     show dream grin 2 at left, bounce
                     with dissolve
                     D "{i}Aww!{/i}"
                     show sapnap disappointed at center, bounce
                     "Sapnap lets out an irritated huff whilst you let out an amused giggle behind your vacant hand."
                     show dream neutral at left, bounce
                     "Dream looked towards you two with a pleased glance before turning to George and heading to his best friend's side."
                     hide dream neutral
                     hide sapnap disappointed
                     hide george grin 2
                     with dissolve
                     scene endexitportal2
                     with dissolve
                     "As you all walked towards the Exit Portal,{w=0.3} you peered down at the swirling,{w=0.3} black vortex."
                     "You were nervous.{w=0.3} Will this actually bring you guys home?"
                     "It seemed that your anxiousness was seeping through the surface as Sapnap's hold on your hand had tightened once more."
                     show sapnap neutral at center, bounce
                     with dissolve
                     "He looked at you with a comforting smile."
                     show sapnap grin 2 at center, bounce
                     S "Y'know,{w=0.3} for a brave person,{w=0.3} you worry too much."
                     show sapnap grin 1 at center, bounce
                     S "Wanna know one thing I've learned from this entire thing?"
                     pause(0.9)
                     "Your silence was a nudge for him to continue his statement."
                     show sapnap grin 2 at center, bounce
                     S "It was that I shouldn't challenge things on all the time.{w=0.3} Trust in the process."
                     show sapnap neutral at center, bounce
                     S "Lean back a little.{w=0.3} Take a deep breath."
                     show sapnap grin 1 at center, bounce
                     S "I learned this from you.{w=0.3} So,{w=0.3} trust in me this time.{w=0.3} Okay?"
                     hide sapnap grin 1 with dissolve
                     "Your heart fluttered at the words of reassurance and thanked him through the squeeze of your hand.{w=0.3} He finds this adorable and lets out a quiet chuckle."
                     show dream grin 1 with dissolve
                     "Dream then looked at each of you."
                     show dream grin 1 at center, bounce
                     D "On three?"
                     hide dream grin 1 with dissolve
                     "Everyone grinned at him."
                     show george grin 1 at right, bounce
                     with dissolve
                     G "One!"
                     show dream grin 2 at left, bounce
                     with dissolve
                     D "Two!"
                     hide dream grin 2
                     hide george grin 1
                     with dissolve
                     show sapnap grin 2 at center, bounce
                     with dissolve
                     YS "{i}Three!!{/i}"
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                          zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}Sapnap went live: chair got wrecked lol.{/i}"
                     "{i}Sapnap.{/i}"
                     "Minecraft.{w=0.3} The realm."
                     "You quickly pressed on the notification,{w=0.3} the stream's audio booming out of your phone's speakers."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     S "-Ha,{w=0.3} ha.{w=0.3} Sure,{w=0.3} chat."
                     S "You guys really think you're sooooo funny."
                     S "At least my chair broke.{w=0.3} Most of you probably are."
                     S "Which is why those other people who /aren't/ should gift more subs while I fix my chair!"
                     "You laughed at the curt reply that came from the male.{w=0.3} That is {i}definitely{/i} your Sapnap."
                     "You decided to send in a dono,{w=0.3} thinking that hopefully it'll catch his attention."
                     "You can hear loud shuffling from the streams audio."
                     S "Okay,{w=0.3} who thought it was funny to just dono me 'Hey, Snapmap'?"
                     S "Who decided that they have the greatest sense of humo-{w=0.3}{nw}"
                     pause(1.0)
                     "He cuts himself off."
                     S "[povname]?"
                     S "Wait,{w=0.3} hold on,{w=0.3} hold on,{w=0.3} hold on.{w=0.3} [povname]?"
                     S "DM me.{w=0.3} DM me on twitter,{w=0.3} right now."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     "Scrambling towards the Twitter app and turning the stream;s video into a picture-in-pictue at the bottom corner of your screen,{w=0.3} you try your best to send him a message as quick as you could."
                     "You were aware at how quick the fanbase could steal an identity,{w=0.3} after all."
                     "You sent him a message."
                     pov "{i}Sapnap!{/i}"
                     pov "{i}It's me.{w=0.3} Do you remember everything?{/i}"
                     pov "{i}The Minecraft realm,{w=0.3} the Hallway,{w=0.3} the Golden Apple?{/i}"
                     "You waited anxiously for an answer when you hear the tell-tale sound of someone joining Teamspeak."
                     play sound "audio/teamspeak.mp3"
                     DG "Sapnap!"
                     S "Wait,{w=0.3} hold on guys,{w=0.3} shut up."
                     G "What do you mean shut up-{w=0.3}{nw}"
                     S "It's [povname]!"
                     D "Oh my god,{w=0.3} Sapnap-{w=0.3}{nw}"
                     G "Mute your audio NOW,{w=0.3} you moron!{w=0.3}{nw}"
                     "And then radio silence followed right after.{w=0.3} The only thing being presented in the stream was someone's fanart of his character."
                     "You looked at your Twitter DMs when your phone buzzed."
                     S "{i}[povname]!{/i}"
                     S "{i}it's you{/i}"
                     S "{i}oh my god it's really you{/i}"
                     "You smiled sweetly at his response.{w=0.3} Before yoou could even reply back,{w=0.3} he sent you another message."
                     S "{i}how do you wanna work this out?{/i}"
                     S "{i}do you wanna like{/i}"
                     S "{i}vc{/i}"
                     S "{i}after stream or smth??????{/i}"
                     S "{i}talk things out there??????????????????{/i}"
                     S "{i}dream's telling me to buy you a ticket to here{/i}"
                     S "{i}he's annoying{/i}"
                     S "{i}but if you want to then i dont mind talking to him about it{/i}"
                     S "{i}imsorry im spammingarnent i{/i}"
                     "You let out a chuckle."
                     pov "{i}You're good sapnap!{/i}"
                     pov "{i}I wouldn't mind talking things out later{/i}"
                     pov "{i}Nor would I mind visiting you :]{/i}"
                     $ scenep ()
                     with dissolve
                     scene cg1
                     with dissolve
                     "When Sapnap unmuted,{w=0.3} you can hear the sound of him stumbling and things creaking and cracking."
                     "George laughter echoed throughout the call."
                     scene sapnapgoodendrom with dissolve:
                           xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 3.3
                           ease 2 yanchor 0.62
                     pause(1.0)
                     G "Did you just fall and break your chair {i}AGAIN?!{/i}"
                     "Dream's wheezy laughter makes its entrance."
                     scene sapnapgoodendrom
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("sapnapgoodendrom")
                     with dissolve
                     D "Sapnap!{w=0.3} Get ahold of yourself!"
                     "You watch the chat as they both push on with questions about you and laughing at Sapnap's antics."
                     $ scenep()
                     with dissolve
                     "You can't wait for the call after the stream ends."
                     scene sapnapgoodendrom
                     pause(1.0)
                     stop music fadeout 1.0
                     scene sapnapromanticend
                     with fade
                     pause(3.0)
                     jump endingcount


                 label sapnapplatonicending:
                     $ persistent.seen_ending_5 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     play music "audio/bensound-adventure.mp3" fadein 5.0 volume 0.5
                     scene sapnapcggood1 with dissolve:
                          xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 2.5
                          ease 2 yanchor 0.62
                     pause(2.0)
                     scene sapnapcggood1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("sapnapcggood1")
                     with dissolve
                     "Sapnap,{w=0.3} who wielded his axe,{w=0.3} and managed to land the last hit at the dragon that had been only one hit away."
                     play sound "audio/enderdragon death.mp3"
                     "The dragon screeches as it levitates up,{w=0.3} light protruding its body as it slowly disintegrates into specks of particles and EXP points."
                     $ scenep ()
                     with dissolve
                     "And right then,{w=0.3} a sound effect echoes about from Sapnap himself."
                     play sound "audio/exp.mp3"
                     "{i}Sapnap has made the advancement {color=#55FF55}(Free the end){/color}"
                     scene endexitportal1
                     with slowdissolve
                     "Everything was silent,{w=0.3} before all three of them began to whoop loudly."
                     show dream grin 1 at left, bounce
                     show george grin 1 at right, bounce
                     with dissolve
                     DG "{i}SAPNAP!!{/i}"
                     show george grin 2 at right, bounce
                     G "Oh my God!!"
                     show dream grin 2 at left, bounce
                     D "You did it,{w=0.3} brother!"
                     hide dream grin 1
                     hide george grin 2
                     with dissolve
                     "They both hoisted the younger male onto each of their shoulders as they continued to holler and celebrate."
                     scene endexitportal1 with dissolve:
                           xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                           ease 2 yanchor 0.62
                     show sapnap grin 2 at center, bounce
                     with dissolve
                     "And,{w=0.3} of course,{w=0.3} Sapnap joined in on making the loudest noises he could pull off;{w=0.3} from screaming to chanting out 'Yeah!' multiple times and in beat with the other two."
                     hide sapnap grin 2 with dissolve
                     pause(2.0)
                     "After a whole while of being stunned,{w=0.3} you let out your share of giggles."
                     show george shock at right, bounce
                     show sapnap shock at center, bounce
                     show dream shock at left, bounce
                     with dissolve
                     "The boys turned around as they heard you laugh."
                     pause(0.5)
                     show george neutral at right
                     show sapnap neutral
                     show dream neutral at left
                     with dissolve
                     "Their faces softened as they lowered the younger male down,{w=0.3} approaching you."
                     hide george neutral
                     hide sapnap neutral
                     hide dream neutral
                     with dissolve
                     "Dream and George helped you up to your feet,{w=0.3} while Sapnap picks up the Golden Apple you dropped."
                     show sapnap neutral at center, bounce
                     with dissolve
                     "He passes it to you,{w=0.3} in which you fumbled catching."
                     show sapnap grin 2 at center, bounce
                     "He simply chuckles at you as he ruffles your hair."
                     show endexitportal1 with hpunch
                     "It's becoming a habit for him,{w=0.3} you thought."
                     show sapnap grin 1 at center, bounce
                     S "Don't go risking your life like that ever again,{w=0.3} okay,{w=0.3} [povname]?"
                     "Bashfully,{w=0.3} you listened to his words but also shoved his hand away playfully."
                     hide sapnap grin 1 with dissolve
                     scene endexitportal1
                     with dissolve
                     show dream grin 2 at left, bounce
                     with dissolve
                     show george grin 1 at right, bounce
                     with dissolve
                     "As you had that exchange with the Texan,{w=0.3} Dream had been comedically dancing around George while whooping in excitement."
                     show dream grin 2 at left, bounce
                     show george grin 2 at right, bounce
                     "You both looked at the two who were fooling around with content smiles on your faces.{w=0.3} You let out a small huff of laughter as you all made your way to the middle,{w=0.3} the Exit Portal."
                     show dream grin 2 at left, bounce
                     show george annoyed at right, bounce
                     "Dream threw an arm around George,{w=0.3} eliciting a noise of complaint from the shorter male as he ended up being practically dragged around by the younger male."
                     hide dream grin 2
                     hide george annoyed
                     with dissolve
                     scene endexitportal2
                     with dissolve
                     "As you all stepped close to the structure,{w=0.3} you looked down.{w=0.3} Anxiety swirls around in your stomach as you peered through the dark,{w=0.3} swirling vortex."
                     show sapnap shock with dissolve
                     "Sapnap takes notice of this and nudges your arm."
                     show sapnap serious at center, bounce
                     S "Hey."
                     show sapnap neutral at center, bounce
                     S "We'll all go home once we jump in.{w=0.3} I'm sure of that."
                     show sapnap grin 1 at center, bounce
                     S "You can't chicken out now,{w=0.3} right?"
                     "You can hear the faintest hint of teasing in the tone he used in his last line,{w=0.3} and that brought a smile on your face."
                     hide sapnap grin 1 with dissolve
                     "You're a brave person.{w=0.3} You know that yourself."
                     "And Sapnap has taken notice of that aspect about you,{w=0.3} too."
                     "You nodded,{w=0.3} trying to shake the nerves off."
                     show dream grin 1 with dissolve
                     "Dream then looked at each of you."
                     show dream grin 1 at center, bounce
                     D "On three?"
                     hide dream grin 1 with dissolve
                     "Everyone grinned at him."
                     show george grin 1 at right, bounce
                     with dissolve
                     G "One!"
                     show dream grin 2 at left, bounce
                     with dissolve
                     D "Two!"
                     hide dream grin 2
                     hide george grin 1
                     with dissolve
                     show sapnap grin 2 at center, bounce
                     with dissolve
                     YS "{i}Three!!{/i}"
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                          zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}Sapnap went live: chair got wrecked lol.{/i}"
                     "{i}Sapnap.{/i}"
                     "Minecraft.{w=0.3} The realm."
                     "You quickly pressed on the notification,{w=0.3} the stream's audio booming out of your phone's speakers."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     S "-Ha,{w=0.3} ha.{w=0.3} Sure,{w=0.3} chat."
                     S "You guys really think you're sooooo funny."
                     S "At least my chair broke.{w=0.3} Most of you probably are."
                     S "Which is why those other people who /aren't/ should gift more subs while I fix my chair!"
                     "You laughed at the curt reply that came from the male.{w=0.3} That is {i}definitely{/i} your Sapnap."
                     "You decided to send in a dono,{w=0.3} thinking that hopefully it'll catch his attention."
                     "You can hear loud shuffling from the streams audio."
                     S "Okay,{w=0.3} who thought it was funny to just dono me 'Hey, Snapmap'?"
                     S "Who decided that they have the greatest sense of humo-{w=0.3}{nw}"
                     pause(1.0)
                     "He cuts himself off."
                     S "[povname]?"
                     S "Wait,{w=0.3} hold on,{w=0.3} hold on,{w=0.3} hold on.{w=0.3} [povname]?"
                     S "DM me.{w=0.3} DM me on twitter,{w=0.3} right now."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     "Scrambling towards the Twitter app and turning the stream;s video into a picture-in-pictue at the bottom corner of your screen,{w=0.3} you try your best to send him a message as quick as you could."
                     "You were aware at how quick the fanbase could steal an identity,{w=0.3} after all."
                     "You sent him a message."
                     pov "{i}Sapnap!{/i}"
                     pov "{i}It's me.{w=0.3} Do you remember everything?{/i}"
                     pov "{i}The Minecraft realm,{w=0.3} the Hallway,{w=0.3} the Ender Dragon?{/i}"
                     "You waited anxiously for an answer when you hear the tell-tale sound of someone joining Teamspeak."
                     play sound "audio/teamspeak.mp3"
                     DG "Sapnap!"
                     S "Wait,{w=0.3} hold on guys,{w=0.3} shut up."
                     G "What do you mean shut up-{w=0.3}{nw}"
                     S "It's [povname]!"
                     D "Oh my god,{w=0.3} Sapnap-{w=0.3}{nw}"
                     G "Mute your audio NOW,{w=0.3} you moron!{w=0.3}{nw}"
                     "And then radio silence followed right after.{w=0.3} The only thing being presented in the stream was someone's fanart of his character."
                     "You looked at your Twitter DMs when your phone buzzed."
                     S "{i}[povname]!{/i}"
                     S "{i}is it really you?{/i}"
                     "You were about to think of all the things you could remember from the digital realm when you received another message."
                     S "{i}actually no don't answer that{/i}"
                     S "{i}that was so dumb you already told me about the hallway and stuff{/i}"
                     "You chuckled at his reaction."
                     S "{i}do you wanna like{/i}"
                     S "{i}hang out later????{w=0.3} like vc with everyone else???{/i}"
                     S "{i}we can make a video if ur cool with that????{/i}"
                     "You raise your eyebrows in surprise.{w=0.3} A video?{w=0.3} With you?"
                     "You began to type your response away."
                     pov "{i}I'm cool with it!!!{/i}"
                     pov "{i}I can't wait to talk to you guys more :D{/i}"
                     $ scenep ()
                     with dissolve
                     scene cg1
                     with dissolve
                     scene sapnapgoodendplat with dissolve:
                            xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 3.3
                            ease 2 yanchor 0.62
                     pause(1.0)
                     S "{i}cool!!!{w=0.3} cool"
                     S "{i}that's pog{/i}"
                     S "{i}:D{/i}"
                     scene sapnapgoodendplat
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("sapnapgoodendplat")
                     with dissolve
                     "You giggled to yourself as you clutch your phone close to your chest."
                     $ scenep()
                     with dissolve
                     "You can't wait to record a video with them."
                     scene sapnapgoodendplat
                     pause(1.0)
                     stop music fadeout 1.0
                     scene sapnapplatonicend
                     with fade
                     pause(3.0)
                     jump endingcount


                 label sapnapbadending:
                     $ persistent.seen_ending_6 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     scene enddragon
                     with wipeupfast
                     show sapnap pained 1 at center, shake
                     with dissolve
                     show sapnap pained 2
                     with dissolve
                     "Sapnap."
                     play music "audio/Twin Musicom - Not Without the Rest.mp3" fadein 5.0 volume 0.5
                     show sapnap serious with dissolve
                     "His face full of determination had slowly morphed into a duller expression as he took the hit from the dragon for you."
                     "The remaining heart began to fade out the moment you had glanced up at his health bar."
                     show sapnap pained 2 at shake
                     hide sapnap pained with dissolve
                     scene enddragon with hpunch:
                         xpos 1.3 ypos 0.45 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                         pause(2.0)
                     "He fell forward,{w=0.3} different parts of his body beginning to flicker and glitch out as you caught him."
                     "He's {i}slowly disappearing into the tiniest bits of particles.{/i}"
                     "{i}No.{w=0.3} No, no, no,{w=0.3} {b}no.{/b}{/i}"
                     "His body felt so {i}cold.{/i}{w=0.3} Your hands were frantic,{w=0.3} you couldn't do anything but {i}hold{/i} him."
                     scene enddragon
                     with dissolve
                     show george angry at center, shake
                     with dissolve
                     G "{i}SAPNAP, NO!!{/i}"
                     hide george angry with fastdissolve
                     "George screamed as he sent his final arrow flying towards the dragon."
                     scene white
                     pause(1.0)
                     scene enddragondeath with dissolve:
                         xpos 0.95 ypos 0.9 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                     pause(2.0)
                     play sound "audio/enderdragon death.mp3"
                     "It lets out a screech as it levitates up,{w=0.3} light portruding its body as it slowly disintegrates into specks of particles and EXP points."
                     scene endexitportal1 with dissolve:
                          xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                          ease 2 yanchor 0.62
                     pause(2.0)
                     show dream cry 1 at right, bounce
                     with dissolve
                     "Right after,{w=0.3} Dream had immediately skidded towards you two.{w=0.3} He holds one of Sapnap's hands in his tightly."
                     D "Hey,{w=0.3} buddy,{w=0.3} stay with us."
                     show dream cry 2 at right, bounce
                     D "It's gonna be okay.{w=0.3} {i}You're{/i} gonna be okay.{w=0.3} We're right here,{w=0.3} Pandas."
                     scene sapnapbadcg1 with dissolve:
                          xpos 1.15 ypos 0.35 xanchor 0.66 yanchor 0.77 zoom 2.8
                          ease 2 yanchor 0.62
                     pause(1.0)
                     "Sapnap shakily looks towards Dream."
                     S "Dream?"
                     S "Dream,{w=0.3} I'm scared."
                     "Dream hushes him as George makes his way to you guys.{w=0.3} His eyes were full of tears and had the look of distraught."
                     "He kneels down next to you and Sapnap."
                     S "George.{w=0.3}.{w=0.3}.{w=0.3}"
                     G "Please don't go."
                     "George grabs ahold of his other hand,{w=0.3} sobbing into the back of it as he brought it up to his face."
                     "Your heart hurts at the sight of all three of them,{w=0.3} broken and crying their hearts out."
                     "Sapnap then looks to you,{w=0.3} his voice barely above a whisper."
                     S ".{w=0.3}.{w=0.3}.{w=0.3}[povname]."
                     S "Will you please do me a favor?"
                     scene sapnapbadcg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("sapnapbadcg1")
                     with dissolve
                     pause(1.0)
                     "You were about to respond when he gave out a dry huff of laughter."
                     S "Of course,{w=0.3} you can.{w=0.3} You're really reliable,{w=0.3} [povname],{w=0.3} and I admire that aspect of yours."
                     S "Might I add 'brave' to that list,{w=0.3} too."
                     "He sends you a pained smile,{w=0.3} his body beginning to dematerialize into tiny specks of pixels."
                     $ scenep()
                     with dissolve
                     S "Watch over them for me,{w=0.3} okay?"
                     scene sapnapbadcg1
                     pause(1.0)
                     scene endexitportal1
                     with dissolve
                     "Before you could even accept his request,{w=0.3} the echoes of his quiet giggles ring out one last before the weight in your arms disappeared altogether."
                     show dream cry 2 at left
                     show george cry 1 at right
                     with dissolve
                     "George lets out a loud wail as Dream covered his mouth to control his sobbing."
                     hide dream cry 2
                     hide george cry 1
                     with dissolve
                     "You sat there,{w=0.3} motionless,{w=0.3} and unable to properly comprehend what had just happened."
                     "You feel numb,{w=0.3} but you also began to shed your own share of tears."
                     scene endexitportal1
                     pause(1.0)
                     "All three of you had stayed there a bit longer,{w=0.3} allowing yourselves to grieve for a while longer."
                     show dream cry 2 at left
                     with dissolve
                     "After a few moments,{w=0.3} Dream took a shaky stance up whilst wiping the tears away from his face.{w=0.3} He reaches out to both you and George to help you both up to your feet."
                     show george cry 2 at right, shake
                     with dissolve
                     show dream cry 2 at left, bounce
                     D "Come on."
                     show dream cry 1 at left
                     with dissolve
                     D "We have to go."
                     hide dream cry 1
                     hide george cry 2
                     with dissolve
                     "He keeps his grip on both of your sleeves and George's as he leads all three of you to the Exit Portal."
                     scene endexitportal2
                     with dissolve
                     "It was silent as he pulls the both of you into the vortex."
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                         zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}GeorgeNotFound went live: Fixing my chair.{/i}"
                     pause(1.0)
                     "Huh."
                     "You tapped on the notification and tuned into the stream."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     D "{i}-Will you have sex with me?{/i}"
                     "George lets out a confused huff of laughter.{w=0.3} You found it funny that this is what you first hear the moment you joined the stream."
                     G "{i}What?!{/i}"
                     D "{i}No.{w=0.3} Will you /please/ reconsider?{/i}"
                     D "Come on,{w=0.3} George,{w=0.3} it's a funny video!"
                     "You then heard the British male scoff lightheartedly at the younger male's antics."
                     G "You're so weird."
                     G "Come on,{w=0.3} restart your Minecraft launcher.{w=0.3} I've fixed my chair the best I can."
                     G "Let's work on the code again right now,{w=0.3} yeah?{w=0.3} Maybe even teach chat a thing or two."
                     D "Alright,{w=0.3} sure.{w=0.3} Gimme a sec."
                     "You smiled.{w=0.3} Their streams together were always so fun to watch,{w=0.3} especially the times where they start to begin being competitive with each other to the point of screaming and leaving calls as a joke."
                     $ scenep ()
                     with dissolve
                     "All of a sudden,{w=0.3} you feel like something was missing."
                     "You glanced down at the charm you had connected to your phone.{w=0.3} Your friend had given it to you as a birthday present."
                     "It was a panda."
                     pause(1.0)
                     scene black
                     with fade
                     "And then you remembered-{w=0.3} Oh yeah!"
                     "Your Hypixel game.{w=0.3} You should really get back online."
                     pause(1.0)
                     stop music fadeout 1.0
                     scene sapnapbadend
                     with fade
                     pause(3.0)
                     jump endingcount


                 label dreamendings:
                     if dream_romantic > max(dream_platonic, dream_bad):
                         jump dreamromanticending
                     elif dream_platonic > max(dream_romantic, dream_bad):
                         jump dreamplatonicending
                     elif dream_bad > max(dream_romantic, dream_platonic):
                         jump truebadending



                 label dreamromanticending:
                     $ persistent.seen_ending_7 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     play music "audio/bensound-adventure.mp3" fadein 5.0 volume 0.5
                     scene dreamcggood1 with dissolve:
                          xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 2.5
                          ease 2 yanchor 0.62
                     pause(2.0)
                     scene dreamcggood1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("dreamcggood1")
                     with dissolve
                     "Dream,{w=0.3} who wielded his axe,{w=0.3} and managed to land the last hit at the dragon that had been only one hit away."
                     play sound "audio/enderdragon death.mp3"
                     "The dragon screeches as it levitates up,{w=0.3} light protruding its body as it slowly disintegrates into specks of particles and EXP points."
                     $ scenep ()
                     with dissolve
                     "And right then,{w=0.3} a sound effect echoes about from Dream himself."
                     play sound "audio/exp.mp3"
                     "{i}Dream has made the advancement {color=#55FF55}(Free the end){/color}"
                     scene endexitportal1
                     with slowdissolve
                     "Everything was silent,{w=0.3} before all three of them began to whoop loudly."
                     show george grin 1 at left, bounce
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     GS "{i}DREAM!!{/i}"
                     show george grin 2 at left, bounce
                     G "{i}LET'S GOOOOO!!{/i}"
                     show sapnap grin 2 at right, bounce
                     S "DREAM,{w=0.3} YOU DID IT!"
                     hide sapnap grin 2
                     hide george grin 2
                     with dissolve
                     "They struggled to hoist the male up,{w=0.3} as he was the tallest of all three of them,{w=0.3} but they still pushed it and managed to pull it off."
                     show dream grin 2 at center, bounce
                     with dissolve
                     "Dream had let out the loudest guffaw as the other two continued to chant out loud."
                     hide dream grin 2 with dissolve
                     scene endexitportal1 with dissolve:
                           xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                           ease 2 yanchor 0.62
                     with dissolve
                     "The adrenaline melting away,{w=0.3} you let out a little huff of relieved laughter behind your hand."
                     pause(2.0)
                     show george shock at left, bounce
                     show sapnap shock at right, bounce
                     show dream shock at center, bounce
                     with dissolve
                     "The boys managed to pick up your sound as they all turned to face you."
                     pause(0.5)
                     show george grin 1 at left, bounce
                     show sapnap grin 1 at right, bounce
                     pause(1.0)
                     show george grin 2 at left, bounce
                     show sapnap grin 2 at right, bounce
                     "Sapnap and George glanced at each other with small smirks on their faces before heading towards your direction at a fast speed."
                     show dream wary at center, bounce
                     "Dream fumbled around to grip at both of their shirts."
                     show dream wary at center, bounce
                     D "W-Woah!"
                     D "Slow down!"
                     hide george grin 2
                     hide sapnap grin 2
                     with dissolve
                     "He lets out a nervous chuckle but went quiet the moment he realized that they have led you to where you are."
                     show dream neutral at center, bounce
                     pause(1.0)
                     hide dream neutral with dissolve
                     "Relieved to see that you were fine,{w=0.3} all in one piece,{w=0.3} he had enveloped you in a tight hug."
                     scene endexitportal1
                     with hpunch
                     "Your heartbeat races as you slowly hugged back.{w=0.3} He squeezes you a bit tighter the moment you do so."
                     "His voice was laced with pure relief."
                     D "I'm so glad you're okay."
                     "You feel your cheeks warm up and decided to hide your face into his shoulder."
                     pause(1.0)
                     "After a moment,{w=0.3} you both pulled away."
                     show sapnap neutral at right
                     with dissolve
                     "Sapnap had walked up to you,{w=0.3} your Golden Apple in his hand,{w=0.3} and gave it over to you."
                     show sapnap grin 2 at right, bounce
                     "You nodded at him in thanks,{w=0.3} replenishing your health after a bite or two,{w=0.3} before walking up to Dream."
                     hide sapnap grin 2 with dissolve
                     show dream shock at center, bounce
                     with dissolve
                     pause(0.5)
                     show dream wary at center, bounce
                     "He gives you a confusing look as you raised the apple up to him,{w=0.3} offering him a bite."
                     show dream neutral with dissolve
                     "Dream then smiles sweetly at you and grabs ahold of your hand as he takes his portion of the apple,{w=0.3} his health slowly regenerating."
                     show dream grin 2 with dissolve
                     D "Thank you,{w=0.3} [povname]."
                     "You nodded,{w=0.3} expecting him to let go of your hand."
                     show dream neutral at center, bounce
                     "He did,{w=0.3} however,{w=0.3} he decided to hold onto your vacant hand instead."
                     show dream grin 2 at center, bounce
                     "Dream then intertwined your fingers with his,{w=0.3} the smile on his face still in its place as he looks at you."
                     pause(1.0)
                     show dream shock at center, bounce
                     "The two of you were broken out of your little reverie when you began hearing screeching from a while away."
                     hide dream shock with dissolve
                     show george wary at left, bounce
                     show sapnap annoyed at right, bounce
                     with dissolve
                     "Looking for the source of the noise,{w=0.3} it turned out to be Sapnap chasing after George as he tried to get the Enderman off of him."
                     show sapnap angry at right, shake
                     S "Why did you even look at them?!"
                     show george angry at left, shake
                     G "That's the thing,{w=0.3} {i}moron,{/i}{w=0.3} I didn't!"
                     hide sapnap angry
                     hide george angry
                     with dissolve
                     show dream sigh at center, bounce
                     with dissolve
                     "You let out a bit of a chuckle as Dream rolled his eyes at their antics.{w=0.3} Reluctantly,{w=0.3} he lets go of your hand and goes over to them to quickly defeat the tall mob."
                     show dream neutral at center, bounce
                     pause(0.1)
                     show sapnap annoyed at right, bounce
                     show george sigh at left, bounce
                     with dissolve
                     "George wheezed out a thank you whilst Sapnap had complained about him 'stealing his kill'."
                     show dream grin 2 at center, bounce
                     "Dream shakes his head as he makes his way back to you.{w=0.3} He grabs your hand once more and began leading all four of you to the Exit Portal."
                     hide dream grin 2 with dissolve
                     show george neutral at left, bounce
                     show sapnap annoyed at right, bounce
                     "George and Sapnap followed his lead,{w=0.3} the latter lightheartedly pouting due to the situation earlier."
                     hide george neutral
                     hide sapnap annoyed
                     with dissolve
                     scene endexitportal2
                     with dissolve
                     "You all peer over the murky vortex."
                     "You wondered if this will actually bring you guys back home."
                     show dream wary with dissolve
                     "Dream notices the slight falter and tightens the grip of his hand on yours."
                     show dream wary at center, bounce
                     D "Hey.{w=0.3} Trust me,{w=0.3} okay?"
                     show dream neutral at center, bounce
                     D "We'll all go home."
                     show dream grin 1 at center, bounce
                     D "You told me to believe in myself,{w=0.3} and to trust in others,{w=0.3} right?"
                     show dream grin 2 at center, bounce
                     D "Now,{w=0.3} it's your turn to do the same."
                     hide dream grin 2 with dissolve
                     "Relief washing over you,{w=0.3} you sent him a smile of your own."
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     "Sapnap peers over to each of you with a grin."
                     show sapnap grin 1 at right, bounce
                     S "On three?"
                     "Everyone grinned at him."
                     show george grin 1 at left, bounce
                     with dissolve
                     G "One!"
                     show sapnap grin 2 at right, bounce
                     S "Two!"
                     hide george grin 1
                     hide sapnap grin 2
                     with dissolve
                     show dream grin 2 at center, bounce
                     with dissolve
                     YD "{i}Three!!{/i}"
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                          zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}dreamwastaken went live: my chair broke.{/i}"
                     "dreamwastaken.{w=0.3} {i}Dream.{/i}"
                     "Minecraft.{w=0.3} The realm."
                     "You quickly pressed on the notification,{w=0.3} the stream's audio booming out of your phone's speakers."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     D "-Oh,{w=0.3} haha,{w=0.3} chat.{w=0.3} Yeah,{w=0.3} whiny Florida man broke his chair,{w=0.3} bla-bla-bla.{w=0.3} You guys sure are funny."
                     "Hearing his voice boom out again,{w=0.3} except this time with a whole lot of distance between you two,{w=0.3} your heart rate begins to rise."
                     D "Yeah,{w=0.3} yeah,{w=0.3} can the other two like,{w=0.3} join already?"
                     D "I'm sure their internet's back already."
                     D "Guess I'll just scroll through donos and answer them while I wait.{w=0.3} Uh.{w=0.3}.{w=0.3}.{w=0.3}"
                     "Donos!{w=0.3} Right,{w=0.3} you can get his attention through a donation!"
                     "You quickly sent in a message,{w=0.3} along with the lowest amount of money you can send to him,{w=0.3} and clutched at your phone as you waited."
                     D "-Soon,{w=0.3} we'll all live together under one roof,{w=0.3} so.{w=0.3} Yeah,{w=0.3} thank you for the dono."
                     D "Next,{w=0.3} is,{w=0.3} uh,{w=0.3} calling me a pissbaby.{w=0.3} Thank you,{w=0.3} [povname]."
                     pause(1.0)
                     "Your heart stops when you heard him say your name.{w=0.3} You can tell that he froze up,{w=0.3} too."
                     D "{i}[povname].{w=0.3}.{w=0.3}.{w=0.3}{/i}"
                     D "Wait,{w=0.3} hold on.{w=0.3} [povname],{w=0.3} send me a Twitter DM,{w=0.3} please?"
                     "You nodded,{w=0.3} even though you were aware that he can't see you,{w=0.3} and immediately transferred to the app."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     "The livestream turns into a picture-in-picture that stays on the bottom right of your phone."
                     "You send him a message as quick you could,{w=0.3} hoping no one beat you to it."
                     play sound "audio/teamspeak.mp3"
                     "The notification of {i}User joined your channel.{/i} had rung out twice."
                     G "Dream!"
                     D "Hold on."
                     S "{i}DREAM!{/i}"
                     D "{i}Dude!{/i}{w=0.3} Shut up.{w=0.3} Look,{w=0.3} I'll messa-{w=0.3}{nw}"
                     "And then the stream became silent a while after that."
                     "You proceeded to watch the chat flood in with questions and {i}[povname]????????????????{/i}s until you got a notification from your Twitter."
                     D "{i}Hey.{/i}"
                     pov "{i}hey.{/i}"
                     D "{i}Please tell me you remember.{/i}"
                     pause(1.0)
                     "You felt your chest tighten as you read his message.{w=0.3} You immediately reply."
                     pov "{i}I remember.{/i}"
                     pov "{i}The realm,{w=0.3} the Portal,{w=0.3} the Golden Apple,{w=0.3} everything.{/i}"
                     pause(1.0)
                     D "{i}holy shit it's you.{/i}"
                     D "{i}it really is you.{/i}"
                     "You laugh at his reaction."
                     pov "{i}It's always been me.{/i}"
                     D "{i}are you up for a call later?{/i}"
                     D "{i}the other two kinda{/i}"
                     D "{i}talked me into getting a ticket for you.{w=0.3} to fly here.{/i}"
                     "You blushed a bit.{w=0.3} Already?"
                     "As if reading your mind,{w=0.3} Dream began to spam."
                     D "{i}i mean{/i}"
                     D "{i}like{/i}"
                     D "{i}if yourerelaly okaywithi t{/i}"
                     D "{i}i dontmena to rush you wait{/i}"
                     D "{i}waitwiatiawiit{/i}"
                     "Quick to reassure him,{w=0.3} you chuckled a bit as you typed in your reply."
                     pov "{i}Dream!{w=0.3} It's okay!{/i}"
                     pov "{i}I'm down to talk with you about it.{/i}"
                     pov "{i}For now,{w=0.3} remember you have a stream to keep up :] I'll send you my discord tag in a bit.{/i}"
                     $ scenep ()
                     with dissolve
                     scene cg1
                     with dissolve
                     scene dreamgoodendrom with dissolve:
                            xpos 1.5 ypos 1.7 xanchor 0.66 yanchor 0.77 zoom 3.3
                            ease 2 yanchor 0.62
                     pause(1.0)
                     "Right as you sent your set of messages,{w=0.3} Dream had unmuted himself on his stream.{w=0.3} The stream came back to the other two bickering as the blonde had let out a whoop."
                     scene dreamgoodendrom
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("dreamgoodendrom")
                     with dissolve
                     "You laughed to yourself,{w=0.3} clutching your phone close to your chest."
                     $ scenep()
                     with dissolve
                     "You can't wait to talk to him later."
                     scene dreamgoodendrom
                     pause(1.0)
                     stop music fadeout 1.0
                     scene dreamromanticend
                     with fade
                     pause(3.0)
                     jump endingcount


                 label dreamplatonicending:
                     $ persistent.seen_ending_8 = True
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     play music "audio/bensound-adventure.mp3" fadein 5.0 volume 0.5
                     scene dreamcggood1 with dissolve:
                          xpos 0.9 ypos 0.4 xanchor 0.66 yanchor 0.77 zoom 2.5
                          ease 2 yanchor 0.62
                     pause(2.0)
                     scene dreamcggood1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("dreamcggood1")
                     with dissolve
                     "Dream,{w=0.3} who wielded his axe,{w=0.3} and managed to land the last hit at the dragon that had been only one hit away."
                     play sound "audio/enderdragon death.mp3"
                     "The dragon screeches as it levitates up,{w=0.3} light protruding its body as it slowly disintegrates into specks of particles and EXP points."
                     $ scenep ()
                     with dissolve
                     "And right then,{w=0.3} a sound effect echoes about from Dream himself."
                     play sound "audio/exp.mp3"
                     "{i}Dream has made the advancement {color=#55FF55}(Free the end){/color}"
                     scene endexitportal1
                     with slowdissolve
                     "Everything was silent,{w=0.3} before all three of them began to whoop loudly."
                     show george grin 1 at left, bounce
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     GS "{i}DREAM!!{/i}"
                     show george grin 2 at left, bounce
                     G "{i}LET'S GOOOOO!!{/i}"
                     show sapnap grin 2 at right, bounce
                     S "DREAM,{w=0.3} YOU DID IT!"
                     hide sapnap grin 2
                     hide george grin 2
                     with dissolve
                     "They struggled to hoist the male up,{w=0.3} as he was the tallest of all three of them,{w=0.3} but they still pushed it and managed to pull it off."
                     show dream grin 2 at center, bounce
                     with dissolve
                     "Dream had let out the loudest guffaw as the other two continued to chant out loud."
                     hide dream grin 2 with dissolve
                     scene endexitportal1 with dissolve:
                           xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                           ease 2 yanchor 0.62
                     with dissolve
                     "The adrenaline melting away,{w=0.3} you let out a little huff of relieved laughter behind your hand."
                     pause(2.0)
                     show george shock at left, bounce
                     show sapnap shock at right, bounce
                     show dream shock at center, bounce
                     with dissolve
                     "The boys managed to pick up your sound as they all turned to face you."
                     pause(0.5)
                     show dream grin 1 at center, bounce
                     show george grin 1 at left, bounce
                     show sapnap grin 1 at right, bounce
                     pause(1.0)
                     show dream grin 2 at center, bounce
                     show george grin 2 at left, bounce
                     show sapnap grin 2 at right, bounce
                     "They looked to each other,{w=0.3} realizing that they probably looked like a bunch of idiots,{w=0.3} before they began laughing for a bit."
                     hide dream grin 2
                     hide sapnap grin 2
                     hide george grin 2
                     with dissolve
                     "They slowly let Dream down and began to walk up to you."
                     show dream neutral with dissolve
                     "The blonde picks up the Golden Apple you dropped and passes it to you.{w=0.3} He pats you on the head."
                     show dream grin 1 at center, bounce
                     D "Don't drop important things next time,{w=0.3} okay?"
                     show dream grin 2 at center, bounce
                     "You roll your eyes playfully as you took a bite from the apple,{w=0.3} replenishing your health."
                     show dream shock at center, bounce
                     "The both of you began hearing screeching from a while away."
                     hide dream shock with dissolve
                     show george wary at left, bounce
                     show sapnap annoyed at right, bounce
                     with dissolve
                     "Looking for the source of the noise,{w=0.3} it turned out to be Sapnap chasing after George as he tried to get the Enderman off of him."
                     show sapnap angry at right, shake
                     S "Why did you even look at them?!"
                     show george angry at left, shake
                     G "That's the thing,{w=0.3} {i}moron,{/i}{w=0.3} I didn't!"
                     hide sapnap angry
                     hide george angry
                     with dissolve
                     show dream sigh at center, bounce
                     with dissolve
                     "You let out a bit of a chuckle as Dream rolled his eyes at their antics.{w=0.3} He leaves your side for a bit and goes over to them to quickly defeat the tall mob."
                     show dream neutral at center, bounce
                     pause(0.1)
                     show sapnap annoyed at right, bounce
                     show george sigh at left, bounce
                     with dissolve
                     "George wheezed out a thank you whilst Sapnap had complained about him 'stealing his kill'."
                     show dream grin 2 at center, bounce
                     "Dream shakes his head as he makes his way back to you.{w=0.3} He beckoned over to you and began leading all four of you to the Exit Portal."
                     hide dream grin 2 with dissolve
                     show george neutral at left, bounce
                     show sapnap annoyed at right, bounce
                     "George and Sapnap followed his lead,{w=0.3} the latter lightheartedly pouting due to the situation earlier."
                     hide george neutral
                     hide sapnap annoyed
                     with dissolve
                     scene endexitportal2
                     with dissolve
                     "You all peer over the murky vortex."
                     "You wondered if this will actually bring you guys back home."
                     show dream wary with dissolve
                     "Dream notices this before playfully nudging your side to catch your attention."
                     show dream wary at center, bounce
                     D "Hey."
                     show dream neutral at center, bounce
                     D "Everything will be fine.{w=0.3} We'll get home after all this."
                     show dream grin 2 at center, bounce
                     D "You can trust me on that."
                     hide dream grin 2 with dissolve
                     "You sent a grin over his way,{w=0.3} alongside a playful shove of your own."
                     show sapnap grin 1 at right, bounce
                     with dissolve
                     "Sapnap peers over to each of you with a grin."
                     show sapnap grin 1 at right, bounce
                     S "On three?"
                     "Everyone grinned at him."
                     show george grin 1 at left, bounce
                     with dissolve
                     G "One!"
                     show sapnap grin 2 at right, bounce
                     S "Two!"
                     hide george grin 1
                     hide sapnap grin 2
                     with dissolve
                     show dream grin 2 at center, bounce
                     with dissolve
                     YD "{i}Three!!{/i}"
                     scene white
                     with dissolve
                     pause(1.0)
                     scene cg1
                     with dissolve
                     show cg1 with vpunch:
                          zoom 1.5
                     "You woke up on your bedroom floor,{w=0.3} clutching at your throbbing head."
                     scene cg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("cg1")
                     with dissolve
                     "It seemed that you had fallen over your chair."
                     "You hear your phone buzzing from your desk.{w=0.3} Groaning,{w=0.3} you crawled over to check what your notifications were going off for."
                     "For the first few spams,{w=0.3} it had been from your friends as you were apparently late for your Hypixel game together with them."
                     "The most recent one was.{w=0.3}.{w=0.3}.{w=0.3}"
                     "{i}dreamwastaken went live: my chair broke.{/i}"
                     "dreamwastaken.{w=0.3} {i}Dream.{/i}"
                     "Minecraft.{w=0.3} The realm."
                     "You quickly pressed on the notification,{w=0.3} the stream's audio booming out of your phone's speakers."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone")
                     show phone
                     with dissolve
                     D "-Oh,{w=0.3} haha,{w=0.3} chat.{w=0.3} Yeah,{w=0.3} whiny Florida man broke his chair,{w=0.3} bla-bla-bla.{w=0.3} You guys sure are funny."
                     "Hearing his voice boom out again,{w=0.3} except this time with a whole lot of distance between you two,{w=0.3} your heart rate begins to rise."
                     D "Yeah,{w=0.3} yeah,{w=0.3} can the other two like,{w=0.3} join already?"
                     D "I'm sure their internet's back already."
                     D "Guess I'll just scroll through donos and answer them while I wait.{w=0.3} Uh.{w=0.3}.{w=0.3}.{w=0.3}"
                     "Donos!{w=0.3} Right,{w=0.3} you can get his attention through a donation!"
                     "You quickly sent in a message,{w=0.3} along with the lowest amount of money you can send to him,{w=0.3} and clutched at your phone as you waited."
                     D "-Soon,{w=0.3} we'll all live together under one roof,{w=0.3} so.{w=0.3} Yeah,{w=0.3} thank you for the dono."
                     D "Next,{w=0.3} is,{w=0.3} uh,{w=0.3} calling me a pissbaby.{w=0.3} Thank you,{w=0.3} [povname]."
                     pause(1.0)
                     "Your heart stops when you heard him say your name.{w=0.3} You can tell that he froze up,{w=0.3} too."
                     D "{i}[povname].{w=0.3}.{w=0.3}.{w=0.3}{/i}"
                     D "Wait,{w=0.3} hold on.{w=0.3} [povname],{w=0.3} send me a Twitter DM,{w=0.3} please?"
                     "You nodded,{w=0.3} even though you were aware that he can't see you,{w=0.3} and immediately transferred to the app."
                     $ mouse_parallax.set ((-20, -5, "l0"), (-40, -10, "l1"))
                     $ showp ("cg1", "phone2")
                     show phone2
                     with dissolve
                     "The livestream turns into a picture-in-picture that stays on the bottom right of your phone."
                     "You send him a message as quick you could,{w=0.3} hoping no one beat you to it."
                     play sound "audio/teamspeak.mp3"
                     "The notification of {i}User joined your channel.{/i} had rung out twice."
                     G "Dream!"
                     D "Hold on."
                     S "{i}DREAM!{/i}"
                     D "{i}Dude!{/i}{w=0.3} Shut up.{w=0.3} Look,{w=0.3} I'll messa-{w=0.3}{nw}"
                     "And then the stream became silent a while after that."
                     "You proceeded to watch the chat flood in with questions and {i}[povname]????????????????{/i}s until you got a notification from your Twitter."
                     D "{i}[povname]?{/i}"
                     pov "{i}Dream!{/i}"
                     pov "{i}It's me.{w=0.3} Do you remember everything?"
                     pov "{i}The Minecraft realm,{w=0.3} the Portal,{w=0.3} the Ender Dragon?"
                     "You anticipated for a response from the male.{w=0.3} Your nerves caused your fingers to shake slightly as you held your phone."
                     "Your phone buzzed with a new message."
                     D "{i}:){/i}"
                     D "{i}I'm glad you're safe and sound!{/i}"
                     D "{i}Did you hit your head?{/i}"
                     D "{i}George told me he did{/i}"
                     pov "{i}luckily enough I didn't{/i}"
                     pov "{i}was your end alright?{/i}"
                     D "{i}yeah!{w=0.3} yeah.{/i}"
                     "Whew.{w=0.3} Smooth conversation,{w=0.3} that's great."
                     "You then heard another {i}ping!{/i} from your phone."
                     D "{i}do you wanna join our call?{/i}"
                     D "{i}after i stream i mean{/i}"
                     D "{i}we can film together :){/i}"
                     "You practically had stars in your eyes as you typed back a response."
                     pov "{i}that'd be so cool!{/i}"
                     pov "{i}yea i'll be down for it! :D{/i}"
                     $ scenep ()
                     with dissolve
                     scene cg1
                     with dissolve
                     scene dreamgoodendplat with dissolve:
                            xpos 1.5 ypos 1.7 xanchor 0.66 yanchor 0.77 zoom 3.3
                            ease 2 yanchor 0.62
                     pause(1.0)
                     "Right as you sent your set of messages,{w=0.3} Dream had unmuted himself on his stream.{w=0.3} The stream came back to the three of them bickering with each other."
                     scene dreamgoodendplat
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("dreamgoodendplat")
                     with dissolve
                     "You laughed to yourself,{w=0.3} clutching the phone close to your chest."
                     $ scenep()
                     with dissolve
                     "You can't wait to talk to your new set of friends later."
                     scene dreamgoodendplat
                     pause(1.0)
                     stop music fadeout 1.0
                     scene dreamplatonicend
                     with fade
                     pause(3.0)
                     jump endingcount


                 label truebadending:
                     "{i}(Quick Kio interruption!{w=0.3} Hello,{w=0.3} this is Kio speaking.){/i}"
                     "{i}(Here is a quick warning,{w=0.3} as there will be flashing lights and slightly unsettling words later on through this ending.){/i}"
                     "{i}(Be careful going down this ending!{w=0.3} Enjoy! :]){/i}"
                     pause(1.0)
                     play sound "audio/fall.mp3"
                     "You heard the noise of a hit.{w=0.3} You didn't feel any pain."
                     "You opened your eyes and saw.{w=0.3}.{w=0.3}.{w=0.3}"
                     scene enddragon
                     with wipeupfast
                     show dream pained 1 at center, shake
                     with dissolve
                     show dream pained 2
                     with dissolve
                     "Dream."
                     "He had his eyes tightly shut,{w=0.3} bracing himself,{w=0.3} but soon after he was hit,{w=0.3} his eyes flew open."
                     "The remaining heart began to fade out the moment you had glanced up at his health bar."
                     show dream pained 2 at shake
                     hide dream pained with dissolve
                     scene enddragon with hpunch:
                         xpos 1.3 ypos 0.45 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                         pause(2.0)
                     "He fell forward,{w=0.3} different parts of his body beginning to flicker and glitch out as you caught him."
                     "He's {i}slowly disappearing into the tiniest bits of particles.{/i}"
                     "{i}No.{w=0.3} No, no, no,{w=0.3} {b}no.{/b}{/i}"
                     "His breathing was slowly turning shallow.{w=0.3} Your breathing,{w=0.3} on the other hand,{w=0.3} had turned erratic as you gripped onto his shirt."
                     scene enddragon
                     with dissolve
                     show sapnap angry at center, shake
                     with dissolve
                     S "{i}DREAM!{/i}"
                     hide sapnap angry with fastdissolve
                     "Sapnap cried out before landing a final hit onto the dragon."
                     scene white
                     pause(1.0)
                     scene enddragondeath with dissolve:
                         xpos 0.95 ypos 0.9 xanchor 0.66 yanchor 0.77 zoom 2.5
                         ease 2 yanchor 0.62
                     pause(2.0)
                     play sound "audio/enderdragon death.mp3"
                     "It lets out a screech as it levitates up,{w=0.3} light portruding its body as it slowly disintegrates into specks of particles and EXP points."
                     scene endexitportal1 with dissolve:
                          xpos 1.2 ypos 1.0 xanchor 0.66 yanchor 0.77 zoom 2.0
                          ease 2 yanchor 0.62
                     pause(2.0)
                     show george wary at left, bounce
                     with dissolve
                     "George had immediately skidded over to your side.{w=0.3} He picks up one of Dream's hands,{w=0.3} which quickly began to deteriorate at the slightest contact."
                     show george wary at left, bounce
                     G "Dream!"
                     show george cry 1 at left, bounce
                     G "No,{w=0.3}, no, no.{w=0.3} Dream,{w=0.3} stay with me.{w=0.3} Stay with {i}us{/i}."
                     pause(0.7)
                     "Dream doesn't even utter a word.{w=0.3} Only soft gasping can be heard."
                     show sapnap wary at right, bounce
                     with dissolve
                     "Sapnap rushes over to your side and sees that Dream is slowly fading away.{w=0.3} He attempts to reach out to the blonde when George smacked his arm away."
                     show george serious at left, shake
                     pause(0.3)
                     show sapnap pained 2 at right, bounce
                     pause(0.3)
                     show sapnap angry at right, bounce
                     S "George!{w=0.3} What th-{w=0.3}{nw}"
                     show george angry at left, bounce
                     G "{i}Don't touch him!{/i}"
                     show sapnap wary at right, bounce
                     show george cry 1 at left, bounce
                     G "He'll disappear even quicker."
                     show george cry 2 at left, bounce
                     G "Please,{w=0.3} just don't."
                     "Sapnap retracts his arm obligingly."
                     pause(1.0)
                     "Dream then gathers the strength to lift his head up from your shoulder,{w=0.3} glancing at the two."
                     "He reaches out to the both of them with his remaining hand."
                     show george shock at left, bounce
                     show sapnap shock at right, bounce
                     "Immediately,{w=0.3} both members had huddled in.{w=0.3} George had clutched at his arm even though it causes more pixels to frazzle out,{w=0.3} while the blonde had cupped Sapnap's cheek."
                     scene dreambadcg1 with dissolve:
                          xpos 0.9 ypos 0.35 xanchor 0.66 yanchor 0.77 zoom 2.8
                          ease 2 yanchor 0.62
                     pause(1.0)
                     G "Please don't go,{w=0.3} Dream."
                     G "Please don't."
                     D ".{w=0.3}.{w=0.3}.{w=0.3}"
                     S "Dream,{w=0.3} we {i}need{/i} you."
                     S "{i}Please.{w=0.3}.{w=0.3}.{w=0.3}{/i}"
                     scene dreambadcg1
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("dreambadcg1")
                     with dissolve
                     pause(1.0)
                     "He looks at them as if they were his entire world shortly before his face began to pixellate away."
                     $ scenep()
                     with dissolve
                     "They truly were his home."
                     scene dreambadcg1
                     pause(1.0)
                     scene endexitportal1
                     with dissolve
                     "And like that,{w=0.3} he's gone."
                     pause(0.6)
                     show george cry 2 at left, shake
                     show sapnap cry 2 at right, shake
                     with dissolve
                     "The remaining two let out a loud wail,{w=0.3} distressed over the loss of their dear friend."
                     hide george cry 2
                     hide sapnap cry 2
                     with dissolve
                     "You,{w=0.3} on the other hand,{w=0.3} feel nothing."
                     "The weight on your arms no longer exists."
                     "You feel numb,{w=0.3} yet you began to cry as harshly as the other two."
                     "You couldnt even bring yourself to wipe away your tears."
                     ".{w=0.3}.{w=0.3}.{w=0.3}"
                     show black:
                         alpha 0.4
                     with dissolve
                     "You knew you had to help the other two."
                     "You knew that you had to help them get out of there.{w=0.3} Get them home."
                     show black:
                         alpha 0.5
                     with dissolve
                     "But.{w=0.3}.{w=0.3}.{w=0.3}"
                     "Was it even worth it anymore?"
                     "You've seen them happy and complete a few times before this."
                     "Now,{w=0.3} you've taken the one thing that ties them all together."
                     "I'm asking you,{w=0.3} as the player,{w=0.3} as the one who's taking control of this very character."
                     show black:
                         alpha 0.6
                     with dissolve
                     "Would you still like to leave,{w=0.3} even after all that you've done?"
                     menu:
                         "{color=#e60000}No{/color}":
                             jump same
                         "{color=#e60000}No{/color}":
                             jump same

                 label same:
                     play music "audio/arcade.mp3"
                     scene endexitportal1
                     with dissolve
                     "Good choice.{w=0.3} A smart one,{w=0.3} too."
                     "There wasn't a point anymore."
                     "You glanced at the portal,{w=0.3} the vortex glitching away due to the imbalance in the timeline and the many uses of it in the past."
                     show george shock at left, bounce
                     show sapnap shock at right, bounce
                     with dissolve
                     "Sapnap and George noticed it,{w=0.3} too."
                     show sapnap wary at right, bounce
                     S "The portal.{w=0.3}.{w=0.3}.{w=0.3}"
                     show george wary at left, bounce
                     G "Shouldn't we make a run for it?"
                     menu:
                         "{color=#e60000}Stay{/color}":
                             jump same2

                 label same2:
                     show george wary at left, bounce
                     G "[povname].{w=0.3}.{w=0.3}.{w=0.3}?"
                     pov "There's no point."
                     pov "We're staying."
                     hide george wary
                     hide sapnap wary
                     with dissolve
                     show black:
                         alpha 0.8
                     with dissolve
                     pause(1.0)
                     hide black
                     with dissolve
                     "You felt something creep up your skin and looked down to see obsidian marks quickly taking over from your fingertips and toes,{w=0.3} making its way to cover everything at a quick pace."
                     scene truebadendcg with dissolve:
                         xpos 0.8 ypos 0.9 xanchor 0.66 yanchor 0.77 zoom 2.0
                         ease 2 yanchor 0.62
                     pause(2.0)
                     "You looked up to the other two,{w=0.3} who began to freak out as the same thing started to happen to them."
                     scene truebadendcg
                     $ mouse_parallax.set ((-20, -5, "l0"))
                     $ showp ("truebadendcg")
                     with dissolve
                     S "What's happening?!"
                     G "[povname]?!"
                     $ scenep()
                     with dissolve
                     "You ignore their panicked voices as a sad smile graces your face, feeling the black material reach your neck."
                     scene black
                     with fade
                     pov "That's final."
                     scene black
                     pause(1.5)
                     scene dreambadend
                     with fade
                     pause(3.0)
                     scene error
                     pause(3.0)
                     scene tverror4
                     pause(2.0)
                     XD "[povname]!!"
                     show XD wary 1 at center, bounce
                     with dissolve
                     XD "[povname]-{w=0.3} Oh,{w=0.3} thank goodness,{w=0.3} I managed to save you."
                     show XD wary 2 at center, bounce
                     XD "I accidentally messed around too much with the code this time,{w=0.3} and put everyone in danger!"
                     show XD wary 1 at center, bounce
                     XD "I could only save you.{w=0.3} I'm so sorry!"
                     show XD wary 2 at center, bounce
                     XD "I should've treated this more seriously!"
                     show XD neutral at center, bounce
                     pause(2.0)
                     show XD neutral at center, bounce
                     XD "Hm?"
                     XD "What do you mean you're asking where they went?"
                     show XD grin at center, bounce
                     XD "They all got deleted due to this bug,{w=0.3} of course!"
                     XD "They couldn't seem to get out by their own,{w=0.3} so I figured maybe you could help!"
                     show XD grin at center, bounce
                     XD "And through that,{w=0.3} I could instead take their places outside as an actual being!{w=0.3} In the real world!"
                     pause(3.0)
                     XD ".{w=0.3}.{w=0.3}.{w=0.3}"
                     pause(3.0)
                     show XD neutral at center, bounce
                     XD ".{w=0.3}.{w=0.3}.{w=0.3}You don't like that?"
                     pause(3.0)
                     show XD neutral at center, bounce
                     XD "Fine.{w=0.3} I don't care."
                     show XD grin at center, bounce
                     XD "I'll find someone else to get me out!{w=0.3} I don't need your help."
                     XD "I'll wipe away every single thing here while I see myself out. You didn't deserve the memories anyway."
                     show XD grin at center, bounce
                     XD "Good bye!{w=0.3} See you never!"
                     scene white
                     pause(3.0)
                     scene credits blank
                     with dissolve
                     pause(2.0)
                     scene credits
                     with dissolve
                     pause(2.0)
                     scene credits 1
                     with dissolve
                     pause(5.0)
                     scene credits 2
                     with dissolve
                     pause(5.0)
                     scene credits 3
                     with dissolve
                     pause(5.0)
                     scene credits 4
                     with dissolve
                     pause(5.0)
                     scene credits 5
                     with dissolve
                     pause(7.0)
                     stop music fadeout 1.0
                     scene black
                     with dissolve
                     pause(2.0)
                     $ persistent._clear(progress=True)
                     $ purge_saves()
                     return



         label endingcount:
             if ending_count == 0:
                 jump XDmeeting
             if ending_count == 5:
                 jump truerouteunlock
             else:
                 return


         label XDmeeting:
             scene white
             with fade
             pause(1.0)
             xd "Oh!"
             show XD grin at center, bounce
             with dissolve
             xd "A new player!{w=0.3} Interesting!"
             show XD neutral at center, bounce
             xd "You must be [povname]."
             show XD grin at center, bounce
             XD "I'm XD!{w=0.3} I'm in charge of everything in between here."
             XD "It seems that you've unlocked an ending!{w=0.3} That's really cool!"
             show XD neutral at center, bounce
             XD "Say,{w=0.3} if you could unlock everyone's endings,{w=0.3} maybe you can help me find a secret code!"
             XD "I've been seeing an opening here and there,{w=0.3} but I'm having some trouble in achieving the code I need.{w=0.3} Maybe it'll benefit you,{w=0.3} too!"
             show XD grin at center, bounce
             XD "But then,{w=0.3} it'll be up to you if you'd like to help me!{w=0.3} It'd be really cool if you do!"
             show XD neutral at center, bounce
             XD "Until then,{w=0.3} I'll see you next time!"
             hide XD neutral with dissolve
             pause(1.0)
             return

         label truerouteunlock:
             $ persistent.trueroute = True
             scene white
             with fade
             pause(1.0)
             XD "[povname]!"
             show XD grin at center, bounce
             with dissolve
             XD "It seems you've done what I've asked!{w=0.3} Good job!"
             show XD neutral at center, bounce
             XD "With your help,{w=0.3} I've discovered a new line of code that'll probably open up something if you run the game one more time!"
             show XD wary 2 at center, bounce
             XD "Though,{w=0.3} I have to keep an eye on it while you do.{w=0.3} Wouldn't want you to get stuck here forever!"
             show XD neutral at center, bounce
             XD "Well!{w=0.3} That'll be it from me!{w=0.3}"
             show XD grin at center, bounce
             XD "See ya!"
             hide XD grin with dissolve
             pause(1.0)
             XD "Oh!{w=0.3} Before I forget!"
             show XD neutral at center, bounce
             XD "If you see any {color=#e60000}red text choices{/color},{w=0.3} it'd be preferrable not to choose them just yet!"
             show XD grin at center, bounce
             XD "You can't take back your word,{w=0.3} after all!"
             XD "G'bye!!"
             hide XD grin with dissolve
             pause(1.0)
             return
