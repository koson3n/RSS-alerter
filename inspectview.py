import webbrowser
import PySimpleGUI as sg
from feedhandler import *


def getInfo(itemTitle, feedUrl):
    linkToItem = getTitleLink(itemTitle, feedUrl)
    return linkToItem
    
def openLink(url):
    webbrowser.open(url)

def popup(item, url):
    sg.theme('DarkAmber')
    
    link = getInfo(item, url)
    
    layout = [
        [sg.Text('Link to the item: ' + link, enable_events=True, key='-link-', pad=(5,5))],
        [sg.Text()],
        [sg.Text()],
        [sg.Button('Close')]
    ]

    window = sg.Window('Inspect', layout, size=(400, 300))

    while True:
        event, values = window.Read(timeout=100)

        if event == 'Close' or event == sg.WIN_CLOSED:
            break

        if event == '-link-':
            openLink(link)
            
    window.close()