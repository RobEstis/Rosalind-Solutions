#!/usr/bin/env python3
"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u
 is formed by replacing all occurrences of 'T' in t
 with 'U' in u.

Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t.

Time Complexity: O(n)
Space Complexity: O(n)
"""

import sys


def transcribe_dna_to_rna(dna: str) -> str:
    """
    Convert a DNA coding strand into its RNA equivalent.

    Parameters
    ----------
    dna : str
        DNA string consisting of characters A, C, G, T.

    Returns
    -------
    str
        RNA string with all 'T' replaced by 'U'.
    """
    return dna.replace("T", "U")


def main() -> None:
    """
    Read DNA string from standard input and print RNA transcription.
    """
    dna_input = sys.stdin.read().strip()
    rna_output = transcribe_dna_to_rna(dna_input)
    print(rna_output)


if __name__ == "__main__":
    main()
