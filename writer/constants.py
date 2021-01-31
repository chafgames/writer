bar_order_prompt = 'What should you order at the bar for the stranger?'
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
stranger_convo_button_2_resp = "stranger_resp_2_here"
stranger_convo_button_2_jump_to = 'stranger_convo'     # TODO
stranger_convo_button_3_text = 'Investigate the car to your left'
stranger_convo_button_3_resp = "stranger_resp_3_here"
stranger_convo_button_3_jump_to = 'L1'
stranger_convo_button_3_resp = "There doesn't seem to be anything amiss here, just another part of the scenery on this rain-soaked street."
stranger_convo_button_3_jump_to = 'stranger_convo'     # TODO

car_boot_prompt = """The sound is like the lock turning in a Stasi cell. But there’s another noise, something soft and gentle, yet it cuts through the chug of diesel engines and snapping riles. Everything is dark, but that sound, that voice… it sounds like light.

But there’s another sound. Something terrifying, though she’s been told to expect it...
...Three taps on the outside of the trunk.
...A Stasi guard...

The letter gave her instructions, but what was she supposed to do?"""
car_boot_button_1_text = 'Open the trunk'
car_boot_button_1_resp = "car_boot_resp_1_here"  # TODO
car_boot_button_1_jump_to = 'car_boot'  # TODO
car_boot_button_2_text = 'Swallow the letter'  # TODO
car_boot_button_2_resp = "car_boot_resp_2_here"  # TODO
car_boot_button_2_jump_to = 'car_boot'  # TODO
car_boot_button_3_text = 'Tap on the left and right of the trunk'
car_boot_button_3_resp = "car_boot_resp_3_here"  # TODO
car_boot_button_3_jump_to = 'car_boot'  # TODO

car_scene_story_text = """Jenny can’t quite believe the letter’s orders. But then, she can’t believe she’s in the
trunk of a car, waiting to cross the most contested border in modern history. She can almost feel the
wheels crunching over barbed wire, feel the barrier falling, trapping her in East Berlin."""
