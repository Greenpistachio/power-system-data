import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



L_0 = 10000

A_i = 1500

mju_i = 16

sigma_i = 4

t = np.linspace(0, 24, 500)


L_t = L_0 + A_i * np.exp(-((t - mju_i)**2) / (2 * sigma_i**2))

# plt.plot(t, L_t)
# plt.xlabel("Tidspunkt (timer)")
# plt.ylabel("Last")
# plt.title("Gauss-modell")
# plt.xticks(range(0, 25 ,2))
# plt.grid()
# plt.show()

#man ser at å endre på L0 endrer på hvor mye grunnlasten er på altså den minste lasten i grafen
# ved å endre på A_i så endres det på hvor høyt toppunktet går opp iforhold til grunnlasten
# ved å endre på mju_i så endrer man på hvilket klokkeslett toppunktet kommer
# og ved å endre på sigma_i så kan man endre på hvor lenge toppunktet varer (i timer)
#
#etter å ha eksperimentert med parameterene så har jeg observert at kurven følger det som ble sagt tidligere ganske likt
# når jeg valgte 16 for mju så var toppunktet kl 16:00. når jeg valgte sigma til å være 2 så var bredden på toppunktet 2timer
#mens om jeg endret den til 4 så var den 4 timer
#grunnlasten viste seg tiø å være den laveste verdien på grafen gitt at det er grunnlasten

############oppg 3#####################



#leser csv fil. usecols leser kun de kolonnene vi trenger
df = pd.read_csv("C:/Users/feddy/Desktop/ELK330/Repos/power-system-data/load/Lastdata_Forbruk_Prisomraade_Elhub.csv", usecols=["START_TIME", "PRICE_AREA", "VOLUME_KWH"])

df = df.rename(columns={"START_TIME": "Tid", "PRICE_AREA": "Prisområde", "VOLUME_KWH": "Forbruk"})

#gjør tid til datetime og bruker tid som datetimeindex
df["Tid"] = pd.to_datetime(df["Tid"], utc=True)
df = df.set_index("Tid")

#
df.index = df.index.tz_convert("Europe/Oslo")

print(df.head())

#setter prisområdet til NO2 slik at det er det vi leser
no2 = df[df["Prisområde"] == "NO2"]

utvalgt_data = no2.loc["2026-02-04"]

# vi har flere forskjellige lastgrupper som hytte industri etc..
#så vi bruker groupby for å gruppere alle rader med samme tidspunkt
#og derreter summerer vi alle gruppene for å få totalt last.
#vi deler på 1000 for å få MWH fordi csv filen er i KWH
last_data = (utvalgt_data["Forbruk"].groupby(level=0).sum() / 1000) 

#Tidspunkter for last_data verdiene, 0-23
tid = last_data.index.hour
last = last_data

print(last_data)

#lager flere tidspunkter slik at modell kurven blir litt mer jevn
modell = np.linspace(0, 23, 500)

#Grunnlast
L_0_Modell = 3500

#Natt
A_1 = 1000
mju_1 = 0
sigma_1 = 3.5

#morgen
A_2 = 700
mju_2 = 8
sigma_2 = 2

#kveld
A_3 = 2000
mju_3 = 17
sigma_3 = 8

Gauss_modell = (

L_0_Modell + A_1 * np.exp(-((modell-mju_1)**2) / (2*sigma_1**2) )

+ A_2*np.exp(-((modell-mju_2)**2) / (2*sigma_2**2) )

+ A_3*np.exp(-((modell-mju_3)**2) / (2*sigma_3**2) )

)

plt.plot(tid, last, "o-", label="Målt last")

plt.plot(modell, Gauss_modell, label="Gauss-modell", color="red")

plt.xlabel("Tidspunkt (Timer)")
plt.ylabel("Belastning [MW]")
plt.title("Modellert døgnprofil for NO2")
plt.xticks(range(0, 24))
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()