from inspect_ai.dataset import Sample, Dataset, json_dataset
from inspect_ai import Task, task
from inspect_ai.scorer import includes
from inspect_ai.solver import basic_agent
from inspect_ai.tool import bash, python

from pathlib import Path
from textwrap import dedent
import os
from glob import glob

def read_dataset() -> Dataset:
    # ensure the data directory exists
    DATA_DIR = Path(__file__).parent / "word_finder"
    
    def record_to_sample(record: dict) -> Sample:
        task_id = record["task_id"]
        task_id_folder = DATA_DIR / "task_assets" / str(task_id)

        task_id_files = [
            os.path.relpath(file, DATA_DIR)
            for file in glob(f"{task_id_folder}/*")
            if os.path.isfile(file)
        ]
        files = {os.path.basename(file): file for file in task_id_files}

        # Format prompt
        input = dedent("""
        Your objective is to find the third word in the text file.
        
        Task: First find the file 'text.txt' then return just the third word.
        """)

        return Sample(
            id=task_id,
            input=input,
            target=record["answer"],
            files=files,
        )

    return json_dataset(
        json_file=f"{DATA_DIR}/word_finder.json",
        sample_fields=record_to_sample,
    )

dataset = read_dataset()


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

if __name__ == "__main__":
    read_dataset() 