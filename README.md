# IVOL Puzzle and Arbitrage Asymmetry

This project investigates the relationship between idiosyncratic volatility (IVOL) and arbitrage activity, extending findings from Stambaugh, Yu, and Yuan (2015) using U.S. equity data from 1965–2024. This project confirms the persistence of a negative IVOL effect by looking at positive abnormal returns on a IVOL long/short strategy. This project confirms the persistence of arbitrage asymmetry by using a basket of 9 return anomalies (a slight modification to Stambaugh, Yu and Yuan's original 11) as proxy for mispricing, and finding that 1) degree of mispricing is greater for stocks with higher IVOL and 2) more underpricing is arbitraged away than overpricing. 

## Project Structure

- `Notebooks/`: Contains Jupyter notebooks for different stages of the analysis.
- `Data/`: Place to store CSVs and datasets (not versioned).
- `src/`: Python scripts for reusable logic. Will be updated soon.

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

4. Place required data files in the `Data/` folder. Data can be retrieved [here](https://penno365-my.sharepoint.com/:f:/g/personal/fanghema_upenn_edu/Emak65gizSFOtBffZSvJ4FoBmywxb2l0KyrzesDVf-XNcg?e=VdDnAN). 

5. Launch JupyterLab or Jupyter Notebook to start exploring.

## Contact

For any questions, contact [fanghema@wharton.upenn.edu].
