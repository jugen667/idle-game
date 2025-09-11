import tkinter as tk

# to do 
# - prestige mode with a multiplier
# - display pack level + max out pack
# - dynamic packs
# - add textures

class App(tk.Frame) :
    def __init__(self, master =None):
        super().__init__(master)        ## permit access to tk.Frame functions
        self.master.title("Idle Game")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        global pack_options
        global glb_text
        global time_text, prixtime
        self.fenprinc = tk.Canvas(self,width = '1280', height = '720', bg = 'white')
        self.fenprinc.pack()

        self.recolte_label = tk.Label(self.master, textvariable = glb_text)
        glb_text.set('10 points (1.0 points/s)')
        self.recolte_label.place(x=270,y=30)

        self.fenprinc.create_text(30,100, text= 'Time')
        time_text.set('Click to reduce time interval by 20% : {} points'.format(int(prixtime)))
        tk.Button(self.master, textvariable = time_text, command = self.time).place(x=300,y=90)

        self.fenprinc.create_text(30,150, text= 'Farm')
        tk.Button(self.master, text = 'Click to farm', command = self.farm).place(x=300,y=140)

        for i in range(len(pack_options)):
            self.fenprinc.create_text(30,200+50*i, text = 'Pack {}'.format(i+1))
            pack_options[i][3].set('Increase pack {} power : {} points'.format(i+1, int(pack_options[i][1])))            
            tk.Button(self.master, textvariable = pack_options[i][3], command = lambda j=i : pack(j)).place(x=300,y=190 + 50*i)

    def time(*args):
        global time, recolte, prixtime
        if(recolte >= prixtime):
            recolte -= prixtime
            prixtime *= 5
            time *= 0.80
            time = int(time)
            time_text.set('Click to reduce time interval by 20% : {} points'.format(int(prixtime)))

    def farm(*args):
        global recolte, time
        global glb_text
        global pack_options
        delta = 0
        for i in range(len(pack_options)):
            delta += pack_options[i][0]*pack_options[i][4]
        recolte+=delta
        glb_text.set('{} points ({} points/s)'.format(int(recolte), round((delta)*(1000/time), 2)))


# init variables
def pack(args):
    print('pack {}'.format(args))
    global recolte
    global pack_options
    if(recolte >= pack_options[args][1]):
        recolte -= pack_options[args][1]
        pack_options[args][0] += 1
        pack_options[args][1] *= pack_options[args][2] 
        pack_options[args][3].set('Increase pack {} power : {} points'.format(args+1, int(pack_options[args][1])))


def idle_task():
    global recolte
    global glb_text
    global time
    global pack_options
    delta = 0
    for i in range(len(pack_options)):
        delta += pack_options[i][0]*pack_options[i][4]
    recolte+=delta
    print(recolte)
    glb_text.set('{} points ({} points/s)'.format(int(recolte), round(delta*(1000/time), 2)))
    app.after(time, idle_task)




if __name__ == "__main__" : 
#init var
    recolte = 10
    cur_pack_amt = 4
    prixtime = 1000
    time = 1000
# init tk 
    fenetre = tk.Tk()
    pack_options = [
        # lvl, price, increase, text, multipier
        [1, 200, 1.2, tk.StringVar(), 1],
        [0, 1000, 1.4, tk.StringVar(), 20],
        [0, 5000, 1.8, tk.StringVar(), 50],
        [0, 10000, 2, tk.StringVar(), 100]
    ]
    # text varaibles
    glb_text = tk.StringVar()
    time_text = tk.StringVar()
#init app
    app = App(master = fenetre)
#main loop
    app.after(time, idle_task)
    app.mainloop()


