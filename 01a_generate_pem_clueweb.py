'''
    Based on:
    Generating p(e|m) index
    https://github.com/informagi/REL/blob/master/scripts/code_tutorials/generate_p_e_m.py

'''

from REL.wikipedia import Wikipedia
from REL.wikipedia_yago_freq import WikipediaYagoFreq

import json

wiki_version = "wiki_2019"
base_url = "/home/hvwesten/Projects/thesis/data/"

# Open file with clueweb counts, choose between ClueWeb09 or ClueWeb09+12
input_url = './save_folder/00_clueweb_full_9.json'
# input_url = './save_folder/00_clueweb_full_9_12.json'

print(f"input_url: {input_url}")

with open(input_url, 'r') as f:
    clueweb_dict = json.load(f)

# Import helper functions; store p(e|m) index etc in class.
print("Loading wikipedia files")
wikipedia = Wikipedia(base_url, wiki_version)

# Init class
wiki_yago_freq = WikipediaYagoFreq(base_url, wiki_version, wikipedia)


# All the different configurations, uncomment the one you want to use
'''
Baseline:
    Compute Wiki+Crosswiki with YAGO p(e|m)
'''
wiki_yago_freq.compute_wiki()
wiki_yago_freq.compute_custom()

'''
# 1. W + CW + C9 (+ C12):
    Compute Wiki+Crosswiki with Clueweb p(e|m)
'''
# wiki_yago_freq.compute_wiki()
# wiki_yago_freq.compute_custom(clueweb_dict)

'''
# 2. W + C9 (+ C12) + Y:
    Compute Wiki+Clueweb and YAGO p(e|m)
'''
# wiki_yago_freq.compute_wiki(custom_add=clueweb_dict)
# wiki_yago_freq.compute_custom()

'''
# 3. W + CW + C9 (+ C12) + Y :
   Compute WIKI + CROSSWIKI + CLUE  and YAGO (= ALL)
'''
# wiki_yago_freq.compute_wiki(special_case="all", custom_main=clueweb_dict)
# wiki_yago_freq.compute_custom()


'''
# 4. CW + C9 (+ C12) +  Y:
   Compute Cross+Clueweb and YAGO p(e|m)
'''
# wiki_yago_freq.compute_wiki(custom_main=clueweb_dict)
# wiki_yago_freq.compute_custom()


'''
# 5. CW + C9 (+ C12) :
   Compute Cross and Clue
'''
# wiki_yago_freq.compute_wiki(special_case="only_crosswiki")
# wiki_yago_freq.compute_custom(clueweb_dict)


'''
# 6. C9 (+ C12) + Y:
    Just Clueweb9_12+YAGO or Clueweb9+YAGO
'''
# wiki_yago_freq.compute_wiki(special_case="only_clueweb", custom_main=clueweb_dict)
# wiki_yago_freq.compute_custom()


'''
# 7. C9 (+ C12):
    Just Clueweb9_12 or ClueWeb9
'''
# wiki_yago_freq.compute_wiki(special_case="only_clueweb", custom_main=clueweb_dict)


# Store dictionary in sqlite3 database
wiki_yago_freq.store()