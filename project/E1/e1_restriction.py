from Bio.Seq import Seq
from Bio.Restriction import EcoRI

# 1. Ein künstlicher DNA-Abschnitt deines E1-Plasmids
# Schau genau hin: Die Sequenz "GAATTC" ist in der Mitte eingebaut
plasmid_dna = Seq("ATCGATCGATCGATCG" + "GAATTC" + "ATCGATCGATCGATCG")

print("--- E1 PRACTICAL: RESTRICTION ANALYSIS ---")
print(f"Isolierte Plasmid-DNA: {plasmid_dna}")

# 2. Wir lassen die molekulare Schere (EcoRI) nach ihrer Schnittstelle suchen
schnittstellen = EcoRI.search(plasmid_dna)

# 3. Ergebnis anzeigen (Python zählt ab Index 1 für biologische Positionen)
print(f"EcoRI schneidet an der Position: {schnittstellen}")

# 4. Wir simulieren das Zerschneiden in zwei Stücke (Fragmente)
if schnittstellen:
    pos = schnittstellen[0]
    fragment_1 = plasmid_dna[:pos]
    fragment_2 = plasmid_dna[pos:]
    print(f"Fragment 1 im Gel (Länge {len(fragment_1)} Basen): {fragment_1}")
    print(f"Fragment 2 im Gel (Länge {len(fragment_2)} Basen): {fragment_2}")
