from Bio.Blast import NCBIWWW

# Eine echte, fehlerfreie Protein-Sequenz (Teil des Zika-Virus-Proteins)
echte_sequenz = "MKNPKKKSGGFRIVNMLKRGVARVSPFGGLK"

print("--- STARTE ECHTEN ONLINE-BLAST ---")
print("Verbindung zu den US-Servern steht. Bitte kurz warten...")

# Wir starten die Suche in den USA
# Da die Sequenz fehlerfrei ist, wird der Server uns echte Treffer liefern
ergebnis_handle = NCBIWWW.qblast("blastp", "nr", echte_sequenz)

print("--- SUCHE ERFOLGREICH BEENDET ---")

# Hier nutzen wir direkt deinen absoluten Pfad, um die neue XML-Datei zu speichern!
speicher_pfad = r"c:\Users\nikdo\OneDrive\Υπολογιστής\Python start\E1\BLAST\real_blast_results.xml"

with open(speicher_pfad, "w") as out_handle:
    out_handle.write(ergebnis_handle.read())
ergebnis_handle.close()

print("Echte Ergebnisse erfolgreich in 'real_blast_results.xml' gespeichert!")


from Bio.Blast import NCBIXML

print("--- CODESKREPT: ECHTE BLAST-AUSWERTUNG ---")

try:
    # Der absolute Pfad zu deiner neuen, echten Ergebnisdatei
    absoluter_pfad = r"c:\Users\nikdo\OneDrive\Υπολογιστής\Python start\E1\BLAST\real_blast_results.xml"
    
    with open(absoluter_pfad) as result_handle:
        blast_records = NCBIXML.parse(result_handle)
        
        for record in blast_records:
            print(f"Genutzte Datenbank: {record.database}")
            print(f"Deine Sequenzlänge: {record.query_length} Aminosäuren\n")
            
            print("=== DIE BESTEN TREFFER IN DER DATENBANK ===")
            
            # Wir gehen durch die gefundenen Treffer (alignments) durch
            anzahl = 0
            for alignment in record.alignments:
                anzahl += 1
                # title enthält den wissenschaftlichen Namen des Organismus
                print(f"Treffer #{anzahl}: {alignment.title}")
                
                # Wir wollen nur die Top 5 Treffer sehen, sonst wird das Terminal überflutet
                if anzahl >= 5:
                    break
                    
            if anzahl == 0:
                print("Seltsam, immer noch keine Treffer gefunden.")
                
except FileNotFoundError:
    print("Fehler: Die Datei 'real_blast_results.xml' wurde nicht gefunden.")

from Bio.Blast import NCBIXML
from collections import Counter

# Use your exact absolute path here
path = r"c:\Users\nikdo\OneDrive\Υπολογιστής\Python start\E1\BLAST\real_blast_results.xml"

organisms = []

with open(path) as result_handle:
    blast_records = NCBIXML.parse(result_handle)
    for record in blast_records:
        for alignment in record.alignments:
            # Extract the organism name from the title string
            title = alignment.title
            if "[" in title and "]" in title:
                org_name = title.split("[")[1].split("]")[0]
                organisms.append(org_name)

# Count how many times each organism appeared
counts = Counter(organisms)

print("=== TOP ORGANISMS FOUND IN YOUR BLAST SEARCH ===")
for org, count in counts.most_common(5):
    print(f"{org}: Found {count} times")