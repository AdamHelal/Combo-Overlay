from abc import ABC, abstractmethod

# abstract base class with a skeleton of methods
class Gamepad(ABC):

    def __init__(self):
        pass

    def get_controller_state(self):
        return self.mapping

    def get_bg_image(self):
        return self.bg_image

    def update(self,event):
        if event.code in self.mapping:
            self.mapping[event.code]['val'] = event.state
        else:
            print(f"Unknown event code: {event.code}")
    
    @abstractmethod
    def handle_analog(self,pygame):
        pass

    @abstractmethod
    def trigger_button(self,pygame):
        pass
        
    @abstractmethod
    def process_state(self,pygame):
        pass
    

class PSFOUR(Gamepad):

    def __init__(self):
        #initialize mapping of buttons and there needed properties
        self.mapping = {
        "BTN_SOUTH": {'type':0,'val':0,'origin_x':848,'origin_y':253,'radius':36},
        "BTN_NORTH":{'type':0,'val':0,'origin_x':848,'origin_y':100,'radius':36},
        "BTN_EAST":{'type':0,'val':0,'origin_x':923,'origin_y':176,'radius':36},
        "BTN_WEST":{'type':0,'val':0,'origin_x':768,'origin_y':176,'radius':36},
        "BTN_TR":{'type':0,'val':0,'origin_x':848,'origin_y':10,'radius':36},
        "BTN_TL":{'type':0,'val':0,'origin_x':204,'origin_y':10,'radius':36},
        "BTN_THUMBL":{'type':0,'val':0,'origin_x':350,'origin_y':313,'radius':36},
        "BTN_THUMBR":{'type':0,'val':0,'origin_x':683,'origin_y':313,'radius':36},
        "BTN_SELECT":{'type':0,'val':0,'origin_x':735,'origin_y':73,'radius':36},
        "BTN_START":{'type':0,'val':0,'origin_x':311,'origin_y':73,'radius':36},
        "ABS_HAT0Y":{'type':2,'val':0,'south':{'origin_x':189,'origin_y':122},'north':{'origin_x':189,'origin_y':229},'radius':38},
        "ABS_HAT0X":{'type':2,'val':0,'north':{'origin_x':240,'origin_y':176},'south':{'origin_x':135,'origin_y':176},'radius':38},
        # "ABS_Z":{'type':0,'val':0,'origin_x':350,'origin_y':313,'radius':36},
        # "ABS_RZ":{'type':0,'val':0,'origin_x':350,'origin_y':313,'radius':36},
        "ABS_RX":{'type':1,'val':0,'origin_x':683,'origin_y':313,'radius':36},
        "ABS_RY":{'type':1,'val':0,'origin_x':683,'origin_y':313,'radius':36},
        "ABS_X":{'type':1,'val':0,'origin_x':350,'origin_y':313,'radius':36},
        "ABS_Y": {'type':1,'val':0,'origin_x':350,'origin_y':313,'radius':36},
        }
        self.bg_image='ps4-white.png'
        self.deadzone=0.1
    
    def handle_analog(self,pygame, button_surface, stickX, stickY):
        analog_x = stickX['val'] / 32767.0  # lower value for analog x-axis (range [-1.0, 1.0])
        analog_y = stickY['val'] / 32767.0  # lower value for analog x-axis (range [-1.0, 1.0])

        #check for deadzone to avoid hypersensitivity and useless updates
        if abs(analog_x) < self.deadzone:
            analog_x=0 
        if abs(analog_y) < self.deadzone:
            analog_y=0 

        circle_x=stickX['origin_x']
        circle_y=stickX['origin_y']
        circle_x += int(analog_x * 40)  #movement speed by a factor of 40
        circle_y -= int(analog_y * 40)  
        
        pygame.draw.circle(button_surface, (255, 255, 255, 128), (circle_x, circle_y), 36)
    
    def trigger_button(self,pygame, button_surface, button):
        if button['val'] and button['type']==0: pygame.draw.circle(button_surface, (0, 0, 0, 128), (button['origin_x'],button['origin_y']), button['radius'])
        elif button['val'] and button['type']==2:
            if button['val'] == -1:
                pygame.draw.circle(button_surface, (0, 0, 0, 128), (button['south']['origin_x'],button['south']['origin_y']), button['radius'])
            elif button['val'] == 1:
                pygame.draw.circle(button_surface, (0, 0, 0, 128), (button['north']['origin_x'],button['north']['origin_y']), button['radius'])
            
                

    def process_state(self,pygame,button_surface):

        #handle buttons and dpad
        for button in self.mapping:
            if self.mapping[button]['type'] ==0:
                self.trigger_button(pygame,button_surface, self.mapping[button])
            elif self.mapping[button]['type'] == 2:
                self.trigger_button(pygame,button_surface, self.mapping[button])

        self.handle_analog(pygame, button_surface, self.mapping['ABS_X'], self.mapping['ABS_Y'])
        self.handle_analog(pygame, button_surface, self.mapping['ABS_RX'], self.mapping['ABS_RY'])
    
