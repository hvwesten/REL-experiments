from urllib.parse import unquote
import json
import os

import tarfile
from mapping.freebasewikimapper import FreebaseWikipediaMapper
from REL.wikipedia import Wikipedia

'''
    Program that processes an entire ClueWeb dataset (as .tgz files)
    and saves the mentions, entities and the counts into a JSON file
    Needs REL to be installed (https://github.com/informagi/rel)
'''

clueweb_dict = {}

def process_clueweb(wikipedia, mapper, clueweb_url):

    # clueweb_dict = {}
    lines_read = 0

    from time import time
    start = time()

    # Loop through all the clueweb files, process them and add the
    # counts to a dictionary
    for _, _, files in os.walk(clueweb_url):
        for fn in files:
            if fn.endswith('.tgz'):
                file_path = os.path.join(clueweb_url, fn)
                print(f"file_path: {file_path}")
                with tarfile.open(file_path, 'r:gz') as tf:
                    for entry in tf:
                        if entry.name.endswith('.tsv'):
                            f = tf.extractfile(entry)
                            for l in f:
                                lines_read += 1
                                if lines_read % 5000000 == 0:
                                    print(
                                        f"Processed {lines_read} lines in {time()-start}")
                                    start = time()
                                    
                                line = str(l, 'utf-8')
                                line = line.rstrip()
                                line = unquote(line)
                                parts = line.split('\t')
                                mention = parts[2]
                                entity_mid = parts[7]

                                entity = mapper.get_title(entity_mid)

                                # Process said wikipedia title
                                ent_name = wikipedia.preprocess_ent_name(
                                    entity)

                                if ent_name in wikipedia.wiki_id_name_map["ent_name_to_id"]:
                                    if mention not in clueweb_dict:
                                        clueweb_dict[mention] = {}

                                    ent_name = ent_name.replace(" ", "_")

                                    if ent_name not in clueweb_dict[mention]:
                                        clueweb_dict[mention][ent_name] = 0
                                    clueweb_dict[mention][ent_name] += 1

if __name__ == "__main__":
    # Modify to your base_url and wiki version
    base_url = "/home/hvwesten/Projects/thesis/data/"
    wiki_version = "wiki_2019"
    wikipedia = Wikipedia(base_url, wiki_version)

    # Modify to location(s) where you saved the ClueWeb data
    clueweb09_url = '../data/ClueWeb09/'
    clueweb12_url = '../data/ClueWeb12/'

    # Modify to location where you want to save your output
    out_url = './save_folder/00_clueweb_full_9_12.json'

    # Move index to base_url, or modify this line
    mapper = FreebaseWikipediaMapper('.', 'index_enwiki-20190420.db')

    print("Calculating Clueweb mention/entity occurrences")

    # Get the clueweb counts and save them in a .json file
    process_clueweb(wikipedia, mapper,  clueweb09_url)
    process_clueweb(wikipedia, mapper,  clueweb12_url)

    # Save the file to the output location
    with open(out_url, 'w') as outfile:
        json.dump(clueweb_dict, outfile)