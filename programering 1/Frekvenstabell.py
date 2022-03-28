#Författare Vilhelm Gustavsson
#Uppgift Frekvenstabell


# tar ut alla unika värden. 
def make_unique(activitiesList, activities):
    for activity in activities:
        if activity not in activitiesList:
            activitiesList.append(activity)
    return activitiesList


#gör en tabell
def generate_table(unique_activities, activitiesTable):
    for activity in activities:
        activitiesTable[activity] = 0
    return activitiesTable


#kollar hur måga av alla grejer det finns
def count_occurances(activities, key):
    result = 0
    for activity in activities:
            if activity == key:
                result += 1
    return result

def add_fequency(activitiesTable, occuranceList):
    for key in activitiesTable.keys():
        activitiesTable[key] = count_occurances(activities, key) 
    return activitiesTable


#funktion som gör en tabell i utskriften med formatering
def print_table(activitiesTable):
    print("{0:<12}{1:1}{2:>10}{3:4}{4:<16}".format("Aktivitet", ":", "Antal", ":", "Relativ frekvens"))
    for i in range(0, 42):
        print("=", end="")
    print("=")
    antal = 0
    for value in activitiesTable.values():
        antal += value
    for key, value in activitiesTable.items(): 
        relativ_frekvens = value / antal
        print("{0:<12}{1:1}{2:>10}{3:4}{4:<.1%}".format(key, ":", value, ":", relativ_frekvens))

activitiesList = []
activitiesTable = {}
occuranceList = []


#en lista på alla grejer
activities = ["Games",
              "Basketball",
              "Track",
              "Football",
              "Dancing",
              "Track",
              "Horses",
              "Football",
              "Basketball",
              "Football",
              "Basketball",
              "Horses",
              "Rpg's",
              "Track",
              "Horses",
              "Football",
              "Basketball",
              "Basketball",
              "Track",
              "Football",
              "Dancing",
              "Track",
              "Horses",
              "Football",
              "Basketball",
              "Football",
              "Football",
              "Basketball",
              "Horses",
              "Rpg's",
              "Football",
              "Track",
              "Football"]



unique_activities = make_unique(activitiesList, activities)
table_with_keys = generate_table(unique_activities, activitiesTable)
table_with_frequencies = add_fequency(table_with_keys, occuranceList)
print_table(table_with_frequencies)


