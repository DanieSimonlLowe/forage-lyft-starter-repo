from car import Car

from capulet import Capulet
from willoughby import Willoughby
from sternman import Sternman

from spindler import Spindler
from nubbit import Nubbin
from tire import Tire

class CarFactory():
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage, tire):
        parts = []
        parts.append(Capulet(current_mileage,last_service_mileage))
        parts.append(Spindler(last_service_date))
        parts.append(tire)
        return Car(parts)

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage, tire):
        parts = []
        parts.append(Willoughby(current_mileage,last_service_mileage))
        parts.append(Spindler(last_service_date))
        parts.append(tire)
        return Car(parts)

    @staticmethod
    def create_palindrome(last_service_date, warning_light_on, tire):
        parts = []
        parts.append(Sternman(warning_light_on))
        parts.append(Spindler(last_service_date))
        parts.append(tire)
        return Car(parts)
    
    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage, tire):
        parts = []
        parts.append(Willoughby(current_mileage,last_service_mileage))
        parts.append(Nubbin(last_service_date))
        parts.append(tire)
        return Car(parts)

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage, tire):
        parts = []
        parts.append(Capulet(current_mileage,last_service_mileage))
        parts.append(Nubbin(last_service_date))
        parts.append(tire)
        return Car(parts)

    
    