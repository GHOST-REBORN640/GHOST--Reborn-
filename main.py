import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from google import genai

# AI Client එක සෙට් කිරීම
client = genai.Client(api_key='AIzaSyApVtvrs_ACdF6LOVjddKgbC3kYVCL2U6E')

class GhostChat(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Logo එක තිබේ නම් පෙන්වීම
        if os.path.exists('logo.jpg'):
            layout.add_widget(Image(source='logo.jpg', size_hint_y=None, height=200))
        
        self.scroll = ScrollView()
        self.chat_history = Label(
            text="Welcome to GHOST Reborn!", 
            size_hint_y=None, 
            halign='left', 
            valign='top', 
            text_size=(400, None)
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        layout.add_widget(self.scroll)
        
        self.input = TextInput(hint_text="Type message...", size_hint_y=None, height=100, multiline=False)
        layout.add_widget(self.input)
        
        btn = Button(text="Ask GHOST", size_hint_y=None, height=100, background_color=(0, 0.7, 1, 1))
        btn.bind(on_press=self.send_message)
        layout.add_widget(btn)
        
        return layout

    def send_message(self, instance):
        if self.input.text.strip():
            user_t = self.input.text
            self.chat_history.text += f"\n\nYou: {user_t}"
            try:
                # Gemini AI එකෙන් පිළිතුර ලබා ගැනීම
                res = client.models.generate_content(model="gemini-2.0-flash", contents=user_t)
                self.chat_history.text += f"\n\nGHOST: {res.text}"
            except:
                self.chat_history.text += "\n\nError: Connection failed"
            self.input.text = ""

if __name__ == '__main__':
    GhostChat().run()
