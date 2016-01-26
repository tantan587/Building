
import sqlite3
import tkinter
import tkinter.messagebox
conn = sqlite3.connect('example.db')
c = conn.cursor()

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

d = c.execute('SELECT date FROM stocks')

for row in d: 
	print(row)

a = row





top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", a)

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()


