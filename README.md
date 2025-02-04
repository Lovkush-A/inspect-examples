# Inspect examples

This repo contains simple self-contained examples of how to use UK AISI's `inspect` package.

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

Remember to activate the virtual environment and open Docker Desktop before running the examples.

- Run the example, e.g. for `example1.py`:

```bash
inspect eval example1.py --model openai/gpt-4o-mini
```

- View the created logs. Following command automatically selects the latest log file:

```bash
inspect view
```

## Explanation of the examples

- `example1.py`: Example of question answering, with chain of thought. No agents.
- `example2.py`: Example of agent with tool use, where agent has access to bash and python to help with the task. Still question answering.
- `example3.py`: Example of agent with tool use and access to files. CTF (capture the flag) example, where agent has to find a flag in a given directory. Simplified version of [the example](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/gdm_capabilities/intercode_ctf) that Inspect points to in [their documentation](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/gdm_capabilities/intercode_ctf).
- `example4.py`: Example of agent with tool use and access to files. Simplified version of example3 as the task is more straightforward (find the 3rd word in a text file).
