'''
    Use database to generate p(e|m)
    Based on:
    Generating p(e|m) index
    https://github.com/informagi/REL/blob/master/scripts/code_tutorials/generate_p_e_m.py

'''

from REL.wikipedia import Wikipedia
from REL.wikipedia_yago_freq_DB import WikipediaYagoFreq

import json

wiki_version = "wiki_2019"
base_url = "/home/hvwesten/Projects/thesis/data/"
input_url = './save_folder/00_clueweb_full.json'


# Open file with clueweb counts
with open(input_url, 'r') as f:
    clueweb_dict = json.load(f)


# Import helper functions; store p(e|m) index etc in class.
print("Loading wikipedia files")
wikipedia = Wikipedia(base_url, wiki_version)

# Init class
wiki_yago_freq = WikipediaYagoFreq(base_url, wiki_version, wikipedia)

# Compute Wiki+Crosswiki with YAGO p(e|m)
wiki_yago_freq.compute_wiki_with_db()
wiki_yago_freq.compute_custom_with_db()

# Compute Wiki+Crosswiki with Clueweb p(e|m)
# wiki_yago_freq.compute_wiki_with_db()
# wiki_yago_freq.compute_custom_with_db(clueweb_dict)


# Store dictionary in sqlite3 database
wiki_yago_freq.store()
