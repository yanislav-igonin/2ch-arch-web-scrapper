# 2ch-arch-web-scrapper
Script to parse all 2ch.hk **/b** archive into csv file and Jupyter Notebook to analize dat shit.

## Prerequisites
Installed conda or miniconda - link to [docs](https://docs.conda.io/en/latest/miniconda.html#).

On mac you can install it with the [brew](https://brew.sh/):
```bash
brew install --cask miniconda
```

Create environment from a file:
```bash
conda env create -f environment.yml python=3.9
```

Additional info:
  * https://code.visualstudio.com/docs/python/environments
  * https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually

> In contrast, if you fail to specify an interpreter, as with conda create --name env-00, the environment won't appear in the list.

## Run
Gather dataset:
```bash
conda activate 2ch-arch-web-scrapper
python scrapper.py
```
Clean dataset from every chuck header: `id,date,title,link`. Just replace it with empty row.

Then you can run notebook.

## Motivation
Want to roll into DS a little, so I decided to analyze 2ch threads with some metrics. Of course, firstly I need a dataset.