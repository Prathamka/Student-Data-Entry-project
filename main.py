import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import textinput
from kivy.uix.button import Button
class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Student Name'))
        self.s_name = textinput()
        self.add_widget(self.s_name)
        
        self.add_widget(Label(text = 'Student gender'))
        self.s_gender = textinput()
        self.add_widget(self.s_gender)

        self.add_widget(Label(text = 'Student Marks'))
        self.s_marks = textinput()
        self.add_widget(self.s_marks)

        self.press = Button(text = 'Click me to store')
        self.press.bind(on_press = self.Click_me)
        self.add_widget(self.press)

    def Click_me(self, instance):
        print("Name of Student is ")
        print(self.s_name.exe)
        print("Gender of Student is ")
        print(self.s_gender.exe)
        print("Marks of Student is ")
        print(self.s_marks.exe)


class studentrecordApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    studentrecordApp().run()
