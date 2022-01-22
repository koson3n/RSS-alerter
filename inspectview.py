import PySimpleGUI as sg

def popup():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text()],
        [sg.Text()],
        [sg.Text()],
        [sg.Button('Close')]
    ]

    window = sg.Window('Inspect', layout, size=(400, 300))

    while True:
        event, values = window.Read(timeout=100)

        if event == 'Close' or event == sg.WIN_CLOSED:
            break


    window.close()