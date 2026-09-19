from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.uplink_device import UplinkDevice


T = TypeVar("T", bound="MonitorDevice")


@_attrs_define
class MonitorDevice:
    """The device to be verified whether it can be monitored

    Attributes:
        mac (str): The device mac
        id (str | Unset): The monitor device Id
        custom_id (str | Unset): The device Id
        name (str | Unset): The device name
        ip (str | Unset): The device ip
        device_type (int | Unset): The device type
        type_ (str | Unset): The device type.Such as: ap, switch, gateway
        show_model (str | Unset): The device showModel
        special_model (str | Unset): The device specialModel
        model (str | Unset): The device model
        model_version (str | Unset): The device modelVersion
        model_model_version (str | Unset): The device modelModelVersion
        client_flag (bool | Unset): Whether the device is a client
        status_category (int | Unset): Whether the device is online
        client_type (str | Unset): Client type
        monitoring_status (int | Unset): The device monitoringStatus
        recovery_cycles (int | Unset): The device recoveryCycles
        uplink_device (UplinkDevice | Unset): The device uplinkDevice
        eligible_flag (bool | Unset): Whether the device can be monitored
        not_eligible_reason (str | Unset): The reason of the device can't be monitored
    """

    mac: str
    id: str | Unset = UNSET
    custom_id: str | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    device_type: int | Unset = UNSET
    type_: str | Unset = UNSET
    show_model: str | Unset = UNSET
    special_model: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    model_model_version: str | Unset = UNSET
    client_flag: bool | Unset = UNSET
    status_category: int | Unset = UNSET
    client_type: str | Unset = UNSET
    monitoring_status: int | Unset = UNSET
    recovery_cycles: int | Unset = UNSET
    uplink_device: UplinkDevice | Unset = UNSET
    eligible_flag: bool | Unset = UNSET
    not_eligible_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        id = self.id

        custom_id = self.custom_id

        name = self.name

        ip = self.ip

        device_type = self.device_type

        type_ = self.type_

        show_model = self.show_model

        special_model = self.special_model

        model = self.model

        model_version = self.model_version

        model_model_version = self.model_model_version

        client_flag = self.client_flag

        status_category = self.status_category

        client_type = self.client_type

        monitoring_status = self.monitoring_status

        recovery_cycles = self.recovery_cycles

        uplink_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink_device, Unset):
            uplink_device = self.uplink_device.to_dict()

        eligible_flag = self.eligible_flag

        not_eligible_reason = self.not_eligible_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if custom_id is not UNSET:
            field_dict["customId"] = custom_id
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if special_model is not UNSET:
            field_dict["specialModel"] = special_model
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if model_model_version is not UNSET:
            field_dict["modelModelVersion"] = model_model_version
        if client_flag is not UNSET:
            field_dict["clientFlag"] = client_flag
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if monitoring_status is not UNSET:
            field_dict["monitoringStatus"] = monitoring_status
        if recovery_cycles is not UNSET:
            field_dict["recoveryCycles"] = recovery_cycles
        if uplink_device is not UNSET:
            field_dict["uplinkDevice"] = uplink_device
        if eligible_flag is not UNSET:
            field_dict["eligibleFlag"] = eligible_flag
        if not_eligible_reason is not UNSET:
            field_dict["notEligibleReason"] = not_eligible_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.uplink_device import UplinkDevice

        d = dict(src_dict)
        mac = d.pop("mac")

        id = d.pop("id", UNSET)

        custom_id = d.pop("customId", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        device_type = d.pop("deviceType", UNSET)

        type_ = d.pop("type", UNSET)

        show_model = d.pop("showModel", UNSET)

        special_model = d.pop("specialModel", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        model_model_version = d.pop("modelModelVersion", UNSET)

        client_flag = d.pop("clientFlag", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        client_type = d.pop("clientType", UNSET)

        monitoring_status = d.pop("monitoringStatus", UNSET)

        recovery_cycles = d.pop("recoveryCycles", UNSET)

        _uplink_device = d.pop("uplinkDevice", UNSET)
        uplink_device: UplinkDevice | Unset
        if isinstance(_uplink_device, Unset):
            uplink_device = UNSET
        else:
            uplink_device = UplinkDevice.from_dict(_uplink_device)

        eligible_flag = d.pop("eligibleFlag", UNSET)

        not_eligible_reason = d.pop("notEligibleReason", UNSET)

        monitor_device = cls(
            mac=mac,
            id=id,
            custom_id=custom_id,
            name=name,
            ip=ip,
            device_type=device_type,
            type_=type_,
            show_model=show_model,
            special_model=special_model,
            model=model,
            model_version=model_version,
            model_model_version=model_model_version,
            client_flag=client_flag,
            status_category=status_category,
            client_type=client_type,
            monitoring_status=monitoring_status,
            recovery_cycles=recovery_cycles,
            uplink_device=uplink_device,
            eligible_flag=eligible_flag,
            not_eligible_reason=not_eligible_reason,
        )

        monitor_device.additional_properties = d
        return monitor_device

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
