from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_information_config_dto_active_status import (
    OnuInformationConfigDTOActiveStatus,
)
from ..models.onu_information_config_dto_admin_status import (
    OnuInformationConfigDTOAdminStatus,
)
from ..models.onu_information_config_dto_config_status import (
    OnuInformationConfigDTOConfigStatus,
)
from ..models.onu_information_config_dto_match_status import (
    OnuInformationConfigDTOMatchStatus,
)
from ..models.onu_information_config_dto_online_status import (
    OnuInformationConfigDTOOnlineStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnuInformationConfigDTO")


@_attrs_define
class OnuInformationConfigDTO:
    """Content

    Attributes:
        key (str | Unset): Identifier of ONU
        pon_port_id (int | Unset): PON port ID of the registered and online ONT
        pon_port_str (str | Unset): String form of pon port.e.g.,PON 1/2/1
        onu_id (int | Unset): Onu Id should be within the range of 0 to 127
        onu_description (str | Unset): Description of ONU.OnuDescription should be 1-32 characters, including letters,
            numbers, and symbols (-@_:/.).
        serial_number (str | Unset): SerialNumber should contain 12, 13, or 16 characters, formatted as
            `XXXXXXXXXXXX`,'XXXX-XXXXXXXX','XXXXXXXXXXXXXXXX'.
        mac_address (str | Unset): Mac address of ONU
        line_profile (str | Unset): Line profile.Display in the format: Line_Profile_Name + Line_Profile_ID.
        service_profile (str | Unset): Service profile.Display in the format: Service_Profile_Name + Service_Profile_ID.
        service_port_profile (str | Unset): Service port profile.Display in the format: Service_Port_Profile_Name +
            Service_Port_Profile_ID.
        admin_status (OnuInformationConfigDTOAdminStatus | Unset): Admin status should be a value as
            follows:ACTIVATE,DEACTIVATE
        online_status (OnuInformationConfigDTOOnlineStatus | Unset): Online status should be a value as
            follows:ONLINE,OFFLINE
        config_status (OnuInformationConfigDTOConfigStatus | Unset): Config status should be a value as follows:SUCCESS:
            Configuration successfully delivered and recognized by the ONU.FAILED: Configuration not successfully delivered
            or not recognized by the ONU.
        match_status (OnuInformationConfigDTOMatchStatus | Unset): Match status should be a value as follows:MATCH: ONU
            hardware capabilities are consistent with the bound service template.MISMATCH: ONU hardware capabilities are
            inconsistent with the bound service template.
        active_status (OnuInformationConfigDTOActiveStatus | Unset): Active status should be a value as follows:ACTIVE:
            ONU is in an active state, capable of data communication and carrying services.
            INACTIVE: ONU is in an inactive state, possibly due to unactivated configuration, being offline, configuration
            failure, or mismatched configuration.
        equipment_id (str | Unset): Matched ONU device ID, equipmentId should contain 1 to 20 characters in ASCII code
            from \\x21 to \\x7e.
        software_version (OnuInformationConfigDTO | Unset): Content
        hardware_version (str | Unset): Hardware version of the ONU, hardwareVersion should contain 1 to 20 characters,
            including uppercase and lowercase letters, numbers, and the symbols -@_:/.
        received_optical_power (str | Unset): ONU's received power, in dBm.
        transmitted_optical_power (str | Unset): ONU's transmission power, in dBm.
        soft_ware_version (str | Unset):
    """

    key: str | Unset = UNSET
    pon_port_id: int | Unset = UNSET
    pon_port_str: str | Unset = UNSET
    onu_id: int | Unset = UNSET
    onu_description: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    line_profile: str | Unset = UNSET
    service_profile: str | Unset = UNSET
    service_port_profile: str | Unset = UNSET
    admin_status: OnuInformationConfigDTOAdminStatus | Unset = UNSET
    online_status: OnuInformationConfigDTOOnlineStatus | Unset = UNSET
    config_status: OnuInformationConfigDTOConfigStatus | Unset = UNSET
    match_status: OnuInformationConfigDTOMatchStatus | Unset = UNSET
    active_status: OnuInformationConfigDTOActiveStatus | Unset = UNSET
    equipment_id: str | Unset = UNSET
    software_version: OnuInformationConfigDTO | Unset = UNSET
    hardware_version: str | Unset = UNSET
    received_optical_power: str | Unset = UNSET
    transmitted_optical_power: str | Unset = UNSET
    soft_ware_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        pon_port_id = self.pon_port_id

        pon_port_str = self.pon_port_str

        onu_id = self.onu_id

        onu_description = self.onu_description

        serial_number = self.serial_number

        mac_address = self.mac_address

        line_profile = self.line_profile

        service_profile = self.service_profile

        service_port_profile = self.service_port_profile

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

        equipment_id = self.equipment_id

        software_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.software_version, Unset):
            software_version = self.software_version.to_dict()

        hardware_version = self.hardware_version

        received_optical_power = self.received_optical_power

        transmitted_optical_power = self.transmitted_optical_power

        soft_ware_version = self.soft_ware_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if pon_port_id is not UNSET:
            field_dict["ponPortId"] = pon_port_id
        if pon_port_str is not UNSET:
            field_dict["ponPortStr"] = pon_port_str
        if onu_id is not UNSET:
            field_dict["onuId"] = onu_id
        if onu_description is not UNSET:
            field_dict["onuDescription"] = onu_description
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if line_profile is not UNSET:
            field_dict["lineProfile"] = line_profile
        if service_profile is not UNSET:
            field_dict["serviceProfile"] = service_profile
        if service_port_profile is not UNSET:
            field_dict["servicePortProfile"] = service_port_profile
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
        if equipment_id is not UNSET:
            field_dict["equipmentId"] = equipment_id
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if hardware_version is not UNSET:
            field_dict["hardwareVersion"] = hardware_version
        if received_optical_power is not UNSET:
            field_dict["receivedOpticalPower"] = received_optical_power
        if transmitted_optical_power is not UNSET:
            field_dict["transmittedOpticalPower"] = transmitted_optical_power
        if soft_ware_version is not UNSET:
            field_dict["softWareVersion"] = soft_ware_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        pon_port_id = d.pop("ponPortId", UNSET)

        pon_port_str = d.pop("ponPortStr", UNSET)

        onu_id = d.pop("onuId", UNSET)

        onu_description = d.pop("onuDescription", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        line_profile = d.pop("lineProfile", UNSET)

        service_profile = d.pop("serviceProfile", UNSET)

        service_port_profile = d.pop("servicePortProfile", UNSET)

        _admin_status = d.pop("adminStatus", UNSET)
        admin_status: OnuInformationConfigDTOAdminStatus | Unset
        if isinstance(_admin_status, Unset):
            admin_status = UNSET
        else:
            admin_status = OnuInformationConfigDTOAdminStatus(_admin_status)

        _online_status = d.pop("onlineStatus", UNSET)
        online_status: OnuInformationConfigDTOOnlineStatus | Unset
        if isinstance(_online_status, Unset):
            online_status = UNSET
        else:
            online_status = OnuInformationConfigDTOOnlineStatus(_online_status)

        _config_status = d.pop("configStatus", UNSET)
        config_status: OnuInformationConfigDTOConfigStatus | Unset
        if isinstance(_config_status, Unset):
            config_status = UNSET
        else:
            config_status = OnuInformationConfigDTOConfigStatus(_config_status)

        _match_status = d.pop("matchStatus", UNSET)
        match_status: OnuInformationConfigDTOMatchStatus | Unset
        if isinstance(_match_status, Unset):
            match_status = UNSET
        else:
            match_status = OnuInformationConfigDTOMatchStatus(_match_status)

        _active_status = d.pop("activeStatus", UNSET)
        active_status: OnuInformationConfigDTOActiveStatus | Unset
        if isinstance(_active_status, Unset):
            active_status = UNSET
        else:
            active_status = OnuInformationConfigDTOActiveStatus(_active_status)

        equipment_id = d.pop("equipmentId", UNSET)

        _software_version = d.pop("softwareVersion", UNSET)
        software_version: OnuInformationConfigDTO | Unset
        if isinstance(_software_version, Unset):
            software_version = UNSET
        else:
            software_version = OnuInformationConfigDTO.from_dict(_software_version)

        hardware_version = d.pop("hardwareVersion", UNSET)

        received_optical_power = d.pop("receivedOpticalPower", UNSET)

        transmitted_optical_power = d.pop("transmittedOpticalPower", UNSET)

        soft_ware_version = d.pop("softWareVersion", UNSET)

        onu_information_config_dto = cls(
            key=key,
            pon_port_id=pon_port_id,
            pon_port_str=pon_port_str,
            onu_id=onu_id,
            onu_description=onu_description,
            serial_number=serial_number,
            mac_address=mac_address,
            line_profile=line_profile,
            service_profile=service_profile,
            service_port_profile=service_port_profile,
            admin_status=admin_status,
            online_status=online_status,
            config_status=config_status,
            match_status=match_status,
            active_status=active_status,
            equipment_id=equipment_id,
            software_version=software_version,
            hardware_version=hardware_version,
            received_optical_power=received_optical_power,
            transmitted_optical_power=transmitted_optical_power,
            soft_ware_version=soft_ware_version,
        )

        onu_information_config_dto.additional_properties = d
        return onu_information_config_dto

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
