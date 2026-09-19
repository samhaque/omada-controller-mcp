from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_client import MonitorClient


T = TypeVar("T", bound="AddMonitorClientList")


@_attrs_define
class AddMonitorClientList:
    """
    Attributes:
        add_client_list (list[MonitorClient] | Unset): The client to be added to the monitor list
    """

    add_client_list: list[MonitorClient] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_client_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.add_client_list, Unset):
            add_client_list = []
            for add_client_list_item_data in self.add_client_list:
                add_client_list_item = add_client_list_item_data.to_dict()
                add_client_list.append(add_client_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_client_list is not UNSET:
            field_dict["addClientList"] = add_client_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.monitor_client import MonitorClient

        d = dict(src_dict)
        _add_client_list = d.pop("addClientList", UNSET)
        add_client_list: list[MonitorClient] | Unset = UNSET
        if _add_client_list is not UNSET:
            add_client_list = []
            for add_client_list_item_data in _add_client_list:
                add_client_list_item = MonitorClient.from_dict(
                    add_client_list_item_data
                )

                add_client_list.append(add_client_list_item)

        add_monitor_client_list = cls(
            add_client_list=add_client_list,
        )

        add_monitor_client_list.additional_properties = d
        return add_monitor_client_list

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
