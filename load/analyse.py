import pandas as pd
import matplotlib.pyplot as plt
###### OPPG 1 ####################################################
#les CVS fil
data = pd.read_csv("C:/Users/feddy/Desktop/ELK330/Repos/power-system-data/load/forbruk_2025.csv", sep=",") #les forbruk_2025
data = data.rename(columns={"Unnamed: 0": "Time(Local)"}) # endre unnamed 0 til Time(Local)

data["Time(Local)"] = pd.to_datetime( #tolk dataen som klokkeslett

    data["Time(Local)"],
    utc=True
)

data = data.set_index("Time(Local)") #gjør tid til indeksen
data = data.sort_index() #sorter indeks
data = data.tz_convert("Europe/Oslo") #converter til tidssone for oslo

# print(data)

# print(data.head())

# print(data.columns)

# print(data.dtypes)

###################################################################
############### OPPG 2 ############################################
gjennomsnitt = data["Actual Load"].resample("ME").mean().reset_index(drop=True).round(2) #del tidperioden inn i måneds grupper og ta gjennomsnitt
gjennomsnitt.name = "Gjennomsnittlig Last (MW)"

maneder = pd.Series([
    "Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August" #en serie av måneder
    , "September", "Oktober", "November", "Desember"

], name="Maaned") #navngi den til "måneder"

maantlig_last = pd.concat([maneder, gjennomsnitt], axis=1) #slå sammen måneder og gjennomsnittslasten

print(maantlig_last.to_string(index=False))

#################### OPPG 3 ##################################################

maantlig_last.to_csv("C:/Users/feddy/Desktop/ELK330/Repos/power-system-data/results/manedlig_last_2025.csv", index=False) #lagre fil som csv


plt.plot(

    maantlig_last["Maaned"], maantlig_last["Gjennomsnittlig Last (MW)"]
    )

plt.title("Gjennomsnittlig Måneds Last For 2025")
plt.xlabel("Måned")
plt.ylabel("Gjennomsnittlig Last (MW)")
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("C:/Users/feddy/Desktop/ELK330/Repos/power-system-data/results/manedlig_last_2025.png")

################# OPPG 5 ###########################################################

min = data["Actual Load"].resample("ME").min().reset_index(drop=True).round(2) #min last
min.name = "Min Last (MW)"

max = data["Actual Load"].resample("ME").max().reset_index(drop=True).round(2) #maks last
max.name = "Maks Last (MW)"

Standard_avvik = data["Actual Load"].resample("ME").std().reset_index(drop=True).round(2) #standard avvik
Standard_avvik.name = "Standard Avvik (MW)"
maantlig_Statistikk_last = pd.concat([maneder, gjennomsnitt, min, max, Standard_avvik], axis=1) #slå sammen måneder, gjennomsnitt, min, maks, standard avvik

print(maantlig_last.to_string(index=False))

maantlig_Statistikk_last.to_csv("C:/Users/feddy/Desktop/ELK330/Repos/power-system-data/results/manedlig_last_statistikk_2025.csv", index=False) #lagre csv