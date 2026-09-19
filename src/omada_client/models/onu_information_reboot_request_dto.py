from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.single_onu_reboot_request_dto import SingleOnuRebootRequestDTO


T = TypeVar("T", bound="OnuInformationRebootRequestDTO")


@_attrs_define
class OnuInformationRebootRequestDTO:
    """
    Attributes:
        reboot_request_list (list[SingleOnuRebootRequestDTO]): Reboot request list
    """

    reboot_request_list: list[SingleOnuRebootRequestDTO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reboot_request_list = []
        for reboot_request_list_item_data in self.reboot_request_list:
            reboot_request_list_item = reboot_request_list_item_data.to_dict()
            reboot_request_list.append(reboot_request_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rebootRequestList": reboot_request_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.single_onu_reboot_request_dto import (
            SingleOnuRebootRequestDTO,
        )

        d = dict(src_dict)
        reboot_request_list = []
        _reboot_request_list = d.pop("rebootRequestList")
        for reboot_request_list_item_data in _reboot_request_list:
            reboot_request_list_item = SingleOnuRebootRequestDTO.from_dict(
                reboot_request_list_item_data
            )

            reboot_request_list.append(reboot_request_list_item)

        onu_information_reboot_request_dto = cls(
            reboot_request_list=reboot_request_list,
        )

        onu_information_reboot_request_dto.additional_properties = d
        return onu_information_reboot_request_dto

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
