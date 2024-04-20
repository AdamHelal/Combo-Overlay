# import pygame, time
# pygame.init()
# joysticks = []
# clock = pygame.time.Clock()
# keepPlaying = True

# def process_transaction(transaction,recent,event):
#     transaction.append(event)
#     recent['val'] = event
#     recent['time'] = time.time()

# def fetch_button_val(event,joystick):
#     button={'val':'','time':''}
#     button['time']=time.time()
#     if hasattr(event,'button'): 
#         button['val']=event.button
#     else:
#         trigger_l2 = joystick.get_axis(4)  # Replace with correct index for R2
#         trigger_r2 = joystick.get_axis(5)  # Replace with correct index for L2

#         # Check if R2 or L2 is pressed (clicked)
#         if trigger_r2 > 0.5:
#             button['val'] = "R2"
#         if trigger_l2 > 0.5:
#             button['val'] = "L2"
#     return button

# # for al the connected joysticks
# for i in range(0, pygame.joystick.get_count()):
#     # create an Joystick object in our list
#     joysticks.append(pygame.joystick.Joystick(i))
#     # initialize the appended joystick (-1 means last array item)
#     joysticks[-1].init()
#     # print a statement telling what the name of the controller is
#     print ("Detected joystick "),joysticks[-1].get_name(),"'"
# joystick=joysticks[-1]
# transactions=[]
# while keepPlaying:
#     clock.tick(60)

#     start_time = time.time()  # Get the current time in seconds
#     end_time = start_time + 2  # Calculate the time when the action should stop
    
#     transaction=[]
#     recent={'val':'','time':''}
#     while time.time() < end_time: 
#         for event in pygame.event.get():
#             button=fetch_button_val(event,joystick)
#             print(recent)
#             print(button)
#             if (recent['time']!='' and (recent['time']==button['time'] or float(button['time'])-float(recent['time']) < 0.2) and button['val'] == recent['val']) or button['val']=='': continue
#             process_transaction(transaction,recent,button['val'])
#             # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
#             # register_event(joystick,event,transaction,recent_button)

#     print(transaction)
#     transactions.append(transaction);
#     transaction=[]
