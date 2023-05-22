import PySimpleGUI as sg
import csv

sg.theme('Tealmono')   # Add a touch of color
sg.set_options(font='Arial 13')
# All the stuff inside your window.
layout = [  [sg.Text('Enter Your First Name'),sg.Push(),sg.InputText(key='-fname-')],
            [sg.Text('Enter Your Last Name'), sg.Push(),sg.InputText(key='-lname-')],
            [sg.Text('Phone Number'), sg.Push(),sg.InputText(key='-phone-')],
            [sg.Text('Email Address'), sg.Push(),sg.InputText(key='-email-')],
            [sg.Text('Job Occupation'), sg.Push(),sg.InputText(key='-job-')],
            [sg.Button('Save'), sg.Button('Cancel')],
            [sg.Text('Search by Last Name'), sg.Push(),sg.InputText(key='-searchText-')],
            [sg.Button('Search')],
            [sg.Text(key='searchOutput')],
            ]

# Create the Window
window = sg.Window('Contact Book ', layout,icon='favicon.ico')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    fname = values['-fname-']
    lname = values['-lname-']
    phone = values['-phone-']
    email = values['-email-']
    job = values['-job-']
    info = [fname,lname,phone,email,job]
    if event == 'Save':
        with open('info.csv','a', newline="") as w:
            cw = csv.writer(w)
            cw.writerow(info)
        window['-fname-'].update('')
        window['-lname-'].update('')
        window['-phone-'].update('')
        window['-email-'].update('')
        window['-job-'].update('')

    searchText = values['-searchText-']
    if event == 'Search':
        with open('info.csv', 'r') as r:
            cr = csv.reader(r)
            for i in cr:
                if i[1] == searchText:
                    window['searchOutput'].update(f"First Name: {i[0]}\nLast Name: {i[1]}\nPhone Number: {i[2]}\nEmail: {i[3]}\nJob Occupation: {i[4]}")

window.close()
if __name__ == '__main__':
    print('welcome to contactbook ')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
