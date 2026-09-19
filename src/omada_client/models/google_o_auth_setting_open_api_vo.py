from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="GoogleOAuthSettingOpenApiVO")


@_attrs_define
class GoogleOAuthSettingOpenApiVO:
    """Google OAuth setting, required when [authType] is 16 and social auth [enabledTypes] contains 17.

    Attributes:
        client_id (str): Google OAuth client ID
        client_secret (str): Google OAuth client secret
    """

    client_id: str
    client_secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientId": client_id,
                "clientSecret": client_secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_id = d.pop("clientId")

        client_secret = d.pop("clientSecret")

        google_o_auth_setting_open_api_vo = cls(
            client_id=client_id,
            client_secret=client_secret,
        )

        google_o_auth_setting_open_api_vo.additional_properties = d
        return google_o_auth_setting_open_api_vo

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
