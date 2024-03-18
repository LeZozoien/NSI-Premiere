import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_192=tk.Entry(root)
        GLineEdit_192["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_192["font"] = ft
        GLineEdit_192["fg"] = "#333333"
        GLineEdit_192["justify"] = "center"
        GLineEdit_192["text"] = "Entry"
        GLineEdit_192.place(x=150,y=50,width=300,height=150)

        GButton_390=tk.Button(root)
        GButton_390["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_390["font"] = ft
        GButton_390["fg"] = "#000000"
        GButton_390["justify"] = "center"
        GButton_390["text"] = "Encrypt"
        GButton_390.place(x=200,y=230,width=70,height=25)
        GButton_390["command"] = self.GButton_390_command

        GButton_496=tk.Button(root)
        GButton_496["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_496["font"] = ft
        GButton_496["fg"] = "#000000"
        GButton_496["justify"] = "center"
        GButton_496["text"] = "Decrypt"
        GButton_496.place(x=330,y=230,width=70,height=25)
        GButton_496["command"] = self.GButton_496_command

    def GButton_390_command(self):
        alphabet = [chr(ord("a") + i) for i in range(26)]

        chaine_a_coder = root.GLineEdit_192.get()
        chaine_a_coder = chaine_a_coder.lower()

        resultat = ""

        cle = ""
        for i in range(20):
            cle += str(randint(0, 9))

        cles = []
        for j in range(5):
            cles.append(cle[j*4 : j*4+4])


        for passage in range(5):
            for index in range(len(chaine_a_coder)):
                try:
                    resultat += alphabet[((alphabet.index(chaine_a_coder[index])) + int(cles[passage][index % len(cles[passage])])) % 26]
                except ValueError:
                    resultat += chaine_a_coder[index]
            chaine_a_coder = resultat
            resultat = ""
            print(chaine_a_coder)
            
        return chaine_a_coder + " " + cle


    def GButton_496_command(self):
        print("Decrypt")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()