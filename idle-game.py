import tkinter as tk

# to do 
# - prestige mode with a multiplier
# - add textures + desgin 

class App(tk.Frame) :
    # init functions
    prestigeMultiplier = 1
    def __init__(self, master =None):
        super().__init__(master)        ## permit access to tk.Frame functions
        self.master.title("Idle Game")
        self.var_init()
        self.pack()
        self.create_widgets()

    def var_init(self):
        self.points = 10
        self.prestigeBtnSet = False
        self.packAmt = 4
        self.priceTime = 1000
        self.timeIdle = 1000
        self.globalText = tk.StringVar()
        self.globalText.set('10 points (1.0 points/s)')
        self.timeText = tk.StringVar()
        self.timeText.set('Click to reduce time interval by 5% : {} points'.format(int(self.priceTime)))
        self.packOptions = [
            # lvl, price, increase, btn text, multipier, lvl label
            [1, 200, 1.2, tk.StringVar(), 1, tk.StringVar()],
            [0, 1000, 1.4, tk.StringVar(), 20, tk.StringVar()],
            [0, 5000, 1.8, tk.StringVar(), 200, tk.StringVar()],
            [0, 10000, 2, tk.StringVar(), 1000, tk.StringVar()]
        ]

    #window functions
    def create_widgets(self):
        self.fenprinc = tk.Canvas(self,width = '600', height = '900')
        self.fenprinc.pack()

        tk.Label(self.fenprinc, textvariable = self.globalText).place(x=200,y=30)

        tk.Button(self.fenprinc, text = 'Click to farm', command = self.farm).place(x=250,y=90)

        tk.Button(self.fenprinc, textvariable = self.timeText, command = self.time).place(x=150,y=140)

        for i in range(len(self.packOptions)):
            tk.Label(self.fenprinc, textvariable = self.packOptions[i][5]).place(x=30,y=250 + 50*i)
            self.packOptions[i][5].set('Pack {} : level {}'.format(i+1, self.packOptions[i][0]))            
            self.packOptions[i][3].set('Increase pack {} power : {:.2E} points'.format(i+1, int(self.packOptions[i][1])))            
            tk.Button(self.fenprinc, textvariable = self.packOptions[i][3], command = lambda j=i : self.pack_upgrade(j)).place(x=300,y=240 + 50*i)



    def add_widgets(self, i):
        if(i < 10):
            tk.Label(self.fenprinc, textvariable = self.packOptions[i][5]).place(x = 30, y=250 + 50*i)
            self.packOptions[i][5].set('Pack {} : level {}'.format(i+1, self.packOptions[i][0]))            
            self.packOptions[i][3].set('Increase pack {} power : {:.2E} points'.format(i+1, int(self.packOptions[i][1])))            
            tk.Button(self.fenprinc, textvariable = self.packOptions[i][3], command = lambda j=i : self.pack_upgrade(j)).place(x=300,y=240 + 50*i)
        else:
            self.prestigeBtnSet = True
            tk.Button(self.fenprinc, text = 'Go to prestige (reset all but x{} on all packs)'.format(self.prestigeMultiplier*10), command = self.prestige_mode).place(x=160,y=190)



    # actions functions
    def time(self, *args):
        if(self.points >= self.priceTime):
            self.points -= self.priceTime
            self.priceTime *= 5
            self.timeIdle = int(self.timeIdle*0.95)
            self.timeText.set('Click to reduce time interval by 5% : {:.2E} points'.format(int(self.priceTime)))



    def prestige_mode(self):
        self.var_init()
        self.fenprinc.destroy()
        self.pack()
        self.prestigeMultiplier *= 10
        self.create_widgets()



    def farm(self, *args):
        delta = 0
        for i in range(len(self.packOptions)):
            delta += self.packOptions[i][0]*self.packOptions[i][4]*self.prestigeMultiplier
        self.points+=delta
        self.globalText.set('{:.2E} points ({:.2E} points/s)'.format(int(self.points), round((delta)*(1000/self.timeIdle), 2)))



    def pack_upgrade(self, args):
        if(self.points >= self.packOptions[args][1] and self.packOptions[args][0] < 32):
            self.points -= self.packOptions[args][1]
            self.packOptions[args][0] += 1
            self.packOptions[args][1] *= self.packOptions[args][2] 
            self.packOptions[args][3].set('Increase pack {} power : {:.2E} points'.format(args+1, int(self.packOptions[args][1])))
            self.packOptions[args][5].set('Pack {} : level {}'.format(args+1, self.packOptions[args][0] if self.packOptions[args][0]<32 else "MAX"))



    def check_max_lvl(self):
        all_32 = True
        if(self.packAmt < 10):
            for i in range(len(self.packOptions)):
                if(self.packOptions[i][0] != 32):
                    all_32 = False
            if(all_32):
                listToAppend = [0, (10**(2*self.packAmt)), (self.packAmt+1)/2,  tk.StringVar(), 10**self.packAmt, tk.StringVar()]
                self.packOptions.append(listToAppend)
                self.add_widgets(self.packAmt)
                self.packAmt += 1
        else:
            for i in range(len(self.packOptions)):
                if(self.packOptions[i][0] != 32):
                    all_32 = False
            if(all_32 and self.prestigeBtnSet == False):
                self.add_widgets(10)



    def idle_task(self):
        delta = 0
        for i in range(len(self.packOptions)):
            delta += self.packOptions[i][0]*self.packOptions[i][4]*self.prestigeMultiplier
        self.points+=delta
        print(self.points)
        self.globalText.set('{:.2E} points ({:.2E} points/s)'.format(int(self.points), round(delta*(1000/self.timeIdle), 2)))
        self.check_max_lvl()
        self.after(self.timeIdle, self.idle_task)




if __name__ == "__main__" : 
    # init tk 
    fenetre = tk.Tk()
#init app
    app = App(master = fenetre)
#main loop
    app.after(app.timeIdle, app.idle_task)
    app.mainloop()


