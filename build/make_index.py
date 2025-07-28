# pip install lunr
from lunr import lunr
import json
import os
import yaml

docs = []

for dirpath, dirnames, filenames in os.walk("../"):
    if len(filenames) > 0 and filenames[0] == "mechanic.yaml":
        with open(os.path.join(dirpath, filenames[0])) as f:
            doc = yaml.safe_load(f)["mechanic"]
            docs.append(doc)

concise_docs = []
symbol_set = []

for doc in docs:
    cd = {}
    if doc["symbol"] in symbol_set:
        print(
            f"Validation failed! {doc['symbol']} from {doc['name']} is used in multiple places."
        )
        exit(1)

    symbol_set.append(doc["symbol"])
    for k in ["symbol", "name", "category", "short_description"]:
        cd[k] = doc[k]

    concise_docs.append(cd)

with open("../static/concise_index.json", "w") as f:
    f.write(json.dumps(concise_docs, indent=4))
print("Wrote concise docs.")

idx = lunr(
    ref="symbol",
    fields=[
        {"field_name": "symbol", "boost": 2},
        {"field_name": "name", "boost": 10},
        {"field_name": "category", "boost": 5},
        {"field_name": "short_description", "boost": 4},
        {"field_name": "long_description", "boost": 2},
        {"field_name": "solved_problems", "boost": 1},
    ],
    documents=docs,
)


# serialize to JSON for the browser
with open("../static/search_index.json", "w") as f:
    json.dump(idx.serialize(), f)
