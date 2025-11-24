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