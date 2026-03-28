import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", page_icon=":tv:", layout="wide")

load_dotenv()

@st.cache_resource
def load_pipeline():
    return AnimeRecommendationPipeline()

pipeline = load_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences or a specific anime you like:") 
if query:
    with st.spinner("Generating recommendation..."):
        try:
            recommendation = pipeline.recommend(query)
            st.subheader("Recommended Anime:")
            st.write(recommendation)
        except Exception as e:
            st.error(f"An error occurred while getting recommendation: {str(e)}")