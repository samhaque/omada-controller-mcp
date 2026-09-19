from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_autofind_config_dto_password_type import (
    OnuAutofindConfigDTOPasswordType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnuAutofindConfigDTO")


@_attrs_define
class OnuAutofindConfigDTO:
    """Content

    Attributes:
        key (str | Unset): Unique identifier for entry
        port_id (str | Unset): Automatic discovery of the PON port ID corresponding to the ONT
        serial_number (str | Unset): SerialNumber of ONU, serialNumber should contain 12, 13, or 16 characters, in the
            format XXXXXXXXXXXX,XXXX-XXXXXXXX,XXXXXXXXXXXXXXXX
        mac_address (str | Unset): Mac address of ONU
        password_type (OnuAutofindConfigDTOPasswordType | Unset): Indicates the password type reported by the automatic
            discovery of the ONT.PasswordType should be a value as follows：ASCII,HEX
        password (str | Unset): Authentication password set by automatic discovery of the ONT, password should contain
            ASCII characters from \\x21 to \\x7e and 1 to 20 hexadecimal digits
        loid (str | Unset): Loid set by automatic discovery of the ONT, loid should be 1-32 characters, including
            letters, numbers, and symbols (-@_:/.).
        loid_password (str | Unset): Loid password set by automatic discovery of the ONT,loidPassword should contain
            ASCII characters from \\x21 to \\x7e
        hardware_version (str | Unset): Hardware version of the automatically discovered ONT
        software_version (str | Unset): Software version of the automatically discovered ONT
        vendor_id (str | Unset): Matching ONT vendor ID, vendorId should contain 1 to 4 ASCII characters from \\x21 to
            \\x7e
        equipment_id (str | Unset): ONT device ID should contain 1 to 20 characters in ASCII code from \\x21 to \\x7e.
    """

    key: str | Unset = UNSET
    port_id: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    password_type: OnuAutofindConfigDTOPasswordType | Unset = UNSET
    password: str | Unset = UNSET
    loid: str | Unset = UNSET
    loid_password: str | Unset = UNSET
    hardware_version: str | Unset = UNSET
    software_version: str | Unset = UNSET
    vendor_id: str | Unset = UNSET
    equipment_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        port_id = self.port_id

        serial_number = self.serial_number

        mac_address = self.mac_address

        password_type: str | Unset = UNSET
        if not isinstance(self.password_type, Unset):
            password_type = self.password_type.value

        password = self.password

        loid = self.loid

        loid_password = self.loid_password

        hardware_version = self.hardware_version

        software_version = self.software_version

        vendor_id = self.vendor_id

        equipment_id = self.equipment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if port_id is not UNSET:
            field_dict["portId"] = port_id
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
        if hardware_version is not UNSET:
            field_dict["hardwareVersion"] = hardware_version
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if vendor_id is not UNSET:
            field_dict["vendorId"] = vendor_id
        if equipment_id is not UNSET:
            field_dict["equipmentId"] = equipment_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        port_id = d.pop("portId", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        _password_type = d.pop("passwordType", UNSET)
        password_type: OnuAutofindConfigDTOPasswordType | Unset
        if isinstance(_password_type, Unset):
            password_type = UNSET
        else:
            password_type = OnuAutofindConfigDTOPasswordType(_password_type)

        password = d.pop("password", UNSET)

        loid = d.pop("loid", UNSET)

        loid_password = d.pop("loidPassword", UNSET)

        hardware_version = d.pop("hardwareVersion", UNSET)

        software_version = d.pop("softwareVersion", UNSET)

        vendor_id = d.pop("vendorId", UNSET)

        equipment_id = d.pop("equipmentId", UNSET)

        onu_autofind_config_dto = cls(
            key=key,
            port_id=port_id,
            serial_number=serial_number,
            mac_address=mac_address,
            password_type=password_type,
            password=password,
            loid=loid,
            loid_password=loid_password,
            hardware_version=hardware_version,
            software_version=software_version,
            vendor_id=vendor_id,
            equipment_id=equipment_id,
        )

        onu_autofind_config_dto.additional_properties = d
        return onu_autofind_config_dto

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
