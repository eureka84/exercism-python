import string

nucleotide_map = dict([
    ('C', 'G'),
    ('G', 'C'),
    ('T', 'A'),
    ('A', 'U')
])


def to_rna(dna_strand):
    rna_sequence = map(lambda n: nucleotide_map[n], list(dna_strand))
    return string.join(rna_sequence, "")
