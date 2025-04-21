# IVOL Puzzle and Arbitrage Asymmetry

This project investigates the relationship between idiosyncratic volatility (IVOL) and arbitrage activity, replicating and extending findings from Stambaugh, Yu, and Yuan (2015) using U.S. equity data from 2014–2024.

## Project Structure

- `notebooks/`: Contains Jupyter notebooks for different stages of the analysis.
- `src/`: Python scripts for reusable logic.
- `data/`: Place to store CSVs and datasets (not versioned).
- `outputs/`: Generated plots, results, etc. (optional).

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/fanghe-ma/IVOL-Puzzle-and-Arbitrage-Asymmetry.git
    cd IVOL-Puzzle-and-Arbitrage-Asymmetry
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use: venv\Scripts\activate
    ```

3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Place required data files in the `data/` folder. Data can be retrieved [here](https://penno365-my.sharepoint.com/:f:/g/personal/fanghema_upenn_edu/Emak65gizSFOtBffZSvJ4FoBmywxb2l0KyrzesDVf-XNcg?e=VdDnAN)

5. Launch JupyterLab or Jupyter Notebook to start exploring

## Tests

## Contact

For any questions, contact [fanghema@wharton.upenn.edu].