# Inspect examples

This repo contains simple self-contained examples of how to use the `inspect` package.

## Installation and setup

- Create virtual environment. E.g. using conda:

```bash
conda create -n inspect-examples python
```

- Activate the virtual environment:

```bash
conda activate inspect-examples
```

- Install the requirements:

```bash
pip install -r requirements.txt
```

- Create .env file in the root directory with the following content:

```
OPENAI_API_KEY=<your_openai_api_key>
```

- Install and open Docker Desktop

## How to run an example

- Run the example, e.g. for `example1.py`:

```bash
inspect eval example1.py --model openai/gpt-4o-mini
```

- View the created logs. Following command automatically selects the latest log file:

```bash
inspect view
```

## Explanation of the examples

- `example1.py`: Basic example of question answering, with chain of thought.
- `example2.py`: Basic tool use example, where agent has access to bash and python to help with the task. Still question answering.
