from delete import *
from write import *
from read import *
from update import *


def start():
    xususiEmr = int(input("""
    Aşağıdakı Əmrlərdən Birini Secin:

    1.Databasedəki məlumatların əldə olunması
    2.Databaseye yeni məlumat əlavə edilməsi
    3.Database üzərində ID görə dəyişikliklərin edilməsi
    4.Databasedən ID görə məlumatların silinməsi
    
Seciminizi Daxil edin:  """))

    if xususiEmr == 1:
        choice = int(input("""
        1. Qiymete gore axtaris ucun
        2. Ada gore axtaris ucun
        
        SECIMINIZI DAXIL EDIN : """))
        if choice == 1:
            getProductbyPrice()
            start()
        if choice == 2:
            getProductbyName()
            start()
    if xususiEmr == 2:
        addNewData()
        start()
    if xususiEmr == 3:
        updateDataFromId()
        start()
    if xususiEmr == 4:
        delProductbyName()
        start()
    else:
        print("Yalnız 1-4 arası bir seçim edə bilərsiniz!")
        start()

start()