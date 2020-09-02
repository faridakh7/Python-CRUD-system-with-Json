from delete import *
from addnewdatas import *
from read import *
from update import *
from showalldata import *


def start():
    xususiEmr = input("""
    Aşağıdakı Əmrlərdən Birini Secin:

    1.Databasedəki məlumatların göstərilməsi
    2.Databasedəki məlumatların Qiymətə və Ada gore əldə olunması
    3.Databaseye yeni məlumat əlavə edilməsi
    4.Databasedəki məlumatlara ID görə dəyişikliklərin edilməsi
    5.Databasedən ID görə məlumatların silinməsi
    6.Programı dayandırmaq
    
Seciminizi Daxil edin:  """).strip()
    if xususiEmr.isnumeric() and 0 < int(xususiEmr) < 7:
        option = int(xususiEmr)

        if option == 1:
            showAllData()
            start()
        if option == 2:
            choice = int(input("""
            1. Qiymətə gore filter edilməsi
            2. Ada görə axtarış edilməsi
            
            SECIMINIZI DAXIL EDIN : """))
            if choice == 1:
                getProductbyPrice()
                start()
            if choice == 2:
                getProductbyName()
                start()
        if option == 3:
            addNewData()
            start()
        if option == 4:
            updateDataFromId()
            start()
        if option == 5:
            delProductbyName()
            start()

        if option == 6:
            def programbitdi():
                print("Program muveffeqiyyətlə dayandırıldı")
                return

            programbitdi()
    else:
        print("Yalnız 1-6 arası bir seçim edə bilərsiniz!")
        start()


start()
