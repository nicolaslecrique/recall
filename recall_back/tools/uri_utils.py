import re
import hashlib
from typing import List

from unidecode import unidecode

letters_numbers_regex = re.compile('[^A-Za-z0-9-]+')
space_regex= re.compile(' +')
sha = hashlib.sha256()
readable_uri_part_size = 60  # too long uri are bad for SEO
hashed_uri_part_size = 12  # // 12 exa = 48 bits; proba collision is 1e-11 with 100 entries. cf. "birthday paradoxe"


def generate_uri(str_to_clean: str, to_hash_to_ensure_uniqueness: List[str] = []) -> str:
    ascii_version: str = unidecode(str_to_clean).lower()
    without_space = space_regex.sub('-', ascii_version)
    letters_numbers: str = letters_numbers_regex.sub('', without_space)
    shortened: str = letters_numbers[0:readable_uri_part_size]

    sha.update(str_to_clean.encode())
    for s in to_hash_to_ensure_uniqueness:
        sha.update(s.encode())
    sha_digest = sha.hexdigest()

    return shortened + "-" + sha_digest[:hashed_uri_part_size]

