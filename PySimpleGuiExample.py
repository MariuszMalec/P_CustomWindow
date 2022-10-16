import PySimpleGUI as sg

# Choose a Theme for the Layout
#sg.theme('DarkPurple2')
theme_list = sg.theme_list()
print(theme_list)
#sg.preview_all_look_and_feel_themes()

layout = [
    [sg.Text('Hello')],
    [sg.Button('Klik')],
    [sg.Cancel()],
    [sg.Submit()],

]

window = sg.Window('My window', layout, size=(300, 150))

event, values = window.read()

window.close()