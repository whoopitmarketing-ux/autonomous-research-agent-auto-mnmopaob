# Autonomous Research Agent

[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-lightgrey.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html)

## Table of Contents

*   [Overview](#overview)
*   [Features](#features)
*   [File Structure](#file-structure)
*   [Installation](#installation)
*   [Usage](#usage)

## Overview

The Autonomous Research Agent is a self-hostable AI second brain that allows you to get answers from the web or your documents, build custom agents, schedule automations, and do deep research. You can turn any online or local LLM into your personal, autonomous AI.

## Features

*   Get answers from the web or your documents
*   Build custom agents
*   Schedule automations
*   Do deep research
*   Turn any online or local LLM into your personal, autonomous AI
*   Support for multiple search models
*   Support for GIN indexes

## File Structure

```
khoj/
database/
management/
commands/
change_default_model.py
...
migrations/
0003_vector_extension.py
0005_embeddings_corpus_id.py
...
models.py
adapters.py
...
processor/
embeddings.py
...
requirements.txt
README.md
```

## Installation

1.  Clone the repository: `git clone https://github.com/your-username/khoj.git`
2.  Install the dependencies: `pip install -r requirements.txt`
3.  Run the migrations: `python manage.py migrate`

## Usage

1.  Run the `change_default_model` command to update the `search_model` field of all `Entry` objects to use the new default search model: `python manage.py change_default_model`
2.  Use the `EmbeddingsModel` to embed input IDs: `embeddings_model = EmbeddingsModel(128); embedded_input_ids = embeddings_model(input_ids)`

## License

This project is licensed under the AGPL-3.0 license.

## Built with AI assistance on 2026-04-06