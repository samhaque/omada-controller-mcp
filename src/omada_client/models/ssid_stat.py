from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSIDStat")


@_attrs_define
class SSIDStat:
    """The total client number of other SSIDs.

    Attributes:
        ssid (str | Unset): SSID name.
        clients_num (int | Unset): Client number.
    """

    ssid: str | Unset = UNSET
    clients_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid = self.ssid

        clients_num = self.clients_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if clients_num is not UNSET:
            field_dict["clientsNum"] = clients_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssid = d.pop("ssid", UNSET)

        clients_num = d.pop("clientsNum", UNSET)

        ssid_stat = cls(
            ssid=ssid,
            clients_num=clients_num,
        )

        ssid_stat.additional_properties = d
        return ssid_stat

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
