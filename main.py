from textSummarizer.pipeline.stage_01_dataingestion import DataIngestionTrainningPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainningPipeline()
    data_ingestion.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================x")
except Exception as e:
    logger.exception(e)
    raise e