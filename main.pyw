import password_generator

import PySimpleGUI as sg

import pyperclip


layout = [  [sg.Text('Password generator')],
            [sg.Checkbox('Do you want numbers?')],
            [sg.Checkbox('Do you want symbols?')],
            [sg.Text('Lenght'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]


window = sg.Window('Password generator', layout)
event, values = window.read()

number, symbol, lenght = values[0], values[1], int(values[2])

password = password_generator.password_generator(number, symbol, lenght)

sg.popup(password)

pyperclip.copy(password)

window.close()