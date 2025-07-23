# pip install lunr
from lunr import lunr
import json
import os
import yaml
import yaml.parser

# your docs: list of dicts with at least an 'id' and whatever fields you want searchable
docs = []

for dirpath, dirnames, filenames in os.walk("../"):
    if len(filenames) > 0 and filenames[0] == "mechanic.yaml":
        with open(os.path.join(dirpath, filenames[0])) as f:
            doc = yaml.safe_load(f)["mechanic"]
            docs.append(doc)

print(docs)

concise_docs = []

for doc in docs:
    cd = {}
    for k in ["symbol", "name", "category", "short_description"]:
        cd[k] = doc[k]

    concise_docs.append(cd)

with open("../static/concise_index.json", "w") as f:
    f.write(json.dumps(concise_docs, indent=4))
# build the index
idx = lunr(
    ref="symbol",
    fields=(
        "symbol",
        "category",
        "name",
        "short_description",
        "long_description",
        "solved_problems",
    ),
    documents=docs,
)

# serialize to JSON for the browser
with open("../static/search_index.json", "w") as f:
    json.dump(idx.serialize(), f)
