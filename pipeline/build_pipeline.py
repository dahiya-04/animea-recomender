from src.vector_store import VectorStoreBuilder
from src.data_loader import AnimeDataLoader

from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

def main():
    """Main function to execute the data loading, processing, and vector store building pipeline."""
    try:
        data_loader = AnimeDataLoader("data/anime_with_synopsis.csv","data/processed_anime.csv")
        processed_csv = data_loader.load_and_process()
        logger.info("Data loaded and processed successfully.")

        vector_store_builder = VectorStoreBuilder(processed_csv)
        vector_store_builder.build_and_save_vectorstore()
        logger.info("Vector store built and saved successfully.")
    except Exception as e:
        logger.error(f"An error occurred during pipeline execution: {e}")
        raise CustomException("error during piepeline",e)

if __name__ == "__main__":
    main()