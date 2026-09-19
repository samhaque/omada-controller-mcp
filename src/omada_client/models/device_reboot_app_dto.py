from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceRebootAppDTO")


@_attrs_define
class DeviceRebootAppDTO:
    """
    Attributes:
        mac (str): List of device keys for devices to be restarted.
        save_current_config (int): Whether to save the current configuration.
        slots (list[int] | Unset): Slot ID list should be within the range of 1 to 4
        issu (int | Unset): Perform non-disruptive software upgrades, first upgrading the backup control board, then
            switching the primary and backup roles, and subsequently upgrading the other control board. Issu should be a
            value as follows: 1:ENABLE;0:DISABLE, effective only on the primary control board.
        reboot_id (str | Unset): Generated device batch restart ID.
        token (str | Unset): User token
        control_type (int | Unset): Types of user access to the Omada Controller, such as local web access, etc.
        status (int | Unset): Status
        status_category (int | Unset): Status category.StatusCategory should be a value as
            follows:0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated.
    """

    mac: str
    save_current_config: int
    slots: list[int] | Unset = UNSET
    issu: int | Unset = UNSET
    reboot_id: str | Unset = UNSET
    token: str | Unset = UNSET
    control_type: int | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        save_current_config = self.save_current_config

        slots: list[int] | Unset = UNSET
        if not isinstance(self.slots, Unset):
            slots = self.slots

        issu = self.issu

        reboot_id = self.reboot_id

        token = self.token

        control_type = self.control_type

        status = self.status

        status_category = self.status_category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "saveCurrentConfig": save_current_config,
            }
        )
        if slots is not UNSET:
            field_dict["slots"] = slots
        if issu is not UNSET:
            field_dict["issu"] = issu
        if reboot_id is not UNSET:
            field_dict["rebootId"] = reboot_id
        if token is not UNSET:
            field_dict["token"] = token
        if control_type is not UNSET:
            field_dict["controlType"] = control_type
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        save_current_config = d.pop("saveCurrentConfig")

        slots = cast(list[int], d.pop("slots", UNSET))

        issu = d.pop("issu", UNSET)

        reboot_id = d.pop("rebootId", UNSET)

        token = d.pop("token", UNSET)

        control_type = d.pop("controlType", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        device_reboot_app_dto = cls(
            mac=mac,
            save_current_config=save_current_config,
            slots=slots,
            issu=issu,
            reboot_id=reboot_id,
            token=token,
            control_type=control_type,
            status=status,
            status_category=status_category,
        )

        device_reboot_app_dto.additional_properties = d
        return device_reboot_app_dto

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
