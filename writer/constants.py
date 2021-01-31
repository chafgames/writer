from pkg_resources import resource_string

bar_order_prompt = f"{resource_string('writer.art', 'restaurant').decode('utf-8')}\nWhat should you order at the bar for the stranger?"
bar_order_button_1_text = 'Black Coffee'
bar_order_button_1_resp = 'The bartender shrugs as you bring the coffee over to the stranger.'
bar_order_button_1_jump_to = 'stranger_convo'
bar_order_button_2_text = 'Franziskaner Weissbier'
bar_order_button_2_resp = "\"Are you sure you don't want to order for two?\". The bartender leers as you walk over to the stranger"
bar_order_button_2_jump_to = 'stranger_convo'
bar_order_button_3_text = 'Miller Light'
bar_order_button_3_resp = "\"Be quick, the next stasi shift gets off soon and you two won't be alone for long\", the bartender whispers as you pay for the drink."
bar_order_button_3_jump_to = 'stranger_convo'


stranger_convo_prompt = """    \"I’m… Michael. Please listen very carefully, I won’t repeat these instructions.
When you leave this bar, cross the road and enter the building with the blue door. Look neither left nor right. Speak to no one.
When you are inside, change into the clothes provided and proceed to the garage. There will be a car waiting there.
Climb into the trunk and open the letter beneath the spare tire.
When you are finished, follow the instructions and swallow the letter. It may be some time before you eat anything else.\"

You leave the bar and cross the road."""
stranger_convo_button_1_text = 'Go through the blue door'
stranger_convo_button_1_resp = """You try to nonchalantly walk over to the garage door. It's been left unlocked.
Inside you find a plain change of clothes you quickly shrug into, hiding away what's left in the trash nearby.
As you bring down the lid of the car's trunk with you inside, you hear the engine begin to rumble.
"""
stranger_convo_button_1_jump_to = 'car'
stranger_convo_button_2_text = 'Speak to the doorman'
stranger_convo_button_2_resp = "You realise you probably shouldn't cause any kind of scene, best to just move on..."
stranger_convo_button_2_jump_to = 'stranger_convo'
stranger_convo_button_3_text = 'Investigate the car to your left'
stranger_convo_button_3_resp = "stranger_resp_3_here"
stranger_convo_button_3_jump_to = 'L1'
stranger_convo_button_3_resp = "There doesn't seem to be anything amiss here, just another part of the scenery on this rain-soaked street."
stranger_convo_button_3_jump_to = 'stranger_convo'

car_boot_prompt = f"""
The sound is like the lock turning in a Stasi cell. But there’s another noise, something soft and gentle, yet it cuts through the chug of diesel engines and snapping riles. Everything is dark, but that sound, that voice… it sounds like light.

But there’s another sound. Something terrifying, though she’s been told to expect it...
...Three taps on the outside of the trunk.
...A Stasi guard...

The letter gave her instructions, but what was she supposed to do?
{resource_string('writer.art', 'guard_scene').decode('utf-8')}"""
car_boot_button_1_text = 'Open the trunk'
car_boot_button_1_resp = "You feel your way across the smooth insides of the trunk, but there doesn't seem to be any way to let yourself out. You're trapped!"  # TODO
car_boot_button_1_jump_to = 'car_boot'
car_boot_button_2_text = 'Swallow the letter'
car_boot_button_2_resp = "You choke down the letter"
car_boot_button_2_jump_to = 'flag'
car_boot_button_3_text = 'Tap on the left and right of the trunk'
car_boot_button_3_resp = "You hear a hollow thunk as you rap either side of the trunk. You don't draw the attention of anyone."
car_boot_button_3_jump_to = 'car_boot'

car_scene_story_text = """Jenny can’t quite believe the letter’s orders. But then, she can’t believe she’s in the
trunk of a car, waiting to cross the most contested border in modern history. She can almost feel the
wheels crunching over barbed wire, feel the barrier falling, trapping her in East Berlin."""

intro_text = """but the biggest thing that has happened in the world in my life, in our lives, is this:
by the grace of God, America won the Cold War.
  - President George H.W. Bush"""
flag_text = "Jenny breaths a sigh of relief as the sound of the guard station fades away. She’s in the East now, and soon to be on her own. A shiver runs through her spine, cold as the war she’s joined. But there’s a warmth too, a pride that tells her what she’s doing matters, that lives can be rebuilt through her actions, families reunited. Where people are willing to risk themselves for others, there’s hope. This is Jenny’s last thought as she closes her eyes in the dark trunk of a Volkswagen."

captain_scene_story_text = """The next week, Jenny meets a family waiting to cross into West Berlin.
The fear in their eyes is nothing new, but she’s never handled a crossing with a child before.
The child is a toddler, barely out of nappies, and presents complications the family can’t imagine.
But Jenny is good at her job. She knows the guard rotas, knows the Wall and all its vagaries,
and most of all she knows the people waiting to cross. She thinks this family can make it.
Behind the fear, there’s a hardness in those eyes, a will to survive. She ushers them out the alley behind her apartment block,
and they disappear into the distance. Jenny makes the final preparations for their journey, then leaves to meet her handler.
But just as Jenny leaves her home, disaster strikes. The Captain stands in the rain, flanked by Stasi."""

mirror_prompt = f"{resource_string('writer.art', 'mirror').decode('utf-8')}\nJenny adjusts her makeup in the mirror one last time. She feels a headache coming on, tension, fear, excitement. It fades as she rubs her temples. But how is she getting to the restaurant? The Captain told her earlier, if only she could remember…"

pig_prompt = f"{resource_string('writer.art', 'chauffeur').decode('utf-8')}\nThe Captain was a pig, but his driver wasn’t. Jenny never got a good look at his face, but that voice, when he asked her “where to?” as if he didn’t know… He sounded so familiar. Jenny reached out with reckless words, knowing they were her best friends, her sharpest weapons.\nBut what did she say? So hard to remember…"
pig_button_1_text = "You're that man... from the bar?"
pig_button_1_resp = 'The driver shakes his head, staring down at his feet.'
pig_button_1_jump_to = 'pig'
pig_button_2_text = "I... know you from somewhere... but I can't remember..."
pig_button_2_resp = "He stares at you silently."
pig_button_2_jump_to = 'pig'
pig_button_3_text = '“Did you drive me across the border?'
pig_button_3_resp = "A smile starts to creep onto the driver's face."
pig_button_3_jump_to = 'Captain'

wall_scene_story_text = """Jenny’s feet pound the rain slick pavement to the beat of her heart.
She’s panting now, running through the night with no hope of escape. She knows she’ll give up the family eventually,
and her shame will burn hotter than any brand upon her skin. She’s close to the Wall now, but what can she do?
Spotlights sweep the river, soldiers stand in guard posts. Without warning, a body slams into her from the side.
The chauffeur! He stares into her eyes, his big and round and brown and terrified. But then he moves,
pushes her down the riverbank. There’s a boat, as though he knew this was happening,
as though he were waiting for her to run. How can he know her so well when they’ve never even shared a conversation?
When he pushes her into the boat, he signals to someone high above. A spotlight winks off."""
