## Exploration v0.8 Notebook

### Introduction
This Jupyter notebook, `Exploration_v0.8.ipynb`, is designed to provide an in-depth exploration of dementia classificaiton. It includes a series of analyses, visualizations, and model training examples to offer comprehensive insights into dementia classification.

### Installation

To run this notebook, you will need to set up a Python environment and install specific packages. Follow these steps:

1. Ensure you have Python 3.x installed.
2. Install Jupyter by running `pip install jupyter`.
3. Navigate to the notebook directory and launch Jupyter Notebook by running `jupyter notebook`.
4. Open `Exploration_v0.8.ipynb` from the Jupyter interface.


### Features

This notebook includes:

- Detailed data preprocessing and EDA steps.
- Machine learning model examples, including training and evaluation.
- Visualization examples using Matplotlib and Seaborn.


### Dependencies

This project relies on the following libraries:

- Numpy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

Ensure you install these by running `pip install numpy pandas matplotlib seaborn scikit-learn`.

### Contributing

Contributions to improve `Exploration_v0.8.ipynb` are welcome. Please submit a pull request or open an issue to discuss your suggestions.




## Dementia Detection Using Deep Learning

### Overview

This project aims to leverage deep learning models for the early detection of dementia from cognitive test scores and brain imaging data. We employ various neural network architectures, including multi-layer perceptrons (MLP) and ResNet models, to classify individuals based on their likelihood of having dementia.

### Getting Started

### Prerequisites

1. Python 3.x
2. PyTorch
3. CUDA (for GPU acceleration)
4. Other Python libraries specified in requirements.txt

### Installation

1. Install the required Python packages:

Example:
```
pip install -r requirements.txt
```

### Data Preparation
Ensure your data is organized correctly. The project expects an Excel file named practical_data.xlsx for processing in the dementia_dataset.py script.

### Running the Experiments
To run the experiments, execute the run_exp.bash script from the terminal:

Example:
```
bash run_exp.bash
```
This script sets up the necessary environment variables and runs the main_ce.py script with predefined settings.

### Running main_ce.py
To run the main_ce.py, execute:
Example:
```
python main_ce.py --print_freq 20 \
                  --save_freq 100 \
                  --batch_size 128 --num_workers 4 --epochs 100 --seed 123 --learning_rate 0.001 --lr_decay_epochs "10,20,30" --lr_decay_rate 0.5 --weight_decay 5e-4 --momentum 0.95 \
                  --model resnet50 --dataset dementia \
                  --first_layer_size 256 --second_layer_size 1024 --third_layer_size 256 --cosine --trial "experiment1" \
                  --enable_wandb
```
- print_freq 20: Print training status every 20 batches.
- save_freq 100: Save the model every 100 batches.
- batch_size 128: Set the batch size to 128.
- num_workers 4: Use 4 worker processes to load data.
- epochs 100: Train for a total of 100 epochs.
- seed 123: Set the random seed to 123 to ensure reproducibility.
- learning_rate 0.001: Set the initial learning rate to 0.001.
- lr_decay_epochs "10,20,30": Lower the learning rate at the 10th, 20th, and 30th epochs.
- lr_decay_rate 0.5: The factor by which the learning rate decays.
- weight_decay 5e-4: Set weight decay to 0.0005.
- momentum 0.95: Set momentum to 0.95.
- model resnet50: The model used is resnet50.
- dataset dementia: The dataset used is dementia.
- first_layer_size 256: Set the size of the first layer to 256.
- second_layer_size 1024: Set the size of the second layer to 1024.
- third_layer_size 256: Set the size of the third layer to 256.
- cosine: Use cosine annealing to adjust the learning rate.
- trial "experiment1": The identifier for the experiment is "experiment1".
- enable_wandb: Enable Weights & Biases for experiment tracking.

### Project Structure
- main_ce.py: The main Python script that orchestrates model training, evaluation, and testing.
- resnet_big.py: Defines the ResNet model architectures adapted for the project.
- mlp.py: Contains the definitions of Multi-Layer Perceptron (MLP) models used in the experiments.
- dementia_dataset.py: A custom PyTorch dataset module for loading and preprocessing the dementia dataset.
- run_exp.bash: A bash script for setting environment variables and running the experiments.


### Models
We explore the use of two primary models in this project:

- Three Layers MLP: A three-layer Multi-Layer Perceptron designed for tabular data.
- Five Layers MLP: A five-layer Multi-Layer Perceptron designed for tabular data.
- ResNet Variants: Adaptations of the ResNet model for one-dimensional data processing.
- LLM: Utilize the advanced capabilities of GPT-4 to encode the data.

### Custom Dataset
The DementiaDataset class in dementia_dataset.py handles the loading, splitting, and preprocessing of the dementia dataset. It is designed to work seamlessly with PyTorch's DataLoader for efficient training and evaluation.

### Results
The results of the experiments, including model accuracy and loss metrics, are logged to TensorBoard and Weights & Biases for visualization and analysis.


## Acknowledgement



## License
This project is licensed under the license found in the LICENSE file in the root directory of this source tree.

[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct)

