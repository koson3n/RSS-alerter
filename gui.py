import PySimpleGUI as sg
import time
from feedhandler import *
from inspectview import *

sg.theme('DarkAmber')

tracking = False
searchOn = sg.Text('Idle', background_color='Red', pad=(20,10), size=(6, 1))
threadList = sg.Listbox([], size=(60,10), enable_events=True, key='-list-')
urlBox = sg.InputText('', key='siteUrl')
trackbtn = sg.Button('Track', disabled=False)
untrackbtn = sg.Button('Untrack', disabled=True)
caseCheckbox = sg.Checkbox('Case sensitive', key='-case-sensitive-')
titleList = []
altList = []
url = ''
keywrds = sg.InputText('', key='input_words')

layout = [
    [sg.Text('Input the .rss URL of the feed you want to track')],
    [urlBox],
    [sg.Text('Input keywords for tracking (separate words with spaces)')],
    [keywrds, caseCheckbox],
    [sg.Text('Threads that match the criteria')],
    [threadList],
    [trackbtn, untrackbtn, sg.Button('Info') , sg.Button('Exit')],
    [searchOn, sg.Checkbox('Alerts', enable_events=True, pad=(40,10), key='-alerts-')],
    [sg.Text('Made by Joonas Lahtinen - Source code available at GitHub', font=('Any 9'), text_color='gray')]
]

window = sg.Window('RSS Alerter', layout, size=(500, 425), icon='icon.ico', finalize=True)

#converting user input into list of filter strings
def inputParser (input):
    resultingList = list(input.split(' '))
    return resultingList


#Main program loop. When broken -> program is terminated
while True:
    event, values = window.read()
    
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
        
    if event == 'Track':
        tracking = True
        url = values['siteUrl']
        searchOn.update('Tracking', background_color='Green')
        titleList = getTitles(inputParser(values['input_words']), url, values['-case-sensitive-'])
        threadList.update(titleList)
        trackbtn.update(disabled=True)
        untrackbtn.update(disabled=False)
        caseCheckbox.update(disabled=True)
        urlBox.update(disabled=True)
        keywrds.update(disabled=True)        
              
    if event == 'Untrack':
        tracking = False
        searchOn.update('Idle', background_color='Red')
        threadList.update([])
        trackbtn.update(disabled=False)
        untrackbtn.update(disabled=True)
        caseCheckbox.update(disabled=False)
        urlBox.update(disabled=False)
        keywrds.update(disabled=False) 
        
    if event == 'Info':
        try:
            selected = window['-list-'].get()
            popup(selected, values['siteUrl'])
        except:
            print('No item selected')
        
          
    altList = getTitles(inputParser(values['input_words']), url, values['-case-sensitive-'])
    
    if altList != titleList and tracking == True:
    
        if values['-alerts-'] == True:
            print('\a')
            
        titleList = altList
        threadList.update(titleList)
        
        try:
            threadList.Widget.itemconfig(0, fg='yellow', bg='green')
        except:
            print('Index not found')
    
    window.refresh()
    
window.close()


#some rss feeds for testing
#news feed url -- https://www.is.fi/rss/tuoreimmat.xml
#techbbs -- https://bbs.io-tech.fi/forums/prosessorit-emolevyt-ja-muistit.73/index.rss