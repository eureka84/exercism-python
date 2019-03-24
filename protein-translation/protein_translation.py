from itertools import takewhile

aminoAcidsDictionary = dict([
    ("AUG", "Methionine"),
    ("UUU", "Phenylalanine"),
    ("UUC", "Phenylalanine"),
    ("UUA", "Leucine"),
    ("UUG", "Leucine"),
    ("UCU", "Serine"),
    ("UCC", "Serine"),
    ("UCA", "Serine"),
    ("UCG", "Serine"),
    ("UAU", "Tyrosine"),
    ("UAC", "Tyrosine"),
    ("UGU", "Cysteine"),
    ("UGC", "Cysteine"),
    ("UGG", "Tryptophan"),
    ("UAA", "STOP"),
    ("UAG", "STOP"),
    ("UGA", "STOP")
])


def proteins(strand):
    codons = split_every_n_chars(strand, 3)
    candidate_sequence = map(lambda c: parse_codon(c), codons)
    return list(takewhile(lambda a: a != "STOP", candidate_sequence))


def split_every_n_chars(string, n):
    return [str(string[i:i + n]) for i in range(0, len(string), n)]


def parse_codon(strand):
    return aminoAcidsDictionary[strand]