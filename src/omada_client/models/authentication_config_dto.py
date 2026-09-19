from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.authentication_config_dto_active_status import (
    AuthenticationConfigDTOActiveStatus,
)
from ..models.authentication_config_dto_admin_status import (
    AuthenticationConfigDTOAdminStatus,
)
from ..models.authentication_config_dto_authentication_method import (
    AuthenticationConfigDTOAuthenticationMethod,
)
from ..models.authentication_config_dto_config_status import (
    AuthenticationConfigDTOConfigStatus,
)
from ..models.authentication_config_dto_discovery_mode import (
    AuthenticationConfigDTODiscoveryMode,
)
from ..models.authentication_config_dto_match_status import (
    AuthenticationConfigDTOMatchStatus,
)
from ..models.authentication_config_dto_online_status import (
    AuthenticationConfigDTOOnlineStatus,
)
from ..models.authentication_config_dto_password_type import (
    AuthenticationConfigDTOPasswordType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationConfigDTO")


@_attrs_define
class AuthenticationConfigDTO:
    """Content

    Attributes:
        key (str | Unset): Identifier of entry
        port_id (str | Unset): Pon port ID,e.g.,PON 1/0/1
        onu_id (int | Unset): ONU ID,This parameter is optional. If not specified, the system will automatically
            allocate the smallest available ONU number under the current port.OnuId should be within the range of 0 to 127
        description (str | Unset): Description of ONU.Only 1-32 bits numbers, Upper and lower letters, -@_:/. are
            allowed.
        serial_number (str | Unset): SerialNumber of ONU should contain 12, 13, or 16 characters, in the format
            XXXXXXXXXXXX ,XXXX-XXXXXXXX,XXXXXXXXXXXXXXXX
        mac_address (str | Unset): Mac address of ONU
        password_type (AuthenticationConfigDTOPasswordType | Unset): Indicates the password type reported by the
            automatic discovery of the ONT.PasswordType should be a value as follows：ASCII,HEX
        password (str | Unset): Authentication password set by automatic discovery of the ONT, password should be ASCII
            characters from \\x21 to \\x7e and 1 to 20 hexadecimal digits
        loid (str | Unset): Loid set by automatic discovery of the ONT, loid should be 1-32 characters, including
            letters, numbers, and symbols (-@_:/.).
        loid_password (str | Unset): Loid password set by automatic discovery of the ONT,loidPassword should be ASCII
            characters from \\x21 to \\x7e
        line_profile (str | Unset): Line profile bound to the ONU, lineProfile is displayed in the format id(name)
        service_profile (str | Unset): Service profile bound to the ONU, serviceProfile displayed in the format id(name)
        admin_status (AuthenticationConfigDTOAdminStatus | Unset): Admin status should be a value as
            follows:ACTIVATE,DEACTIVATE
        online_status (AuthenticationConfigDTOOnlineStatus | Unset): Online status should be a value as follows:ONLINE:
            ONU is online.OFFLINE: ONU is offline; it does not support version information queries or any service
            operations.
        config_status (AuthenticationConfigDTOConfigStatus | Unset): Config status should be a value as follows:SUCCESS:
            Configuration successfully delivered and recognized by the ONU.FAILED: Configuration not successfully delivered
            or not recognized by the ONU.
        match_status (AuthenticationConfigDTOMatchStatus | Unset): Match status should be a value as follows:MATCH: ONU
            hardware capabilities are consistent with the bound service template.MISMATCH: ONU hardware capabilities are
            inconsistent with the bound service template.
        active_status (AuthenticationConfigDTOActiveStatus | Unset): Active status should be a value as follows:ACTIVE:
            ONU is in an active state, capable of data communication and supporting services.INACTIVE: ONU is in an inactive
            state, which may be due to reasons such as unactivated configuration, being offline, configuration failure, or
            configuration mismatch.
        authentication_method (AuthenticationConfigDTOAuthenticationMethod | Unset): Authentication mode used by the
            automatically discovered ONU.AuthenticationMethod should be a value as
            follows:PASSWORD_AUTH,SN_AUTH,LOID_AUTH,SN_AND_PASSWORD_AUTH,LOID_AND_PASSWORD_AUTH
        re_register_authentication (str | Unset): Re-Register-Authentication
        discovery_mode (AuthenticationConfigDTODiscoveryMode | Unset): ONU auto discovery mode.DiscoveryMode should be a
            value as follows:ALWAYS_ON,ONCE_ON
        service_port_profile (str | Unset): Service port profile bound to the ONU is  in the format id(name)
    """

    key: str | Unset = UNSET
    port_id: str | Unset = UNSET
    onu_id: int | Unset = UNSET
    description: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    password_type: AuthenticationConfigDTOPasswordType | Unset = UNSET
    password: str | Unset = UNSET
    loid: str | Unset = UNSET
    loid_password: str | Unset = UNSET
    line_profile: str | Unset = UNSET
    service_profile: str | Unset = UNSET
    admin_status: AuthenticationConfigDTOAdminStatus | Unset = UNSET
    online_status: AuthenticationConfigDTOOnlineStatus | Unset = UNSET
    config_status: AuthenticationConfigDTOConfigStatus | Unset = UNSET
    match_status: AuthenticationConfigDTOMatchStatus | Unset = UNSET
    active_status: AuthenticationConfigDTOActiveStatus | Unset = UNSET
    authentication_method: AuthenticationConfigDTOAuthenticationMethod | Unset = UNSET
    re_register_authentication: str | Unset = UNSET
    discovery_mode: AuthenticationConfigDTODiscoveryMode | Unset = UNSET
    service_port_profile: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        port_id = self.port_id

        onu_id = self.onu_id

        description = self.description

        serial_number = self.serial_number

        mac_address = self.mac_address

        password_type: str | Unset = UNSET
        if not isinstance(self.password_type, Unset):
            password_type = self.password_type.value

        password = self.password

        loid = self.loid

        loid_password = self.loid_password

        line_profile = self.line_profile

        service_profile = self.service_profile

        admin_status: str | Unset = UNSET
        if not isinstance(self.admin_status, Unset):
            admin_status = self.admin_status.value

        online_status: str | Unset = UNSET
        if not isinstance(self.online_status, Unset):
            online_status = self.online_status.value

        config_status: str | Unset = UNSET
        if not isinstance(self.config_status, Unset):
            config_status = self.config_status.value

        match_status: str | Unset = UNSET
        if not isinstance(self.match_status, Unset):
            match_status = self.match_status.value

        active_status: str | Unset = UNSET
        if not isinstance(self.active_status, Unset):
            active_status = self.active_status.value

        authentication_method: str | Unset = UNSET
        if not isinstance(self.authentication_method, Unset):
            authentication_method = self.authentication_method.value

        re_register_authentication = self.re_register_authentication

        discovery_mode: str | Unset = UNSET
        if not isinstance(self.discovery_mode, Unset):
            discovery_mode = self.discovery_mode.value

        service_port_profile = self.service_port_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if onu_id is not UNSET:
            field_dict["onuId"] = onu_id
        if description is not UNSET:
            field_dict["description"] = description
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if password_type is not UNSET:
            field_dict["passwordType"] = password_type
        if password is not UNSET:
            field_dict["password"] = password
        if loid is not UNSET:
            field_dict["loid"] = loid
        if loid_password is not UNSET:
            field_dict["loidPassword"] = loid_password
        if line_profile is not UNSET:
            field_dict["lineProfile"] = line_profile
        if service_profile is not UNSET:
            field_dict["serviceProfile"] = service_profile
        if admin_status is not UNSET:
            field_dict["adminStatus"] = admin_status
        if online_status is not UNSET:
            field_dict["onlineStatus"] = online_status
        if config_status is not UNSET:
            field_dict["configStatus"] = config_status
        if match_status is not UNSET:
            field_dict["matchStatus"] = match_status
        if active_status is not UNSET:
            field_dict["activeStatus"] = active_status
        if authentication_method is not UNSET:
            field_dict["authenticationMethod"] = authentication_method
        if re_register_authentication is not UNSET:
            field_dict["reRegisterAuthentication"] = re_register_authentication
        if discovery_mode is not UNSET:
            field_dict["discoveryMode"] = discovery_mode
        if service_port_profile is not UNSET:
            field_dict["servicePortProfile"] = service_port_profile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        port_id = d.pop("portId", UNSET)

        onu_id = d.pop("onuId", UNSET)

        description = d.pop("description", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        _password_type = d.pop("passwordType", UNSET)
        password_type: AuthenticationConfigDTOPasswordType | Unset
        if isinstance(_password_type, Unset):
            password_type = UNSET
        else:
            password_type = AuthenticationConfigDTOPasswordType(_password_type)

        password = d.pop("password", UNSET)

        loid = d.pop("loid", UNSET)

        loid_password = d.pop("loidPassword", UNSET)

        line_profile = d.pop("lineProfile", UNSET)

        service_profile = d.pop("serviceProfile", UNSET)

        _admin_status = d.pop("adminStatus", UNSET)
        admin_status: AuthenticationConfigDTOAdminStatus | Unset
        if isinstance(_admin_status, Unset):
            admin_status = UNSET
        else:
            admin_status = AuthenticationConfigDTOAdminStatus(_admin_status)

        _online_status = d.pop("onlineStatus", UNSET)
        online_status: AuthenticationConfigDTOOnlineStatus | Unset
        if isinstance(_online_status, Unset):
            online_status = UNSET
        else:
            online_status = AuthenticationConfigDTOOnlineStatus(_online_status)

        _config_status = d.pop("configStatus", UNSET)
        config_status: AuthenticationConfigDTOConfigStatus | Unset
        if isinstance(_config_status, Unset):
            config_status = UNSET
        else:
            config_status = AuthenticationConfigDTOConfigStatus(_config_status)

        _match_status = d.pop("matchStatus", UNSET)
        match_status: AuthenticationConfigDTOMatchStatus | Unset
        if isinstance(_match_status, Unset):
            match_status = UNSET
        else:
            match_status = AuthenticationConfigDTOMatchStatus(_match_status)

        _active_status = d.pop("activeStatus", UNSET)
        active_status: AuthenticationConfigDTOActiveStatus | Unset
        if isinstance(_active_status, Unset):
            active_status = UNSET
        else:
            active_status = AuthenticationConfigDTOActiveStatus(_active_status)

        _authentication_method = d.pop("authenticationMethod", UNSET)
        authentication_method: AuthenticationConfigDTOAuthenticationMethod | Unset
        if isinstance(_authentication_method, Unset):
            authentication_method = UNSET
        else:
            authentication_method = AuthenticationConfigDTOAuthenticationMethod(
                _authentication_method
            )

        re_register_authentication = d.pop("reRegisterAuthentication", UNSET)

        _discovery_mode = d.pop("discoveryMode", UNSET)
        discovery_mode: AuthenticationConfigDTODiscoveryMode | Unset
        if isinstance(_discovery_mode, Unset):
            discovery_mode = UNSET
        else:
            discovery_mode = AuthenticationConfigDTODiscoveryMode(_discovery_mode)

        service_port_profile = d.pop("servicePortProfile", UNSET)

        authentication_config_dto = cls(
            key=key,
            port_id=port_id,
            onu_id=onu_id,
            description=description,
            serial_number=serial_number,
            mac_address=mac_address,
            password_type=password_type,
            password=password,
            loid=loid,
            loid_password=loid_password,
            line_profile=line_profile,
            service_profile=service_profile,
            admin_status=admin_status,
            online_status=online_status,
            config_status=config_status,
            match_status=match_status,
            active_status=active_status,
            authentication_method=authentication_method,
            re_register_authentication=re_register_authentication,
            discovery_mode=discovery_mode,
            service_port_profile=service_port_profile,
        )

        authentication_config_dto.additional_properties = d
        return authentication_config_dto

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
