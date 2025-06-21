from transformers import pipeline
from PIL import Image
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


image = Image.open("test.jpg")

obj_detector = pipeline("object-detection", model="facebook/detr-resnet-50")
output = obj_detector(image)
logger.info(f"Detected {len(output)} objects.")
for i, obj in enumerate(output):
    logger.info(f"Object {i + 1}:")
    logger.info(f"  Label: {obj['label']}")
    logger.info(f"  Score: {obj['score']:.2f}")
    logger.info(
        f"  Bounding box: {obj['box']}"
    )  # box is in the format [x_min, y_min, x_max, y_max]
