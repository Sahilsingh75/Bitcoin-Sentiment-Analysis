# Bitcoin Sentiment Analysis Project by Sahil Singh

This project includes a Jupyter notebook for analyzing Bitcoin tweet sentiment and a Streamlit app for interactive sentiment analysis of any tweet dataset.

## Project Structure
- `Notebook/Bitcoin_Sentiment_Analysis.ipynb`: Jupyter notebook for analyzing Bitcoin tweets.
- `Streamlit_app/Bitcoin_Sentiment_Analysis_Streamlit_Application.py`: Streamlit app for interactive sentiment analysis.
- `DATA/`: Contains the dataset (not uploaded to GitHub).
- `requirements.txt`: Dependencies for the project.

## Setup Instructions
1. **Install Python**: Ensure Python 3.7+ is installed.
2. **Create Virtual Environment**:
   - Run: `python -m venv streamlit_env`
   - Activate:
     - Windows: `streamlit_env\Scripts\activate`
     - macOS/Linux: `source streamlit_env/bin/activate`
3. **Install Dependencies**:
   - Run: `pip install -r requirements.txt`
4. **Run the Notebook**:
   - Start Jupyter: `jupyter notebook`
   - Open `Notebook/Bitcoin_Sentiment_Analysis.ipynb` and run all cells.
5. **Run the Streamlit App**:
   - Run: `streamlit run Streamlit_app/Bitcoin_Sentiment_Analysis_Streamlit_Application.py`
   - Access the app at `http://localhost:8501`.

## Deployment on Streamlit Community Cloud
- The Streamlit app is deployed on Streamlit Community Cloud.
- Access the deployed app at: https://bitcoin-sentiment-analysis-jgwxq5gbzredffn9ogtlj8.streamlit.app/.

## Dataset
- Place your tweet dataset (e.g., `Bitcoin_tweets.csv`) in the `DATA/` folder for the notebook.
- The Streamlit app allows uploading any tweet dataset in CSV format and specify the column that contain tweet content for analysis.
