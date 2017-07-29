#!/usr/bin/env python3
#
# calculator - A simple calculator.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk

__version__ = '1.0'

class Calculator(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(expand=True, fill='both')
        self.master.title('Calculator - '+__version__)
        #self.master.geometry('300x200')
        self.master.protocol('WM_DELETE_WINDOW', self.closeApp)
        self.setupUI()

    def setupUI(self):
        keys = ('AC', 'CE', '%', '÷',
            '7', '8', '9', 'x',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=')

        row = 0
        column = 0
        for idx, char in enumerate(keys):
            if column == 4:
                row += 1
                column = 0
            cal_btn = tk.Button(self, text=char)
            cal_btn.grid(row=row, column=column)
            cal_btn.bind('<Button-1>', self.buttonHandler)
            column += 1

    def buttonHandler(self, event):
        print(event.widget.cget('text'))

    def closeApp(self):
        self.master.destroy()

def main():
    app = Calculator()
    app.mainloop()

if __name__ == '__main__':
    main()
