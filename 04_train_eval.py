from REL.training_datasets import TrainingEvaluationDatasets
from REL.entity_disambiguation import EntityDisambiguation

base_url = "/home/hvwesten/Projects/thesis/data/"
wiki_version = "wiki_2019"

datasets = TrainingEvaluationDatasets(base_url, wiki_version).load()

# model_pth = f"{base_url}/{wiki_version}/baseline_cw_5/model"
# model_pth = f"{base_url}/{wiki_version}/baseline_cw_6/model"
# model_pth = f"{base_url}/{wiki_version}/baseline_cw_7/model"
# model_pth = f"{base_url}/{wiki_version}/baseline_cw_8/model"
# model_pth = f"{base_url}/{wiki_version}/baseline_cw_9/model"

# model_pth = f"{base_url}/{wiki_version}/baseline_cw_10/model"
# model_pth = f"{base_url}/{wiki_version}/baseline_cw_11/model"
# model_pth = f"{base_url}/{wiki_version}/baseline_cw_12/model"
# model_pth = f"{base_url}/{wiki_version}/baseline_cw_13/model"
model_pth = f"{base_url}/{wiki_version}/baseline_cw_14/model"

config = {
    "mode": "eval",
    "model_path": model_pth,
    # "dev_f1_change_lr": 0.88,
    # "model_path":  "ed-wiki-2019"
}

model = EntityDisambiguation(base_url, wiki_version, config)

if config["mode"] == "train":
    model.train(
        datasets["aida_train"], {k: v for k, v in datasets.items() if k != "aida_train"}
    )
else:
    model.evaluate({k: v for k, v in datasets.items() if "train" not in k})




# model_path_lr = "{}/{}/generated/".format(base_url, wiki_version)

# model_path_lr = f"{base_url}/{wiki_version}/baseline/"


# model.train_LR(
#     datasets,
#     model_path_lr
# )
