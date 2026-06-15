# bioinformatics-start

Small scripts as I learn bioinformatics and Python.

## protein_charge_calculator.py
Calculates the net charge of a protein sequence by counting K/R 
(positive) and D/E (negative) residues, to check whether a 
sequence looks like a histone.

## blast_search.py
Sends a protein sequence (part of Zika virus protein) to NCBI BLAST 
and saves the results as XML.

## blast_parse_results.py
Reads the BLAST XML output and prints the top hits.