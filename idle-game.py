import tkinter as tk
import time

class App(tk.Frame) :
    def __init__(self, master =None):
        super().__init__(master)        ## permit access to tk.Frame functions
        self.master.title("Idle Game")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        global prix1, prix2, prix3, prix4
        global btn_text1, btn_text2, btn_text3, btn_text4
        global glb_text

        self.fenprinc = tk.Canvas(self,width = '640', height = '480', bg = 'white')
        self.fenprinc.pack()

        self.recolte_label = tk.Label(fenetre, textvariable = glb_text)
        self.recolte_label.place(x=270,y=30)
       
        self.fenprinc.create_text(30,100, text = 'Pack 1')
        self.pack1_button = tk.Button(fenetre, textvariable = btn_text1, command = self.pack1)
        self.pack1_button.place(x=300,y=90)

        self.fenprinc.create_text(30,150, text= 'Pack 2')        
        self.pack2_button = tk.Button(fenetre, textvariable = btn_text2, command = self.pack2)
        self.pack2_button.place(x=300,y=140)
        
        self.fenprinc.create_text(30,200, text= 'Pack 3')
        self.pack3_button = tk.Button(fenetre, textvariable = btn_text3, command = self.pack3)
        self.pack3_button.place(x=300,y=190)
        
        self.fenprinc.create_text(30,250, text= 'Pack 4')
        self.pack4_button = tk.Button(fenetre, textvariable = btn_text4, command = self.pack4)
        self.pack4_button.place(x=300,y=240)

        self.fenprinc.create_text(30,300, text= 'Time')
        self.farm_button = tk.Button(fenetre, textvariable = time_text, command = self.time)
        self.farm_button.place(x=300,y=290)

        self.fenprinc.create_text(30,350, text= 'Farm')
        self.farm_button = tk.Button(fenetre, text = 'Click to farm', command = self.farm)
        self.farm_button.place(x=300,y=340)


    def time(*args):
        global time, recolte, prixtime
        if(recolte >= prixtime):
            recolte -= prixtime
            prixtime *= 5
            time *= 0.80
            time = int(time)
            time_text.set('Click to reduce time interval by 20% : {} points'.format(int(prixtime)))

    def farm(*args):
        global recolte
        global glb_text
        global lvl_pack1, lvl_pack2, lvl_pack3, lvl_pack4
        recolte += lvl_pack1*1 + lvl_pack2*2 + lvl_pack3*5 + lvl_pack4*10
        glb_text.set('{} points'.format(int(recolte)))

    def pack1(*args):
        global prix1, lvl_pack1, btn_text1, recolte
        if(recolte >= prix1):
            recolte -= prix1
            lvl_pack1 += 1
            prix1 *= 1.2
            btn_text1.set('Increase pack 1 power : {} points'.format(int(prix1)))

    def pack2(*args):
        global prix2, lvl_pack2, recolte
        if(recolte >= prix2):
            recolte -= prix2
            lvl_pack2 += 1
            prix2 *= 1.4
            btn_text2.set('Increase pack 2 power : {} points'.format(int(prix2)))
    
    def pack3(*args):
        global prix3, lvl_pack3, recolte
        if(recolte >= prix3):
            recolte -= prix3
            lvl_pack3 += 1
            prix3 *= 1.8
            btn_text3.set('Increase pack 3 power : {} points'.format(int(prix3)))
    
    def pack4(*args):
        global prix4, lvl_pack4, recolte
        if(recolte >= prix4):
            recolte -= prix4
            lvl_pack4 += 1 
            prix4 *= 2
            btn_text4.set('Increase pack 4 power : {} points'.format(int(prix4)))

# init variables

recolte = 10
lvl_pack1 = 1
lvl_pack2 = 0
lvl_pack3 = 0
lvl_pack4 = 0
prix1 = 200
prix2 = 1000
prix3 = 5000
prix4 = 10000
prixtime = 1000
time = 1000

def idle_task():
    global recolte
    global glb_text
    global time
    global lvl_pack1, lvl_pack2, lvl_pack3, lvl_pack4
    recolte += lvl_pack1*1 + lvl_pack2*20 + lvl_pack3*50 + lvl_pack4*100
    print(recolte)
    glb_text.set('{} points'.format(int(recolte)))
    app.after(time, idle_task)

fenetre = tk.Tk()
# text varaibles
glb_text = tk.StringVar()
time_text = tk.StringVar()
btn_text1 = tk.StringVar()
btn_text2 = tk.StringVar()
btn_text3 = tk.StringVar()
btn_text4 = tk.StringVar()
glb_text.set('{} points'.format(recolte))
time_text.set('Click to reduce time interval by 5% : {} points'.format(int(prixtime)))
btn_text1.set('Increase pack 1 power : {} points'.format(prix1))
btn_text2.set('Increase pack 2 power : {} points'.format(prix2))
btn_text3.set('Increase pack 3 power : {} points'.format(prix3))
btn_text4.set('Increase pack 4 power : {} points'.format(prix4))
# ######
app = App(master = fenetre)
app.after(time, idle_task)
app.mainloop()


# if __name__ == "__main__" : 

