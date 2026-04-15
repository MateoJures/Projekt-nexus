import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import requests

df_lokacije = pd.read_csv('mars_lokacije.csv', sep=';', decimal=',')
df_uzorci = pd.read_csv('mars_uzorci.csv', sep=';', decimal=',')

df_spojeno = pd.merge(df_lokacije, df_uzorci, on='id')

anomalije = df_spojeno[(df_spojeno['temperatura'] < -140) | (df_spojeno['vlaga'] < 0)]
df_cisto = df_spojeno.drop(anomalije.index)

sns.set_theme(style="darkgrid")

# --- GRAF 1
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='temp_tla', y='vlaga', hue='metan', palette='viridis')
plt.title('Odnos temperature i vlage (boja = metan)')
plt.savefig('graph1_temp_h2o.png')
plt.close()
"""
# --- GRAF 2
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='dubina_busenja', palette='magma')
plt.title('Karta planiranih dubina bušenja')
plt.savefig('graph2_heatmap_depth.png')
plt.close()

# --- GRAF 3
plt.figure(figsize=(10, 8))
boje_metana = {True: 'red', False: 'blue'}
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='metan', palette=boje_metana)
plt.title('Detekcija metana po lokacijama (Crveno = Pozitivno)')
plt.savefig('graph3_methane_scatter.png')
plt.close()

# --- GRAF 4: Kandidati
plt.figure(figsize=(10, 8))

sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='vlaga', alpha=0.5)

kandidati = df_cisto[(df_cisto['metan'] == True) & (df_cisto['organske_molekule'] == True)]

plt.scatter(kandidati['GPS_LONG'], kandidati['GPS_LAT'], marker='*', s=250, color='red', label='Kandidati')
plt.title('Lokacije kandidata za bušenje (Metan + Organske molekule)')
plt.legend()
plt.savefig('scatter_plot.png')
plt.close()

# --- GRAF 5
plt.figure(figsize=(12, 8))

extent_koordinate = [
    df_cisto['GPS_LONG'].min(), df_cisto['GPS_LONG'].max(),
    df_cisto['GPS_LAT'].min(), df_cisto['GPS_LAT'].max()
]

try:
    slika_kratera = plt.imread('jezero_crater_satellite_map.jpg')
    plt.imshow(slika_kratera, extent=extent_koordinate, aspect='auto', alpha=0.7)
except FileNotFoundError:
    print("Greška: Slika 'jezero_crater_satellite_map.jpg' nije pronađena!")


sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', color='cyan', s=20, alpha=0.6)
plt.title('Navigacijska karta: Misija Nexus u krateru Jezero')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.savefig('jezero_mission_map.jpg')
plt.show()


extent_koordinate = [
    df_cisto['GPS_LONG'].min(), df_cisto['GPS_LONG'].max(),
    df_cisto['GPS_LAT'].min(), df_cisto['GPS_LAT'].max()
]

plt.imshow(slika_kratera, extent=extent_koordinate, aspect='auto', alpha=0.7)
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='tip_tla')
plt.savefig('jezero_mission_map.jpg')

nalozi = []
for index, redak in kandidati.iterrows():
    nalog = {
        "id": redak['id'],
        "koordinate": [redak['GPS_LONG'], redak['GPS_LAT']],
        "akcije": ["NAVIGACIJA", "SONDIRANJE", "SLANJE_PODATAKA"]
    }
    nalozi.append(nalog)


url = https://webhook.site/03f33f00-c3a0-4a66-8b06-63f1af147efa
response = requests.post(url, json={"misija": "Nexus", "podaci": nalozi})

if response.status_code == 200:
    print("Misija uspješno izvršena! Robot prima upute.")
"""