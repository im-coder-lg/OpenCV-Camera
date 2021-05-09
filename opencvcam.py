import pyautogui
import pysimplegui as sg
import cv2
import numpy


def main():
    sg.theme('White')
    
    layout=[[sg.Text('Camera',size=(40,1),justification='center',font='Montserrat 20')],
            [sg.Image]