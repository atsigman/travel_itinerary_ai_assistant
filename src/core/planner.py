from langchain_core.messages import HumanMessage, AIMessage

from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException


logger = get_logger(__name__)


class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.n_days = 0
        self.city = ""
        self.interests = []
        self.itinerary = ""

        logger.info("Initialized TravelPlanner instance")

    def set_n_days(self, n_days: str) -> None:
        try:
            self.n_days = int(n_days)
            self.messages.append(HumanMessage(content=n_days))
            logger.info("n_days set successfully")

        except Exception as e:
            logger.error(f"Error while setting n_days: {e}")
            raise CustomException("Failed to set n_days", e)

    def set_city(self, city: str) -> None:
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully")

        except Exception as e:
            logger.error(f"Error while setting city: {e}")
            raise CustomException("Failed to set city", e)

    def set_interests(self, interests_str: str) -> None:
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests set successfully")

        except Exception as e:
            logger.error(f"Error while setting interests: {e}")
            raise CustomException("Failed to set interests", e)

    def create_itinerary(self) -> str:
        logger.info(
            f"Generating itinerary for {self.n_days} days in {self.city} "
            f"for the following interests: {self.interests}"
        )

        try:
            self.itinerary = generate_itinerary(self.n_days, self.city, self.interests)
            self.messages.append(AIMessage(content=self.itinerary))
            logger.info("Itinerary generated successfully")

            return self.itinerary

        except Exception as e:
            logger.error(f"Error while creating itinerary: {e}")
            raise CustomException("Failed to create itinerary", e)
