from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile

class App:
  def __init__(self, master):

##########
    frame_database = LabelFrame(master, text='Connection Info', padx=5, pady=5)
    frame_database.pack(padx=5, pady=5, fill='x')

    self.lbl_browse = Label(frame_database, text='Database:').grid(row=0, column=0, padx=5, pady=5)
    self.ent_browse = Entry(frame_database).grid(row=0, column=1, padx=5, pady=5)
    self.btn_browse = Button(frame_database, text='Browse..', command=self.load_file).grid(row=0, column=2, padx=5, pady=5)

    self.lbl_uname = Label(frame_database, text='Username:').grid(row=1, column=0, padx=5, pady=5)
    self.ent_uname = Entry(frame_database).grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='we')

    self.lbl_pword = Label(frame_database, text='Password:').grid(row=2, column=0, padx=5, pady=5)
    self.ent_pword = Entry(frame_database, show='*').grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky='we')

##########
    frame_output = LabelFrame(master, text='Output File', padx=5, pady=5)
    frame_output.pack(padx=5, pady=5, fill='x')

    self.lbl_ofile = Label(frame_output, text='File:').grid(row=0, column=0, padx=5, pady=5)
    self.ent_ofile = Entry(frame_output).grid(row=0, column=1, padx=5, pady=5)
    self.btn_ofile = Button(frame_output, text='Save As..', command=self.save_file).grid(row=0, column=2, padx=5, pady=5)

    self.lbl_ftype = Label(frame_output, text='Format:').grid(row=1, column=0, padx=5, pady=5)
    self.ftype = StringVar(master)
    self.ftype.set('CSV')
    #(S - binary, Si - INSERTs, Sc - CSV, Sh - HTML)
    self.menu_ftype = OptionMenu(frame_output, self.ftype, 'binary', 'INSERTs', 'CSV', 'HTML').grid(row=1, column=1, padx=5, pady=5)

##########
    frame_data = LabelFrame(master, text='Data', padx=5, pady=5)
    frame_data.pack(padx=5, pady=5, fill='x')

    self.lbl_table = Label(frame_data, text='Table:').grid(row=0, column=0, padx=5, pady=5)
    self.ent_table = Entry(frame_data).grid(row=0, column=1, padx=5, pady=5)

##########
    self.btn_export = Button(master, text='Export', command=self.export)
    self.btn_export.pack(padx=5, pady=5)


  def load_file(self):
    name = askopenfilename(filetypes=[("Firebird Database","*.fdb")])
    # TODO Error!?
    self.ent_browse.insert(0, name)

  def save_file(self):
    # TODO
    return

  def export(self):
    # TODO
    return


root = Tk()

root.title('fbexport GUI')

menubar = Menu(root)
menubar.add_command(label='File')
menubar.add_command(label='About')
root.config(menu=menubar)

root.resizable(False, False)


app = App(root)
root.mainloop()
