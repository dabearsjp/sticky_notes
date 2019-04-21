#Library for Gui
from tkinter import *

#Class for individual notes
class Note:

    def __init__(self, saved_text):

        #The type of window
        self.note = Toplevel()

        #Creating visual
        self.note.title("note")
        self.note.config(bg="khaki1")
        self.note.geometry("300x300")

        #Save button on notes
        save = Button(self.note, text="Press to save", font=(None, 16))
        save.pack(side="bottom", )

        #Delete button on notes
        delete = Button(self.note, text="Press to delete", font=(None, 16))
        delete.pack(side="bottom")

        #Creating the text which allows for typing on notes
        self.content = Text(self.note, font=(None, 12), bg="khaki1", width=200, height=200)
        self.content.insert(END, saved_text)
        self.content.pack(side="left")
        self.content.focus_set()

        #Setting the commands of the buttons
        save.config(command=self.save_it)
        delete.config(command=self.delete_it)


    def save_it(self):
        #Makes sure nothing is still running
        self.note.update()

        #Puts the text into one line for easy storing
        a = " ".join(self.content.get(1.0, END).splitlines())

        #Storing the text in my text file for later
        f = open("notes.txt", "a+")
        if f.read() == "":
            f.write(a + "\n")
        else:
            f.write("\n" + a)

        f.close()

    def delete_it(self):
        self.note.update()
        #Getting the text from the note
        content = self.content.get(1.0, END)

        f = open("notes.txt", "r+")

        #Putting the saved notes in a list for enumeration
        notes = f.read().splitlines()

        #Converting the notes into tkinter.Text files for comparison
        for i in range(len(notes)):
            text = notes[i]
            notes[i] = Text(self.note)
            notes[i].insert(END, text)
            if notes[i].get(1.0, END) == content:
                del notes[i]
                break

        #Converting the files back for storing
        for i in range(len(notes)):
            if type(notes[i]) != str:
                notes[i] = notes[i].get(1.0, END)

        #Clears the text files old info and rewrites it without the deleted note
        f.truncate(0)
        for i in notes:
            f.write(i)



#Main Tkinter Application (Main menu)
class Application:

    def __init__(self, master):
        self.master = master
        master.title("Sticky self.notes")
        master.config(bg="khaki1")
        master.geometry("500x250")
        master.attributes("-topmost", True)

        welcome = Label(master, text="Welcome to Sticky note!", bg="khaki1",
                        font=(None, 26), width=200, height=3)
        welcome.pack()

        button = Button(master, text="Create a sticky note", command=lambda : self.create_note(""),
                        width=15, height=3, font=(None, 16))
        button.pack()

    #Creates a new note object which we defined above and doesn't pass in any text
    def create_note(self, saved_text):
        Note("")






#Creating the main Tk Application, this is necessary
root = Tk()
gui = Application(root)

#Looking through the notes.txt where we stored our notes and creating new notes with the data
f = open("notes.txt", "r")

for i in f.read().splitlines():
    Note(i)

f.close()

#This is what keeps the program running, this is necessary
root.mainloop()

