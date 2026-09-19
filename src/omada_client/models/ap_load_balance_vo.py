from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApLoadBalanceVO")


@_attrs_define
class ApLoadBalanceVO:
    """
    Attributes:
        lb_enable (bool | Unset):
        max_clients (int | Unset):
    """

    lb_enable: bool | Unset = UNSET
    max_clients: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lb_enable = self.lb_enable

        max_clients = self.max_clients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lb_enable is not UNSET:
            field_dict["lbEnable"] = lb_enable
        if max_clients is not UNSET:
            field_dict["maxClients"] = max_clients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lb_enable = d.pop("lbEnable", UNSET)

        max_clients = d.pop("maxClients", UNSET)

        ap_load_balance_vo = cls(
            lb_enable=lb_enable,
            max_clients=max_clients,
        )

        ap_load_balance_vo.additional_properties = d
        return ap_load_balance_vo

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
