#A GUI calculator application by Neil Patel
import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [
    [sg.InputText()],
    [sg.Button("Calculate"), sg.Exit()]
]

window = sg.Window("Calculator App", layout)

while True: #persistence window loop
    event, values = window.read()
    print (event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
