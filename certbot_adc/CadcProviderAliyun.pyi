# -*- coding: utf8 -*-

from certbot_adc import CadcProviderBase
from aliyunsdkcore.client import AcsClient


class CadcProviderAliyun(CadcProviderBase):
    acs_client: AcsClient

    def __init__(self, acs_client: AcsClient): ...

    def get_txt_record(self, recordId: str) -> dict: ...

    def update_txt_record(self, recordId: str, rr: str, value: str) -> str: ...

    def add_txt_record(self, domain: str, rr: str, value: str) -> str: ...

    def find_target_txt_record(self, domain: str, rr: str) -> str: ...

    def update_dns01(self, domain: str, token: str) -> None: ...