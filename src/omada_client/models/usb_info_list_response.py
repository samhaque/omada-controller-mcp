from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usb_info import UsbInfo


T = TypeVar("T", bound="UsbInfoListResponse")


@_attrs_define
class UsbInfoListResponse:
    """
    Attributes:
        usb_list (list[UsbInfo] | Unset): USB info list.
    """

    usb_list: list[UsbInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usb_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usb_list, Unset):
            usb_list = []
            for usb_list_item_data in self.usb_list:
                usb_list_item = usb_list_item_data.to_dict()
                usb_list.append(usb_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usb_list is not UNSET:
            field_dict["usbList"] = usb_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usb_info import UsbInfo

        d = dict(src_dict)
        _usb_list = d.pop("usbList", UNSET)
        usb_list: list[UsbInfo] | Unset = UNSET
        if _usb_list is not UNSET:
            usb_list = []
            for usb_list_item_data in _usb_list:
                usb_list_item = UsbInfo.from_dict(usb_list_item_data)

                usb_list.append(usb_list_item)

        usb_info_list_response = cls(
            usb_list=usb_list,
        )

        usb_info_list_response.additional_properties = d
        return usb_info_list_response

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
