# Skriv en inledande kommentar som talar om vad programmet gör. 



# Placera dina modulimpoter här:
import csv


# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
def read_file():
    filename = str(input("Ange filnamn eller tryck bara Enter för pisadata.csv : "))
    if filename == '': #använd defaultvärden ifall användaren trycker enter
        filename = "pisadata.csv" 
    pisadata= []

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            pisadata.append(row)
    return pisadata

#print(read_file())

# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
def sort_best_and_worst(pisadata, data_index):
    year_header = pisadata[0]
    average_header = pisadata[1]
    data = pisadata[2:]
    
    #iterate over pisadata and retrieve name and average 2018
    pisadata_sorterad = sorted(data, key=lambda row:row[data_index])

    
    #kopiera top 10
    print("De tio länder som hade bäst resultat år 2018")
    print("---------------------------------------------")
    print(f"{'Land':<20}{'Resultat':<10}")
    print("---------------------------------------------")
    for i in range(-1, -11, -1):
        print(f"{pisadata_sorterad[i][0]:<20} {pisadata_sorterad[i][data_index]:^10} ")
    
    print("\n")
    
    #print bottom 10
    print("De tio länder som hade sämst resultat år 2018")
    print("---------------------------------------------")
    print(f"{'Land':<20}{'Resultat':<10}")
    print("---------------------------------------------")
    for i in range(0,10):
        print(f"{pisadata_sorterad[i][0]:<20} {pisadata_sorterad[i][data_index]:^10} ")
        
    pisadata_sorterad.insert(0, year_header)
    pisadata_sorterad.insert(1,average_header)

    return pisadata_sorterad

#testData = read_file()
#sort_best_and_worst(testData, 13)




# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
def kolumnmedel(listan,index):
    list_data = listan[2:]
    summation = 0
    num_of_items = len(list_data)
    for i in list_data:
        summation += int(i[index])
    medel = round(summation / num_of_items)
    return medel

def arsmedel(listan):
    list_data = listan[2:]
    medel_2018 = kolumnmedel(list_data,13)
    medel_2015 = kolumnmedel(list_data,14)
    medel_2012 = kolumnmedel(list_data,15)
    medel_2009 = kolumnmedel(list_data,16)
    medel_2006 = kolumnmedel(list_data,17)
    medel_2003 = kolumnmedel(list_data,18)
    armedel = [medel_2018, medel_2015, medel_2012, medel_2009, medel_2006, medel_2003]
    return armedel

#data = read_file()
#print(arsmedel(data))

def nordTabell(listan, armedel=None):
    #list_data = listan[2:]
    nordic_countries = ["Sweden", "Norway", "Denmark", "Finland", "Iceland"]
    #list to store data for nordic countries
    nordic_data = []
    for i in listan:
        if i[0] in nordic_countries:
            nordic_data.append(i)
    
    print(f"{'Kunskapsutveckling i matematik enligt PISA-undersökningen 2003 – 2018.':^100}")
    print(f"{'-------------------------------------------------------------------------------------------------------------------':^100}")
    print(f"{'Länder:':^100}")
    print(f"{'År':<10} {nordic_countries[0]:<15} {nordic_countries[1]:<15} {nordic_countries[2]:<15} {nordic_countries[3]:<15} {nordic_countries[4]:<15} {'Medelvärde alla länder':15}")
    print(f"{'-------------------------------------------------------------------------------------------------------------------':^100}")
    for i in nordic_data:
        print(f"{listan[0][13]:<10} {i[0]:<15}")

data = read_file()
nordTabell(data)

# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:


# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här: