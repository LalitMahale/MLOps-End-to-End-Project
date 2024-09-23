import os
from pathlib import Path
import logging

list_file = [
    ".github/workflow/.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_validation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    'src/pipeline/prediction_pipeline.py',
    "src/logger/logging.py",
    "src/exception/exception.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    'requirements_dev.txt',
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"
]


for file in list_file:
    file_path = Path(file)
    folder, filename = os.path.split(file_path)
    if folder != "":
        os.makedirs(folder, exist_ok=True)
        logging.info(f"Created folder {folder} for {filename}")

    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            pass
