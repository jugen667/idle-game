import tkinter as tk
import time

class App(tk.Frame) :
    def __init__(self, master =None):
        super().__init__(master)        ## permit access to tk.Frame functions
        self.master.title("Window name")
        self.pack()
        self.create_widgets()
        lvl_pack1 = 1
        lvl_pack2 = 0
        lvl_pack3 = 0
        lvl_pack4 = 0

    def create_widgets(self):
        global prix1, prix2, prix3, prix4
        self.fenprinc = tk.Canvas(self,width = '600', height = '400', bg = 'white')
        self.fenprinc.pack()

        self.fenprinc.create_text(300,30, text = 'Selectionner un pack à ameliorer')
       
        self.fenprinc.create_text(30,100, text = 'Pack 1')

        self.pack1_button = tk.Button(fenetre, text ='Ameliorer le pack n°1 : {} points'.format(prix1), command = self.pack1)
        self.pack1_button.place(x=300,y=90)

        # self.fenprinc.create_text(30,150, text= 'Pack 2')
        
        # self.pack2_button = tk.Button(fenetre, text ='Ameliorer le pack n°2 : {} points'.format(prix2),  config = pack2)
        # self.pack2_button.place(x=300,y=140)
        
        # self.fenprinc.create_text(30,200, text= 'Pack 3')
        
        # self.pack3_button = tk.Button(fenetre, text ='Ameliorer le pack n°3 : {} points'.format(prix3),  config = pack3)
        # self.pack3_button.place(x=300,y=190)
        
        # self.fenprinc.create_text(30,250, text= 'Pack 4')
        
        # self.pack4_button = tk.Button(fenetre, text ='Ameliorer le pack n°4 : {} points'.format(prix4),  config = pack4)
        # self.pack4_button.place(x=300,y=240)



    def pack1(*args):
        lvl_pack1 += 1
        prix1 *= 2

    # def pack2():
    #     lvl_pack2 += 1
    #     prix2 *= 4
    
    # def pack3():
    #     lvl_pack3 += 1
    #     prix3 *= 8
    
    # def pack4():
    #     lvl_pack4 += 1 
    #     prix4 *= 16

recolte = 10
lvl_pack1 = 1
lvl_pack2 = 0
lvl_pack3 = 0
lvl_pack4 = 0


# recolte += lvl_pack1*1 + lvl_pack2*2 + lvl_pack3*5 + lvl_pack4*10
# print(recolte)
# time.sleep(1)


# recolte = 10

prix1 = 1
prix2 = 10
prix3 = 100
prix4 = 1000

print(recolte)
print(lvl_pack4)

fenetre = tk.Tk()
app = App(master = fenetre)
app.mainloop()


# while(True) :
#     recolte += lvl_pack1*1 + lvl_pack2*2 + lvl_pack3*5 + lvl_pack4*10
#     print(recolte)
#     time.sleep(1)

# if __name__ == "__main__" : 

