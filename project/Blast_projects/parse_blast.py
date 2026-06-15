# Die XML-Datei von den US-Servern ist für Python erst einmal nur ein riesiger, unübersichtlicher String (Textwurst). 
# Der Befehl NCBIXML.parse()nimmt diesen Text, filtert die nervösen XML-Tags (wie <Iteration_hits>) heraus 
# und übersetzt das Ganze in saubere Python-Listen und -Objekte, die wir ganz einfach mit .databaseoder .alignmentsabfragen können.
from Bio.Blast import NCBIXML

print("--- ANALYSIERE BLAST-DATEI ---")

try:
    # Das hat ja eben schon perfekt geklappt:
    absoluter_pfad = r"c:\Users\nikdo\OneDrive\Υπολογιστής\Python start\E1\BLAST\my_blast_results.xml"
    
    with open(absoluter_pfad) as result_handle:
        blast_records = NCBIXML.parse(result_handle)
        
        for record in blast_records:
            print(f"Datenbank: {record.database}")
            print(f"Länge deiner Sequenz: {record.query_length} Aminosäuren")
            
            # KORREKTUR: Bei Biopython heißt es 'alignments', nicht 'hits'!
            anzahl_treffer = len(record.alignments)
            print(f"Anzahl gefundener Treffer: {anzahl_treffer}")
            
            if anzahl_treffer == 0:
                print("\nErgebnis: Keine Treffer gefunden.")
                print("Grund: Die Sequenz enthält Stoppcodons (*).")
except FileNotFoundError:
    print("Fehler: Datei wurde nicht gefunden.")