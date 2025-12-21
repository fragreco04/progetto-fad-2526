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
Year trasformata in Age, seguirà direttamente la scala ratio, in quanto in Age, lo 0, è un valore VERO.

--In brand bisogna fare one hot 
-- Kilometers da fare trasformazione logaritmica. Forse fare radice quadrata in realtà.
-- Trasmission e Fuel_Type diventano 0 e 1
-- Owner_type: variabile ordinale 1,2,3 per il problema delle classi sbilanciate
-- Age apposto così
-- Location fare one hot
-- Mileage apposto
-- Engine : logaritmo
-- Power uguale engine, ma probabilmente si dovrà rimuovere
-- Seats va bene così
-- Price trasformazione logaritmica
-- Infine standard scaler di tutto

Multicollinearità
Tenere Power

-- Verificare se rispondiamo a tutte le domande fatte all inzio dell analisi
