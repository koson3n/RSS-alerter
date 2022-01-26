import PySimpleGUI as sg
from feedhandler import *
from inspectview import *
    
sg.theme('DarkAmber')

tracking = False
searchOn = sg.Text('Idle', background_color='Red', pad=(20,10), size=(6, 1))
threadList = sg.Listbox([], size=(70,10), enable_events=True, key='-list-')
urlBox = sg.InputText('', key='siteUrl', size=(70, 1))
trackbtn = sg.Button('Track', disabled=False)
untrackbtn = sg.Button('Untrack', disabled=True)
caseCheckbox = sg.Checkbox('Case sensitive', key='-case-sensitive-')
summaryCheckbox = sg.Checkbox('Expand search to summary', key='-summary-search-')
alertCheckbox = sg.Checkbox('Alerts', enable_events=True, pad=(40,10), key='-alerts-')
titleList = []
altList = []
url = ''
keywrds = sg.InputText('', key='input_words', size=(70, 1))

layout = [
    [sg.Text('Input the URL of the feed you want to track')],
    [urlBox],
    [sg.Text('Input keywords for tracking (separate words with spaces)')],
    [keywrds],
    [caseCheckbox],
    [sg.Text('Threads that match the criteria')],
    [threadList],
    [trackbtn, untrackbtn, sg.Button('Info') , sg.Button('Exit')],
    [searchOn, alertCheckbox],
    [sg.Text('Made by Joopajoonas - Source code available at GitHub', font=('Any 7'), text_color='gray')]
]

window = sg.Window('RSS Alerter', layout, size=(550, 450), icon='icon.ico', finalize=True)

#converting user input into list of filter strings
def inputParser (input):
    resultingList = list(input.split(' '))
    return resultingList

def checkUrl(url):
    tempUrl = url.lower()
    if tempUrl[-4:] == '.rss' or tempUrl[-4:] == '.xml':
        return True
    return False

#Main program loop. When broken -> program is terminated
while True:
    event, values = window.Read(timeout=5000)
    
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
        
    if event == 'Track':
        if len(values['siteUrl']) > 0:
        
            url = values['siteUrl']
            if checkUrl(url):
                titleList = getTitles(inputParser(values['input_words']), url, values['-case-sensitive-']) 
                tracking = True
                searchOn.update('Tracking', background_color='Green')
                threadList.update(titleList)
                trackbtn.update(disabled=True)
                untrackbtn.update(disabled=False)
                caseCheckbox.update(disabled=True)
                urlBox.update(disabled=True)
                keywrds.update(disabled=True)
            else:
                sg.popup_error(f'No feed found in given URL.')
            
        else:
            sg.popup_error(f'No URL provided!')
              
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
            sg.popup_error(f'Nothin was selected.')
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