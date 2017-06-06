from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile


class App:
  def __init__(self, master):

    menubar = Menu(master)
    menubar.add_command(label='File')
    menubar.add_command(label='About')
    master.config(menu=menubar)

    master.title('fbexport GUI')
    master.resizable(False, False)

##########
    self.frame_database = LabelFrame(master, text='Connection Info', padx=5, pady=5)
    self.frame_database.pack(padx=5, pady=5, fill='x')

    Label(self.frame_database, text='Database:').grid(row=0, column=0, padx=5, pady=5)
    Entry(self.frame_database, name='browse').grid(row=0, column=1, padx=5, pady=5)
    Button(self.frame_database, text='Browse..', command=self.load_file).grid(row=0, column=2, padx=5, pady=5)

    Label(self.frame_database, text='Username:').grid(row=1, column=0, padx=5, pady=5)
    Entry(self.frame_database, name='dtb').grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='we')

    Label(self.frame_database, text='Password:').grid(row=2, column=0, padx=5, pady=5)
    Entry(self.frame_database, name='pword', show='*').grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky='we')

##########
    self.frame_output = LabelFrame(master, text='Output File', padx=5, pady=5)
    self.frame_output.pack(padx=5, pady=5, fill='x')

    Label(self.frame_output, text='File:').grid(row=0, column=0, padx=5, pady=5)
    Entry(self.frame_output, name='ofile').grid(row=0, column=1, padx=5, pady=5)
    Button(self.frame_output, text='Save As..', command=self.save_file).grid(row=0, column=2, padx=5, pady=5)

    Label(self.frame_output, text='Format:').grid(row=1, column=0, padx=5, pady=5)
    self.ftype = StringVar(master)
    self.ftype.set('CSV')
    #(S - binary, Si - INSERTs, Sc - CSV, Sh - HTML)
    self.menu_ftype = OptionMenu(self.frame_output, self.ftype, 'binary', 'INSERTs', 'CSV', 'HTML').grid(row=1, column=1, padx=5, pady=5)

##########
    self.frame_data = LabelFrame(master, text='Data', padx=5, pady=5)
    self.frame_data.pack(padx=5, pady=5, fill='x')

    Label(self.frame_data, text='Table:').grid(row=0, column=0, padx=5, pady=5)
    Entry(self.frame_data, name='table').grid(row=0, column=1, padx=5, pady=5)

##########
    self.btn_export = Button(master, text='Export', command=self.export)
    self.btn_export.pack(padx=5, pady=5)

  def load_file(self):
    name = askopenfilename(filetypes=[("Firebird Database","*.fdb")])

    self.frame_database.children['browse'].insert(0, name)
    self.frame_database.children['browse'].xview(END)

  def save_file(self):
    # TODO
    return

  def export(self):
    # TODO
    '''
    info = {
      'connection': {
        'file': self.ent_browse.get(),
        'usernmae': self.ent_uname.get(),
        'password': self.ent_pword.get()
      },
      'output': {
        'file': self.ent_ofile.get(),
        'type': self.ftype
      },
      'data': {
        'table': self.ent_table.get()
      }
    }
    '''
    return

root = Tk()
app = App(root)
root.mainloop()
