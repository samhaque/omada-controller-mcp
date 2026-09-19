from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.switch_alert_vo import SwitchAlertVO
    from ..models.switch_reboot_times_vo import SwitchRebootTimesVO


T = TypeVar("T", bound="SwitchAlertRebootVO")


@_attrs_define
class SwitchAlertRebootVO:
    """
    Attributes:
        switch_alert (SwitchAlertVO | Unset): Switch alert
        switch_reboot_times (SwitchRebootTimesVO | Unset): Switch reboot times
    """

    switch_alert: SwitchAlertVO | Unset = UNSET
    switch_reboot_times: SwitchRebootTimesVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        switch_alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_alert, Unset):
            switch_alert = self.switch_alert.to_dict()

        switch_reboot_times: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_reboot_times, Unset):
            switch_reboot_times = self.switch_reboot_times.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if switch_alert is not UNSET:
            field_dict["switchAlert"] = switch_alert
        if switch_reboot_times is not UNSET:
            field_dict["switchRebootTimes"] = switch_reboot_times

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.switch_alert_vo import SwitchAlertVO
        from ..models.switch_reboot_times_vo import SwitchRebootTimesVO

        d = dict(src_dict)
        _switch_alert = d.pop("switchAlert", UNSET)
        switch_alert: SwitchAlertVO | Unset
        if isinstance(_switch_alert, Unset):
            switch_alert = UNSET
        else:
            switch_alert = SwitchAlertVO.from_dict(_switch_alert)

        _switch_reboot_times = d.pop("switchRebootTimes", UNSET)
        switch_reboot_times: SwitchRebootTimesVO | Unset
        if isinstance(_switch_reboot_times, Unset):
            switch_reboot_times = UNSET
        else:
            switch_reboot_times = SwitchRebootTimesVO.from_dict(_switch_reboot_times)

        switch_alert_reboot_vo = cls(
            switch_alert=switch_alert,
            switch_reboot_times=switch_reboot_times,
        )

        switch_alert_reboot_vo.additional_properties = d
        return switch_alert_reboot_vo

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
