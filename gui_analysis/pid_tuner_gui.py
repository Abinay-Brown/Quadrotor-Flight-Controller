import numpy as np
from tkinter import *
from tkinter import ttk
import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import count
import threading
import random
import serial
import datetime
import serial.tools.list_ports
x_vals = []
y_vals = []
y_vals2 = []
index = count()
index2 = count()
class mainWindow(Tk):
    def __init__(self):
        super(mainWindow,self).__init__()
        
        plt.style.use('fivethirtyeight')
        self.logo = tk.Label(self,text="Data Visualization GUI", font = "Courier 18 bold")
        self.logo.place(x=420,y=5)
        self.plotGraph()
        
        # Serial Interface Group Box
        self.LB = LabelFrame(self,text="Serial Interface", font ="Courier 15 bold",width =620, height=130)
        self.LB.place(x=0,y=670)

        self.com_port_label = Label(self,text="COM Port ", font ="Courier 12 bold")
        self.com_port_label.place(x=20, y = 700)
        
        
        com_ports = serial.tools.list_ports.comports()
        self.com_port_dropdown = ttk.Combobox(self, font ="Courier 12", width = 20, state="readonly", values=com_ports)
        self.com_port_dropdown.place(x=120, y = 700)

        baud_rate_values = ["110", "300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "38400", "57600", "115200", "230400", "460800", "921600"]
        self.baud_rate_label = Label(self,text="Baud Rate ", font ="Courier 12 bold")
        self.baud_rate_label.place(x=20, y = 750)
        
        self.baud_rate_dropdown = ttk.Combobox(self, font ="Courier 12", width = 20, state="readonly", values=baud_rate_values)
        self.baud_rate_dropdown.place(x=120, y = 750)

        self.connect_Button = Button(self, text = "Connect", font ="Courier 12 bold", height = 1, width =10, command=lambda:threading.Thread(target=self.click_connectButton).start())
        self.connect_Button.place(x = 430, y = 700)

        self.connect_status_label = Label(self, text="Status: ", font="Courier 12 bold")
        self.connect_status_label.place(x = 430, y =750)


        
        # Data Recorder Group Box
        self.RB = LabelFrame(self,text="Record", font ="Courier 15 bold",width =910, height=130)
        self.RB.place(x=620,y=670)

        self.data_field_label = Label(self, text="Data fields:", font ="Courier 12 bold")
        self.data_field_label.place(x = 650, y = 700)
    
        self.data_field_values_label = Label(self, text="1, 2, 3, 4 ", font ="Courier 12 bold")
        self.data_field_values_label.place(x = 850, y = 700)

        self.data_field_select_label = Label(self, text="Data fields Select: ", font ="Courier 12 bold")
        self.data_field_select_label.place(x = 650, y = 730)

        self.data_field_select_entry = Entry(self, font ="Courier 12", width = 20)
        self.data_field_select_entry.place(x = 850, y = 730)
    
        self.file_name_label = Label(self, text="File Name: ", font ="Courier 12 bold")
        self.file_name_label.place(x = 650, y = 760)

        self.file_name_entry = Entry(self, font ="Courier 12", width = 20)
        self.file_name_entry.place(x = 850, y = 760)
    
        
        
        self.record_Button = Button(self, text = "Record", font ="Courier 12 bold", height = 1, width =10, command=lambda:threading.Thread(target=self.click_recordButton).start())
        self.record_Button.place(x = 1200, y = 690)
        
        self.stop_Button = Button(self, text = "Stop", font ="Courier 12 bold", height = 1, width =10, command=lambda:threading.Thread(target=self.click_stopButton).start())
        self.stop_Button.place(x = 1320, y = 690)
        
        self.clear_Button = Button(self, text = "Clear", font ="Courier 12 bold", height = 1, width =10, command=lambda:threading.Thread(target=self.click_clearButton).start())
        self.clear_Button.place(x = 1200, y = 730)
        
        self.write_Button = Button(self, text = "Write", font ="Courier 12 bold", height = 1, width =10, command=lambda:threading.Thread(target=self.click_writeButton).start())
        self.write_Button.place(x = 1320, y = 730)
        
        self.record_status_label = Label(self, text = "Status:", font = "Courier 12 bold")
        self.record_status_label.place(x = 1200, y = 770)
        
        self.record_status_val_label = Label(self, text = "Recording", font = "Courier 12 bold")
        self.record_status_val_label.place(x = 1300, y = 770)
        
        # Live group box
        self.RV = LabelFrame(self,text="Live", font ="Courier 15 bold",width =390, height=670)
        self.RV.place(x=1150,y=0)
    
    def plotGraph(self):
        self.fig=plt.figure(figsize = (5, 2))
        
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 5))
        y_vals2.append(random.randint(0, 5))
        # Plot new data
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().place(x = -60, y = 30)
        
        ani = FuncAnimation(self.fig, self.animate, interval=10, blit=False)
        self.canvas.draw()

    def animate(self, i):
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 5))
        plt.cla()  # clear the current axes
        plt.plot(x_vals, y_vals)
        
    def click_connectButton(self):
        
        return True




if __name__=='__main__':
  root = mainWindow()
  root.mainloop()