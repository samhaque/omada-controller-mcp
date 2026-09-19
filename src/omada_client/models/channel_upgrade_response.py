from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.software_update_response import SoftwareUpdateResponse


T = TypeVar("T", bound="ChannelUpgradeResponse")


@_attrs_define
class ChannelUpgradeResponse:
    """
    Attributes:
        current_channel (int | Unset): Current Channel
        controller_channel (int | Unset): Controller Channel
        current_controller_ver (str | Unset): Current Controller Version
        upgrade_list (list[SoftwareUpdateResponse] | Unset): Upgrade List
    """

    current_channel: int | Unset = UNSET
    controller_channel: int | Unset = UNSET
    current_controller_ver: str | Unset = UNSET
    upgrade_list: list[SoftwareUpdateResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_channel = self.current_channel

        controller_channel = self.controller_channel

        current_controller_ver = self.current_controller_ver

        upgrade_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.upgrade_list, Unset):
            upgrade_list = []
            for upgrade_list_item_data in self.upgrade_list:
                upgrade_list_item = upgrade_list_item_data.to_dict()
                upgrade_list.append(upgrade_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_channel is not UNSET:
            field_dict["currentChannel"] = current_channel
        if controller_channel is not UNSET:
            field_dict["controllerChannel"] = controller_channel
        if current_controller_ver is not UNSET:
            field_dict["currentControllerVer"] = current_controller_ver
        if upgrade_list is not UNSET:
            field_dict["upgradeList"] = upgrade_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.software_update_response import (
            SoftwareUpdateResponse,
        )

        d = dict(src_dict)
        current_channel = d.pop("currentChannel", UNSET)

        controller_channel = d.pop("controllerChannel", UNSET)

        current_controller_ver = d.pop("currentControllerVer", UNSET)

        _upgrade_list = d.pop("upgradeList", UNSET)
        upgrade_list: list[SoftwareUpdateResponse] | Unset = UNSET
        if _upgrade_list is not UNSET:
            upgrade_list = []
            for upgrade_list_item_data in _upgrade_list:
                upgrade_list_item = SoftwareUpdateResponse.from_dict(
                    upgrade_list_item_data
                )

                upgrade_list.append(upgrade_list_item)

        channel_upgrade_response = cls(
            current_channel=current_channel,
            controller_channel=controller_channel,
            current_controller_ver=current_controller_ver,
            upgrade_list=upgrade_list,
        )

        channel_upgrade_response.additional_properties = d
        return channel_upgrade_response

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
