# Salary Prediction Web App

This is a simple web application for predicting salaries based on years of experience using a linear regression model. The app is built using Streamlit and provides an interactive interface for data visualization and salary prediction.

## Features

- View the salary data table
- Interactive and non-interactive data visualization
- Predict salaries based on years of experience
- Contribute new data points to the dataset

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kunal5711/Salary-Prediction.git
    cd Salary-Prediction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and go to `http://localhost:8501` to access the app.

## File Structure

- `app.py`: The main script for running the Streamlit app.
- `Salary_data.csv`: The dataset containing years of experience and corresponding salaries.
- `requirements.txt`: The list of required Python packages.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.
