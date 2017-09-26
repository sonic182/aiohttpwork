
[![Build Status](https://travis-ci.org/{{cookiecutter.project_repo}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.project_repo}})
[![Coverage Status](https://coveralls.io/repos/github/{{cookiecutter.project_repo}}/badge.svg?branch=master)](https://coveralls.io/github/{{cookiecutter.project_repo}}?branch=master)
# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

# Development

Install packages with pip-tools:
```bash
pip install pip-tools
pip-compile
pip-compile dev-requirements.in
pip-sync requirements.txt dev-requirements.txt
```

# Contribute

1. Fork
2. create a branch `feature/your_feature`
3. commit - push - pull request

Thanks :)
