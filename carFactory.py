from car import Car

from capulet import Capulet
from willoughby import Willoughby
from sternman import Sternman

from spindler import Spindler
from nubbit import Nubbin

class CarFactory():
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        parts = []
        parts.append(Capulet(current_mileage,last_service_mileage))
        parts.append(Spindler(last_service_date))
        return Car(parts)

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        parts = []
        parts.append(Willoughby(current_mileage,last_service_mileage))
        parts.append(Spindler(last_service_date))
        return Car(parts)

    @staticmethod
    def create_palindrome(last_service_date, warning_light_on):
        parts = []
        parts.append(Sternman(warning_light_on))
        parts.append(Spindler(last_service_date))
        return Car(parts)
    
    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        parts = []
        parts.append(Willoughby(current_mileage,last_service_mileage))
        parts.append(Nubbin(last_service_date))
        return Car(parts)

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        parts = []
        parts.append(Capulet(current_mileage,last_service_mileage))
        parts.append(Nubbin(last_service_date))
        return Car(parts)

    
    