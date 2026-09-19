from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineOfflineVO")


@_attrs_define
class OnlineOfflineVO:
    """
    Attributes:
        time (int | Unset): time
        total (int | Unset): total number of device
        online (int | Unset): total number of online device
        offline (int | Unset): total number of offline device
    """

    time: int | Unset = UNSET
    total: int | Unset = UNSET
    online: int | Unset = UNSET
    offline: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        total = self.total

        online = self.online

        offline = self.offline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if total is not UNSET:
            field_dict["total"] = total
        if online is not UNSET:
            field_dict["online"] = online
        if offline is not UNSET:
            field_dict["offline"] = offline

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        total = d.pop("total", UNSET)

        online = d.pop("online", UNSET)

        offline = d.pop("offline", UNSET)

        online_offline_vo = cls(
            time=time,
            total=total,
            online=online,
            offline=offline,
        )

        online_offline_vo.additional_properties = d
        return online_offline_vo

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
