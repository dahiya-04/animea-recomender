from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException
from config.config import GROQ_API_KEY,MODEL_NAME

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    """Pipeline class to execute the anime recommendation process."""
    
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Initializing AnimeRecommendationPipeline.")
            vector_builder = VectorStoreBuilder(csv_path="",persist_dir=persist_dir)
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever,model_name=MODEL_NAME,api_key=GROQ_API_KEY)
            logger.info("AnimeRecommendationPipeline initialized successfully.")
        except Exception as e:
            logger.error(f"An error occurred while initializing the pipeline: {e}")
            raise CustomException("error during pipeline initialization", e)
 
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)