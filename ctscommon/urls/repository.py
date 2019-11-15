from typing import Optional, List

# from ctscommon.data.repository import Repository, role_repository_session
from ctscommon.urls.models import UrlMapping
from ctscommon.urls.schemas import HttpMethod
from ctscommon.utils import SingletonWrapper


@SingletonWrapper
class ApiUrlRepository(Repository):
    def __init__(self):
        super().__init__(UrlMapping)

    def get_by_service_url_and_method(self, service: str, url: str, method: HttpMethod) -> Optional[UrlMapping]:
        return self.get_one_by_conditions([UrlMapping.service == service, UrlMapping.url == url,
                                           UrlMapping.method == method])

    def get_by_service_operation_id_and_method(self, service: str, operation_id: str, method: HttpMethod) -> Optional[UrlMapping]:
        return self.get_one_by_conditions([UrlMapping.service == service, UrlMapping.operation_id == operation_id,
                                           UrlMapping.method == method])

    def get_all_by_service(self, service: str) -> List[UrlMapping]:
        return self.get_all_by_conditions([UrlMapping.service == service])
