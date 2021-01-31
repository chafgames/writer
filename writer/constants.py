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
stranger_convo_button_1_resp = "stranger_resp_1_here"  # TODO
stranger_convo_button_1_jump_to = 'L1'
stranger_convo_button_2_text = 'Speak to the doorman'
stranger_convo_button_2_resp = "stranger_resp_2_here"  # TODO
stranger_convo_button_2_jump_to = 'L1'
stranger_convo_button_3_text = 'Investigate the car to your left'
stranger_convo_button_3_resp = "stranger_resp_3_here"
stranger_convo_button_3_jump_to = 'L1'
