import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# maks innstråling på 800 W/m^2
A = 800

#maks innståling ved kl 13.00
mju = 13

#en bredde på 3 timer
sigma = 3

#en 24 timer tidsakse med 500 punkter 
t = np.linspace(0, 24, 500)

#formel for Gauss-modell for solinnstråling
G_t = A * np.exp(-((t - mju)**2) / (2 * sigma**2))

#plotter gauss-modellen
# plt.plot(t, G_t)
# plt.xlabel("Tidspunkt (timer)")
# plt.ylabel("Innstråling")
# plt.title("Solinstråling")
# plt.grid()
# plt.show()


####### oppg 2 #########

# maks innstråling på 800 W/m^2
A = 800

#maks innståling ved kl 13.00
mju = 13

#en bredde på 3 timer
sigma = 3

G_t = A * np.exp(-((t - mju)**2) / (2 * sigma**2))

# plt.plot(t, G_t)
# plt.xlabel("Tidspunkt (timer)")
# plt.ylabel("Innstråling")
# plt.title("Solinstråling")
# plt.grid()
# plt.show()

#når vi øker sigma så vil solinnstråling starte tidligere på morgningen og slutte senere på kvelden
#når den derimot reduseres så vil den starte senere på morningen/dagen og slutte tidligere dagen/kvelden
#i tillegg så vil solinnstrålingen på høy sigma gå mer gradvis opp over dagen
#mens på lav sigma så vil solinnstrålingen være mer spiss

#hvilken verdi som mest realistisk kurve kommer faktisk litt ann på hvilken sesong du er på i året
#om det er vinter så vil sigma være litt lavere enn om det er sommer
#grunnen er att om sommer (spesielt i norge) så vil solyset starte veldig tidlig og vare til langt ut på kvelden
# på vinteren vil vi da ha veldig lite solys så den starter senere på morningen og avtas allerede ved ettermiddag

#oppg 3#
#lengde grad: 59.170920 bredde grad: 5.873860

#oppg 4#
#lastet ned csv og lagt inn i load for å lese i python

#oppg 5#

#leser csv filen og bruker skiprows for å hoppe over all informasjon som ikke er en tabell
df = pd.read_csv("C:/Users/feddy/Desktop/ELK330/Repos/power-system-data/load/Solinnstaaling_PVGIS_2023.csv", skiprows=8, 
                skipfooter=10, usecols=("time", "G(i)") 
                 
                 )
df = df.rename(columns={"time": "Tid", "G(i)" : "Global Solinnstråling"})


df["Tid"] = pd.to_datetime(df["Tid"], format="%Y%m%d:%H%M", utc=True)
df = df.set_index("Tid")

print(df.head())
print(df["Global Solinnstråling"].idxmax())

dag = df.loc["2023-06-04"]

dag["Global Solinnstråling"].plot()
plt.xlabel("Tid")
plt.ylabel("SolInnstråling W/M^2")
plt.grid()
plt.legend()
plt.show()