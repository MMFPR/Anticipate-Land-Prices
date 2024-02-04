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

    def future_price_meter(self,future):
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


print(" Welcome to the land price calculator program ")
while True:
    try:
        district = input("Enter the district name : ").lower()
        if district.isalpha() == True:
            break
        else:
            print("الرجاء ادخال اسم صحيح")
    except Exception:
        print("لقد تم ادخال قيمة خاطئة الرجاء ادخال قيمة صحيحة")

while True:
    try:
        area = float(input("Enter the land area : "))
        streets = int(input("Enter the number of streets : "))
        break
    except Exception:
        print("لقد تم ادخال قيمة خاطئة الرجاء ادخال قيمة صحيحة")

my_lands = lands(district,area,streets)
my_lands_price = my_lands.price_land()
print("Current price per meter : ",format(my_lands.price_meter(),".3f"),"SAR")

try:
    print("The price of the land is : ", format(my_lands_price, ".3f"), "SAR")
except Exception:
    print("ادخال خاطئ")

while True:
    try:
        future_price = int(input("The expected price per meter after how many years in the future : "))
        if future_price >= 0:
            break
    except Exception:
        print("الرجاء ادخال عدد صحيح")

print("The expected future price per meter :",format(my_lands.future_price_meter(future_price),".3f"),"SAR")