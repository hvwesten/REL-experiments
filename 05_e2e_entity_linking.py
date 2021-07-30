from http.server import HTTPServer

from REL.entity_disambiguation import EntityDisambiguation
from REL.ner import Cmns, load_flair_ner
from REL.server import make_handler

wiki_version = "wiki_2019"
base_url = "/home/hvwesten/Projects/thesis/data/"

# These are all the same paths we used to save our models

model_path = f"{base_url}/{wiki_version}/baseline_cw_5/model"

# model_path = f"{base_url}/{wiki_version}/baseline_cw_7/model"
# model_path = f"{base_url}/{wiki_version}/baseline_cw_9/model"
# model_path = f"{base_url}/{wiki_version}/baseline_cw_14/model"


config = {
    "mode": "eval",
    "model_path": model_path,
}

model = EntityDisambiguation(base_url, wiki_version, config)

# Using Flair:
tagger_ner = load_flair_ner("ner-fast")

# Alternatively, using n-grams:
# tagger_ngram = Cmns(base_url, wiki_version, n=5)

server_address = ("127.0.0.1", 5555) # was 1235
server = HTTPServer(
    server_address,
    make_handler(
        base_url, wiki_version, model, tagger_ner
    ),
)

try:
    print("Ready for listening.")
    server.serve_forever()
except KeyboardInterrupt:
    exit(0)


# IP_ADDRESS = "http://localhost"
# PORT = "1235"
# text_doc = "If you're going to try, go all the way - Charles Bukowski"

# document = {
#     "text": text_doc,
#     "spans": [],  # in case of ED only, this can also be left out when using the API
# }


# # # Example ED.
# # document = {
# #     "text": text_doc,
# #     "spans": [(41, 16)]
# # }

# API_result = requests.post("{}:{}".format(IP_ADDRESS, PORT), json=document).json()

# print(API_result)
