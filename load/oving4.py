import pandas as pd  
import matplotlib.pyplot as plt

############ oppg 4

df = pd.read_csv("C:/Users/feddy/Desktop/ELK330/Repos/power-system-data/load/load_data.csv")
 #les cvs data og tolk innholdet for "Time(Local)" som dato og klokkeslett

df["Time(Local)"] = pd.to_datetime(
    df["Time(Local)"],
    format="%d.%m.%Y %H:%M:%S %z",
    utc=True

).dt.tz_convert("Europe/Oslo")

df = df.set_index("Time(Local)")

df["Production"] = (df["Production"].str.replace(",", ".", regex=False).astype(float)) #gjør om , til . for production

df["Consumption"] = (df["Consumption"].str.replace(",", ".", regex=False).astype(float)) #gjør om , til . for consumption

print(df.head())

##########################################3
# forklar Datetimeindex og hvorfor tidsstempelet har +01:00
#
# Datetimeindex er en index som brukes til å håndtere tidsrekker. den gjør det mulig å bruke tidsrekkene til forskjellige ting
# som å filtrere data fra forskjellige måneder år, eller å resample tidsintervall ut etter hva du vil ha. du kan også konvertere mellom ulike tidssoner.
#
# tidsstempelet +01:00 betyr at tiden ligger en time foran UTC. som er tidssonen for Oslo
############################## oppg 5 

print(df.index[0])

##################################################
#forklar resultatet
#
# resultatet viser 01.01.2026 00:00:00 +01:00 dette er da den første registrerte tiden av målingene. grunnen til at vi får 1.januar.2026 er fordi man går ut ifra UTC +1 
# det betyr at om man hadde vært på UTC tid så ville resultatet blitt 31.12.2025 23.00.00 +00:00
#
#############oppg 6##############
print(df.loc["2026-01-01 03:00"])

# når man bruker .loc her så sier man at man har raden med dato "2026-01-01 03:00" 
# så får vi all informasjon som er relatert til den datoen som i dette tilfellet er production og consumption

lastprofil_dogn = df.loc["2026-01-01 00:00" : "2026-01-01 23:00" ]
print(lastprofil_dogn)
print(len(lastprofil_dogn))

plt.figure(figsize=(10,5))

plt.plot(lastprofil_dogn.index, lastprofil_dogn["Production"], label="Produksjon")

plt.plot(lastprofil_dogn.index, lastprofil_dogn["Consumption"], label="Forbruk")

plt.title("Produksjon Og Forbruk 1.Januar.2026")
plt.xlabel("Tid")
plt.ylabel("Effekt")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
################## oppg 7 ########################

df["Netto"] = (
    df["Production"]
    - df["Consumption"]
)
##################### oppg 8 #######################
print(df.head())

min_prod = round(df["Production"].min(), 2)
max_prod = round(df["Production"].max(), 2)
std_prod = round(df["Production"].std(), 2)

print(min_prod)
print(max_prod)
print(std_prod)

################### oppg 9#######################
min_netto = round(df["Netto"].min(), 2)
max_netto = round(df["Netto"].max(), 2)

print(min_netto)
print(max_netto)

# når intreffer netto min og netto max?

tid_max_netto = df["Netto"].idxmax()
tid_min_netto = df["Netto"].idxmin()

print("maksimal netto intreffer:" ,tid_max_netto)
print("min netto intreffer:" ,tid_min_netto)

##################### oppg 10 #####################

print(df["Production"].sum())
#denne koden viser total energi som har blitt produsert fra 1.januar.2026 til 20.mai.2026 (det er målt i MWh siden tidsintervallet er i timer)

########################### oppg 11 ##########################

df.plot(
    y=["Production", "Consumption"],
    figsize=(10, 5),
    title="Produksjon Og Forbruk Over Tid",
    xlabel="Tid",
    ylabel="Effekt",
    grid=True,
    legend=True,
)

plt.tight_layout()
plt.show()

########################### Oppg 12 ################

df.plot(
    y=["Production", "Consumption", "Netto"],
    figsize=(10, 5),
    title="Produksjon, Forbruk Og Netto Over Tid",
    xlabel="Tid",
    ylabel="Effekt",
    grid=True,
    legend=True,
)

plt.tight_layout()
plt.show()

