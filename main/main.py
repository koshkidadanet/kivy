from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import  CreateQR
import SQL_method

Window.size = (1024, 768)
Window.clearcolor = ('#313132')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')


class ScreenMain(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        floatlayout = FloatLayout(size=(1024, 768))
        name = Label(text='Наклейка', font_size='36sp', pos=(-10, 250))
        button_create = Button(
            background_normal='..\\front\\Group 1.png',
            background_down='..\\front\\Group 1.png',
            size_hint=(.19, .14),
            on_press=self.press_create,
            pos=(1024 / 2 - 1024 * .21 / 2, 405)
        )
        button_create_add = Button(
            background_normal='..\\front\\Group 2.png',
            background_down='..\\front\\Group 2.png',
            size_hint=(.23, .14),
            on_press=self.press_create_add,
            pos=(1024/2-1024*.26/2, 263)
        )

        floatlayout.add_widget(name)
        floatlayout.add_widget(button_create)
        floatlayout.add_widget(button_create_add)
        self.add_widget(floatlayout)

    def press_create(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'create'

    def press_create_add(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'create_add'


class Create(Screen):
    invent = ''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        def on_enter(instance):
            print('User pressed enter in', instance.text)
            self.invent = instance.text
            print(self.invent)

        name = Label(text='Наклейка', font_size='36sp', pos=(-10, 250))
        floatlayout = FloatLayout(size=(1024, 768))
        '''self.input_name = TextInput(hint_text = "Наименование",
                               multiline = False,
                               size_hint=(.42, .05),
                               pos=(1024/2-1024*.42/2, 510),
                               on_text_validate=on_enter
                               )'''

        self.input_num = TextInput(hint_text="Инвентарник",
                               multiline=False,
                               size_hint=(.42, .05),
                               pos=(1024 / 2 - 1024 * .42 / 2, 510),
                               on_text_validate=on_enter
                               )

        back = Button(
            background_normal='..\\front\\Group 3.png',
            background_down='..\\front\\Group 3.png',
            on_press=self.press_back,
            size_hint=(.1, .1),
            pos=(0, 650)
        )

        create = Button(
            background_normal='..\\front\\Group 1.png',
            background_down='..\\front\\Group 1.png',
            size_hint=(.19, .14),
            on_press=self.create,
            pos=(1024 / 2 - 1024 * .21 / 2, 310)
        )

        floatlayout.add_widget(name)
        floatlayout.add_widget(back)
        floatlayout.add_widget(create)
        floatlayout.add_widget(self.input_num)
        '''floatlayout.add_widget(self.input_name)'''
        self.add_widget(floatlayout)

    def create(self, *args):
        self.input_num.text = ""
        stroka = SQL_method.FindInvent(self.invent)
        print(stroka)
        CreateQR.itog(stroka[1],stroka[0],stroka[2])
        self.invent = ""


    def press_back(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_screen'


class Create_add(Screen):
    stroka_add = ''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        name = Label(text='Наклейка', font_size='36sp', pos=(-10, 250))
        floatlayout = FloatLayout(size=(1024, 768))

        def on_enter(instance):
            print('User pressed enter in', instance.text)
            self.stroka_add = instance.text
            print(self.stroka_add)

        self.input_all = TextInput(hint_text="номер, название, кабинет, кол-во",
                               multiline=False,
                               size_hint=(.42, .05),
                               pos=(1024 / 2 - 1024 * .42 / 2, 510),
                               on_text_validate=on_enter
                               )

        '''self.input_num = TextInput(hint_text="Инвентарник",
                              multiline=False,
                              size_hint=(.42, .05),
                              pos=(1024 / 2 - 1024 * .42 / 2, 450),
                              on_text_validate=on_enter
                              )

        self.input_kab = TextInput(hint_text="Кабинет",
                               multiline=False,
                               size_hint=(.42, .05),
                               pos=(1024 / 2 - 1024 * .42 / 2, 390),
                               on_text_validate=on_enter
                               )

        self.input_sum = TextInput(hint_text="Количество",
                              multiline=False,
                              size_hint=(.42, .05),
                              pos=(1024 / 2 - 1024 * .42 / 2, 330),
                              on_text_validate=on_enter
                              )'''

        back = Button(
            background_normal='..\\front\\Group 3.png',
            background_down='..\\front\\Group 3.png',
            on_press=self.press_back,
            size_hint=(.1, .1),
            pos=(0, 650)
        )

        create = Button(
            background_normal='..\\front\\Group 1.png',
            background_down='..\\front\\Group 1.png',
            size_hint=(.19, .14),
            on_press=self.create,
            pos=(1024 / 2 - 1024 * .21 / 2, 310)

        )

        floatlayout.add_widget(name)
        floatlayout.add_widget(back)
        floatlayout.add_widget(create)
        floatlayout.add_widget(self.input_all)
        #floatlayout.add_widget(self.input_name)
        #floatlayout.add_widget(self.input_kab)
        #floatlayout.add_widget(self.input_sum)
        self.add_widget(floatlayout)

    def create(self, *args):
        self.input_all.text = ""
        self.stroka_add = ""
        print(self.stroka_add)
    def press_back(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main_screen'



class PaswordingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenMain(name='main_screen'))
        sm.add_widget(Create(name='create'))
        sm.add_widget(Create_add(name='create_add'))
        return sm


if __name__ == "__main__":
    PaswordingApp().run()
