from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_capacity import DeviceCapacity
    from ..models.disk_condition import DiskCondition


T = TypeVar("T", bound="ControllerStatus")


@_attrs_define
class ControllerStatus:
    """
    Attributes:
        name (str | Unset): Controller Name
        mac_address (str | Unset): MAC address, should be a valid MAC address format, e.g. AA-BB-CC-DD-11-22
        time_zone (str | Unset): For the values of timeZone, refer to section 5.1 of the Open API Access Guide.
        system_time (int | Unset): System time
        up_time (int | Unset): Up time (unit: s)
        controller_version (str | Unset): Controller version
        category (str | Unset): Category should be a value as follows: localPro; local; advanced; pro.
        model (str | Unset): Controller Model
        firmware_version (str | Unset): Firmware Version
        hwc_storage (list[DiskCondition] | Unset): Hardware Storage
        device_capacity (DeviceCapacity | Unset): Device capacity
        sn (str | Unset): Device serial number
        area_info (str | Unset): Storage area information
        inform_url (str | Unset): Inform URL
        controller_type (int | Unset): Controller type should be a value as follows: 0: Windows; 1: Linux; 10: OC200;
            11: OC300; 12: ER7212PC; 13: OC400; 20: CBC.
    """

    name: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    system_time: int | Unset = UNSET
    up_time: int | Unset = UNSET
    controller_version: str | Unset = UNSET
    category: str | Unset = UNSET
    model: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    hwc_storage: list[DiskCondition] | Unset = UNSET
    device_capacity: DeviceCapacity | Unset = UNSET
    sn: str | Unset = UNSET
    area_info: str | Unset = UNSET
    inform_url: str | Unset = UNSET
    controller_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac_address = self.mac_address

        time_zone = self.time_zone

        system_time = self.system_time

        up_time = self.up_time

        controller_version = self.controller_version

        category = self.category

        model = self.model

        firmware_version = self.firmware_version

        hwc_storage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hwc_storage, Unset):
            hwc_storage = []
            for hwc_storage_item_data in self.hwc_storage:
                hwc_storage_item = hwc_storage_item_data.to_dict()
                hwc_storage.append(hwc_storage_item)

        device_capacity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_capacity, Unset):
            device_capacity = self.device_capacity.to_dict()

        sn = self.sn

        area_info = self.area_info

        inform_url = self.inform_url

        controller_type = self.controller_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if system_time is not UNSET:
            field_dict["systemTime"] = system_time
        if up_time is not UNSET:
            field_dict["upTime"] = up_time
        if controller_version is not UNSET:
            field_dict["controllerVersion"] = controller_version
        if category is not UNSET:
            field_dict["category"] = category
        if model is not UNSET:
            field_dict["model"] = model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if hwc_storage is not UNSET:
            field_dict["hwcStorage"] = hwc_storage
        if device_capacity is not UNSET:
            field_dict["deviceCapacity"] = device_capacity
        if sn is not UNSET:
            field_dict["sn"] = sn
        if area_info is not UNSET:
            field_dict["areaInfo"] = area_info
        if inform_url is not UNSET:
            field_dict["informUrl"] = inform_url
        if controller_type is not UNSET:
            field_dict["controllerType"] = controller_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_capacity import DeviceCapacity
        from ..models.disk_condition import DiskCondition

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        system_time = d.pop("systemTime", UNSET)

        up_time = d.pop("upTime", UNSET)

        controller_version = d.pop("controllerVersion", UNSET)

        category = d.pop("category", UNSET)

        model = d.pop("model", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        _hwc_storage = d.pop("hwcStorage", UNSET)
        hwc_storage: list[DiskCondition] | Unset = UNSET
        if _hwc_storage is not UNSET:
            hwc_storage = []
            for hwc_storage_item_data in _hwc_storage:
                hwc_storage_item = DiskCondition.from_dict(hwc_storage_item_data)

                hwc_storage.append(hwc_storage_item)

        _device_capacity = d.pop("deviceCapacity", UNSET)
        device_capacity: DeviceCapacity | Unset
        if isinstance(_device_capacity, Unset):
            device_capacity = UNSET
        else:
            device_capacity = DeviceCapacity.from_dict(_device_capacity)

        sn = d.pop("sn", UNSET)

        area_info = d.pop("areaInfo", UNSET)

        inform_url = d.pop("informUrl", UNSET)

        controller_type = d.pop("controllerType", UNSET)

        controller_status = cls(
            name=name,
            mac_address=mac_address,
            time_zone=time_zone,
            system_time=system_time,
            up_time=up_time,
            controller_version=controller_version,
            category=category,
            model=model,
            firmware_version=firmware_version,
            hwc_storage=hwc_storage,
            device_capacity=device_capacity,
            sn=sn,
            area_info=area_info,
            inform_url=inform_url,
            controller_type=controller_type,
        )

        controller_status.additional_properties = d
        return controller_status

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
