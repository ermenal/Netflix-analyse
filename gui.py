import pandas as pd
import PySimpleGUI as sg


def main():
    sg.theme("DarkAmber")
    CLOSE_button = sg.Button("CLOSE", key="CLOSE")
    OK_button = sg.Button("OK", key="OK")
    welcome_text = sg.Text("Welkom", size=(20, 1), font=5)


    buttons_column = [[OK_button], [CLOSE_button]]
    text_column = [[welcome_text]]

    layout = [[sg.Column(text_column), sg.VSeparator(), sg.Column(buttons_column)]]

    window = sg.Window(title="Netflix-analyser", layout=layout, margins=(100, 50))

    while True:
        event, values = window.read()
        print(event, values)
        if event == "CLOSE" or event == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == "__main__":
    main()
