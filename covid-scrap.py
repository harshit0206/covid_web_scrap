import requests
url = "https://api.covid19india.org/states_daily.json"
req = requests.get(url).json()
loc = input("Enter location : ")
mon = input("Enter month (mm) : ")
year = input("Enter year (yyyy) : ")
my = year + "-" + mon
count_c = 0
count_r = 0
count_d = 0
for data in req['states_daily'] :
    if ( mon == "01" or mon == "03" or mon == "05" or mon == "07" or mon == "08" or mon == "10" or mon == "12" ) :
       for i in range(1,32) :
           if i < 10:
               j = str(i)
               date = my + "-" + "0" + j
           if i > 9 :
               j = str(i)
               date = my + "-" + j
           if data["dateymd"] == date :
               if data["status"] == "Confirmed" :
                   count_c += int(data[loc])
               if data["status"] == "Recovered" :
                   count_r += int(data[loc])
               if data["status"] == "Deceased" :
                   count_d += int(data[loc])
    if ( mon == "04" or mon == "06" or mon == "09" or mon == "11" ) :
       for i in range(1,31) :
           if i < 10:
               j = str(i)
               date = my + "-" + "0" + j
           if i > 9 :
               j = str(i)
               date = my + "-" + j
           if data["dateymd"] == date :
               if data["status"] == "Confirmed" :
                   count_c += int(data[loc])
               if data["status"] == "Recovered" :
                   count_r += int(data[loc])
               if data["status"] == "Deceased" :
                   count_d += int(data[loc])
    if mon == ( "02" ) :
       for i in range(1,29) :
           if i < 10:
               j = str(i)
               date = my + "-" + "0" + j
           if i > 9 :
               j = str(i)
               date = my + "-" + j
           if data["dateymd"] == date :
               if data["status"] == "Confirmed" :
                   count_c += int(data[loc])
               if data["status"] == "Recovered" :
                   count_r += int(data[loc])
               if data["status"] == "Deceased" :
                   count_d += int(data[loc])
print("Confirmed :",count_c)
print("Recovered :",count_r)
print("Deceased  :",count_d)
