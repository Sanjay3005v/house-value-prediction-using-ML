# House Value Prediction using Machine Learning

This project predicts house prices using machine learning on the King County housing dataset.

## Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run the Notebook

- Open `housesales.ipynb` in Jupyter or VS Code.
- Run all cells to explore the data, train the model, and save the trained model (e.g., as `house_model.pkl` using `joblib`).

### 3. Launch the Web Interface

- Make sure you have saved your trained model as `house_model.pkl`.
- Run the Streamlit app:

```bash
streamlit run web_app.py
```

- Enter house features in the web form to get price predictions.

## Tech Stack

- Python, pandas, scikit-learn, matplotlib, seaborn
- Streamlit (for web interface)

## Notes

- Ensure `house_model.pkl` is in the same directory as `web_app.py`.
- You can customize the web interface by editing `web_app.py`.


Thank you
