import gzip, re, os, json
from wikimapper import WikiMapper

"""
Class responsible for mapping Freebase ids to Wikipedia titles.
Uses the wikimapper (https://github.com/jcklie/wikimapper)
"""

class FreebaseWikipediaMapper:
    def __init__(self, base_url, wikimapper_path):
        self.mapping_folder = os.path.join(base_url, 'mapping/data')
        self.fb2w_url = os.path.join(self.mapping_folder, 'fb2w.nt.gz')  # Freebase to Wikidata file
        self.wikimapper_url = os.path.join(self.mapping_folder, wikimapper_path) 
        self.wikimapper = WikiMapper(self.wikimapper_url) # Mapper from Wikidata to Wikipedia
        self.mapping_dict = self.__create_fb2wp_dict() 

    def __create_fb2wp_dict(self):
        lines_read = 0
        fb2wp_dict = {}
        fb2wp_save_file = os.path.join(self.mapping_folder, 'fb2wp_dict.json')

        if os.path.isfile(fb2wp_save_file):
            print("Loading Freebase to Wikipedia mapping dictionary")
            with open(fb2wp_save_file, 'r') as f:
                fb2wp_dict = json.load(f)
        else:
            print("Creating Freebase to Wikipedia mapping dictionary")
            with gzip.open(self.fb2w_url, 'rt') as f:
                fb_regex = re.compile('<http://rdf.freebase.com/ns(.*)>')
                wd_regex = re.compile('<http://www.wikidata.org/entity/(.*)>')

                for line in f:  
                    lines_read += 1
                    if lines_read % 100000 == 0:
                        print("Processed {} lines".format(lines_read))
                        break

                    if line.startswith('#') or lines_read == 4:
                        pass
                    else:
                        line = line.strip()
                        parts = line.split('\t')
                        
                        fb_url = parts[0]
                        fb_id = fb_regex.match(fb_url).group(1).replace('.', '/')

                        wd_url = parts[2]
                        wd_id = wd_regex.match(wd_url).group(1)

                        # Get wikipedia titles for wikidata ID using wikimapper
                        wp_titles = self.wikimapper.id_to_titles(wd_id)
                
                        fb2wp_dict[fb_id] = {wd_id: wp_titles}
            
            # Save the dictionary in a json file for future experiments
            with open(fb2wp_save_file, 'w') as f:
                json.dump(fb2wp_dict, f)
        return fb2wp_dict

    def get_title(self, freebase_id):
        
        if freebase_id in self.mapping_dict:
            results = list(self.mapping_dict[freebase_id].values())[0]
            if len(results) > 0:
                return results[0] # return first candidate of the wikipedia titles
  
        return "<>"


if __name__ == "__main__":
    base_url = ""
    fbwikimapper = FreebaseWikipediaMapper(base_url, 'index_enwiki-20190420.db')

    print(fbwikimapper.get_title('/m/0695j'))


