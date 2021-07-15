from tkinter import*
import random
import os
import matplotlib.pyplot as plt
import numpy as np


def __Library__():
       filename = 'Library_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)

def __information__():
       filename = 'Std_info_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __FeeReport__():
       filename = 'Fee_Frontend.py'
       os.system(filename)
       os.system('notepad' + filename)

def __Graph__():
       # set width of bar
       barWidth = 0.25
       fig = plt.subplots(figsize =(12, 8))

       # set height of bar
       IT = [100, 50, 69, 58, 82]
       ECE = [29, 46, 25, 32, 20]
       CSE = [49, 83, 94, 65, 77]

       # Set position of bar on X axis
       br1 = np.arange(len(IT))
       br2 = [x + barWidth for x in br1]
       br3 = [x + barWidth for x in br2]

       # Make the plot
       plt.bar(br1, IT, color ='r', width = barWidth,
                     edgecolor ='grey', label ='IT')
       plt.bar(br2, ECE, color ='g', width = barWidth,
                     edgecolor ='grey', label ='ECE')
       plt.bar(br3, CSE, color ='b', width = barWidth,
                     edgecolor ='grey', label ='CSE')

       # Adding Xticks
       plt.xlabel('Book Name', fontweight ='bold', fontsize = 15)
       plt.ylabel('Number of Books', fontweight ='bold', fontsize = 10)
       plt.xticks([r + barWidth for r in range(len(IT))],
                     ['C++ by Y.Kanetkar', 'Java by J.Bloch', 'Pyhton by John Zelle', 'PHP by Alan Forbes', 'OS by S.Abraham'])

       plt.legend()
       plt.show()
       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'navajo white')
       
       title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'raise', bd = 13)
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'V.E.S.I.T', font = ('arial',30,'bold'), bg = 'navajo white')
       title_Label.grid(row = 0, column = 0, padx = 150)


       #========================================================FRAMES===================================================================
       Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_1.grid(row = 1, column = 0, padx = 280)
       Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
       Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_3.grid(row = 3, column = 0, pady = 7)
       Frame_4 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'navajo white', relief = 'ridge', bd = 10)
       Frame_4.grid(row = 4, column = 0, pady = 7)
       


       #========================================================LABELS===================================================================
       Label_1 = Label(Frame_1, text = 'STUDENT PROFILE', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_1.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2 = Label(Frame_2, text = 'FEE REPORT', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_2.grid(row = 0, column = 0, padx = 100, pady = 5)
       Label_3 = Label(Frame_3, text = 'LIBRARY SYSTEM', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_3.grid(row = 0, column = 0, padx = 60, pady = 5)
       Label_4 = Label(Frame_4, text = 'ANALYSIS GRAPH', font = ('arial',25,'bold'), bg = 'navajo white')
       Label_4.grid(row = 0, column = 0, padx = 60, pady = 5)
       


       #========================================================BUTTONS===================================================================
       Button_1 = Button(Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __information__)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __FeeReport__)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Library__)
       Button_3.grid(row = 0, column = 3, padx = 50)
       Button_4 = Button(Frame_4, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __Graph__)
       Button_4.grid(row = 0, column = 3, padx = 50)
       
       

       root.mainloop()


       
       
if __name__ == '__main__':
       menu()
