import PySimpleGUI as sg
s3 = "*Enter a valid number for both boxes*"

layout = [ [sg.Text("\nPercent of a number \n")],
           [sg.Text("Enter the Number"), sg.Input(enable_events=True)],
           [sg.Text("Enter the Percentage"), sg.Input(enable_events=True)],
           [sg.Text("result:\n")],
           [sg.Text(size=(30,1), key='-OUTPUT-')]]
window = sg.Window('Lesley percent calculator', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    try:
        s = values[0]
        s0 = float(s)
        s1 = int(s0)
        p = values[1]
        p0 = float(p)
        p1 = int(p0)
        p2 = p1 * .01
        s2  = s1 * p2

    except ValueError:
        window['-OUTPUT-'].update(s3)
        continue
    if values[0]:
        window['-OUTPUT-'].update(s2)
window.close()