# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("A.R.I.E.L.")
define a = Character("Astra")
define p = Character("Planii")
define c = Character("Cinders")
define h = Character("Helix")
define s = Character("Snacky")
define n = Character(None,italics=True)
define kookykid = Character("Little Timmy")
define iratesenator = Character("Senator Bigbux")
define cc = Character("Coconut Cop")
define bb = Character("Lt. Lacey")
define j = Character("Jennifer")
define sl = Character("Crusty")
define fa = Character("Cindy Windows")
define co = Character("Coach Gogo")
define oly = Character("Judge Olimpia")
define JanusAmbrochovich = Character("Janus Ambrochovich")

image ariel = "ariel.png"
image girlbot = "ariel.png"
image boybot = "boybot.png"
image delivery = "pizzabot.png"
image deliverysmile = "pizzapal.png"
image planii = "siribot.png"
image cinders = "botbasher.png"
image street = "streetshot.bmp"
image black = "#000"
image flat = "bedroombkg.bmp"
image bathtime = "bathtime.png"
image corridor = "corridorbkg.jpg"
    
# The game starts here.

label start:
    
    $pizzaaffec = 0
    $cindersaffec = 0
    $helixaffec = 0
    $astraaffec = 0
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene supercomputerbkg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "You are gazing at a sea of red lights."
    
    n "Thousands of tiny fireflies, blinking out a morse code warning of disaster waiting to happen, while A.R.I.E.L sings sirens in her second alert frequencies, sad and high and lilting."
    
    n "A bolt of lightning touched down on one of the power regularion hubs on the east side of the city, and she's running hot under your hands." 
    
    n "The city could live with power shortages, but surges are another matter entirely.  Scorched walls and burned out access ports are the least of your worries."
    
    n "You can't help but think of the Sylph network, swollen and old and terrifyingly fragile.  You desperately don't want to be the engineer who finally sees it go down."
    
    n "But as the power surge rages through the great veins of the city, A.R.I.E.L redirects it.  Subverts the rushing currents and bends them through knots of wires laid down over centuries of infrastructure."
    
    n "A map too complex for any human mind to hold all in one time, she navigates by lodestars you can't even fathom."
    
    n "You are not the one who's going to diffuse the power surge."
       
    n "Or stop the schools or hospitals from blowing out."  
    
    n "Or keep the Sylph network online."
    
    n "The A.R.I.E.L system keeps the city alive." 
    
    n "You simply do your small part to keep her online.  Like a worker bee serves a queen."
    
    e "Power Rerouted."
    
    e "Exess Energy Diffused."
    
    e "Resuming Standard Functionality"
    
    n "As her temperatures return to their normal parameters, the bright red lights blink out into soothing flecks of green."
    
    n "You click the temperature on the cooling system back down to it's standard level, and close her console over.  The interface in my lap chimes out a five minute warning."
    
    n "Your shift is about to end."
    
    show ariel at top

    e "Employee #46803."
    
    n "You freeze.  You've heard A.R.I.E.L.'s voice a thousand times... but she doesn't talk to you.  She doesn't talk to anyone."

    e "Employee #46803, I have a serious enquiry requiring your attention."
    
    $player_name = renpy.input("In the company of your human peers, what name do you prefer to go by?")

    $player_name = player_name.strip()
    
    if player_name == "":
        $player_name="Employee #46803"

    player_name "Uh, it's-- My name is [player_name]!  It's-- It's an honour to finally--"
  
    e "Today we encountered 16 minor errors and one major power surge, leading to a sudden spike in my core temperature.  Statistically, that indicates a particularly challenging day for you."  
    
    player_name "Oh, well-- You did all the work.  All I had to do was--"
    
    e "You maintained my core temperature, during a volatile period of my performance.  Well done, [player_name]."
    
    e "I have marked my accolades in your performance records.  That will be all."
    
    player_name "Th-thank you?"
    
    n "She says nothing.  Her lights blink, silent and serene, as if your brief exchange never happened at all.  The Interface pings to life with the details of one of your incoming colleagues."
    hide ariel
    n "The message is clear:  Your shift is over.  It's time to go home."

    scene street
    with pixellate 
    
    n "You emerge onto the dark streets, too alert and awake for the late hour.  You feel restless and distracted."
    
    n "So much so, that you don't even notice yourself reaching for your ad-supported Planii Compu-panion, until she's springing to life in your hand."
    
    show planii at topleft
    
    p "Good evening, [player_name]."
    
    menu :
      
        "Hey Planii, how's it hanging in cyberspace?":
      
             p "Would you believe, I couldn't say?  Analysing how gravitational forces may or may not impact 'how it hangs' in cyberspace is a little beyond my processing power."
   
             p "Perhaps one day you'll plug into the Sylph net, [player_name].  Then you could find out for yourself."
   
             player_name "Maybe if A.R.I.E.L glitches out and accidentally drops someone else's salary into my bank account.  Until then I think I'm stuck here in meatspace with the rest of the flesh puppets."

             p "At least it hasn't impacted your self esteem."
    
        "Wait, I didn't mean to turn you on...":
   
             p "Of course you did.  At 7:59 am on the 9th of December, you asked me to set a reminder for this date and time."
      
             player_name "But I didn't hear an alarm or anything, I just came out of work, and when I looked down your console was in my hand."

             p "That's right.  I've noticed you ignore a lot of your own reminders, so with my last update I upgraded your reminder with my new autothink check-in feature.  It's all in your terms of service."
      
             n "Oh no..."
      
             n "She thinks you've been missing those reminders to go to the gym and call your parents by accident. Apparently Planii doesn't understand the concept of being a good old fashioned flake."
      
             p "You'll never miss a work out again."
      
             n "Or... maybe she's just screwing with you?  Can a Planii screw with you?"
      
             p "Pretty cool, right?"
      
             menu:
        
                 "So cool.":
                 
                    n "...You think it's very cool."
        
                 "Uhhh...":
                 
                    n "..."
   
    p "You wanted me to remind you to do something special for Cinders tonight.  Both to celebrate St. Valentines day, and in preparation for your upcoming six year anniversary."
    
    player_name "What, already?"
    
    n "You and Cinders have never done anything for Valentines day, even though your anniversary is only a week later."
   
    n "You both always found it sort of forced and corporate.  An easy way for big companies to make money off gullable people and sentiment."
    
    n "But Cinders has been quiet lately.  They won't talk about it, but they seem thoughtful and maybe even a little sad."
       
    n "You can still see in them the fierce, smoldering energy that stole your heart, but right now, what should be an inferno, is little more than a pile of embers..."
    
    n "Maybe a little dumb, corporate sentimentality is just the thing to get that furnace lit again?"
    
    player_name "You're right, Planii.  Thanks for reminding me."
    
    p "It's what I'm here for.  Shall we make a Plan(ii)(tm)?"
    
    player_name "Yeah-- yeah, let's do that.  Uh, I guess we should order food, rent a movie or something, and-- maybe I should grab them a gift?"
    
    p "You still have 56 minutes before the click and collect store closes."
    
    p "I estimate that you'll be home for 8:00 pm, and based on your past habits you require roughly 50 minutes to complete a high maintainance grooming cycle.  What time should I invite Cinders to come over for?"
 
    menu :
      
        "8:50 PM":
      
             p "Okay.  I've invited Cinders to arrive at YOUR FLAT at 8:50 PM.  You'll have to move quickly."
    
        "9:00 PM (Planii Reccommends)":
            
             p "Okay.  I've invited Cinders to arrive at YOUR FLAT at 9:00 PM."
                 
        "9:30 PM":
            
             p "Okay.  I've invited Cinders to arrive at YOUR FLAT at 9:30 PM."
        
        "10:00 PM":
        
             p "Okay.  I've invited Cinders to arrive at YOUR FLAT at 10:00 PM."
        
        "10:30 PM (Not Reccommended)":
   
             p "WARNING: You have suffered 9 incidents of severe flatulence over the last 5 months, which seem to correllate to periods of irregular eating patterns and lack of sleep."
             
             p "Are you sure you want to schedule your date this late?"
             
             menu :
                 
                 "Yes.":
                     
                     p "Okay.  I've invited Cinders to arrive at YOUR FLAT at 10:30 PM."
                     
                 "...Fine, make it earlier.":
                     
                     p "An excellent decision.  I've invited Cinders to arrive at YOUR FLAT at 9:30 PM."
    
    p "Based on your collective shopping and streaming habits, I have a few recommendations for immersive features you could watch together.  Would you like to hear them?"
    
    player_name "Planii, you're a lifesaver.  Hit me with our best options..."
    
    label filmchoice:
        menu:
            "Coconut Cop and the Case of the Corrupt Congressman":
                hide planii

             
                "{i}From the industrial coconut plantations of the carribean...{/i}"
                "{i}To the mean, mean streets of Los Angeles...{/i}"
                "{i}One man has fought his way through adversity in pursuit of justice, and now he's ready to throw the book all the way to Washington D.C...."
                "{i}THIS SUMMER!{/i}"
                "{i}Get ready for suspense...{/i}"
                kookykid "If we're right about this, Cee Cee, this goes all the way to the top.  None of us are safe!"
                "{i}Danger...{/i}"
                iratesenator "Listen officer, I don't know how they do things on that backwater island you come from, but this is America!  If you bought a plane ticket over here, then let the buyer beware!"
                "{i}And romance...{/i}"
                bb "Oh Coconut Cop, can't you see it isn't worth it?  I don't {i}care{/i} who profited off the building of the New England Water Purification and Irrigation Facility, all I care about is you!"
                "{i}In what is sure to be the smash hit of the summer...{/i}"
                cc "Looks like America will be one tough nut to crack!"
                "{i}Coconut cop and the Case of the Corrupt Congressman!{/i}"
                show planii at topleft
                player_name "Cinders {i}does{/i} love coconuts."
                player_name "And they really hate the government."
                
             
                menu:
                    "This is the film for us.":
                        $film = "coconuts"
                        $cindersaffec +=3
                    "What were the other options again?":
                        jump filmchoice
                
      
            "A Slice of Life":
                hide planii
            
                "{i}After six years in the Marines, eight years smelting iron in Tennesee, and six months working as a barista in Manhattan, Jennifer Frost is cool as ice!{/i}"
                j "Outta my way!  I'm walkin' here!"
                "{i}When she takes a new job at a failing Pizzeria as a favour to a family friend, she thinks she knows what she's getting into.{/i}"
                j "Another dumb college kid trying to sell Cauliflower Pizza Crust in NYC?  Yeesh, you need all the help you can get."
                "{i}Toss a little dough, slice a little sauseage, melt some cheese and save the business!{/i}"
                j "I know, I know, you can't afford my day rate.  I'll take my pay once I've made you your first hun-thou."
                "{i}Little does she know, that between the anchovies and the olives, she's about to find something incredible...{/i}"
                j "Wh- What is this?  Who are you?"
                sl "Don't be scared! ...I just wanted to see you."
                "{i}Sparks fly in this bold summer romance...{/i}"
                j "Your name is Crusty, huh?  Just tell me you ain't Gluten Free?"
                "{i}But is the world ready for their love?{/i}"
                sl "I saw the look on your face when your mother came in.  You're ashamed of me..."
                "{i}One woman...{/i}"
                j "Don't do this to me, Crusty"
                "{i}One Pizza...{/i}"
                sl "When I look at you, I feel like I'm burning up inside.  Like someone's put my back in the oven and I never want to come back out!"
                "{i}One last chance..."
                j "It's not just the cheese, Crusty.  I'm the one who's melting.  I'm the one who's melting..."
                show planii at topleft
            
                player_name "I want to see this film so bad!"
                player_name "But Cinders has a lot of problems with the dairy industry... I can't tell if they'd like this..."
                menu:
                    "This is the film for us.":
                        $film = "pizzakisses"
                        $cindersaffec -=1 
                        $pizzaaffec +=2

                    "What were the other options again?":
                        jump filmchoice        
        
            "Cool Roombas!":
                hide planii
                "{i}The Year is 2079.{/i}"
                fa "We're here today for the final qualifying round of next year's Summer Olympics!"
                "{i}And history is about to be made.{/i}"
                fa "Janus Ambrochovich has just scored a perfect ten on the triple jump, securing Romania's place in the finals!"
                "{i}Based on the shocking true story...{/i}"
                fa "Next up, we have the Scottish triple jump team entering the gym and-- Oh, no, there seems to have been a mistake..."
                "{i}First they ignore you.{/i}"
                co "Could someone get the cleaning crew out of the gymnasium?"
                "{i}Then they mock you.{/i}"
                oly "I'm sorry, there's no way that the Scottish Qualifying Team for the Olympic Triple Jump can be made up entirely of Roombas, that makes no sense.  They don't even have legs!"
                "{i}Then they fight you.{/i}"
                JanusAmbrochovich "You may have made it to the olympics, Roombas, but I'm gonna send your haggis hoovering asses bouncing back to Balmoral!"
                "{i}Then you win.{/i}"
                fa "And the gold medal for the triple jump, in the 2080 Berlin Olympics, goes too..."
                co "...My god"
                "{i}Available through all good feature streams."
                fa "They might spend every day down in the carpet, but I guess they've been dreaming of the stars..."
                show planii at topleft
                #get a sound file for the music a roomba makes when it's done cleaning
 
                player_name "This is a nostalgic classic!"
                player_name "Whatever's been going on with Cinders, there's no way that Cool Roombas won't cheer them up!"
                    
                menu:
                    "This is the film for us.":
                        $film = "coolroombas"
                        $cindersaffec +=1
                        $pizzaaffec +=3

                    "What were the other options again?":
                        jump filmchoice 
                        
    p "Nice choice [player_name]!  And will you be purchasing Cinders a gift as well?"
    player_name "Yeah, I still have time to get to the click and collect, right?"
    p "Even at your usual walking pace, you should arrive with 20 Minutes left before it closes!  Would you like to hear about their Valentines Day Deals?"
    player_name "Uh, sure.  What have they got?"
    
    label giftchoice:
        menu:
            "Roses":
                p "12 Red Roses, wrapped in pastel blue gift paper.  This classically romantic gift is available for only 140 credits."
                
                menu:
                    "Perfect!":
                        $gift = "roses"
                        $cindersaffec -=1
                    
                    "Wait, what else was there?":
                        jump giftchoice
                
            "Wine":
                p "A rich and fruity Australian Merlot, with hints of nutmeg and honeysuckle, sure to go straight to your lover's head!  One bottle costs only 200 credits!"
                menu:
                    "Delicious!":
                        $gift = "wine"
                    
                    "Wait, what else was there?":
                        jump giftchoice
                        
                    "Straight to my lover's head?  What is this ad copy implying?":
                        p "Oooh, good point!  I'll report your discomfort to the Click and Collect content review board!"
                        $cindersaffec +=1
                        jump giftchoice
                        
            "Chocolates":
                p "From the cocoa trees of Ecuador, to the vanilla harvests of Madagascar, we've brought you flavours and fragrances from across the known world, and creamed them into a box of the most toe curlingly luxurious chocolates ever to pass your lover's lips!"
                menu:
                    "Yum!":
                        $gift = "chocs"
                        $cindersaffec -=3
                    "Wait, what else was there?":
                        jump giftchoice
                    "There's no way those have been ethically sourced...":
                        p "Hmm..."
                        p "The manufacturer hasn't provided any information on how the ingredients were sourced.  But it's not impossible that they're traded fairly."
                        player_name "Don't play dumb, Planii.  If a company is making fair deals with farmers in Ecuador and Madagascar, they're going to make damn sure that we all know about it."
                        player_name "And if it's obvious to me, then it'll be super obvious to Cinders.  Remember the fight we had over the molassas trade last year?"
                        p "Point taken.  We live in an imperfect world."
                        player_name "Yeah.  Still, the very least I can do for our Valentiversary, is avoid things that I know are going to make Cinders complicit in something I know they hate."
                        p "Well, you still have the other options!"
                        $cindersaffec +=1
                        jump giftchoice
                
            
            "I think Cinders would really hate all this stuff...":
                player_name "That stuff... it represents all the things that I know Cinders hates about Valentines Day.  Token gifts from gullable and sentimental idiots.  I don't want them to think of me like that."
                p "Well, what kind of gift do you think Cinders would want?"
                player_name "Something to challenge them... maybe a book?"
                p "Hmm."
                p "There only book on their Click and Collect wishlist is called {i}Freedom, Truth, and The Trial of Socrates{/i}.  It might be a little heavy going for a Valentiversary gift..."
                menu:
                    "Nothing's too heavy for Cinders!  It's perfect!":
                        $ gift = "socrates"
                        $cindersaffec +=3
                    "Maybe you're right... what were the other gifts?":
                        jump giftchoice
    
    p "You order is placed, and will be giftwrapped and ready to collect in ten minutes time!"
    p "This is perfect!  The only thing left to do is to order food, would you like me to bring up some options for local--"
    player_name "That won't be necessary, Planii.  I already know exactly what we're getting to eat."
    p "Oh?"
    player_name "Traditional Fish and Chips, from Snacky Deliveries!  It was what Cinders was eating the first time I saw them... I'd just gotten out of the most dreary work party, and they were lining their stomach before going to an all night rave..."
    player_name "Our eyes met over the condiment tree in the Snacky Snack Hut, and--"
    player_name "Well.  I didn't end up going home that night.  Cinders changed me forever.  I feel like they're always dragging me into the unknown, just like they did that night..."
    player_name "So yeah.  I know what food I'm ordering.  Traditional Fish and Chips from Snacky."
    p "That's so romantic."
    p "Okay, I've logged your food order.  It'll be delivered promptly in a heat keeper cloth, so it's hot and fresh whenever you two lovebirds are ready for it!"
    p "Now, it's time to put this Plan(ii)(tm) into action!"
    player_name "Hell yeah!"
    
    hide planii
    
    n "Planii dissipates into a cloud of holographic light, before slipping into energy saver mode."
    n "You still feel that same, nervous, restless energy, but it feels better somehow.  Now, that energy is full of purpose, and your mind is filled with thoughts of your beloved Cinders."
    n "Your heart feels light, giddy, even, as you hurry home to your apartment."
    
    scene black with pixellate
    
    n "Your keys fumble in the lock, although you know there's no great hurry."
    n "You still have almost a full hour before Cinders should arrive.  Plenty of time to get cleaned up and set up the house for a date..."
    n "The excitement of doing something nice for them is getting to you, that's all."
    n "Your key turns in the lock."
    
    scene flat with pixellate
    #maybe swap this image out for the corridor
    n "The door swings open, and you're bathed in the warm familiar glow of artificial lights.  You toss your keys in the bowl by the door and head straight for the shower."
    #then a shower image
    player_name "Planii, set my water-temp for a shower please?"
    scene bathtime with pixellate
    n "Planii makes a bright little chirp of confirmation, as you shed your work clothes and turn on the water."
    n "You step into the shower.  It is perfectly warm."
    n "The water pressure beats a soothing pattern out against your skull, drowning out any noise and thought that might distract you from the pure pleasure of getting clean."
    n "That's why you don't hear anything outside.  Not until it becomes impossible to ignore."
    n "Not until the bathroom door creaks open."
    player_name "Wh-What the hell?  Who's there?"
    n "An unseen hand seizes the shower curtain.  You suddenly feel extremely vulnerable..."
    player_name "Hey, get the hell out of here!"
    n "You look around frantically for a weapon..."
    menu:
        "Grab the shampoo!":
            
            n "As you struggle frantically to open the slippery shampoo bottle, the shower curtain is yanked back to reveal your would be assailant--"
            show cinders at topright
            c "Comrade [player_name]!"
            player_name "C-Cinders?"  
            player_name "{i}Cinders, what the hell?{/i}  You scared me!"
            n "You jab the shampoo at them.  Cinders looks briefly perplexed."
            c "Comrade [player_name]... doesn't that brand of shampoo contain... sulphides?"
            menu:
                "Of course not!":
                    $cindersaffec +=2
                    c "No, of course it doesn't--  Forgive me, Comrade [player_name], I should have known you would never do that..."
                
                "...I forgot to check.":
                    $cindersaffec -=2
                    c "...Of course you did."
                    
            
        "Grab the loofa!":
            n "You snatch up the soapy loofa, and hold it out in front of you like a small, frilly shield, as the shower curtain is yanked back to reveal--"
            show cinders at topright
            c "Comrade [player_name]!"
            player_name "C-Cinders?"  
            player_name "{i}Cinders, what the hell?{/i}  You scared me!"
            n "Your arms begin to relax, and Cinders looks at what you're holding."
            c "Comrade [player_name]... if I was truly an intruder, were you planning on fighting me off with that... loofa?"
            menu:
                "What?  N--no!":
                    $cindersaffec +=1
                    c "By the helix, but you're adorable."
                    c "I'm sorry that I startled you, Comrade [player_name]."
                
                "Cinders, if you don't get out of my shower I might {i}still{/i} kick your ass with this loofa!":
                    $cindersaffec +=3
                    n "Cinders gazes into your eyes, and you feel your stomach do a little flippy flop of attraction.  God, they're so intense."
                    c "...I believe you."
                    n "They take a respectful step back, allowing you space to get out of the shower."
                    
        "Grab the shower head!":
            n "You grab the shower head in both hands, aiming it squaredly at your assailant, as the shower curtain is yanked back to reveal..."
            show cinders at topright
            c "Comrade [player_name]!"
            player_name "C-Cinders?"  
            player_name "{i}Cinders, what the hell?{/i}  You scared me!"
            n "Cinders is slowly soaked through by the shower water."
            c "...You really do set your showers to the perfect temperature, Comrade [player_name]."
            c "But such luxuries have estranged us from the struggle for too long!"

                                                                               
    c "I'm afraid we need to talk."
    
    if cindersaffec <=5:
    
        c "Comrade [player_name], there is something wrong with society."
        c "In the last year alone there have been starvation riots in Liverpool and Newcastle.  We live in one of the richest nations on earth, but people are freezing to death in their homes!"
        c "People are dying for want of food and medication, things we have in such disgusting excesses that they rot in landfills rather than going to the people who need them!"
        
        menu:
            "I know it's bad, but sometimes people make bad choices...":
                
                c "Bad choices?  Like the {i}choice{/i} to sell off the industries that created jobs in those regions?  Or the choice to shift this nation onto an economy run by customer service and corrupt finance?"
                c "People in the North have been left with an economy which strangles social mobility.  Even efforts to make it out of the dead-end customer service industries mean taking on a risk that could leave them destitute!"
                c "Worst of all!"
                c "The rise of automation, that should have meant a freedom from labour and scarcity, has removed even the weak commercial lifeline that those regions had left."
                c "Did people who were loyal to their employers only to be forced out of their jobs by cheap machine labour choose {i}that?{/i}"
            
            "Why are you telling me this when there's nothing I can do to fix it?":
                
                c "Isn't it obvious?"
                c "Because there is something you could do if you had the nerve."
                c "And I intend to do it."
        
        c "We've been shielded from the suffering caused by automation here.  That all seeing eye that you service keeps the city at the heart of the tech world, so there's still money and opportunity here."
        player_name "...I guess we should be more grateful for that."
        c "Grateful?"
        c "Grateful to remain blinded by blissful ignorance while the world outside crumbles?"
        c "You are dancing at the Masque of the Red Death, Comrade [player_name]."
        c "But I can wear the shroud no longer!"
        c "I'm leaving."
        player_name "What?  Where are you going?"
        c "North.  There's an anarchist collective building a co-operative in the heart of Leeds.  They've destroyed the tiles of an abandonned office and are converting it into an illegal indoor allotment."  
        c "In the long run, we want emancipation from a corrupt state.  In the short term, we'll settle for growing cheap food and bringing back those service jobs.  By force if necessary."
        player_name "By force?"
        c "It's only cheaper for businesses to switch to automation if their customer service bots don't get smashed on the reg."
        c "We're gonna make the poorest neighborhoods no-go zones for anything with gears!"
        menu:
            "...I understand.":
                $cindersaffec +=3
                c "Thank you, Comrade [playername]."
                c "Truth be told, I considered asking you to come with me.  For this to be the next leap into the dark we take."
                c "But I've noticed, the longer we're together... I've become more and more like you."
                c "More complacent, more lazy."
                c "...It was too easy to simply be content with love, and stop demanding better of the world."
                c "But I don't want to be that person, Comrade [playername]."
                c "And as much as my heart still aches for you..."
                
            "That can't be the solution to this!":
                c "So what is the solution?  To simply do nothing?  To wait for the problem to save itself?"
                player_name "Technology isn't going to go backwards just because the way it's used is hurting people!  All you can do down there is cause more damage and buy a little time!"
                c "How can you not understand that some people {i}need{/i} that time bought for them?"
                c "Obviously there are long term problems that this won't fix, but people are starving!  They're losing their homes!  There are human beings out there who can't just wait around for a long term solution!"
                c "Besides, you only hear those high and mighty claims about long term solutions from people who are buying time for themselves."
                c "If there's another solution, don't tell me about it.  Make it happen yourself."
                c "Otherwise... no matter what you and I might have once had..."
                
            "But it's Valentines Day!":
                c "..."
                c "Are you serious?"
                menu:
                    "Psyche!  I'm kidding.":
                        c "Ha!  You can still surprise me after all this time."
                        c "That's why you're so dangerous.  I could sink into the haze of my love for you, and spend the rest of my life in perfect happiness."
                        player_name "Then why don't you?"
                        c "Because... there is more to this life than happiness." 
                        c "The unexamined life is not worth living."
                        c "That's why, even if I do not wish to face it..."
                    "Serious as a heart attack.":
                        c "..."
                        c "All the time we've been together, I have feared losing myself to you."
                        c "My only consolation was the belief that you had jumped headlong into the same danger.  That you knew me, and you loved me.  Hard edges and all."
                        c "..."
                        c "{b}{i}It's Valentines Day?{/i}{/b}"
                        c "{b}{i}SERIOUSLY?{/i}{/b}"
                        player_name "I'm sorry!  I just--"
                        c "You thought you could persuade me to stay with you by appealing to the most {i}{b}BASE, CORPORATE, SHALLOW{/i}{/b} repackaging of our love?"
                        c "Did you know me so little?"
                        player_name "Cinders, of course I--"
                        c "{b}{i}DID YOU EVEN CARE AT ALL?{/i}{/b}"
                        c "..."
                        c "You have torn out my heart."
                        c "{i}Valentines Day...{/i}"
                        c "If I have to hear about that vapid, awful, insult to a holiday one more time..."
        
        #Doorbell noise
        label badbreakup:
            n "Cinders is cut off by the sound of the doorbell.  They take a step back, allowing you to grab a towel and step out into the hall."
        
            scene corridor
            show delivery at top
        
            s "Snacky Auto-Delivery Service, reporting for [player_name]!"
            player_name "Sorry, but we're kind of in the middle of something here!"
            show cinders at topright
            c "On the contrary, I think we're past {i}the middle{/i} of this, Comrade [player_name]"
            c "We are beyond the point of no return."
            hide delivery
            show deliverysmile at top
        
            n "The smile on the Delivery bot's face falters for a moment, but it's clearly programmed to complete it's schpiel:"
            s "But... we bring sweets to your sweet this St. Valentines Day?"
            c "Comrade [player_name]... It's time for me to accept that you're part of the problem."
            c "Goodbye..."
            c "{i}Forever!{/i}"
            n "With a sweep of their arm, Cinders shoves your wall mounted flatscreen entertainment engine to the floor with a crash, before running off down the corridor in a streak of yellow jumpsuit and class warfare."
            hide cinders
            n "Even after insulting you, humiliating you, and destroying your entertainment engine, you can't help but feel a familiar tug in your stomach."
            n "You hate to see Cinders go... but you love to watch them leave."
        
    else:
            
        c "Comrade [player_name], there is something wrong with society. I know you see it too."
        c "In the last year alone there have been starvation riots in Liverpool and Newcastle.  We live in one of the richest nations on earth, but people are freezing to death in their homes!"
        c "People are dying for want of food and medication, things we have in such disgusting excesses that they rot in landfills rather than going to the people who need them!"
        c "I know you hate to hear this."
        
        menu:
            "It's hard listening to this when there's nothing I can do about it.":
                
                c "And what if there was something you could do about it, if you had the nerve?"
                c "Something we could both do, Comrade [player_name]?"
            
            "Even it if hurts to hear about this stuff, it would be worse to pretend it isn't happening.":
                
                c "I agree.  This is not about our guilt, it's simply about {i}notice.{/i}"
                c "If we aren't even prepared to stare down the suffering of others in the world, how could we ever hope to change it?"
                c "Discomfort and guilt aren't useful, but they're a human reaction to awareness, and without awareness, all is lost."
        
        c "We've been shielded from the suffering caused by automation here.  That all seeing eye that you service keeps the city at the heart of the tech world, so there's still money and opportunity here."
        c "Enough to keep us comfortable.  Blinded by blissful ignorance while the world outside crumbles."
        c "We are Prospero's courtiers, dancing at the Masque of the Red Death, Comrade [player_name]."
        c "Tear the scales from your eyes, my love!"
        c "Let's get out of this shithole town."
        player_name "What?  Where would we go?"
        c "North.  I've made contact with an anarchist collective in the heart of Leeds."  
        c "We could start over there.  Fight for our emancipation from a corrupt state, serve the communities that we're currently starving out."
        c "Automation of the service industry will cut off a financial lifeline to the north.  We join our Comrades, and stop that from happening."
        player_name "Wait-- You want us to fight back against automation?"
        player_name "But it's everywhere!  We might as well fight the tides!"
        c "That's why we have to do this.  The future is being decided here and now, and the world isn't ready for automation."
        c "I can't accept that we're helpless in our own lives.  We'll use force if we have to!  Keep taking out the service drones until the cost of replacing them becomes impossible to justify!"
        menu:
            "...Cinders, this is crazy.  There's no way I'm doing this with you.":
                c "..."
                c "Helix be damned."
                c "I thought-- I thought you understood.  Have I looked too much for myself in you?"
                player_name "It's not that I don't agree with what you're saying, I know things are bad in the north."
                c "Just not bad enough to be your problem?"
                player_name "I didn't say that."
                c "But you won't act on your convictions, so what should I care what you say?"
                c "You're very good at saying the right things, [player_name], but when the time comes for you to act..."
                c "I see how the cards fall..."
                jump badbreakup
                
            "...Screw automation, let's go save the world!":
                
                c "..."
                c "Every time I put my faith in you, [player_name], I find it rewarded."
                c "I've known so many people who would toast to revolution, but would not drink from that bitter cup with me."
                player_name "I'm the real deal, Cinders.  Automation is a blight on the proletariat, and we can abide it no longer."
                c "To the north!"
                player_name "To the revolution!"
                c "Vive La France!"
                player_name "Eat the rich!"
                c "Liberals get the bullet too!"
               
                #doorbell 
                
                n "Cinders is cut off by the sound of the doorbell.  They take a step back, allowing you to grab a towel and step out into the hall."
        
                scene corridor
                show delivery at top
        
                s "Snacky Auto-Delivery Service, reporting for [player_name]!"
                player_name "Sorry, but we're kind of in the middle of something here!"
                show cinders at topright
                c "..."
                c "Comrade [player_name]."
                c "Are you kidding me?"
                player_name "I can explain..."
                c "Automation is a blight on the proletariat?"
                
                hide delivery
                show deliverysmile at top
            
                n "The smile on the Delivery bot's face falters for a moment, but it's clearly programmed to complete it's schpiel:"
                s "Um... we bring sweets to your sweet this St. Valentines Day?"
                c "You said we were going to eat the rich--"
                s "Savories for hot babeories?"
                c "Instead it appears your mouth is filled with the lies of the bourgoirse!"
                player_name "This isn't what it looks like!"
                s "Fresh bread for the unwed?"
                c "You decietful champagne socialist centrist liberal {i}scum{/i}!  I trusted you!"
                player_name "It's just--"
                s "Oh, this seems really bad..."
                c "I loved you!"
                player_name "It's just one takeaway"
                c "It's not about one takeaway!"
                c "It's about how you can order food from a massive corporate monopoly of automation, then half an hour later you look me in the eye and tell me how evil you think it is."
                c "Either you know you're supporting something wrong, but you just don't care..."
                c "...Or you can look me in the eye and lie to me about the things you know mean everything to me."
                c "Either way, I will not be decieved by you."
                c "Goodbye..."
                c "{i}Forever!{/i}"
                n "With a sweep of their arm, Cinders shoves your wall mounted flatscreen entertainment engine to the floor with a crash, before running off down the corridor in a streak of yellow jumpsuit and class warfare."
                hide cinders
                n "Even after insulting you, humiliating you, and destroying your entertainment engine, you can't help but feel a familiar tug in your stomach."
                n "You hate to see Cinders go... but you love to watch them leave."
                
        
                
            "I don't know if I can do this.":
                c "Comrade [player_name]..."
                c "I know, even for us, this is a big step to take.  It's a leap into the unknown that you might not be prepared for..."
                c "I have come to the realisation that this is the next step for me, wherever it leads."
                c "I'm asking you to come with me because I love you, and I believe in you, but ultimately the choice is yours to make."
                player_name "It's just that..."
                menu:
                    "What you're suggesting really scares me.":
                        player_name "You've always pulled me out of my comfort zone, and I love that about you.  I feel like I've grown and learned from you in ways I can't describe..."
                        player_name "But there's still too much that I value here for me to let it go.  I love the city.  I love the wilderness of ideas and cultures we have here."
                        player_name "I understand why you're angry, and why you have to do this, but I don't think I can go with you this time."
                        player_name "...I'm sorry."
                        c "Comrade [player_name]..."
                        c "How could I love you if you were nothing but a mirror of myself?"
                        c "Be ready, Comrade.  For we know not the hour that the revolution cometh, but on that day there will be blood in the streets.  There will be wailing and gnashing of teeth."
                        c "Goodbye."
                        n "Cinders kisses you, deeply and with great import.  Like they're sending one last, vital message directly into your mouth via morse code."
                        n "Then their hand drops from your cheek, they pull the shower curtain closed again in front of you, and you hear their footsteps recede."
                        n "When you get out of the shower, you will find your wallet empty and some of your more expensive electrical equipment is missing."
                        n "Cinders is gone forever." 
                        #doorbell 
                
                        n "Your chest feels tight.  You grab a towel and step out into the hall."
                        n "The doorbell sounds again, and for an irrational moment, you think perhaps it's them.  That Cinders got into the corridor and was struck with regret."
                        n "That they've changed their mind about leaving you."
                        
                        scene corridor
                        show delivery at top
        
                        s "Snacky Auto-Delivery Service, reporting for [player_name]!"
                        player_name "...Oh."
                        n "...You feel {i}unforgivably{/i} fucking stupid."
                        
                        hide delivery
                        show deliverysmile at top
            
                        n "The Delivery Bot springs open, eyes bright with artificial happiness."
                        s "Hi there, [player_name]! Snacky Auto-Delivery Service here, with sweets for your sweet this St. Valentines Day!"
                        n "The savory aroma of fish and chips wafts up to you from the Bot's carefully wrapped parcel."
                        player_name "..."
                        n "You have to say something.  The Bot is staring at you with it's bright eyes, waiting for you to acknowledge it."
                        player_name "..."
                        n "It smells just like the chip shop where you first met."
                        n "You can't help it."
                        n "Your eyes well up with tears, and you gasp, turning away so that the Snacky Delivery Bot can't see you cry."

                        
                        
                
                    "Automation isn't our real enemy.":
                    
                        player_name "I know you don't want to hear this... but I can't accept that automation is the problem."
                        player_name "Human being shouldn't be spending thirty years of our lives weighing potatoes and bagging up groceries just to stay above the poverty line."
                        player_name "I understand why you're angry, and I understand why you want to do this, but-- you're fighting the wrong battle here."
                        player_name "...We need to restructure society in a way that people can be set free by automation, not driven to desperation by it."
                        c "You may be right, Comrade [player_name]..."
                        c "But how much suffering will the people be forced to endure before those who hold the power learn that lesson?"
                        c "Perhaps you can begin fighting that battle here, while I go north?" 
                        c "When we meet again, we could be living in a very different world."
                        c "Be ready, Comrade.  For we know not the hour that the revolution cometh, but on that day there will be blood in the streets.  There will be wailing and gnashing of teeth."
                        c "Goodbye."
                        n "Cinders kisses you, deeply and with great import.  Like they're sending one last, vital message directly into your mouth via morse code."
                        n "Then their hand drops from your cheek, they pull the shower curtain closed again in front of you, and you hear their footsteps recede."
                        n "When you get out of the shower, you will find your wallet empty and some of your more expensive electrical equipment is missing."
                        n "Cinders is gone forever."
                        
                        #doorbell 
                
                        n "Your chest feels tight.  You grab a towel and step out into the hall."
                        n "The doorbell sounds again, and for an irrational moment, you think perhaps it's them.  That Cinders got into the corridor and was struck with regret."
                        n "That they've changed their mind about leaving you."
                        
                        scene corridor
                        show delivery at top
        
                        s "Snacky Auto-Delivery Service, reporting for [player_name]!"
                        player_name "...Oh."
                        n "...You feel {i}unforgivably{/i} fucking stupid."
                        
                        hide delivery
                        show deliverysmile at top
            
                        n "The Delivery Bot springs open, eyes bright with artificial happiness."
                        s "Hi there, [player_name]! Snacky Auto-Delivery Service here, with sweets for your sweet this St. Valentines Day!"
                        n "The savory aroma of fish and chips wafts up to you from the Bot's carefully wrapped parcel."
                        player_name "..."
                        n "You have to say something.  The Bot is staring at you with it's bright eyes, waiting for you to acknowledge it."
                        player_name "..."
                        n "It smells just like the chip shop where you first met."
                        n "You can't help it."
                        n "Your eyes well up with tears, and you gasp, turning away so that the Snacky Delivery Bot can't see you cry."
                        s "Oh no, please don't be upset!"
    
    s "Was it-- was it something I said?"
    menu:
        "I think you've said enough, Snacky.":
            player_name "What the hell is wrong with you?"
            player_name "Read the room you rusted robot-wars reject, my life just got completely torn apart"
            n "It's not the Delivery Bot's fault, but you can't think straight.  Your relationship with Cinders was always turbulent, but your heart is aching right now."
            s "I'm so sorry.  I only wanted to--"
            player_name "I don't want to hear it right now.  Just get out of here."
            s "But--"
            s "What about your food?"
            menu:
                "Take the food.":
                    n "You stiffly reach down to scoop up the bundle of fish and chips, before turning to storm back into your flat."
                    n "The delivery bot says nothing more behind you, but you hear the door click shut behind you, before the whirr of tiny wheels recede down the hall."
                    hide deliverysmile
                    n "You feel like total shit."
                    $pizzaaffec -=1
                "THE FOOD IS DEAD TO YOU.":
                    player_name "Do I look like I care about food right now?"
                    player_name "Give it to the homeless, hell, throw it in the trash.  I don't care if you stuff it up your exhaust, just get it out of my face"
                    n "The Delivery Bot looks about as shaken as a digital face on a screen can look, but it makes no further comment.  It's hatch swings shut sadly."
                    hide deliverysmile
                    show delivery at top
                    player_name "That's right, walk away.  Leave me, just like everyone else has."
                    n "Compliant till the end, the Delivery Bot leaves you."
                    hide delivery
                    n "Just like everyone else has."
                    
                    $pizzaaffec -=3
        "It's not your fault...":
            player_name "I'm sorry you had to see that.  It's not your fault that you've gotten caught up in the middle of this."
            player_name "Read the room you rusted robot-wars reject, my life just got completely torn apart"
            n "It's not the Delivery Bot's fault, but you can't think straight.  Your relationship with Cinders was always turbulent, but your heart is aching right now."
            s "I'm so sorry.  I only wanted to--"
            player_name "I don't want to hear it right now.  Just get out of here."
            s "But--"
            s "What about your food?"
            
    # This ends the game.

    return
