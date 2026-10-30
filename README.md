# SpaceX Falcon 9 First-Stage Landing Prediction
Runnable starter project for the IBM Applied Data Science Capstone.

**Important:** This is runnable project code, not a claim that results have already been generated. Run the notebooks, save your actual outputs/screenshots, and use those verified results in your report.

## Setup
`pip install -r requirements.txt`

## Run in order
1. `notebooks/01_data_collection_and_wrangling.ipynb`
2. `notebooks/02_eda_and_visualizations.ipynb`
3. `notebooks/03_sql_analysis.ipynb`
4. `notebooks/04_folium_interactive_map.ipynb`
5. `notebooks/05_classification_models.ipynb`

Then run `python app.py` and open the local Dash URL. The notebooks collect current public data from the SpaceX API. Unknown landing outcomes are excluded from supervised learning. Review the target definition and data quality before interpreting results.
