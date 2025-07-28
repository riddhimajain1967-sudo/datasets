import pandas as pd
import requests

def load_dataset(dataset_name):
    """
    Load a dataset from the MasteriNeuron/datasets GitHub repository.
    
    Args:
        dataset_name (str): Name of the dataset (e.g., 'titanic', 'diabetes').
    
    Returns:
        pandas.DataFrame: The loaded dataset.
    
    Raises:
        ValueError: If the dataset cannot be loaded.
    """
    valid_datasets = [
        "BBC News Train",
        "Fertilizer Prediction",
        "Waste_Management_and_Recycling_India",
        "diabetes",
        "flight_price",
        "googleplaystore",
        "hr_analytics",
        "pima-indians-diabetes",
        "titanic"
    ]
    
    if dataset_name not in valid_datasets:
        raise ValueError(f"Dataset '{dataset_name}' not found. Available datasets: {valid_datasets}")
    
    # Map user-friendly names to actual file names
    file_mapping = {
        "BBC News Train": "BBC News Train.csv",
        "Fertilizer Prediction": "Fertilizer Prediction.csv",
        "Waste_Management_and_Recycling_India": "Waste_Management_and_Recycling_India.csv",
        "diabetes": "diabetes.csv",
        "flight_price": "flight_price.csv",
        "googleplaystore": "googleplaystore.csv",
        "hr_analytics": "hr_analytics.csv",
        "pima-indians-diabetes": "pima-indians-diabetes.csv",
        "titanic": "titanic.csv"
    }
    
    base_url = "https://raw.githubusercontent.com/MasteriNeuron/datasets/main/"
    url = f"{base_url}{file_mapping[dataset_name]}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        df = pd.read_csv(url)
        return df
    except Exception as e:
        raise ValueError(f"Failed to load dataset '{dataset_name}': {str(e)}")
