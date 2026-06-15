# BLAST

from Bio.Blast import NCBIWWW

print("--- STARTING ONLINE BLAST SEARCH ---")
print("Bitte warten, die Suche in den USA läuft...")

# Wir schicken dein mutiertes Protein an den Server der US-Regierung
# Das kann 1-2 Minuten dauern, da Millionen Sequenzen durchsucht werden
ergebnis_handle = NCBIWWW.qblast("blastp", "nr", "RC*SV*VRLRQFESEARANNSINRFNLDLE") # nr steht für Non-redundant protein sequences

print("--- BLAST SEARCH COMPLETED ---")

# Wir speichern das Ergebnis erst einmal als XML-Datei ab
with open("my_blast_results.xml", "w") as out_handle:
    out_handle.write(ergebnis_handle.read())
ergebnis_handle.close()

print("Ergebnisse erfolgreich unter 'my_blast_results.xml' gespeichert!")