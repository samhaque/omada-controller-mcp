from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dot1XEapPortInfoOpenApiVO")


@_attrs_define
class Dot1XEapPortInfoOpenApiVO:
    """EAP port information

    Attributes:
        port (str | Unset): Port number
        dot_1_x_enable (bool | Unset): 802.1x enable status
        mab_enable (bool | Unset): MAB enable status
        support_dot_1_x (bool | Unset): Whether this port support configuring dot1x.
    """

    port: str | Unset = UNSET
    dot_1_x_enable: bool | Unset = UNSET
    mab_enable: bool | Unset = UNSET
    support_dot_1_x: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        dot_1_x_enable = self.dot_1_x_enable

        mab_enable = self.mab_enable

        support_dot_1_x = self.support_dot_1_x

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if dot_1_x_enable is not UNSET:
            field_dict["dot1xEnable"] = dot_1_x_enable
        if mab_enable is not UNSET:
            field_dict["mabEnable"] = mab_enable
        if support_dot_1_x is not UNSET:
            field_dict["supportDot1x"] = support_dot_1_x

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        dot_1_x_enable = d.pop("dot1xEnable", UNSET)

        mab_enable = d.pop("mabEnable", UNSET)

        support_dot_1_x = d.pop("supportDot1x", UNSET)

        dot_1x_eap_port_info_open_api_vo = cls(
            port=port,
            dot_1_x_enable=dot_1_x_enable,
            mab_enable=mab_enable,
            support_dot_1_x=support_dot_1_x,
        )

        dot_1x_eap_port_info_open_api_vo.additional_properties = d
        return dot_1x_eap_port_info_open_api_vo

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
