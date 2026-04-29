#Projekt nexus

#Opis projekta

1. Sažetak projekta

Ovaj projekt istražuje mogućnost postojanja života na Marsu pomoću analize podataka. 
Sustav automatski obrađuje očitanja sa senzora i identificira lokacije s najvećim znanstvenim potencijalom. 
Program je dizajniran da bude precizan, brz i jednostavan za korištenje u istraživačke svrhe.

2. Metodologija rada

Analiza se temelji na provjeri tri ključna faktora: prisutnosti vode, temperaturi i kemijskom sastavu atmosfere.

Prikupljanje podataka: Simulacija unosa sa senzora.

Obrada: Algoritam uspoređuje podatke sa strogo definiranim biološkim granicama.

Interpretacija: Sustav generira vizualne prikaze radi lakšeg donošenja odluka

3. Analiza i Vizualizacije

Grafikon kretanja temperature: Prikazuje periode kada je život fizički moguć.

Karta vlažnosti tla: Identificira područja s ostacima vode.

Spektar atmosferskih plinova: Detektira prisutnost metana kao ključnog markera.

Usporedba lokacija: Rangiranje mjesta slijetanja prema sigurnosti i potencijalu.

Finalna detekcija života: Sažeti prikaz vjerojatnosti pronalaska mikroorganizama


Evo prikaza podataka koje smo generirali:


1.![Ovaj prikaz vizualizira podatke prikupljene sa senzora, fokusirajući se na to kako toplina tla utječe na postotak vode (H2O)](assets/graph1_temp_h2o.png)

2.![Ova toplinska mapa vizualizira distribuciju podataka kroz različite dubinske profile.](assets/graph2_heatmap_depth.png)

3.![Pomoću scatter plota vizualizirali smo raspodjelu koncentracije metana u promatranom razdoblju.](assets/graph3_methane_scatter.png)

4.![Ovaj scatter plot omogućuje nam dubinski uvid u distribuciju podataka i identifikaciju korelacija koje nisu vidljive u tabličnom prikazu.](assets/graph4_scatter_plot.png)

5.![Svi prikupljeni podaci dolaze iz specifičnih zona kratera Jezero. Mapa ispod prikazuje točke na kojima su senzori zabilježili vrijednosti prikazane u prethodnim grafikonima.](assets/graph5_jezero_mission_map.jpg)

Kloniraj repozitorij:
```bash
   git clone MateoJures/Projekt-nexus
   ```
Pokreni glavni program:
[Pritisni ovdje za otvaranje dokumenta](src/zavrsna_simulacija.py)

Popis alata koje sam koristio:

**Jezik** Python 

**HTML** za kostur i sadržaj stranice.

**CSS** za boje, fontove i raspored elemenata.

**Git** za spremanje verzija koda.

Struktura datoteka:

`src/zavrsna_simulacija.py`

`data/mars_uzorci (1).csv`: [Pritisni ovdje za otvaranje dokumenta](data/mars_uzorci.csv)

`data/mars_lokacije (1).csv`: [Pritisni ovdje za otvaranje dokumenta](data/mars_lokacije.csv)

-Mateo Jures - [@MateoJures](https://github.com/MateoJures)
