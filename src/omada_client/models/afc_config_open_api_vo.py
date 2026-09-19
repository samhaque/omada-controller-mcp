from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AfcConfigOpenApiVO")


@_attrs_define
class AfcConfigOpenApiVO:
    """
    Attributes:
        support_afc (bool | Unset): Indicates whether the device supports AFC
        enable (bool | Unset): Whether to enable AFC
    """

    support_afc: bool | Unset = UNSET
    enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_afc = self.support_afc

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support_afc is not UNSET:
            field_dict["supportAfc"] = support_afc
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support_afc = d.pop("supportAfc", UNSET)

        enable = d.pop("enable", UNSET)

        afc_config_open_api_vo = cls(
            support_afc=support_afc,
            enable=enable,
        )

        afc_config_open_api_vo.additional_properties = d
        return afc_config_open_api_vo

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
