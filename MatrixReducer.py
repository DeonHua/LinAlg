__author__ = 'Deon Hua'
__date__ = '2 November 2014'
'''
This GUI-based program will row-reduce a matrix to RREF form.
It will ask the user to enter the size of the matrix (rows and columns), with their preferred output format.
'''
import tkinter
import tkinter.ttk as ttk
from sympy import *
init_printing()

class Reducer:
    '''
    Takes user input of a matrix and row-reduces it to RREF.

    GUI-Based interface that asks the user for the # of rows and columns, as well as output formatting.
    The program can output as a fraction or a decimal with a specified number of decimals.
    '''


    def __init__(self):
        '''
        Initializes the GUI interface that asks the user for input.

        No parameters or returns.
        '''

        self.main_window = tkinter.Tk()
        self.main_window.wm_title("Matrix Format Setup")


        #Initalize frames.
        self.info_frame = ttk.Frame()
        self.size_frame = ttk.Frame()
        self.format_frame = ttk.Frame()
        self.digit_frame = ttk.Frame()
        self.button_frame = ttk.Frame()

        #Object for the information frame.
        self.info_label = ttk.Label(self.info_frame, text="Enter the number of rows and columns, your preferred output format,"
                                               " and the number of trailing decimals if applicable.", justify="left",
                                        wraplength=275).pack()

        #Objects for the size frame - the matrix's rows/columns are set here.
        self.row_label = ttk.Label(self.size_frame, text="Rows:").pack(side="left")
        self.row = ttk.Entry(self.size_frame, width=3)
        self.row.pack(side="left")
        self.col_label = ttk.Label(self.size_frame, text="Columns:").pack(side="left")
        self.col = ttk.Entry(self.size_frame, width=3)
        self.col.pack(side="left")

        #Objects for the digit frame
        self.digit_label = ttk.Label(self.digit_frame, text="Digits:")
        self.digit = ttk.Entry(self.digit_frame, width=3)

        #Objects for the format frame - the output formatting is specified here.
        self.output_var = tkinter.IntVar()
        self.output_var.set(0)

        self.fraction = ttk.Radiobutton(self.format_frame, text="Fraction", variable=self.output_var, value=0,
                                            command=self.hide_digits).pack(side="left")

        self.decimal = ttk.Radiobutton(self.format_frame, text="Decimal", variable=self.output_var, value=1,
                                           command=self.show_digits).pack(side="left")

        #Object for the bottom frame

        self.button = ttk.Button(self.button_frame, text="Enter Values", command=self.matrix_input).pack()

        #Pack frames.
        self.info_frame.pack(anchor="nw")
        self.size_frame.pack(anchor="nw")
        self.format_frame.pack(anchor="nw")
        self.digit_frame.pack(anchor="nw")
        self.button_frame.pack(anchor="n")

        self.main_window.mainloop()

    def show_digits(self):
        self.digit_label = ttk.Label(self.digit_frame, text="Digits:")
        self.digit = ttk.Entry(self.digit_frame, width=3)
        self.digit_label.pack(side="left")
        self.digit.pack(side="left")

    def hide_digits(self):
        self.digit_label.destroy()
        self.digit.destroy()

    def matrix_input(self):
        '''
        Uses a 2D array of entry fields to take input.
        :return:
        '''
        input_win = tkinter.Tk()
        input_win.wm_title("Matrix Input")

        self.num_rows = int(self.row.get())
        self.num_cols = int(self.col.get())
        self.input_fields = [ttk.Entry()] * self.num_rows * self.num_cols

        instructions = ttk.Label(input_win, text = "Enter your values below.").pack()

        for i in range (self.num_rows):
            frame = tkinter.Frame(input_win)
            for j in range(self.num_cols):
                self.input_fields[i+j] = ttk.Entry(frame, width = 5)
                self.input_fields[i+j].pack(side = "left")
            frame.pack()
        reduce = ttk.Button(input_win, text = "Reduce Matrix!", command = self.reduce).pack()
        input_win.mainloop()

    def reduce(self):
        #Sets up entries, a 2D Array (Matrix of size rows X cols)
        self.entries = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(self.input_fields[i+j].get())
            self.entries.append(row)

        print(self.entries)
        self.matrix = Matrix(self.entries)

        print(latex(self.matrix))


        self.reduced = self.matrix.rref()[0]
        print (self.reduced)
        return latex(self.matrix)

    def reduceTest(self):
        self.entries = [[3,4], [1,2]]
        self.matrix = Matrix(self.entries)
        print (latex(self.matrix))
        return latex(self.matrix)

    def output(self):
        pass

reducer = Reducer()
reducer.reduceTest()