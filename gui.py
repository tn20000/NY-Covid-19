from plotting import get_county, predi_covid
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class MainApp(App):
    def build(self):
        self.button = Button(text='Predict',
                        size_hint=(.4, .1),
                        pos_hint={'center_x': 0.5, 'center_y': .9})
        self.button.bind(on_press=self.on_press_button)
        self.sp = Spinner(text='Saratoga', values=get_county(),size_hint=(1,.1),pos_hint={'y':.1})
        self.main_layout = BoxLayout(orientation='vertical',padding=10)
        self.main_layout.add_widget(self.sp)
        self.img = Image(source='NY.png')
        self.main_layout.add_widget(self.img)
        self.main_layout.add_widget(self.button)
        return self.main_layout

    def on_press_button(self, instance):
        predi_covid(self.sp.text)
        self.main_layout.remove_widget(self.img)
        self.img = Image(source='diff.png')
        self.img.reload()
        self.main_layout.add_widget(self.img)
        self.main_layout.remove_widget(self.button)
        self.button = Button(text='Return', size_hint=(.4,.1), pos_hint={'center_x':0.5,'center_y':0})
        self.button.bind(on_press=self.on_press_button_return)
        self.main_layout.add_widget(self.button)
    
    def on_press_button_return(self, instance):
        self.main_layout.remove_widget(self.button)
        self.main_layout.remove_widget(self.img)
        self.img = Image(source='NY.png')
        self.button = Button(text='predict',
                        size_hint=(.4, .1),
                        pos_hint={'center_x': 0.5, 'center_y': .9})
        self.button.bind(on_press=self.on_press_button)
        self.main_layout.add_widget(self.img)
        self.main_layout.add_widget(self.button)
        
if __name__ == '__main__':
    app = MainApp()
    app.run()


