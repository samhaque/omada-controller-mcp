from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.ppsk_setting import PpskSetting


T = TypeVar("T", bound="AddPSKsOpenApiVO")


@_attrs_define
class AddPSKsOpenApiVO:
    """
    Attributes:
        ppsk_list (list[PpskSetting]): PSK entries that need to be added to the PPSK Profile
    """

    ppsk_list: list[PpskSetting]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ppsk_list = []
        for ppsk_list_item_data in self.ppsk_list:
            ppsk_list_item = ppsk_list_item_data.to_dict()
            ppsk_list.append(ppsk_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ppskList": ppsk_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ppsk_setting import PpskSetting

        d = dict(src_dict)
        ppsk_list = []
        _ppsk_list = d.pop("ppskList")
        for ppsk_list_item_data in _ppsk_list:
            ppsk_list_item = PpskSetting.from_dict(ppsk_list_item_data)

            ppsk_list.append(ppsk_list_item)

        add_ps_ks_open_api_vo = cls(
            ppsk_list=ppsk_list,
        )

        add_ps_ks_open_api_vo.additional_properties = d
        return add_ps_ks_open_api_vo

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
