from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="TagOutItemOpenApiVO")


@_attrs_define
class TagOutItemOpenApiVO:
    """The Tag Outbound configuration of class type, must contains class 1, class 2, class 3 and others.

    Attributes:
        class_type (int): Class type should be a value as follows: 1: class 1, 2: class 2, 3: class 3, 0: others.
        enable (bool): The status of Class Type, valid value is true or false.
        dscp (str): The DSCP value selected in the Precedence configuration should be a value as follows: 8: IP
            precedence 1; 16: IP precedence 2; 24: IP precedence 3; 32: IP precedence 4; 40: IP precedence 5; 48: IP
            precedence 6; 56: IP precedence 7; 10: AF Class 1 (Low Drop); 12: AF Class 1 (Medium Drop); 14: AF Class 1 (High
            Drop); 18: AF Class 2 (Low Drop); 20: AF Class 2 (Medium Drop); 22: AF Class 2 (High Drop); 26: AF Class 3 (Low
            Drop); 28: AF Class 3 (Medium Drop); 30: AF Class 3 (High Drop); 34: AF Class 4 (Low Drop); 36: AF Class 4
            (Medium Drop); 38: AF Class 4 (High Drop); 46: EF Class.
    """

    class_type: int
    enable: bool
    dscp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_type = self.class_type

        enable = self.enable

        dscp = self.dscp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "classType": class_type,
                "enable": enable,
                "dscp": dscp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        class_type = d.pop("classType")

        enable = d.pop("enable")

        dscp = d.pop("dscp")

        tag_out_item_open_api_vo = cls(
            class_type=class_type,
            enable=enable,
            dscp=dscp,
        )

        tag_out_item_open_api_vo.additional_properties = d
        return tag_out_item_open_api_vo

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
