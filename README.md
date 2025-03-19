# cit-qr-builder
Easily create QR codes for users in [cit](https://github.com/ITvitae/cit)'s users.txt

## Quickstart

```bash
python build_codes.py ./users.txt ./output --scale 50
```

## Setup

### Virtual environment and requirements

Set up an environment, we'll use one named `env3`, and install `requirements.txt`.

> We assume a Python install under `python3`.

```bash
python3 -m venv env3
source env3/bin/activate
pip install -r requirements.txt
```

> See `requirements.txt` for dependencies and required external libraries.

## Running

Make sure you have a correctly formatted configuration file (such as `users.txt`).
The example assumes `users.txt`.

Create a directory to store your output.
The example assumes `output/`.

Make sure your environment is active and then proceed to run:

```bash
python build_codes.py ./users.txt ./output --scale 50
```
