class Button(object):
    html = ""
    button_Type = ""

    def get_html(self):
        return self.html

    def print_Button_Type(self):
        return self.button_Type

class Image(Button):
    button_Type = "Imagebutton is created"
    html = "<img></img>"

class Input(Button):
    button_Type = "Input Button is created"
    html = "<input></input>"

class Flash(Button):
    button_Type = "Flash button is created"
    html = "<flash></flash>"

class ButtonFactory():
   def create_button(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]() #get class with metaname

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
   print (button_obj.create_button(b).get_html())
   print(button_obj.create_button(b).print_Button_Type())