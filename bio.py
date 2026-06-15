# =================================================================
# PROJEKT: Automatisierte Zika-Virus Genomanalyse
# Entwickelt in der Bibliothek Heidelberg
# Zweck: Download von NCBI-Daten und Protein-Eigenschafts-Analyse
# =================================================================

from Bio.Seq import Seq

# 1. Eine echte (beispielhafte) virale DNA-Sequenz
# In der Pharmaforschung liest man diese aus großen Datenbanken ein
virus_dna = Seq("ATGGCCGGTGCTCGTTTGTTCTGGGTGATTGTACTG")

# 2. Automatische Übersetzung: DNA -> RNA -> Protein
protein_sequenz = virus_dna.translate()

# 3. Professionelle Analyse-Ausgabe
print("--- PHARMA RESEARCH DATA ---")
print(f"Eingelesene Virus-DNA: {virus_dna}")
print(f"Uebersetzte Protein-Kette: {protein_sequenz}")
print(f"Anzahl der Aminosaeuren: {len(protein_sequenz)}")

from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# 1. Deine virale Proteinkette aus dem vorherigen Schritt
# (Wir nehmen die Aminosäuren von vorhin, ohne das Stopp-Codon '*')
protein_str = "MAGARLFWVIVL"

# 2. Das Python-Werkzeug für Protein-Eigenschaften aktivieren
analyse = ProteinAnalysis(protein_str)

# 3. Berechnungen durchführen
gewicht = analyse.molecular_weight()
aminos_prozent = analyse.amino_acids_percent

print("--- ADVANCED PROTEIN REPORT ---")
print(f"Exaktes Molekulargewicht: {gewicht:.2f} Da (Dalton)")
print(f"Anteil an Leucin (L): {aminos_prozent['L']:.1f}%")

from Bio import Entrez
from Bio import SeqIO

# 1. Der Datenbank sagen, wer wir sind (Vorschrift der US-Behörde)
Entrez.email = "nikolaos.domenikiotis@stud.uni-heidelberg.de"

# 2. Die Gen-Datenbank (GenBank) nach der Zika-Virus-ID abfragen
# AY632535 ist die weltweite offizielle ID für einen Zika-Virus-Stamm
with Entrez.efetch(db="nucleotide", id="AY632535", rettype="gb", retmode="text") as handle:
    virus_datensatz = SeqIO.read(handle, "genbank")

# 3. Den echten Namen und die Länge des Virus-Gens anzeigen
print("--- DATABASE FETCH SUCCESSFUL ---")
print(f"Name in der Datenbank: {virus_datensatz.description}")
print(f"Länge der echten RNA-Kette: {len(virus_datensatz.seq)} Basen")

# 1. Wir holen uns die reine DNA-Sequenz aus dem Zika-Datensatz
zika_dna = virus_datensatz.seq

# 2. Wir schneiden uns ein bestimmtes Stück heraus (z.B. die ersten 90 Basen)
# Das ist wie ein genetisches Skalpell
gen_abschnitt = zika_dna[0:90]

# 3. Wir übersetzen diesen echten Abschnitt in ein Virus-Protein
zika_protein = gen_abschnitt.translate()

# 4. Wir zählen, wie oft die Aminosäure Alanin (A) vorkommt
alanin_anzahl = zika_protein.count("A")

print("--- GENETIC CUTTING SUCCESSFUL ---")
print(f"Länge des ausgeschnittenen Gens: {len(gen_abschnitt)} Basen")
print(f"Daraus entstehendes Virus-Protein: {zika_protein}") # stern=stop-codon
print(f"Anzahl an Alanin (A) in diesem Protein: {alanin_anzahl}")

from Bio.Seq import MutableSeq

# 1. Wir nehmen unseren Gen-Abschnitt (die ersten 90 Basen) von vorhin
# und machen ihn veränderbar (MutableSeq)
mutation_dna = MutableSeq(gen_abschnitt)

print("--- MUTATION ANALYSIS ---")
print(f"Originale DNA: {mutation_dna}")

# 2. Wir simulieren eine Punktmutation: 
# Wir tauschen die allererste Base (Index 0) gegen ein 'C' aus
mutation_dna[0] = "C"
print(f"Mutierte DNA: {mutation_dna}")

# 3. Wir übersetzen das mutierte Gen in ein neues Protein
mutiertes_protein = mutation_dna.translate()
print(f"Neues Protein : {mutiertes_protein}")

from Bio.Align import PairwiseAligner

# 1. Wir definieren die beiden Proteine, die wir vergleichen wollen
# Das Original von vorhin und dein neues, mutiertes Protein
protein_original = "MAGARLFWVIVL"
protein_mutiert  = "CAGARLFWVIVL" # Das 'M' wurde durch die Mutation zum 'C'

# 2. Wir aktivieren den Aligner (das Vergleichswerkzeug)
aligner = PairwiseAligner()

# 3. Wir setzen die Parameter für den globalen Vergleich (wie auf Seite 10 deines PDFs)
aligner.mode = 'global'
aligner.match_score = 10
aligner.mismatch_score = -9

# 4. Das Alignment ausführen
alignments = aligner.align(protein_original, protein_mutiert)

print("--- SEQUENZ ALIGNMENT REPORT ---")
print(f"Anzahl bester Alignments gefunden: {len(alignments)}")

# 5. Das beste grafische Alignment im Terminal anzeigen
print(alignments[0])

# mit vorherigen Variablen
aligner = PairwiseAligner()

aligner.mode = 'global'
aligner.match_score = 10
aligner.mismatch_score = -9

# 4. Das Alignment ausführen
alignments = aligner.align(zika_protein, mutiertes_protein)
print("--- SEQUENZ ALIGNMENT REPORT 2 ---")
print(f"Anzahl bester Alignments gefunden: {len(alignments)}")

print(alignments[0])

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
