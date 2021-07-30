# REL-experiments

This is the code for our bachelor thesis project "Effect of Surface Form Dictionary on Effectiveness in Entity Linking" 

#### Recreating the experiments

This project relies on our modified REL to execute the experiments, which can be found    [here](https://github.com/hvwesten/REL/tree/master/REL). We mostly follow the [tutorials](https://github.com/informagi/REL/tree/master/tutorials) given in the original REL, but using our own modified version of REL.

To recreate the experiments, you should first do the setup described in the tutorial [here](https://github.com/informagi/REL/blob/master/tutorials/01_How_to_get_started.md). You can then download the ClueWeb09 and ClueWeb12 annotations, and place them in the `base_url` folder alongside `wiki_2019/` and `generic/`. Your folder structure should look something like this:

```
base_url
|----generic/
|----wiki_2019/
|----ClueWeb09/
     |---- ClueWeb09_English_1.tgz
     |---- ...
|----ClueWeb12/
     |---- ClueWeb12_English_1.tgz
     |---- ...
```

You can then execute the following steps:

0. Generate ClueWeb counts with *00\_clueweb\_to\_json.py*.

1. Create $p(e|m)$ in one of two ways:

        a) Using memory, with *01a\_generate\_pem\_clueweb.py*

        b) Using the database, with *01b\_generate\_pem\_clueweb\_using\_DB.py*

2. (Not Required) Re-create embeddings with *02_train_embeddings.py*

3. Generate the training and test files with *03_generate_train_test_files.py*

4. Train or evaluate with *04_train_eval.py*

5. End-to-end entity link with *05_e2e_entity_linking.py*

The code contains comments that should help with understanding the steps. Finally, we provide the following diagram as an overview of the various steps that we just described.


<p align="center">
  <img src="images/diagram.svg">
</p>
