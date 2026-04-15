import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import requests

df_mars = pd.read_csv("mars_lokacije.csv", sep = ';', decimal = ',')
df_mars = pd.read_csv("mars_uzorci.csv", sep = ';', decimal = ',')

df_spajanje = pd.merge(lokacije, uzorci, on='Id_uzorka')

df_cisto = df[
    (df['Vlaga'] >= 0) & (df['Temperatura'] > -150)].copy()
    (df['Temp_Tla_C'] >= -140), (df['Temp_Tla_C'] <= 40),
    (df['pH_Vrijednost'] >= 0), (df['pH_Vrijednost'] <= 14),
    (df['Dubina_Busenja_cm'] >= 0),
    (df['H2O_Postotak'] >= 0) & (df['H2O_Postotak'] <= 100)
]

print(f"Izbačeno je {len(df) - len(df_cisto)} anomalija.")

kandidati = df_cisto[(df_cisto['Metan'] == True) & (df_cisto['Organske_Molekule'] == True)]


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='Vlaga', palette='Blues')
plt.scatter(kandidati['GPS_LONG'], kandidati['GPS_LAT'], marker='*', s=250, color='red', label='Kandidati')
plt.legend()
plt.savefig('scatter_plot.png')

plt.figure(figsize=(12, 8))
extent_koordinate = [
    df_cisto['GPS_LONG'].min(), df_cisto['GPS_LONG'].max(),
    df_cisto['GPS_LAT'].min(), df_cisto['GPS_LAT'].max()
]

slika_kratera = plt.imread('jezero_crater_satellite_map.jpg')
plt.imshow(slika_kratera, extent=extent_koordinate, aspect='auto', alpha=0.7)
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', size='Dubina', alpha=0.5)
plt.savefig('jezero_mission_map.jpg')


url = https://webhook.site/03f33f00-c3a0-4a66-8b06-63f1af147efa
response = requests.post(url, json={"misija": "Nexus", "nalozi": nalozi})

if response.status_code == 200:
    print("Misija uspješna! Podaci poslani robotu.")