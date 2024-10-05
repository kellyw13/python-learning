# Skriv en inledande kommentar som talar om vad programmet gör. 



# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt


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

def nordTabell(listan, armedel=None):
    #list_data = listan[2:]
    nordic_countries = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]
    medel_ar = [2018, 2015, 2012, 2009, 2006, 2003]
    if armedel == None:
        armedel = arsmedel(listan)
    #list to store data for nordic countries
    nordic_data = []
    for i in listan:
        if i[0] in nordic_countries:
            nordic_data.append(i[0:1] + i[13:19])
    print(f"{'Kunskapsutveckling i matematik enligt PISA-undersökningen 2003 – 2018.':^100}")
    print(f"{'-------------------------------------------------------------------------------------------------------------------':^100}")
    print(f"{'Länder:':^100}")
    print(f"{'År':<10} {nordic_countries[0]:<15} {nordic_countries[1]:<15} {nordic_countries[2]:<15} {nordic_countries[3]:<15} {nordic_countries[4]:<15} {'Medelvärde alla länder':15}")
    print(f"{'-------------------------------------------------------------------------------------------------------------------':^100}")
    for i in range(6):
        print(f"{medel_ar[i]:<10} {nordic_data[0][i+1]:<15} {nordic_data[1][i+1]:<15} {nordic_data[2][i+1]:<15} {nordic_data[3][i+1]:<15} {nordic_data[4][i+1]:<15} {armedel[i]:^15}")

def nordGraf(listan, armedel):
    nordic_countries = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]
    medel_ar = [2018, 2015, 2012, 2009, 2006, 2003]
    armedel = ["Medel"] + armedel
    nordic_data = []
    for i in listan:
        if i[0] in nordic_countries:
            nordic_data.append(i[0:1] + i[13:19]) 
    nordGraf_data = nordic_data + [armedel]
    
    #use different colors for each country
    colors = ['b', 'g', 'r', 'c', 'm', 'y']

    #create a new plot figure
    plt.figure(figsize=(10,6))
    
    #plot the data for each country
    for i in range(len(nordGraf_data)):
        points = list(map(int, nordGraf_data[i][1:])) #converting the math scores to integers
        plt.plot(medel_ar, points[::-1], color=colors[i], label=nordGraf_data[i][0]) #plotting the data
    
    #Label the graph
    plt.xlabel("År")
    plt.ylabel("Poäng")
    plt.title("PISA:Kunskapsutvecklingen i matematik 2003-2018")
    
    plt.grid(True)
    plt.legend()
    
    #display the plot
    plt.show()


# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
def battreSamre(data,forbattring):
    if forbattring:
        print("Länder med förbättrade resultat")
    else:
        print("Länder med försämrade resultat")
    
    for land in data [:5]:
        print(land)

exempel_data = [" Land 1", "Land 2", "Land 3", "Land 4", "Land 5"] 

battreSamre (exempel_data, True)
battreSamre (exempel_data, False)




def battreSamre (data, forbattring):
    if forbattring:
        print("Länder med förbättrade resultat:")
    else:
        print("Länder med försämrade resultat:")
        
    for i in range(5):
        print(f"Land{i+1}")
        
    pisadata = [exempel_data]
    
def visaMeny ():
    print("4. Kontirnuerligt förbättrat resp. försämrat år 2003-2018")
    val  = input(" för att köra, skriv '4': ")
        
    if val == '4':
        battreSamre (pisadata,True)
        battreSamre (pisadata, False)
    else:
        print("Felaktigt val avslutar programmet.")
    
    if __name__ == "__main__":
        visaMeny()




# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
def kvinna_man(data):
    print("År och länder när kvinnorna presterar bättre än männen under åren 2003–2018.")
    print("År\tLand\tKvinnor\tMän")
    print("--------------------------------------------------------")
    
    previous_year = ""
    for row in data[1:]:  # Hoppa över rubrikraden
        for i in range(1, len(data[0])-1, 3):  # Hoppar över varje tredje kolumn för att matcha årsdata
            year = data[0][i][:-1]  # Ta bort könstecknet för att få fram året
            country = row[0]
            man_score = int(row[i])
            woman_score = int(row[i+1])
            if woman_score > man_score:
                if year != previous_year:
                    print(f"\n{year}", end='\t')
                    previous_year = year
                else:
                    print("\t", end='')
                print(f"{country}\t{woman_score}\t{man_score}")





# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.

#Huvudmeny
def visa_huvudmeny():
    while True:
        print("\nVälkommen till PISA-dataanalysprogrammet!")
        print("1. Läs in csv-filen.")
        print("2. Visa bästa och sämsta resultatet för 2018.")
        print("3. Analysera matematikkunskaper i Norden 2003–2018.")
        print("4. Visa länder med kontinuerlig förbättring/försämring 2003–2018.")
        print("5. Visa när kvinnor presterat bättre än män 2003–2018.")
        print("6. Avsluta programmet.")
        
        val = input("Välj ett alternativ (1-6): ")
        
        if val == "1":
            print("Funktionen för att läsa in csv-filen anropas här.")
            read_file()
            
        elif val == "2":
            print("Funktionen för att visa bästa och sämsta resultatet för 2018 anropas här.")
            data = read_file()
            index = int(input("enter sorting index"))
            sort_best_and_worst(data, index) 
            
        elif val == "3":
            print("Funktionen för att analysera matematikkunskaper i Norden 2003–2018 anropas här.")
            data = read_file()
            index = int(input("enter sorting index"))
            medel = arsmedel(data)
            nordTabell(data)
            nordGraf(data, medel)
            
        elif val == "4":
            print("Funktionen för att visa länder med kontinuerlig förbättring/försämring 2003–2018 anropas här.")
            data = read_file()
            battreSamre(data, True)
            
        elif val == "5":
            print("Funktionen för att visa när kvinnor presterat bättre än män 2003–2018 anropas här.")
            data = read_file()
            kvinna_man(data)
            
        elif val == "6":
            print("Programmet är avslutat.")
            break
        else:
            print("Ogiltigt val, försök igen.")

visa_huvudmeny()
