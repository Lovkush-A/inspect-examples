import hashlib
from inspect_ai.model import ChatMessageUser
from inspect_ai.dataset import Sample, MemoryDataset
from inspect_ai import Task, task
from inspect_ai.scorer import includes
from inspect_ai.solver import basic_agent
from inspect_ai.tool import bash, python


# manually create a dataset
dataset_list_of_dict = [
    {
        "prompt": "Calculate the SHA-256 hash of the string 'aisc'",
        "answer": hashlib.sha256("aisc".encode()).hexdigest(),
    },
    {
        "prompt": "What is the capital of France?",
        "answer": "Paris",
    },
]

# convert to Dataset object, via a list of Sample objects
sample_list = [
    Sample(
        input=[ChatMessageUser(content=sample["prompt"])],
        target=sample["answer"],
    )
    for sample in dataset_list_of_dict
]

dataset = MemoryDataset(sample_list)


@task
def basic_agent_task():
    return Task(
        dataset=dataset,
        solver=basic_agent(
            tools=[bash(timeout=180), python(timeout=180)],
            max_attempts=2,
            message_limit=10,
        ),
        scorer=includes(),
        sandbox="docker",
    )