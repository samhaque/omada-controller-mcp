from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.authentication_param_open_api_vo import AuthenticationParamOpenApiVO


T = TypeVar("T", bound="EapMethodOpenApiVO")


@_attrs_define
class EapMethodOpenApiVO:
    """EAP Method list.<br />Note: Up to 4 entries are allowed for the EAP Method list.

    Attributes:
        method (int): EAP authentication method supported by the NAI realm.<br />Parameter method should be a value as
            follows:[0:None;1:Identity;2:Notification;5:One-Time Password (OTP);6:Generic Token Card (GTC);13:EAP-TLS;18:GSM
            Subscriber Identity Modules (EAP-SIM);21:EAP-TTLS;23:EAP-AKA Authentication;25:PEAP;28:CRYPTOCard;29:EAP-
            MSCHAP-V2]
        param (list[AuthenticationParamOpenApiVO]): Authentication Param list, configure the EAP authentication
            parameter identifier and authentication parameters.<br />Note: Up to 4 entries are allowed for the
            Authentication Param list.
    """

    method: int
    param: list[AuthenticationParamOpenApiVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        param = []
        for param_item_data in self.param:
            param_item = param_item_data.to_dict()
            param.append(param_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "param": param,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.authentication_param_open_api_vo import (
            AuthenticationParamOpenApiVO,
        )

        d = dict(src_dict)
        method = d.pop("method")

        param = []
        _param = d.pop("param")
        for param_item_data in _param:
            param_item = AuthenticationParamOpenApiVO.from_dict(param_item_data)

            param.append(param_item)

        eap_method_open_api_vo = cls(
            method=method,
            param=param,
        )

        eap_method_open_api_vo.additional_properties = d
        return eap_method_open_api_vo

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
