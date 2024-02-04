from tkinter import *
from tkinter import messagebox
from tkinter import ttk

my_quarter1 = ["alsuli","hatayn" ,"alyasamin" ,"almaghrizat","alfalah","aleulya",
               "alkhuzamaa","almasif","almilqa","alquds","alnahda","alsahafa",
               "king abdullah","alrafiea","alnakhil","alrayaan","iishbilia","almaedhir",
               "alsulaymania","alsalam","alwadi","almunisia","alfayha","alnazim",
               "alhazm","manfuha","almansura","aleawali","alqadisia","king faisal",
               "aljaradia","king fahd","alrawda","alnasim algharbiu","alnuzha","qurtuba",
               "alearayja","almarwa","alnadaa", "alwurud","alaizdihar","alrabwa",
               "alkhalij","alnafl","alkhalidia","almilz","alrabie","almanar",
               "albayan","alyarmuk","zahrat albadiea","aleaqiq","alhamra","alsiwidiu algharbii",
               "alsiwidiu","almuhamadia","eakaz","manfuhat aljadida","alrawabi","alsaeada",
               "alrimal","alghanamia","badr", "zahrat laban","albariya","ahad",
               "aleazizia","alrahmania","alshafa", "alhayir","ghabira","laban",
               "sultana","tawiq","almahdia", "alnadwa","albadiea","aleud","almursalat"]

class lands:
    global quarter
    quarter = {"alsuli" : 1818,"hatayn" : 4849,"alyasamin" : 4674,
               "almaghrizat": 3617,"alfalah":3724,"aleulya":2982,
               "alkhuzamaa":4656,"almasif":2552,"almilqa":4916,
               "alquds":2964,"alnahda":2154,"alsahafa":3754,
               "king abdullah":3330,"alrafiea":2227,"alnakhil":4570,
               "alrayaan":2935,"iishbilia":2923,"almaedhir":3577,
               "alsulaymania":3307,"alsalam":2487,"alwadi":3879,
               "almunisia":3037,"alfayha":2903,"alnazim":1454,
               "alhazm":1960,"manfuha":1871,"almansura":1873,
               "aleawali":4111,"alqadisia":2588,"king faisal":2265,
               "aljaradia":2840,"king fahd":2631,"alrawda":2312,
               "alnasim algharbiu":1688,"alnuzha":3367,"qurtuba":3370,
               "alearayja":1740,"almarwa":1872,"alnadaa":3974,
               "alwurud":3232,"alaizdihar":3375,"alrabwa":2717,
               "alkhalij":2464,"alnafl":3219,"alkhalidia":1228,
               "almilz":1799,"alrabie":4293,"almanar":2346,
               "albayan":2012,"alyarmuk":3026,"zahrat albadiea": 1596,
               "aleaqiq":3315,"alhamra":2998,"alsiwidiu algharbii":1789,
               "alsiwidiu":1726,"almuhamadia":3641,"eakaz":1309,
               "manfuhat aljadida":1624,"alrawabi":2772,"alsaeada":3002,
               "alrimal":1969,"alghanamia":275,"badr":1303,
               "zahrat laban":2535,"albariya":349,"ahad":1561,
               "aleazizia":1931,"alrahmania":3564,"alshafa":1303,
               "alhayir":291,"ghabira":1397,"laban":2244,
               "sultana":1192,"tawiq":2455,"almahdia":2002,
               "alnadwa":1929,"albadiea":1262,"aleud":1085,
               "almursalat":2893
               }
    def __init__(self,district,area,streets):
        self.district = district
        self.area = area
        self.streets = streets

    def price_land(self):
        try:
            price = quarter[self.district] * self.area
        except Exception:
            print("تم اختيار حي غير متاح في البرنامج")
            return "تم اختيار حي غير متاح في البرنامج"
        if self.streets>3:
            price *= 1.5
        elif self.streets>2:
            price *= 1.3
        elif self.streets>1:
            price *= 1.2
        return price

    def price_meter(self):
        price = quarter[self.district]
        return price

    def future_price_meter(self):
        future = int(com3.get())
        self.future = future
        quarter1 = {"alsuli": (1818*0.284)+1818,"hatayn": (4849*0.282)+4849,
                   "alyasamin": (4674*0.274)+4674,"almaghrizat": (3617*0.265)+3617,
                   "alfalah": (3724*0.258)+3724,"aleulya": (2982*0.244)+2982,
                   "alkhuzamaa": (4656*0.242)+4656,"almasif": (2552*0.239)+2552,
                   "almilqa": (4916*0.238)+4916,"alquds": (2964*0.231)+2964,
                   "alnahda": (2154*0.231)+2154,"alsahafa": (3754*0.224)+3754,
                   "king abdullah": (3330*0.223)+3330,"alrafiea": (2227*0.222)+2227,
                   "alnakhil": (4570*0.213)+4570,"alrayaan": (2935*0.212)+2935,
                   "iishbilia": (2923*0.205)+2923,"almaedhir": (3577*0.198)+3577,
                   "alsulaymania": (3307*0.190)+3307,"alsalam": (2487*0.187)+2487,
                   "alwadi": (3879*0.173)+3879,"almunisia": (3037*0.172)+3037,
                   "alfayha": (2903*0.16)+2903,"alnazim": (1454*0.16)+1454,
                   "alhazm": (1960*0.154)+1960,"manfuha": (1871*0.154)+1871,
                   "almansura": (1873*0.15)+1873,"aleawali": (4111*0.137)+4111,
                   "alqadisia": (2588*0.136)+2588,"king faisal": (2265*0.13)+2265,
                   "aljaradia": (2840*0.129)+2840,"king fahd": (2631*0.127)+2631,
                   "alrawda": (2312*0.123)+2312,"alnasim algharbiu": (1688*0.119)+1688,
                   "alnuzha": (3367*0.118)+3367,"qurtuba": (3370*0.117)+3370,
                   "alearayja": (1740*0.116)+1740,"almarwa": (1872*0.11)+1872,
                   "alnadaa": (3974*0.104)+3974,"alwurud": (3232*0.103)+3232,
                   "alaizdihar": (3375*0.103)+3375,"alrabwa": (2717*0.93)+2717,
                   "alkhalij": (2464*0.87)+2464,"alnafl": (3219*0.86)+3219,
                   "alkhalidia": (1228*0.76)+1228,"almilz": (1799*0.7)+1799,
                   "alrabie": (4293*0.63)+4293,"almanar": (2346*0.57)+2346,
                   "albayan": (2012*0.53)+2012,"alyarmuk": (3026*0.43)+3026,
                   "zahrat albadiea": (1596*0.4)+1596,"aleaqiq": (3315*0.24)+3315,
                   "alhamra": (2998*0.5)+2998,"alsiwidiu algharbii": (1789*0.4)+1789,
                   "alsiwidiu": (1726*0.3)+1726,"almuhamadia": 3641-(3641*0.018),
                   "eakaz": 1309-(1309*0.019),"manfuhat aljadida": 1624-(1624*0.021),
                   "alrawabi": 2772-(2772*0.029),"alsaeada": 3002-(3002*0.036),
                   "alrimal": 1969-(1969*0.052),"alghanamia": 275-(275*0.065),
                   "badr": 1303-(1303*0.071),"zahrat laban": 2535-(2535*0.071),
                   "albariya": 349-(349*0.077),"ahad": 1561-(1561*0.092),
                   "aleazizia": 1931-(1931*0.128),"alrahmania": 3564-(3564*0.134),
                   "alshafa": 1303-(1303*0.136),"alhayir": 291-(291*0.152),
                   "ghabira": 1397-(1397*0.157),"laban": 2244-(2244*0.168),
                   "sultana": 1192-(1192*0.169),"tawiq": 2455-(2455*0.176),
                   "almahdia": 2002-(2002*0.194),"alnadwa": 1929-(1929*0.242),
                   "albadiea": 1262-(1262*0.243),"aleud": 1085-(1085*0.286),
                   "almursalat": (2893*0.145)+2893
                   }
        future_price = quarter1[self.district]
        future_price *= self.future
        return future_price

def predict():
    district = str(com1.get())
    area = float(en2.get())
    streets = int(com2.get())
    my_lands = lands(district, area, streets)
    my_lands_price = my_lands.price_land()
    my_lands.price_meter()
    messagebox.showinfo("السعر المتوقع",f"\nThe price of the land is {my_lands_price:,.2f} SAR for land located in a neighborhood {district}\n"
                                         f"\nCurrent price per meter {my_lands.price_meter():,.2f} SAR\n"
                                        f"\nThe expected future price per meter {my_lands.future_price_meter():,.2f} SAR\n")

def predict1():
    district = str(com1.get())
    area = float(en2.get())
    streets = int(com2.get())
    my_lands = lands(district, area, streets)
    my_lands.price_meter()
    messagebox.showinfo("السعر المستقبلي المتوقع للمتر",f"\nThe expected future price per meter {my_lands.future_price_meter():,.2f} SAR\n")


window1 = Tk()
window1.title("توقع اسعار الاراضي")
photo = PhotoImage(file="img/11.png")
labg = Label(window1,image=photo)
labg.place(x=0,y=0,relwidth=1,relheight=1)
la = Label(window1,text=" Welcome to the land price calculator program ",width=69)
la.grid(padx=10, pady=5)
frame = Frame(window1)
frame.grid(padx=10, pady=5)
info = LabelFrame(frame,text="Land Information",pady=20,padx=45)
info.grid(row= 0,column=0)


la1 = Label(info,text="Enter the district name : \n")
la1.grid(row=0, column=0, padx=10, pady=5)
com1 = ttk.Combobox(info,values=(my_quarter1),state="readonly")
com1.grid(row=0, column=1, padx=10, pady=5)

la2 =Label(info,text="Enter the land area : \n")
la2.grid(row=1, column=0, padx=10, pady=5)
en2=Entry(info,width=23)
en2.grid(row=1, column=1, padx=10, pady=5)

la3 = Label(info,text="Enter the number of streets : \n")
la3.grid(row=3, column=0, padx=10, pady=5)
com2 =  ttk.Combobox(info,values=("1","2","3","4"),state="readonly")
com2.grid(row=3, column=1, padx=10, pady=5)

la4 = Label(info,text="Choose how many years the expected \nprice per meter will be in the future : ")
la4.grid(row=4, column=0, padx=10, pady=5)
com3 =  ttk.Combobox(info,values=("1","2","3","4","5"),state="readonly")
com3.grid(row=4, column=1, padx=10, pady=5)

bu1 = Button(info,text="حساب السعر", command=predict)
bu1.grid(row=5, column=1, padx=10, pady=5)

bu2 = Button(info,text="سعر المتر المتوقع", command=predict1)
bu2.grid(row=5, column=0, padx=10, pady=5)

window1.mainloop()