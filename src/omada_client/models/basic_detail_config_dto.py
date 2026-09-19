from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.basic_detail_config_dto_active_status import (
    BasicDetailConfigDTOActiveStatus,
)
from ..models.basic_detail_config_dto_admin_status import (
    BasicDetailConfigDTOAdminStatus,
)
from ..models.basic_detail_config_dto_config_status import (
    BasicDetailConfigDTOConfigStatus,
)
from ..models.basic_detail_config_dto_match_status import (
    BasicDetailConfigDTOMatchStatus,
)
from ..models.basic_detail_config_dto_online_status import (
    BasicDetailConfigDTOOnlineStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicDetailConfigDTO")


@_attrs_define
class BasicDetailConfigDTO:
    """
    Attributes:
        equipment_id (str): ONT device ID should contain 1 to 20 characters in ASCII code from \\x21 to \\x7e.
        onu_description (str | Unset): ONU description.onuDescription should contain 0 to 32 characters, including
            uppercase and lowercase letters, numbers, and the symbols -@_:/.
        serial_number (str | Unset): SerialNumber of ONU should contain 12, 13, or 16 characters, in the format
            XXXXXXXXXXXX ,XXXX-XXXXXXXX,XXXXXXXXXXXXXXXX
        mac_address (str | Unset): Mac address of ONU
        vendor_id (str | Unset): The matching ONT vendor ID,vendorId should contain 1 to 4 characters in ASCII, with
            character range from \\x21 to \\x7e.
        admin_status (BasicDetailConfigDTOAdminStatus | Unset): Admin status should be a value as
            follows:ACTIVATE,DEACTIVATE
        online_status (BasicDetailConfigDTOOnlineStatus | Unset): Online status should be a value as
            follows:ONLINE,OFFLINE,UPGRADING
        config_status (BasicDetailConfigDTOConfigStatus | Unset): Config status should be a value as follows:SUCCESS:
            Configuration successfully delivered and recognized by the ONU.FAILED: Configuration not successfully delivered
            or not recognized by the ONU.
        match_status (BasicDetailConfigDTOMatchStatus | Unset): Match status should be a value as follows:MATCH: ONU
            hardware capabilities are consistent with the bound service template.MISMATCH: ONU hardware capabilities are
            inconsistent with the bound service template.
        active_status (BasicDetailConfigDTOActiveStatus | Unset): Active status should be a value as follows:ACTIVE: ONU
            is in an active state, capable of data communication and carrying services.
            INACTIVE: ONU is in an inactive state, possibly due to unactivated configuration, being offline, configuration
            failure, or mismatched configuration.
        onu_distance (int | Unset): Distance between ONU and OLT should be within the range of  0 to 20,000 m
        online_time (str | Unset): Duration of ONU registration and online status, format: hh:mm:ss.
        hardware_version (str | Unset): Hardware version of the ONU, hardwareVersion should contain 1 to 20 characters,
            including uppercase and lowercase letters, numbers, and the symbols -@_:/.
        line_profile (str | Unset): LineProfile is displayed in the format id(name)
        service_profile (str | Unset): ServiceProfile is displayed in the format id(name)
    """

    equipment_id: str
    onu_description: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    vendor_id: str | Unset = UNSET
    admin_status: BasicDetailConfigDTOAdminStatus | Unset = UNSET
    online_status: BasicDetailConfigDTOOnlineStatus | Unset = UNSET
    config_status: BasicDetailConfigDTOConfigStatus | Unset = UNSET
    match_status: BasicDetailConfigDTOMatchStatus | Unset = UNSET
    active_status: BasicDetailConfigDTOActiveStatus | Unset = UNSET
    onu_distance: int | Unset = UNSET
    online_time: str | Unset = UNSET
    hardware_version: str | Unset = UNSET
    line_profile: str | Unset = UNSET
    service_profile: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        equipment_id = self.equipment_id

        onu_description = self.onu_description

        serial_number = self.serial_number

        mac_address = self.mac_address

        vendor_id = self.vendor_id

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

        onu_distance = self.onu_distance

        online_time = self.online_time

        hardware_version = self.hardware_version

        line_profile = self.line_profile

        service_profile = self.service_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "equipmentId": equipment_id,
            }
        )
        if onu_description is not UNSET:
            field_dict["onuDescription"] = onu_description
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if vendor_id is not UNSET:
            field_dict["vendorId"] = vendor_id
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
        if onu_distance is not UNSET:
            field_dict["onuDistance"] = onu_distance
        if online_time is not UNSET:
            field_dict["onlineTime"] = online_time
        if hardware_version is not UNSET:
            field_dict["hardwareVersion"] = hardware_version
        if line_profile is not UNSET:
            field_dict["lineProfile"] = line_profile
        if service_profile is not UNSET:
            field_dict["serviceProfile"] = service_profile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        equipment_id = d.pop("equipmentId")

        onu_description = d.pop("onuDescription", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        vendor_id = d.pop("vendorId", UNSET)

        _admin_status = d.pop("adminStatus", UNSET)
        admin_status: BasicDetailConfigDTOAdminStatus | Unset
        if isinstance(_admin_status, Unset):
            admin_status = UNSET
        else:
            admin_status = BasicDetailConfigDTOAdminStatus(_admin_status)

        _online_status = d.pop("onlineStatus", UNSET)
        online_status: BasicDetailConfigDTOOnlineStatus | Unset
        if isinstance(_online_status, Unset):
            online_status = UNSET
        else:
            online_status = BasicDetailConfigDTOOnlineStatus(_online_status)

        _config_status = d.pop("configStatus", UNSET)
        config_status: BasicDetailConfigDTOConfigStatus | Unset
        if isinstance(_config_status, Unset):
            config_status = UNSET
        else:
            config_status = BasicDetailConfigDTOConfigStatus(_config_status)

        _match_status = d.pop("matchStatus", UNSET)
        match_status: BasicDetailConfigDTOMatchStatus | Unset
        if isinstance(_match_status, Unset):
            match_status = UNSET
        else:
            match_status = BasicDetailConfigDTOMatchStatus(_match_status)

        _active_status = d.pop("activeStatus", UNSET)
        active_status: BasicDetailConfigDTOActiveStatus | Unset
        if isinstance(_active_status, Unset):
            active_status = UNSET
        else:
            active_status = BasicDetailConfigDTOActiveStatus(_active_status)

        onu_distance = d.pop("onuDistance", UNSET)

        online_time = d.pop("onlineTime", UNSET)

        hardware_version = d.pop("hardwareVersion", UNSET)

        line_profile = d.pop("lineProfile", UNSET)

        service_profile = d.pop("serviceProfile", UNSET)

        basic_detail_config_dto = cls(
            equipment_id=equipment_id,
            onu_description=onu_description,
            serial_number=serial_number,
            mac_address=mac_address,
            vendor_id=vendor_id,
            admin_status=admin_status,
            online_status=online_status,
            config_status=config_status,
            match_status=match_status,
            active_status=active_status,
            onu_distance=onu_distance,
            online_time=online_time,
            hardware_version=hardware_version,
            line_profile=line_profile,
            service_profile=service_profile,
        )

        basic_detail_config_dto.additional_properties = d
        return basic_detail_config_dto

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
