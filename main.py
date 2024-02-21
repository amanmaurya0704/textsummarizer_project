from textSummarizer.pipeline.stage_01_dataingestion import DataIngestionTrainningPipeline
from textSummarizer.pipeline.stage_02_datavalidation import DataValidationTrainningPipeline
from textSummarizer.pipeline.stage_03_datatransformation import DataTransformationTrainningPipeline
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

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainningPipeline()
    data_validation.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainningPipeline()
    data_transformation.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========================x")
except Exception as e:
    logger.exception(e)
    raise e