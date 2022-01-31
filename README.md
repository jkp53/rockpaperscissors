# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage (including player customization)

Set a custom playere name by changing the name in the quotation marks and run the rock paper scissors game with the following code:

```sh
PLAYER_NAME="Jon Snow" python game.py
```

## Testing

Run tests:

```sh
pytest
```
