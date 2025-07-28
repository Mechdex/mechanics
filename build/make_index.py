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

        print(f"Completed {doc['symbol']}.")

concise_docs = []
symbol_set = []

try:
    for doc in docs:
        with open("compiled.txt", "a") as f:
            json.dump(doc, f, indent=4)
            f.write("\n\n")
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
except Exception as e:
    print("Error with document:")
    print(doc)
    print(e)
    exit(1)

with open("../static/concise_index.json", "w") as f:
    f.write(json.dumps(concise_docs, indent=4))
print("Wrote concise docs.")


def extract_solved_problems(doc):
    texts = []
    sp = doc.get("solved_problems", [])
    if isinstance(sp, str):
        texts.append(sp)
    elif isinstance(sp, dict):
        # handle legacy object (mapping) format
        for k, v in sp.items():
            texts.append(str(k))
            texts.append(str(v))
    elif isinstance(sp, list):
        for item in sp:
            if isinstance(item, str):
                texts.append(item)
            elif isinstance(item, dict):
                texts.append(item.get("title", ""))
                texts.append(item.get("description", ""))
    return " ".join(texts)


def extract_examples(doc):
    texts = []
    ex = doc.get("examples", [])
    if isinstance(ex, str):
        texts.append(ex)
    elif isinstance(ex, list):
        for item in ex:
            if isinstance(item, str):
                texts.append(item)
            elif isinstance(item, dict):
                texts.append(item.get("title", ""))
                texts.append(item.get("description", ""))
    return " ".join(texts)


idx = lunr(
    ref="symbol",
    fields=[
        {"field_name": "symbol", "boost": 2},
        {"field_name": "name", "boost": 10},
        {"field_name": "category", "boost": 5},
        {"field_name": "short_description", "boost": 4},
        {"field_name": "long_description", "boost": 2},
        {
            "field_name": "solved_problems",
            "boost": 3,
            "extractor": extract_solved_problems,
        },
        {"field_name": "examples", "boost": 1, "extractor": extract_examples},
    ],
    documents=docs,
)


# serialize to JSON for the browser
with open("../static/search_index.json", "w") as f:
    json.dump(idx.serialize(), f)
