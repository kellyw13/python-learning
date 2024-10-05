 
#Programmet granskar och presenterar data från en PISA-undersökning om matematikkunskaper


# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt


# Deluppgift 1: Funktioner från deluppgift 1 i ordning.

def read_file():                         #En funktion som läser in innehållet från en CSV_fil
    filename = str(input("Ange filnamn eller tryck bara Enter för pisadata.csv : "))
    if filename == '':                   #Använd defaultvärden ifall användaren trycker enter
        filename = "pisadata.csv" 
    pisadata = []

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            pisadata.append(row)
    return pisadata

# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
def sort_best_and_worst(pisadata, data_index):
    year_header = pisadata[0]
    average_header = pisadata[1]
    data = pisadata[13:]
    
    #Sorterat baserat på medelvärdet år 2018
    pisadata_sorterad = sorted(pisadata, key=lambda row:row[data_index])

    
    #Print de 10 länder med bäst resultat
    print("De tio länder som hade bäst resultat år 2018")
    print("---------------------------------------------")
    print(f"{'Land':<20}{'Resultat':<10}")
    print("---------------------------------------------")
    for i in range(-2, -12, -1):
        print(f"{pisadata_sorterad[i][0]:<20} {pisadata_sorterad[i][data_index]:^15} ")
    
    print("\n")
    
    #Print de 10 länder med sämst resultat
    print("De tio länder som hade sämst resultat år 2018")
    print("---------------------------------------------")
    print(f"{'Land':<20}{'Resultat':^15}")
    print("---------------------------------------------")
    for i in range(1,11):
        print(f"{pisadata_sorterad[i][0]:<20} {pisadata_sorterad[i][data_index]:^15} ")
        
    #pisadata_sorterad.insert(0, year_header)
    #pisadata_sorterad.insert(1,average_header)

    return pisadata_sorterad

# Deluppgift 3: Funktioner från deluppgift 3 i ordning.

#Beräknar medelvärde för fastställda kolumner
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
    print()
    print(f"{'År':<10} {nordic_countries[0]:<15} {nordic_countries[1]:<15} {nordic_countries[2]:<15} {nordic_countries[3]:<15} {nordic_countries[4]:<15} {'Medelvärde alla länder':15}")
    print(f"{'-------------------------------------------------------------------------------------------------------------------':^100}")
    for i in range(6):
        print(f"{medel_ar[i]:<10} {nordic_data[0][i+1]:<15} {nordic_data[1][i+1]:<15} {nordic_data[2][i+1]:<15} {nordic_data[3][i+1]:<15} {nordic_data[4][i+1]:<15} {armedel[i]:^15}")

def nordGraf(listan, armedel):
    nordic_countries = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]
    medel_ar = [2018, 2015, 2012, 2009, 2006, 2003]  # Specific years to be displayed on the x-axis
    nordic_data = []
    for i in listan:
        if i[0] in nordic_countries:
            nordic_data.append(i[0:1] + i[13:19])
    # Note: 'armedel' already contains average scores, so no need to prepend "Medel"

    # Use different colors for each country + one for the average
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Added 'k' for black, representing the average

    # Create a new plot figure
    #fig = plt.figure(figsize=(10, 6))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    #set background color on plot
    ax.set_facecolor('cyan')

    # Plot the data for each Nordic country
    for i in range(len(nordic_data)):
        points = list(map(int, nordic_data[i][1:]))  # Converting the scores to integers
        plt.plot(medel_ar, points, color=colors[i], label=nordic_data[i][0])  # Plotting all data points

    # Plot the average scores separately
    average_points = list(map(int, armedel))  # Ensure this is correctly mapped to integers
    plt.plot(medel_ar, average_points, color='k', linestyle='--', label='Medel')  # Distinguished by color and linestyle

    # Explicitly set the x-axis ticks to the years in medel_ar
    plt.xticks(medel_ar)

    # Label the graph
    plt.xlabel("År")
    plt.ylabel("Poäng")
    plt.title("PISA: Kunskapsutvecklingen i matematik 2003-2018")

    plt.grid(True)
    plt.legend()

    # Display the plot
    plt.show()

# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
    
def battreSamre(lista, forbattring):
  list_forbattring = []
  list_forsamring = []
  år = lista[0][-6:]
  for rad in lista[2:]:
    is_forbattring = True
    is_forsamring = True

    #Jämför varje års resultat med följande års resultat
    for i in range(13, 18):
      if int(rad[i]) < int(rad[i + 1]):
        is_forbattring = False
      if int(rad[i]) > int(rad[i + 1]):
        is_forsamring = False

    if is_forbattring:
      list_forbattring.append([rad[0]] + rad[13:19])

    elif is_forsamring:
      list_forsamring.append([rad[0]] + rad[13:19])

  print("Länder som ständigt har förbättrat sina resultat mellan år 2003 - 2018:")
  print("-" * 83)
  print("                         År och resultat                      ")
  print("-" * 83)
  list_forbattring.insert(0, år)
  list_forbattring[0].insert(0, "Land")

  #Varje rad skrivs ut med särskilt avstånd.
  for rad in list_forbattring:
    Mellanslag = 10
    for item in rad:
      print(f"{item:<{2 + Mellanslag}}", end=" ")
      Mellanslag = 10

    print()
    print()
    print()

  print("Länder som ständigt har försämrat sina resultat mellan år 2003 - 2018:")
  print("-" * 83)
  print("                          År och resultat                    ")
  print("-" * 83)

  list_forsamring.insert(0, år)
  list_forsamring[0].insert(0, "Land")

  for rad_index, rad in enumerate(list_forsamring):
    Mellanslag = 10
    for item_index, item in enumerate(rad):

      if rad_index == 0 and item_index == 0:
        continue  
      print(f"{item:<{2 + Mellanslag}}", end=" ")
      Mellanslag = 10

    print()
    print()


# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
    
#En funktion som visar år och länder då kvinnor har presterat bättre än män
def kvinna_man(pisadata):             
    print("År och länder när kvinnorna presterar bättre än männen under åren 2003–2018.")
    print()               

#Formatera och skriv ut kolumnrubtiken för tabellen         
    rubrik = "{:<5} {:<19} {:<7} {:<7}".format("År", "Land", "Kvinnor", "Män")                                  
    print(rubrik)                                                                                               
    print("-" * 40)                                                                                           

    år_dict = {}                                                                                       

#Loopa igenom varje rad i pisadatan med början från det tredje elementet
    for rad in pisadata[2:]:                                                                                    
        år = 2018                                                                                              
        while år >= 2003:                                                                                       
            år_skillnad = (2018 - år) / 3                                                                       
            man, kvinna = 1 + år_skillnad * 2, 2 + år_skillnad * 2                                  
            man, kvinna = int(man), int(kvinna)                                         

            k_poang = int(rad[kvinna])                                                            
            m_poang = int(rad[man])                                                                  

            if k_poang > m_poang:                                                                      
                if år not in år_dict:                                                                           
                    år_dict[år] = []                                                                            
                år_dict[år].append((rad[0], k_poang, m_poang))                                           

            år -= 3                                                                                             

    for år, resultat in sorted(år_dict.items(), reverse=True):                                                 
        print(f"{år}")                                                                                          
        for data in resultat:                                                                                   
            rad_data = "{:<4} {:<20} {:<7} {:<7}".format(' ', *data)                                            
            print(rad_data)


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
                
def print_huvudmeny():

    print("Program för att läsa in och analysera data från PISA-undersökningen")

    print()

    print("1. Läs in csv-filen.")
    print("2. Bästa resp. sämsta resultatet år 2018.")
    print("3. Matematikkunskaper i norden år 2003 – 2018.")
    print("4. Kontinuerlig förbättrat resp. försämrat år 2003 – 2018.")
    print("5. Kvinnor presterar bättre än män under åren 2003 – 2018.")
    print("6. Avsluta programmet.")
    
    print()

while True: 
    print()
    print_huvudmeny()

    val = input("Välj ett alternativ (1-6): ")
        
    if val == "1":
        pisadata = read_file()
        for i in range(5):
            print(pisadata[i])

        
    elif val == "2":
            print("Funktionen för att visa bästa och sämsta resultatet för år 2018 anropas här.")
            #hitta index för medelvärde år 2018
            def sok_index_2018(row1, row2):
                for i in range(min(len(row1), len(row2))):
                    if row1[i] == '2018' and row2[i] == 'medel':
                        return i
                return None
            index_2018_medel = sok_index_2018(pisadata[0], pisadata[1])
            sort_best_and_worst(pisadata, index_2018_medel)
            
    elif val == "3":
            print("Funktionen för att analysera matematikkunskaper i Norden år 2003–2018 anropas här.")
            medel = arsmedel(pisadata)
            nordTabell(pisadata)
            nordGraf(pisadata, medel)
            
    elif val == "4":
            print("Funktionen för att visa länder med kontinuerlig förbättring resp. försämring år 2003–2018 anropas här.")
            print()
            print()
            battreSamre(pisadata, True)
            
    elif val == "5":
            print("Funktionen för att visa när kvinnor presterat bättre än män år 2003–2018 anropas här.")
            print()
            print()
            print(kvinna_man(pisadata))

    elif val == "6":
        print("Programmet är avslutat.")

        break

    else:
        print("Menyalternativet finns ej. Vänligen välj ett alternativ mellan (1-6)")

