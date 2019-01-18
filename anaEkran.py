from tkinter import *
from tkinter import ttk
import math

### Global Değişkenler ###


def bosfonk():
    print("Boş fonksiyon!")

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        ### Sınıf Değişkenleri ###
        self.stateBeacon = BooleanVar()

        ### Pencere Ayarları ###
        self.master.title("pitConnect Kumanda Paneli (v1.0)")
        self.master.iconbitmap('img/favicon.ico')
        self.master.minsize(640, 400)
        self.master.state("zoomed")

        ### Menu Ayarları ###
        menu = Menu(self.master)
        self.master.config(menu=menu)
        menuOturum = Menu(menu)
        menuOturum.add_command(label="Yeni Oturum", command=bosfonk)
        menuOturum.add_command(label="Oturumu Sonlandır", command=bosfonk)
        menuOturum.add_separator()
        menuOturum.add_command(label="Çıkış", command=self.master.quit)
        menuYardim = Menu(menu)
        menuYardim.add_command(label="Hakkında", command=bosfonk)
        menu.add_cascade(label="Oturum", menu=menuOturum)
        menu.add_cascade(label="Yardım", menu=menuYardim)

        ### TAB Ayarları ###
        tabControl = ttk.Notebook(self.master)
        tabGK = ttk.Frame(tabControl)
        tabUK = ttk.Frame(tabControl)
        tabControl.add(tabGK, text="Görev Kontrol")
        tabControl.add(tabUK, text="Uçuş Kontrol")
        tabControl.pack(expan=1, fill="both")

        ### Görev Kontrol ###
        lblHazirlik = Label(tabGK, text="Görev Kontrol Kısmı Tasarlanıyor...")
        lblHazirlik.grid()

        ### Uçuş Kontrol ###
        for r in range(5):
            tabUK.rowconfigure(r, weight=1)
        for c in range(5):
            tabUK.columnconfigure(c, weight=1)

        tabUK.frManuel = Frame(tabUK)
        tabUK.frManuel.grid(row=0, column=0, rowspan=3, columnspan=3, sticky=W + E + N + S)
        tabUK.frOtonom = Frame(tabUK)
        tabUK.frOtonom.grid(row=2, column=0, rowspan=3, columnspan=3, sticky=W + E + N + S)
        tabUK.frTelemetri = Frame(tabUK)
        tabUK.frTelemetri.grid(row=0, column=2, rowspan=6, columnspan=3, sticky=W + E + N + S)

        ### Frame: Manuel Kontrol
        lblManKont = Label(tabUK.frManuel, text="Manuel Kontrol")
        lblManKont.grid(row=0)
        lblGaz = Label(tabUK.frManuel, text="Gaz Kolu(%):")
        lblGaz.grid(row=1)
        sldGazKolu = Scale(tabUK.frManuel, from_=100, to=0)
        sldGazKolu.grid(row=1, column=1)

        cbMnBeacon = Checkbutton(tabUK.frManuel, text="Beacon Işıkları", var=self.stateBeacon, command=self.stateUpdate)
        cbMnBeacon.grid(row=2,sticky=E)

        self.ledCnv = Canvas(tabUK.frManuel, width=20, height=20)
        self.ledCnv.grid(row=2, column=1)
        self.ledStatCrc = self.ledCnv.create_oval(2,2,20,20,fill="red")


        ### Frame: Otonom
        lblOtonom = Label(tabUK.frOtonom, text="Otonom Kontrol")
        lblOtonom.grid()
        cbOtonomYukseklik = Checkbutton(tabUK.frOtonom, text="Asılı Kal (1m)")
        cbOtonomYukseklik.grid(row=1, sticky=E)
        cbTakeOff = Checkbutton(tabUK.frOtonom, text="Take-Off")
        cbTakeOff.grid(row=2, sticky=E)

        ### Frame: Telemetri
        lblTelem = Label(tabUK.frTelemetri, text="Telemetri")
        lblTelem.grid(sticky=E)
        lblRoll = Label(tabUK.frTelemetri, text="Roll:")
        lblRoll.grid(row=1, sticky=E)
        lblRollVal = Label(tabUK.frTelemetri, text="-15 \N{DEGREE SIGN}")
        lblRollVal.grid(row=1, column=1, sticky=E)
        lblPitch = Label(tabUK.frTelemetri, text="Pitch:")
        lblPitch.grid(row=2, sticky=E)
        lblPitchVal = Label(tabUK.frTelemetri, text="218 \N{DEGREE SIGN}")
        lblPitchVal.grid(row=2, column=1, sticky=E)
        lblYaw = Label(tabUK.frTelemetri, text="Yaw:")
        lblYaw.grid(row=3, sticky=E)
        lblYawVal = Label(tabUK.frTelemetri, text="-173 \N{DEGREE SIGN}")
        lblYawVal.grid(row=3, column=1, sticky=E)

        self.cnvYapayUfuk = Canvas(tabUK.frTelemetri, width=100, height=100)
        self.cnvYapayUfuk.grid(row=1, column=3)
        self.yuYatay = self.cnvYapayUfuk.create_line(0,50,100,50, fill="black")

        self.dondur(25)

        ### StatusBar ###
        lblStatus = Label(self.master, text="Hazır...", bd=1, relief=SUNKEN, anchor=W)
        lblStatus.pack(side=BOTTOM, fill=X)

    def stateUpdate(self):
        if self.stateBeacon.get():
            print("Işıkları Yak!")
            self.ledCnv.itemconfig(self.ledStatCrc, fill="#53c20f")
        else:
            print("Işıkları Söndür")
            self.ledCnv.itemconfig(self.ledStatCrc, fill="red")

    def dondur(self,aciDerece):
        aciRad = aciDerece*math.pi/180
        uzunlukB2 = 50
        center_x = 50
        center_y = 50
        x0 = center_x - uzunlukB2 * math.cos(aciRad)
        x1 = center_x + uzunlukB2 * math.cos(aciRad)
        y1 = center_y + uzunlukB2 * math.sin(aciRad)
        y0 = center_y - uzunlukB2 * math.sin(aciRad)
        self.cnvYapayUfuk.coords(self.yuYatay,x0,y0,x1,y1)

root = Tk()
app = Application(master=root)
app.mainloop()