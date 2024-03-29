import numpy as np
from sklearn.model_selection import train_test_split

from pipeline import titanic_pipe
from config.core import config
from processing.data_management import (
    load_dataset,
    save_pipeline
)

def run_training() -> None:

    data = load_dataset(file_name=config.app_config.training_data_file)

    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state
    )

    titanic_pipe.fit(X_train[config.model_config.features], y_train)

    save_pipeline(pipeline_to_persist=titanic_pipe)

if __name__ == "__main__":
    run_training()