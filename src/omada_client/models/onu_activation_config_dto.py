from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_activation_config_dto_authentication_method import (
    OnuActivationConfigDTOAuthenticationMethod,
)
from ..models.onu_activation_config_dto_discovery_mode import (
    OnuActivationConfigDTODiscoveryMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnuActivationConfigDTO")


@_attrs_define
class OnuActivationConfigDTO:
    """
    Attributes:
        keys (list[str]): Entry identifier list
        authentication_method (OnuActivationConfigDTOAuthenticationMethod): Authentication mode used by the
            automatically discovered ONU.AuthenticationMethod should be a value as
            follows:PASSWORD_AUTH,SN_AUTH,LOID_AUTH,SN_AND_PASSWORD_AUTH,LOID_AND_PASSWORD_AUTH
        line_profile (str): Line profile id bound to the ONU
        service_profile (str): Service profile id bound to the ONU
        onu_id (int | Unset): Onu ID should be within the range of 0 to 127
        description (str | Unset): Display the configured port description.Only 1-32 bits numbers, Upper and lower
            letters, -@_:/. are allowed.
        discovery_mode (OnuActivationConfigDTODiscoveryMode | Unset): ONU auto discovery mode.DiscoveryMode should be a
            value as follows:ALWAYS_ON,ONCE_ON
        re_register_authentication (str | Unset): Re-Register-Authentication
        service_port_profile (str | Unset): Service port profile id bound to the ONU
    """

    keys: list[str]
    authentication_method: OnuActivationConfigDTOAuthenticationMethod
    line_profile: str
    service_profile: str
    onu_id: int | Unset = UNSET
    description: str | Unset = UNSET
    discovery_mode: OnuActivationConfigDTODiscoveryMode | Unset = UNSET
    re_register_authentication: str | Unset = UNSET
    service_port_profile: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys = self.keys

        authentication_method = self.authentication_method.value

        line_profile = self.line_profile

        service_profile = self.service_profile

        onu_id = self.onu_id

        description = self.description

        discovery_mode: str | Unset = UNSET
        if not isinstance(self.discovery_mode, Unset):
            discovery_mode = self.discovery_mode.value

        re_register_authentication = self.re_register_authentication

        service_port_profile = self.service_port_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keys": keys,
                "authenticationMethod": authentication_method,
                "lineProfile": line_profile,
                "serviceProfile": service_profile,
            }
        )
        if onu_id is not UNSET:
            field_dict["onuId"] = onu_id
        if description is not UNSET:
            field_dict["description"] = description
        if discovery_mode is not UNSET:
            field_dict["discoveryMode"] = discovery_mode
        if re_register_authentication is not UNSET:
            field_dict["reRegisterAuthentication"] = re_register_authentication
        if service_port_profile is not UNSET:
            field_dict["servicePortProfile"] = service_port_profile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keys = cast(list[str], d.pop("keys"))

        authentication_method = OnuActivationConfigDTOAuthenticationMethod(
            d.pop("authenticationMethod")
        )

        line_profile = d.pop("lineProfile")

        service_profile = d.pop("serviceProfile")

        onu_id = d.pop("onuId", UNSET)

        description = d.pop("description", UNSET)

        _discovery_mode = d.pop("discoveryMode", UNSET)
        discovery_mode: OnuActivationConfigDTODiscoveryMode | Unset
        if isinstance(_discovery_mode, Unset):
            discovery_mode = UNSET
        else:
            discovery_mode = OnuActivationConfigDTODiscoveryMode(_discovery_mode)

        re_register_authentication = d.pop("reRegisterAuthentication", UNSET)

        service_port_profile = d.pop("servicePortProfile", UNSET)

        onu_activation_config_dto = cls(
            keys=keys,
            authentication_method=authentication_method,
            line_profile=line_profile,
            service_profile=service_profile,
            onu_id=onu_id,
            description=description,
            discovery_mode=discovery_mode,
            re_register_authentication=re_register_authentication,
            service_port_profile=service_port_profile,
        )

        onu_activation_config_dto.additional_properties = d
        return onu_activation_config_dto

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
