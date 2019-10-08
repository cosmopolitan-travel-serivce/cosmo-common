from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import PccCredential, PccCredentialUpdate
from typing import List


class PccCredntialClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "/api/pcc-credentials")

    def get_all_pcc_credentials(self) -> List[PccCredential]:
        return self._get_url("/")

    def get_credentials_by_gds_and_pcc(self, gds: str, pcc: str) -> List[PccCredential]:
        return self._get_url(f"/{gds}/{pcc}")

    def get_credentials_by_gds(self, gds: str) -> List[PccCredential]:
        return self._get_url(f"/{gds}")

    def create_pcc_credential(self, pcc_credential: PccCredential) -> PccCredential:
        return self._post_url("/", pcc_credential)

    def update_pcc_credential(self, pcc_code: str, pcc_credential: PccCredentialUpdate) -> PccCredential:
        return self._put_url(f"/{pcc_code}", pcc_credential)

    # def remove_pcc_credentials(self, gds: str, pcc: str):
    #     pcc_credential = self.get_credentials_by_gds_and_pcc(gds, pcc)
    #     return self._delete_url(f"/{gds}/{pcc}", pcc_credential)

        # def remove_pcc_credentials(self, pcc: str):
        #     return self._delete_url("/", pcc_credential)
