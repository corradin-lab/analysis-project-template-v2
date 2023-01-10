import os

toml_template = \
"""
[tool.poetry]
name = "{project_name}"
version = "0.1.0"
description = "{project_description}"
authors = ["{author_username}"]

[tool.poetry.dependencies]
python = ">=3.8,<3.11"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
"""

key_val_dict = {}
with open("copier-answers.yaml") as file:
    for line in file.readlines():
        if len(line.split(":")) == 2:
            key_val = [ele.strip() for ele in line.strip().split(":")]
            key_val_dict[key_val[0]] = key_val[1]

#print(key_val_dict)
#print(toml_template)
with open("pyproject.toml", "w") as file:
    file.write(toml_template.format(**key_val_dict))


            
