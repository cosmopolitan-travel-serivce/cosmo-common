
from ctscommon.urls.schemas import ApiUrl
class ApiUrlService:
    def __init__(self, service_name):
        self.service_name = service_name

        
    def get_api_urls(self, service: str = None) -> List[ApiUrl]:
        """
        Get API urls for a service or globally
        :param service: str -> The optional service
        :return: List[ApiUrl]
        """
        if service:
            api_urls = self.api_url_repository.get_all_by_service(service)
        else:
            api_urls = self.api_url_repository.get_all()
        return [from_db_to_model(api_url) for api_url in api_urls]
        
api_common_service = ApiUrlService("COMMON")