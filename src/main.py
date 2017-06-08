from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile


class App:

  RADIO_URL = 1
  RADIO_FILE = 2
  RADIO_TABLE = 1
  RADIO_SQL = 2

  def __init__(self, master, ttk):

    master.title('fbexport GUI')
    master.resizable(False, False)

    menubar = Menu(master)
    menubar.add_command(label='File')
    menubar.add_command(label='About')
    master.config(menu=menubar)

########## DATABASE INFO
    self.frame_database = LabelFrame(master, text='Connection Info', padx=5, pady=5)
    self.frame_database.pack(padx=5, pady=5, fill='x')

    self.stream = IntVar()
    self.stream.set(1)

    Radiobutton(self.frame_database, value=App.RADIO_URL, variable=self.stream, text='URL:', command=self.conn_type).grid(row=0, column=0, padx=5, pady=5)
    Entry(self.frame_database, name='url').grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='we')

    Radiobutton(self.frame_database, value=App.RADIO_FILE, variable=self.stream, text='File:', command=self.conn_type).grid(row=1, column=0, padx=5, pady=5)
    Entry(self.frame_database, name='browse').grid(row=1, column=1, padx=5, pady=5)
    Button(self.frame_database, name='browse_btn', text='Browse..', command=self.load_file).grid(row=1, column=2, padx=5, pady=5)

    Label(self.frame_database, text='Username:').grid(row=2, column=0, padx=5, pady=5)
    Entry(self.frame_database, name='dtb').grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky='we')

    Label(self.frame_database, text='Password:').grid(row=3, column=0, padx=5, pady=5)
    Entry(self.frame_database, name='pword', show='*').grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky='we')

##########
    self.frame_data = LabelFrame(master, text='Data', padx=5, pady=5)
    self.frame_data.pack(padx=5, pady=5, fill='x')

    self.data = IntVar()
    self.data.set(1)

    Radiobutton(self.frame_data, value=App.RADIO_TABLE, variable=self.data, command=self.data_type, text='Table:').grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    Entry(self.frame_data, name='table').grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='we')

    Label(self.frame_data, text='Where:').grid(row=1, column=1, padx=5, pady=5, sticky='we')
    Entry(self.frame_data, name='where').grid(row=1, column=2, columnspan=2, sticky='we', padx=5, pady=5)

    Radiobutton(self.frame_data, value=App.RADIO_SQL, variable=self.data, command=self.data_type, text='SQL:').grid(row=2, column=0, padx=5, pady=5, columnspan=2)
    Entry(self.frame_data, name='sql').grid(row=2, column=2, padx=5, pady=5)
    Button(self.frame_data, name='sql_btn', text='Browse..', command=self.load_file).grid(row=2, column=3, padx=5, pady=5)

##########
    self.action_frame = Frame(master)
    self.action_frame.pack()
    Button(self.action_frame, text='Save As...').grid(row=0, column=0, padx=5, pady=5)
    Button(self.action_frame, text='Export As...', command=self.export()).grid(row=0, column=1, padx=5, pady=5)

    self.data_type()
    self.conn_type()


  def save(self):
    return

  def data_type(self):
    radio_val = self.data.get()
    data_children = self.frame_data.children
    table_widgets = [data_children['table'], data_children['where']]
    sql_widgets = [data_children['sql'], data_children['sql_btn']]

    if radio_val == App.RADIO_TABLE:
      for widget in sql_widgets:
        widget.configure(state='disable')

      for widget in table_widgets:
        widget.configure(state='normal')

      table_widgets[0].focus()
    elif radio_val == App.RADIO_SQL:
      for widget in table_widgets:
        widget.configure(state='disable')

      for widget in sql_widgets:
        widget.configure(state='normal')

      sql_widgets[0].focus()

  def conn_type(self):
    radio_val = self.stream.get()
    dtb_children = self.frame_database.children
    browse_widgets = [dtb_children['browse'], dtb_children['browse_btn']]
    url_widgets = [dtb_children['url']]

    if radio_val == App.RADIO_URL:
      for widget in browse_widgets:
        widget.configure(state='disable')

      for widget in url_widgets:
        widget.configure(state='normal')
      url_widgets[0].focus()

    elif radio_val == App.RADIO_FILE:
      for widget in url_widgets:
        widget.configure(state='disable')

      for widget in browse_widgets:
        widget.configure(state='normal')
      browse_widgets[0].focus()


  def load_file(self):
    name = askopenfilename(filetypes=[("Firebird Database", "*.fdb")])

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
app = App(root, ttk)
root.mainloop()
