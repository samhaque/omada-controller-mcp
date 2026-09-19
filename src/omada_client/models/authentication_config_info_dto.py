from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.authentication_config_info_dto_authentication_method import (
    AuthenticationConfigInfoDTOAuthenticationMethod,
)
from ..models.authentication_config_info_dto_discovery_mode import (
    AuthenticationConfigInfoDTODiscoveryMode,
)
from ..models.authentication_config_info_dto_password_type import (
    AuthenticationConfigInfoDTOPasswordType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationConfigInfoDTO")


@_attrs_define
class AuthenticationConfigInfoDTO:
    """OUN authentication information

    Attributes:
        authentication_method (AuthenticationConfigInfoDTOAuthenticationMethod): Authentication mode used by the
            automatically discovered ONU.AuthenticationMethod should be a value as
            follows:PASSWORD_AUTH,SN_AUTH,LOID_AUTH,SN_AND_PASSWORD_AUTH,LOID_AND_PASSWORD_AUTH
        line_profile (str): Line profile id bound to the ONU
        service_profile (str): Service profile id bound to the ONU
        password_type (AuthenticationConfigInfoDTOPasswordType | Unset): Indicates the password type reported by the
            automatic discovery of the ONT.PasswordType should be a value as follows：ASCII,HEX
        password (str | Unset): Automatic discovery ONT Authentication Password.Password should contain 1 to 10
            characters in ASCII (from \\x21 to \\x7e) or 1 to 20 characters in hexadecimal.
        discovery_mode (AuthenticationConfigInfoDTODiscoveryMode | Unset): ONU auto discovery mode.DiscoveryMode should
            be a value as follows:ALWAYS_ON,ONCE_ON
        serial_number (str | Unset): SerialNumber of ONU, serialNumber should contain 12, 13, or 16 characters, in the
            format XXXXXXXXXXXX,XXXX-XXXXXXXX,XXXXXXXXXXXXXXXX.When the serialNumber contains 16 characters, the first 8
            characters will be grouped into pairs of two, resulting in 4 hexadecimal characters, and each hexadecimal
            character must fall within the range of 0x21 to 0x7E.
        loid (str | Unset): Loid set by automatic discovery of the ONT, loid should be 1-32 characters, including
            letters, numbers, and symbols (-@_:/.).
        loid_password (str | Unset): Loid password set by automatic discovery of the ONT,loidPassword should be ASCII
            characters from \\x21 to \\x7e
        re_register_authentication (str | Unset): Re-Register-Authentication
        service_port_profile (str | Unset): Service port profile id bound to the ONU
        description (str | Unset): Display the configured port description.Only 1-32 bits numbers, Upper and lower
            letters, -@_:/. are allowed.
        online_status (str | Unset): Online status should be a value as follows:DISABLE,ENABLE
        admin_status (str | Unset): Admin status of ONU.AdminStatus should be a value as follows:ACTIVE,DEACTIVE
        config_status (str | Unset): Whether OLT has successfully delivered configurations to ONU.ConfigStatus should be
            a value as follows:FAILED,SUCCESS
    """

    authentication_method: AuthenticationConfigInfoDTOAuthenticationMethod
    line_profile: str
    service_profile: str
    password_type: AuthenticationConfigInfoDTOPasswordType | Unset = UNSET
    password: str | Unset = UNSET
    discovery_mode: AuthenticationConfigInfoDTODiscoveryMode | Unset = UNSET
    serial_number: str | Unset = UNSET
    loid: str | Unset = UNSET
    loid_password: str | Unset = UNSET
    re_register_authentication: str | Unset = UNSET
    service_port_profile: str | Unset = UNSET
    description: str | Unset = UNSET
    online_status: str | Unset = UNSET
    admin_status: str | Unset = UNSET
    config_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authentication_method = self.authentication_method.value

        line_profile = self.line_profile

        service_profile = self.service_profile

        password_type: str | Unset = UNSET
        if not isinstance(self.password_type, Unset):
            password_type = self.password_type.value

        password = self.password

        discovery_mode: str | Unset = UNSET
        if not isinstance(self.discovery_mode, Unset):
            discovery_mode = self.discovery_mode.value

        serial_number = self.serial_number

        loid = self.loid

        loid_password = self.loid_password

        re_register_authentication = self.re_register_authentication

        service_port_profile = self.service_port_profile

        description = self.description

        online_status = self.online_status

        admin_status = self.admin_status

        config_status = self.config_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authenticationMethod": authentication_method,
                "lineProfile": line_profile,
                "serviceProfile": service_profile,
            }
        )
        if password_type is not UNSET:
            field_dict["passwordType"] = password_type
        if password is not UNSET:
            field_dict["password"] = password
        if discovery_mode is not UNSET:
            field_dict["discoveryMode"] = discovery_mode
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if loid is not UNSET:
            field_dict["loid"] = loid
        if loid_password is not UNSET:
            field_dict["loidPassword"] = loid_password
        if re_register_authentication is not UNSET:
            field_dict["reRegisterAuthentication"] = re_register_authentication
        if service_port_profile is not UNSET:
            field_dict["servicePortProfile"] = service_port_profile
        if description is not UNSET:
            field_dict["description"] = description
        if online_status is not UNSET:
            field_dict["onlineStatus"] = online_status
        if admin_status is not UNSET:
            field_dict["adminStatus"] = admin_status
        if config_status is not UNSET:
            field_dict["configStatus"] = config_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        authentication_method = AuthenticationConfigInfoDTOAuthenticationMethod(
            d.pop("authenticationMethod")
        )

        line_profile = d.pop("lineProfile")

        service_profile = d.pop("serviceProfile")

        _password_type = d.pop("passwordType", UNSET)
        password_type: AuthenticationConfigInfoDTOPasswordType | Unset
        if isinstance(_password_type, Unset):
            password_type = UNSET
        else:
            password_type = AuthenticationConfigInfoDTOPasswordType(_password_type)

        password = d.pop("password", UNSET)

        _discovery_mode = d.pop("discoveryMode", UNSET)
        discovery_mode: AuthenticationConfigInfoDTODiscoveryMode | Unset
        if isinstance(_discovery_mode, Unset):
            discovery_mode = UNSET
        else:
            discovery_mode = AuthenticationConfigInfoDTODiscoveryMode(_discovery_mode)

        serial_number = d.pop("serialNumber", UNSET)

        loid = d.pop("loid", UNSET)

        loid_password = d.pop("loidPassword", UNSET)

        re_register_authentication = d.pop("reRegisterAuthentication", UNSET)

        service_port_profile = d.pop("servicePortProfile", UNSET)

        description = d.pop("description", UNSET)

        online_status = d.pop("onlineStatus", UNSET)

        admin_status = d.pop("adminStatus", UNSET)

        config_status = d.pop("configStatus", UNSET)

        authentication_config_info_dto = cls(
            authentication_method=authentication_method,
            line_profile=line_profile,
            service_profile=service_profile,
            password_type=password_type,
            password=password,
            discovery_mode=discovery_mode,
            serial_number=serial_number,
            loid=loid,
            loid_password=loid_password,
            re_register_authentication=re_register_authentication,
            service_port_profile=service_port_profile,
            description=description,
            online_status=online_status,
            admin_status=admin_status,
            config_status=config_status,
        )

        authentication_config_info_dto.additional_properties = d
        return authentication_config_info_dto

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
