py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pandas numpy matplotlib seaborn scikit-learn joblib ipykernel
.\.venv\Scripts\python.exe -c "import pandas, numpy, matplotlib, seaborn, sklearn; print('Core libraries OK')"
.\.venv\Scripts\python.exe -m pip install streamlit