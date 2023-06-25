class Controller:
    def __init__(self, model):
        self.model = model

    def get_button_text(self):
        return self.model.button_text
    
    def get_label_text(self):
        return self.model.label_text

    def button_pressed(self):
        self.model.label_text = 'Button Pressed'
        
    
    def button_released(self):
        self.model.label_text = 'Button Released'