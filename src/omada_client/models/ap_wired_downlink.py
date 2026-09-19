from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_down_link_status_vo import ApDownLinkStatusVO


T = TypeVar("T", bound="ApWiredDownlink")


@_attrs_define
class ApWiredDownlink:
    """
    Attributes:
        wired_downlink_list (list[ApDownLinkStatusVO] | Unset): Wired downlink device list
    """

    wired_downlink_list: list[ApDownLinkStatusVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wired_downlink_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wired_downlink_list, Unset):
            wired_downlink_list = []
            for wired_downlink_list_item_data in self.wired_downlink_list:
                wired_downlink_list_item = wired_downlink_list_item_data.to_dict()
                wired_downlink_list.append(wired_downlink_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wired_downlink_list is not UNSET:
            field_dict["wiredDownlinkList"] = wired_downlink_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_down_link_status_vo import ApDownLinkStatusVO

        d = dict(src_dict)
        _wired_downlink_list = d.pop("wiredDownlinkList", UNSET)
        wired_downlink_list: list[ApDownLinkStatusVO] | Unset = UNSET
        if _wired_downlink_list is not UNSET:
            wired_downlink_list = []
            for wired_downlink_list_item_data in _wired_downlink_list:
                wired_downlink_list_item = ApDownLinkStatusVO.from_dict(
                    wired_downlink_list_item_data
                )

                wired_downlink_list.append(wired_downlink_list_item)

        ap_wired_downlink = cls(
            wired_downlink_list=wired_downlink_list,
        )

        ap_wired_downlink.additional_properties = d
        return ap_wired_downlink

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
