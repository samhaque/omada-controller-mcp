from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AuthenticationParamOpenApiVO")


@_attrs_define
class AuthenticationParamOpenApiVO:
    """Authentication Param list, configure the EAP authentication parameter identifier and authentication parameters.<br
    />Note: Up to 4 entries are allowed for the Authentication Param list.

        Attributes:
            id (int): EAP authentication parameter identifier.<br />Parameter id should be a value as follows: [2: None-EAP
                Inner Authentication Type; 3: Inner Authentication EAP Method Type; 5: Credential Type; 6: Tunneled EAP Method
                Credential Type]
            value (int): Authentication parameters.<br />When id = 2, parameter value should be a value as
                follows:[1:PAP;2:CHAP;3:MSCHAP;4:MSCHAPV2].<br />When id = 3, parameter value should be a value as
                follows:[0:None;1:Identity;2:Notification;5:One-Time Password (OTP);6:Generic Token Card (GTC);13:EAP-TLS;18:GSM
                Subscriber Identity Modules (EAP-SIM);21:EAP-TTLS;23:EAP-AKA Authentication;25:PEAP;28:CRYPTOCard;29:EAP-
                MSCHAP-V2]<br />When id = 5, parameter value should be a value as follows:[1:SIM;2:USIM;3:NFC Secure
                Element;4:Hardware Token;5:Softoken;6:Certificate;7:username/password;8:None;10:Vendor Specific]<br />When id =
                6, parameter value should be a value as follows:[1:SIM;2:USIM;3:NFC Secure Element;4:Hardware
                Token;5:Softoken;6:Certificate;7:username/password;9:Anonymous;10:Vendor Specific].
    """

    id: int
    value: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        value = d.pop("value")

        authentication_param_open_api_vo = cls(
            id=id,
            value=value,
        )

        authentication_param_open_api_vo.additional_properties = d
        return authentication_param_open_api_vo

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
