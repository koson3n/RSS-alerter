import webbrowser
import PySimpleGUI as sg
import html2text
from feedhandler import *

#function converts raw html from the feed summary to plaintext
def convertHtml(string):
    tt = html2text.HTML2Text()
    tt.ignore_links = True
    tt.ignore_images = True
    retrn = tt.handle(string)
    return retrn

#fetching info about the feed items
def getInfo(itemTitle, feedUrl):
    infoList = getAllInfo(itemTitle, feedUrl)
    return infoList

#opens default web browser and redirects to given url    
def openLink(url):
    webbrowser.open(url)

#opens popup window that contains info about feed item of users choice.
#window closes when after this function
def popup(item, url):

    sg.theme('DarkAmber')
    infoList = getInfo(item, url)
    
    layout = [
        [sg.Text('Link: ', font=('bold'), text_color='White'), sg.Text(infoList[0], pad=(5,5), size=(200,1))],
        [sg.Text('Item title: ', font=('bold'), text_color='White'), sg.Text(infoList[1])],
        [sg.Text('Published: ', font=('bold'), text_color='White'), sg.Text(infoList[2])],
        [sg.Text('Summary: ', font=('bold'), text_color='White')],
        [sg.Multiline(convertHtml(infoList[3]), size=(70, 10), disabled=True)], 
        [sg.Button('Close'), sg.Button('Visit site')]
    ]

    window = sg.Window('Inspect', layout, size=(500, 350))

    while True:
        event, values = window.Read(timeout=500)

        if event == 'Close' or event == sg.WIN_CLOSED:
            break

        if event == 'Visit site':
            openLink(infoList[0])
            
    window.close()