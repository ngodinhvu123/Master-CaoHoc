# Tìm được nhờ weka
#outlook = sunny
#|   humidity = high: no (3.0)
#|   humidity = normal: yes (2.0)
#outlook = overcast: yes (4.0)
#outlook = rainy
#|   windy = TRUE: no (2.0)
#|   windy = FALSE: yes (3.0)
outlook = input("Nhập vào giá trị của outlook (sunny, rainy, overcast):")
humidity = input("Nhập vào giá trị của humidity (high, normal): ")
temperature = input("Nhập vào giá trị temperature (hot, coll, mild): ")
windy = input("Nhập vào giá trị windy (TRUE, FALSE): ")

loikhuyen = "Không quyết định được"

if outlook == "sunny":
    if humidity == "high":
        loikhuyen= ("Không nên di")
    if humidity == "normal":
        loikhuyen = ("Có thể đi chơi")
if outlook == "overcast":
    loikhuyen = ("đi chơi")
if outlook == "rainy":
    if windy == "TRUE":
        loikhuyen = ("go")
    if humidity == "YES":
        loikhuyen = ("Stop")

print(loikhuyen)
print("--DONE--")