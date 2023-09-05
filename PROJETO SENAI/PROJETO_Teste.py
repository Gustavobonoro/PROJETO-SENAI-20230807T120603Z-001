from tkinter import *
import pandas as pd

arquivo = pd.read_excel('Rogerio.xlsx')
arquivo = arquivo.to_string(index=False, col_space=20, justify='left')





wdw = Tk()
label = Label(wdw, text=arquivo, relief='solid', font='Arial 16')
label.pack()
wdw.mainloop()