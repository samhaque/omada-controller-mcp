from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_vo import OswVO


T = TypeVar("T", bound="OswStackSwitchVO")


@_attrs_define
class OswStackSwitchVO:
    """
    Attributes:
        adopted_switches (list[OswVO] | Unset): Adopted Switches
        detected_switches (list[OswVO] | Unset): Detected Switches
    """

    adopted_switches: list[OswVO] | Unset = UNSET
    detected_switches: list[OswVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adopted_switches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.adopted_switches, Unset):
            adopted_switches = []
            for adopted_switches_item_data in self.adopted_switches:
                adopted_switches_item = adopted_switches_item_data.to_dict()
                adopted_switches.append(adopted_switches_item)

        detected_switches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.detected_switches, Unset):
            detected_switches = []
            for detected_switches_item_data in self.detected_switches:
                detected_switches_item = detected_switches_item_data.to_dict()
                detected_switches.append(detected_switches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adopted_switches is not UNSET:
            field_dict["adoptedSwitches"] = adopted_switches
        if detected_switches is not UNSET:
            field_dict["detectedSwitches"] = detected_switches

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_vo import OswVO

        d = dict(src_dict)
        _adopted_switches = d.pop("adoptedSwitches", UNSET)
        adopted_switches: list[OswVO] | Unset = UNSET
        if _adopted_switches is not UNSET:
            adopted_switches = []
            for adopted_switches_item_data in _adopted_switches:
                adopted_switches_item = OswVO.from_dict(adopted_switches_item_data)

                adopted_switches.append(adopted_switches_item)

        _detected_switches = d.pop("detectedSwitches", UNSET)
        detected_switches: list[OswVO] | Unset = UNSET
        if _detected_switches is not UNSET:
            detected_switches = []
            for detected_switches_item_data in _detected_switches:
                detected_switches_item = OswVO.from_dict(detected_switches_item_data)

                detected_switches.append(detected_switches_item)

        osw_stack_switch_vo = cls(
            adopted_switches=adopted_switches,
            detected_switches=detected_switches,
        )

        osw_stack_switch_vo.additional_properties = d
        return osw_stack_switch_vo

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
