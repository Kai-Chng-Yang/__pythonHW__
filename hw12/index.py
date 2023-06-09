'''
專案在學習grid的編排
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Window(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('red.TFrame', background='#ff0000')
        ttkStyle.configure('white.TFrame',background='#ffffff')
        ttkStyle.configure('yellow.TFrame',background='yellow')
        ttkStyle.configure('white.TLabel', background='#ffffff')
        ttkStyle.configure('gridLabel.TLabel', font=('Helvetica', 16),foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry', font=('Helvetica', 16))


        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand = True, fill =tk.BOTH,padx=30,pady=30)

        topFrame = ttk.Frame(mainFrame, heigh = 100)
        topFrame.pack(expand = True, fill = tk.X)

        ttk.Label(topFrame, text="BMI試算表", font=('Helvetica', '20')).pack(pady=20)

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True, fill=tk.BOTH)
        bottomFrame.columnconfigure(0,weight=3,pad=20)
        bottomFrame.columnconfigure(1,weight=5,pad=20)
        bottomFrame.rowconfigure(0, weight=1,pad=20)
        bottomFrame.rowconfigure(3, weight=1,pad=20)
        bottomFrame.rowconfigure(4, weight=1,pad=20)
        bottomFrame.rowconfigure(5, weight=1,pad=20)
        bottomFrame.rowconfigure(6, weight=1,pad=20)
        

        ttk.Label(bottomFrame, text="姓名:", style='gridLabel.TLabel').grid(column=0, row=0, sticky=tk.E)
        nameEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        nameEntry.grid(column=1,row=0,sticky=tk.W,padx=10)
    

        ttk.Label(bottomFrame,text="出生年月日:",style='gridLabel.TLabel').grid(column=0,row=1,sticky=tk.E)
        ttk.Label(bottomFrame,text="(2000/03/01)",style='gridLabel.TLabel').grid(column=0,row=2,sticky=tk.E)

        birthEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        birthEntry.grid(column=1,row=1,sticky=tk.W,rowspan=2,padx=10)

        ttk.Label(bottomFrame,text="身高(cm):",style='gridLabel.TLabel').grid(column=0,row=3,sticky=tk.E)
        heightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        heightEntry.grid(column=1,row=3,sticky=tk.W,padx=10)

        ttk.Label(bottomFrame,text="體重(kg):",style='gridLabel.TLabel').grid(column=0,row=4,sticky=tk.E)
        weightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        weightEntry.grid(column=1,row=4,sticky=tk.W,padx=10)

        self.height = tk.DoubleVar
        self.weight = tk.DoubleVar

        heightEntry.delete(0, tk.END)
        weightEntry.delete(0, tk.END)

        self.r = tk.DoubleVar
        
        
        messageText = tk.Text(bottomFrame,height=5,width=35,state=tk.DISABLED,takefocus=0,bd=0)
        messageText.grid(column=0,row=5,sticky=tk.N+tk.S,columnspan=2)

        commitBtn = ttk.Button(bottomFrame,text="計算", command=calculate_BMI, font=12)
        commitBtn.grid(column=1,row=6,sticky=tk.W)

        self.ent6 = tk.Entry(self.win, textvariable=self.r)
        self.ent6.delete(0, tk.END)
        self.ent6.grid(row=6, columnspan=2, padx=10, pady=10)
    
        def calculate_BMI():
            try:
                self.r.set(self.weight / (self.height/100) ** 2)
            except:
                heightEntry.delete(0, tk.END)
                weightEntry.delete(0, tk.END)
                self.ent6.delete(0, tk.END)
                
            commitBtn = ttk.Button(bottomFrame,text="計算", command=calculate_BMI, font=12)
            commitBtn.grid(column=1,row=6,sticky=tk.W)

        



'''class Window(tk.Tk):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.configure('back.TFrame', background = "#ff5")
        
        mainFrame = ttk.Frame(self, style ='back.TFrame')
        mainFrame.pack(expand = True, fill = tk.BOTH)

        topFame = ttk.Frame(mainFrame, style ='back.TFrame')
        topFame.pack(expand = True, fill = tk.X)

        bottomFrame = ttk.Frame(mainFrame, style ='back.TFrame')
        bottomFrame.pack(expand=True, fill=tk.BOTH)
'''


def main():
    '''
    這是程式的執行點
    '''
    window = Window()
    window.title("BMI計算")
    #window.geometry("400x500")
    window.mainloop()

if __name__ == "__main__":
    main()

#round(self.weight / (self.height/100) ** 2, ndigits=2)