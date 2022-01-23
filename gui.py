import PySimpleGUI as sg
import time
from feedhandler import *
from inspectview import *

sg.theme('DarkAmber')

tracking = False
searchOn = sg.Text('Idle', background_color='Red', pad=(20,10))
threadList = sg.Listbox([], size=(60,10), enable_events=True, key='-list-')
titleList = []
altList = []
url = ''

layout = [
    [sg.Text('Input the .rss URL of the feed you want to track')],
    [sg.InputText('', key='siteUrl')],
    [sg.Text('Input keywords for tracking (separate words with spaces)')],
    [sg.InputText('', key='input_words')],
    [sg.Text('Threads that match the criteria')],
    [threadList],
    [sg.Button('Track'), sg.Button('Untrack'), sg.Button('Close'), sg.Button('Info')],
    [searchOn, sg.Checkbox('Alerts', enable_events=True, pad=(40,10), key='-alerts-')]
]

window = sg.Window('RSS Alerter', layout, size=(500, 400))
window.finalize()

def inputParser (input):
    resultingList = list(input.split(' '))
    return resultingList

def updateList (originalList):
    altList = getTitles(inputParser(values['input_words']))
    
    if areThereNewTitles(altList, originalList):
        return True
    
    time.sleep(5)
    print('updatelist')
    updateList()

def areThereNewTitles (list1, list2):
    if list1 != list2:
        if values['-alerts-'] == True:
            print('\a')
        return True
    return False



while True:
    event, values = window.Read(timeout=100)
    
    if event == 'Close' or event == sg.WIN_CLOSED:
        break
        
    if event == 'Track':
        tracking = True
        url = values['siteUrl']
        searchOn.update('Tracking', background_color='Green')
        titleList = getTitles(inputParser(values['input_words']), url)
        threadList.update(titleList)
              
    if event == 'Untrack':
        tracking = False
        searchOn.update('Idle', background_color='Red')
        threadList.update([])
        
    if event == 'Info':
        selected = window['-list-'].get()
        popup(selected, values['siteUrl'])
        
          
    altList = getTitles(inputParser(values['input_words']), url)
    
    if altList != titleList and tracking == True:
    
        if values['-alerts-'] == True:
            print('\a')
            
        titleList = altList
        threadList.update(titleList)
        threadList = window['ListBox']
        index = threadList.GetIndexes()[0]
        threadList.Widget.itemconfig(index, fg='red', bg='green')
        
    window.refresh()
        
window.close()




#is feed url -- https://www.is.fi/rss/tuoreimmat.xml

#techbbs prossut linkki -- https://bbs.io-tech.fi/forums/prosessorit-emolevyt-ja-muistit.73/index.rss