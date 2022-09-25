#petalwidth <= 0.6: Iris-setosa (50.0)
#petalwidth > 0.6
#|   petalwidth <= 1.7
#|   |   petallength <= 4.9: Iris-versicolor (48.0/1.0)
#|   |   petallength > 4.9
#|   |   |   petalwidth <= 1.5: Iris-virginica (3.0)
#|   |   |   petalwidth > 1.5: Iris-versicolor (3.0/1.0)
#|   petalwidth > 1.7: Iris-virginica (46.0/1.0)

petal_width     = float( input("Nhập vào giá trị petal_width (cm): "))
petal_length    = float( input("Nhập vào giá trị petal_length (cm): "))
sepal_width     = float( input("Nhập vào giá trị của sepal_width (cm): "))
sepal_length    = float( input("Nhập vào giá trị của sepal_length (cm):"))

str_output = "Không xác định"

if petal_width <= 0.6:
    str_output = "Iris-setosa"
else: #petalwidth > 0.6
    if petal_width <= 1.7:
        if petal_length <= 4.9:
            str_output = "Iris-versicolor"
        else: #petallength > 4.9
            if petal_width <= 1.5:
                str_output = "Iris-virginica"
            else: #petalwidth > 1.5
                str_output = "Iris-versicolor"
    else:
        str_output = "Iris-virginica"

print("Result: " + str_output)
print("--DONE--")

#Exec 1
# Nhập vào giá trị petal_width (cm): 0.7
# Nhập vào giá trị petal_length (cm): 0.7
# Nhập vào giá trị của sepal_width (cm): 0.7
# Nhập vào giá trị của sepal_length (cm):0.7
# Result: Iris-versicolor
# --DONE--

#Exec 2
# Nhập vào giá trị petal_width (cm): 0.3
# Nhập vào giá trị petal_length (cm): 0.6
# Nhập vào giá trị của sepal_width (cm): 0.3
# Nhập vào giá trị của sepal_length (cm):0.2
# Result: Iris-setosa
# --DONE--