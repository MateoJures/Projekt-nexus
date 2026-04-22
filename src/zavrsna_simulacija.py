import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import requests

df_lokacije = pd.read_csv('mars_lokacije.csv', sep=';', decimal=',')
df_uzorci = pd.read_csv('mars_uzorci.csv', sep=';', decimal=',')

df_spojeno = pd.merge(df_lokacije, df_uzorci, on='ID_Uzorka')

anomalije = df_spojeno[(df_spojeno['Temp_Tla_C'] < -140) | (df_spojeno['H2O_Postotak'] < 0)]
df_cisto = df_spojeno.drop(anomalije.index)

sns.set_theme(style="darkgrid")

# --- GRAF 1: Odnos temperature i vlage
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_cisto,
    x='Temp_Tla_C',
    y='H2O_Postotak',
    hue='Metan_Senzor',
    palette='viridis'
)
plt.title('Odnos temperature i vlage u krateru Jezero')
plt.savefig('graph1_temp_h2o.png')

# --- GRAF 2: Karta planiranih dubina bušenja
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='Dubina_Busenja_cm', palette='magma')
plt.title('Karta planiranih dubina bušenja')
plt.savefig('graph2_heatmap_depth.png')
plt.close()

# --- GRAF 3: Detekcija metana
plt.figure(figsize=(10, 8))
boje_metana = {"Pozitivno": "red", "Negativno": "blue"}
sns.scatterplot(
    data=df_cisto,
    x='GPS_LONG',
    y='GPS_LAT',
    hue='Metan_Senzor',
    palette=boje_metana
)

plt.title('Detekcija metana po lokacijama (Crveno = Pozitivno)')
plt.savefig('graph3_methane_scatter.png')
plt.close()

# --- GRAF 4: Kandidati (Popravljeno filtriranje)
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='H2O_Postotak', alpha=0.5)
kandidati = df_cisto[
    (df_cisto['Metan_Senzor'] == 'Pozitivno') &
    (df_cisto['Organske_Molekule'] == 'Pozitivno')
]

if not kandidati.empty:
    plt.scatter(kandidati['GPS_LONG'], kandidati['GPS_LAT'], marker='*', s=250, color='red', label='Kandidati')
    print(f"Pronađeno {len(kandidati)} lokacija s metanom i organskim molekulama.")
else:
    print("Nema kandidata koji zadovoljavaju oba uvjeta.")

plt.title('Lokacije kandidata za bušenje (Metan + Organske molekule)')
plt.legend()
plt.savefig('graph4_scatter_plot_plot.png')
plt.close()

# --- GRAF 5: Navigacijska karta
plt.figure(figsize=(12, 8))

extent_koordinate = [
    df_cisto['GPS_LONG'].min(), df_cisto['GPS_LONG'].max(),
    df_cisto['GPS_LAT'].min(), df_cisto['GPS_LAT'].max()
]

try:
    slika_kratera = plt.imread('jezero_crater_satellite_map.jpg')
    plt.imshow(slika_kratera, extent=extent_koordinate, aspect='auto', alpha=0.7)
except FileNotFoundError:
    print("Napomena: Satelitska slika nije pronađena.")

sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='ID_Uzorka', s=40, legend=False)

plt.title('Navigacijska karta: Misija Nexus u krateru Jezero')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.savefig('graph5_jezero_mission_map.jpg')
plt.show()

nalozi = []
for index, redak in kandidati.iterrows():
    nalog = {
        "id": int(redak['id']),
        "koordinate": [float(redak['GPS_LONG']), float(redak['GPS_LAT'])],
        "akcije": ["NAVIGACIJA", "SONDIRANJE", "SLANJE_PODATAKA"]
    }
    nalozi.append(nalog)

url = "https://webhook.site/03f33f00-c3a0-4a66-8b06-63f1af147efa"

try:
    response = requests.post(url, json={"misija": "Nexus", "podaci": nalozi}, timeout=10)
    if response.status_code == 200:
        print("Misija uspješno izvršena! Robot prima upute.")
    else:
        print(f"Server javlja grešku: {response.status_code}")
except Exception as e:
    print(f"Greška pri slanju podataka: {e}")