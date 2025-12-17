Aggiunte:
- Più grafici in cui incrociamo più variabili (vedi parte-1 della lezine_3)
- Vedere se si possono mettere in atto le 2 idee che ti ho scritto.
- Uso delle tabelle di frequenza
- 


# es. tabella di frequenza

# 1. Calcola le frequenze assolute
frequenze_assolute = df_clean['Transmission'].value_counts()

# 2. Calcola le frequenze relative (percentuali)
frequenze_relative = df_clean['Transmission'].value_counts(normalize=True) * 100

# 3. Combina i risultati in un unico DataFrame

tabella_frequenza = pd.DataFrame({
    'Conteggio Assoluto': frequenze_assolute,
    'Frequenza Relativa (%)': frequenze_relative.round(2)
})

print(tabella_frequenza)



Consiglio per il tool:
Utilizzare un classificatore, in cui dentro creiamo dei regressori


---- PARTE 1: SISTEMAZIONI-----
Le scale delle variabili vengono convertite perché a un modello di regressione lineare, per come è costruito matematicamente, è meglio utilizzare scale nominali e ratio. Semplicemente Owner_Type quando sarà convertita in discreta non dovrà essere: 1,2,3,4. Ma invece in dummy variables: Is_First_Hand (0 o 1) ecc...
Year trasformata in Age, seguirà direttamente la scala ratio, in quanto in Age, lo 0, è un valore VERO.

