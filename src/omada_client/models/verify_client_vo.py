from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_client import MonitorClient


T = TypeVar("T", bound="VerifyClientVO")


@_attrs_define
class VerifyClientVO:
    """
    Attributes:
        monitor_client (MonitorClient | Unset): The client to be verified whether it can be monitored
    """

    monitor_client: MonitorClient | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monitor_client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor_client, Unset):
            monitor_client = self.monitor_client.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monitor_client is not UNSET:
            field_dict["monitorClient"] = monitor_client

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.monitor_client import MonitorClient

        d = dict(src_dict)
        _monitor_client = d.pop("monitorClient", UNSET)
        monitor_client: MonitorClient | Unset
        if isinstance(_monitor_client, Unset):
            monitor_client = UNSET
        else:
            monitor_client = MonitorClient.from_dict(_monitor_client)

        verify_client_vo = cls(
            monitor_client=monitor_client,
        )

        verify_client_vo.additional_properties = d
        return verify_client_vo

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
