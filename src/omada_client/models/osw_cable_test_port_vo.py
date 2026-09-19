from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_brief_vo import DeviceBriefVO
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswCableTestPortVO")


@_attrs_define
class OswCableTestPortVO:
    """
    Attributes:
        port (int | Unset): Port Id
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
        type_ (int | Unset): Port type, it should be a value as follows: 1: Copper, 2: Combo, 3: SFP
        name (str | Unset): Port name.
        edit_enable (bool | Unset): It indicates whether the port can run cable test.
        is_upper_port (bool | Unset): It indicates whether the port is upper port.
        is_disabled (bool | Unset): It indicates whether the port is disabled.
        is_stack_port (bool | Unset): It indicates whether the port is stack port
        reasons (list[int] | Unset): Only valid when editEnable is false.It indicates why the port can not run cable
            test. Each item should be a value as follows: -1:uplink port. -2:disabled port. -3:SFP port. -4:console port.
            -5:USB port. -5:Stack port
        downlink_devices (list[DeviceBriefVO] | Unset): Downlink Devices
        is_copper (bool | Unset): Whether the port is copper when the port is combo.
    """

    port: int | Unset = UNSET
    standard_port: OswStandPortVO | Unset = UNSET
    type_: int | Unset = UNSET
    name: str | Unset = UNSET
    edit_enable: bool | Unset = UNSET
    is_upper_port: bool | Unset = UNSET
    is_disabled: bool | Unset = UNSET
    is_stack_port: bool | Unset = UNSET
    reasons: list[int] | Unset = UNSET
    downlink_devices: list[DeviceBriefVO] | Unset = UNSET
    is_copper: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        type_ = self.type_

        name = self.name

        edit_enable = self.edit_enable

        is_upper_port = self.is_upper_port

        is_disabled = self.is_disabled

        is_stack_port = self.is_stack_port

        reasons: list[int] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons

        downlink_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_devices, Unset):
            downlink_devices = []
            for downlink_devices_item_data in self.downlink_devices:
                downlink_devices_item = downlink_devices_item_data.to_dict()
                downlink_devices.append(downlink_devices_item)

        is_copper = self.is_copper

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if edit_enable is not UNSET:
            field_dict["editEnable"] = edit_enable
        if is_upper_port is not UNSET:
            field_dict["isUpperPort"] = is_upper_port
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled
        if is_stack_port is not UNSET:
            field_dict["isStackPort"] = is_stack_port
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if downlink_devices is not UNSET:
            field_dict["downlinkDevices"] = downlink_devices
        if is_copper is not UNSET:
            field_dict["isCopper"] = is_copper

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_brief_vo import DeviceBriefVO
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        _standard_port = d.pop("standardPort", UNSET)
        standard_port: OswStandPortVO | Unset
        if isinstance(_standard_port, Unset):
            standard_port = UNSET
        else:
            standard_port = OswStandPortVO.from_dict(_standard_port)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        edit_enable = d.pop("editEnable", UNSET)

        is_upper_port = d.pop("isUpperPort", UNSET)

        is_disabled = d.pop("isDisabled", UNSET)

        is_stack_port = d.pop("isStackPort", UNSET)

        reasons = cast(list[int], d.pop("reasons", UNSET))

        _downlink_devices = d.pop("downlinkDevices", UNSET)
        downlink_devices: list[DeviceBriefVO] | Unset = UNSET
        if _downlink_devices is not UNSET:
            downlink_devices = []
            for downlink_devices_item_data in _downlink_devices:
                downlink_devices_item = DeviceBriefVO.from_dict(
                    downlink_devices_item_data
                )

                downlink_devices.append(downlink_devices_item)

        is_copper = d.pop("isCopper", UNSET)

        osw_cable_test_port_vo = cls(
            port=port,
            standard_port=standard_port,
            type_=type_,
            name=name,
            edit_enable=edit_enable,
            is_upper_port=is_upper_port,
            is_disabled=is_disabled,
            is_stack_port=is_stack_port,
            reasons=reasons,
            downlink_devices=downlink_devices,
            is_copper=is_copper,
        )

        osw_cable_test_port_vo.additional_properties = d
        return osw_cable_test_port_vo

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
