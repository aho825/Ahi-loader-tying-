from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class AhiLoaderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.label = Label(text="Ahi Loader Başlatıldı!", font_size='20sp')
        btn = Button(text="Tıkla", size_hint=(1, 0.3))
        btn.bind(on_press=self.on_button_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        self.label.text = "Butona Tıklandı!"

if __name__ == '__main__':
    AhiLoaderApp().run()
  
