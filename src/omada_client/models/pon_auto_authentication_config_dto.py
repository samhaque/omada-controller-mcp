from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pon_auto_authentication_config_dto_authentication_method import (
    PonAutoAuthenticationConfigDTOAuthenticationMethod,
)
from ..models.pon_auto_authentication_config_dto_auto_authentication_status import (
    PonAutoAuthenticationConfigDTOAutoAuthenticationStatus,
)
from ..models.pon_auto_authentication_config_dto_discovery_mode import (
    PonAutoAuthenticationConfigDTODiscoveryMode,
)
from ..models.pon_auto_authentication_config_dto_onu_match_mode import (
    PonAutoAuthenticationConfigDTOOnuMatchMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PonAutoAuthenticationConfigDTO")


@_attrs_define
class PonAutoAuthenticationConfigDTO:
    """
    Attributes:
        pon_port (str): Pon port.e.g.GPON 1/0/1
        auto_authentication_status (PonAutoAuthenticationConfigDTOAutoAuthenticationStatus | Unset): Auto authentication
            status should be a value as follows:ENABLE,DISABLE
        onu_match_mode (PonAutoAuthenticationConfigDTOOnuMatchMode | Unset): ONU match mode of automatic
            authentication.OnuMatchMode should be a value as follows:ALL_ONU,EQUID_AUTH,EQUID_SWVER_AUTH,VENDOR_AUTH
        authentication_method (PonAutoAuthenticationConfigDTOAuthenticationMethod | Unset): Authentication mode used by
            the automatically discovered ONU.AuthenticationMethod should be a value as
            follows:PASSWORD_AUTH,SN_AUTH,LOID_AUTH,SN_AND_PASSWORD_AUTH,LOID_AND_PASSWORD_AUTH
        discovery_mode (PonAutoAuthenticationConfigDTODiscoveryMode | Unset): ONU auto discovery mode.DiscoveryMode
            should be a value as follows:ALWAYS_ON,ONCE_ON
        re_register_authentication (str | Unset): Re-Register-Authentication
    """

    pon_port: str
    auto_authentication_status: (
        PonAutoAuthenticationConfigDTOAutoAuthenticationStatus | Unset
    ) = UNSET
    onu_match_mode: PonAutoAuthenticationConfigDTOOnuMatchMode | Unset = UNSET
    authentication_method: (
        PonAutoAuthenticationConfigDTOAuthenticationMethod | Unset
    ) = UNSET
    discovery_mode: PonAutoAuthenticationConfigDTODiscoveryMode | Unset = UNSET
    re_register_authentication: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pon_port = self.pon_port

        auto_authentication_status: str | Unset = UNSET
        if not isinstance(self.auto_authentication_status, Unset):
            auto_authentication_status = self.auto_authentication_status.value

        onu_match_mode: str | Unset = UNSET
        if not isinstance(self.onu_match_mode, Unset):
            onu_match_mode = self.onu_match_mode.value

        authentication_method: str | Unset = UNSET
        if not isinstance(self.authentication_method, Unset):
            authentication_method = self.authentication_method.value

        discovery_mode: str | Unset = UNSET
        if not isinstance(self.discovery_mode, Unset):
            discovery_mode = self.discovery_mode.value

        re_register_authentication = self.re_register_authentication

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ponPort": pon_port,
            }
        )
        if auto_authentication_status is not UNSET:
            field_dict["autoAuthenticationStatus"] = auto_authentication_status
        if onu_match_mode is not UNSET:
            field_dict["onuMatchMode"] = onu_match_mode
        if authentication_method is not UNSET:
            field_dict["authenticationMethod"] = authentication_method
        if discovery_mode is not UNSET:
            field_dict["discoveryMode"] = discovery_mode
        if re_register_authentication is not UNSET:
            field_dict["reRegisterAuthentication"] = re_register_authentication

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pon_port = d.pop("ponPort")

        _auto_authentication_status = d.pop("autoAuthenticationStatus", UNSET)
        auto_authentication_status: (
            PonAutoAuthenticationConfigDTOAutoAuthenticationStatus | Unset
        )
        if isinstance(_auto_authentication_status, Unset):
            auto_authentication_status = UNSET
        else:
            auto_authentication_status = (
                PonAutoAuthenticationConfigDTOAutoAuthenticationStatus(
                    _auto_authentication_status
                )
            )

        _onu_match_mode = d.pop("onuMatchMode", UNSET)
        onu_match_mode: PonAutoAuthenticationConfigDTOOnuMatchMode | Unset
        if isinstance(_onu_match_mode, Unset):
            onu_match_mode = UNSET
        else:
            onu_match_mode = PonAutoAuthenticationConfigDTOOnuMatchMode(_onu_match_mode)

        _authentication_method = d.pop("authenticationMethod", UNSET)
        authentication_method: (
            PonAutoAuthenticationConfigDTOAuthenticationMethod | Unset
        )
        if isinstance(_authentication_method, Unset):
            authentication_method = UNSET
        else:
            authentication_method = PonAutoAuthenticationConfigDTOAuthenticationMethod(
                _authentication_method
            )

        _discovery_mode = d.pop("discoveryMode", UNSET)
        discovery_mode: PonAutoAuthenticationConfigDTODiscoveryMode | Unset
        if isinstance(_discovery_mode, Unset):
            discovery_mode = UNSET
        else:
            discovery_mode = PonAutoAuthenticationConfigDTODiscoveryMode(
                _discovery_mode
            )

        re_register_authentication = d.pop("reRegisterAuthentication", UNSET)

        pon_auto_authentication_config_dto = cls(
            pon_port=pon_port,
            auto_authentication_status=auto_authentication_status,
            onu_match_mode=onu_match_mode,
            authentication_method=authentication_method,
            discovery_mode=discovery_mode,
            re_register_authentication=re_register_authentication,
        )

        pon_auto_authentication_config_dto.additional_properties = d
        return pon_auto_authentication_config_dto

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
