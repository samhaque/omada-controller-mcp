from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswDetailOpenApiVO")


@_attrs_define
class OswDetailOpenApiVO:
    """
    Attributes:
        network_id (str): Network ID.
        vlan (int): VLAN ID.
        macs (list[str] | Unset): The collection of macs of the general switches.
        stack_ids (list[str] | Unset): The collection of stack ids of the stack switches.
    """

    network_id: str
    vlan: int
    macs: list[str] | Unset = UNSET
    stack_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        vlan = self.vlan

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        stack_ids: list[str] | Unset = UNSET
        if not isinstance(self.stack_ids, Unset):
            stack_ids = self.stack_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkId": network_id,
                "vlan": vlan,
            }
        )
        if macs is not UNSET:
            field_dict["macs"] = macs
        if stack_ids is not UNSET:
            field_dict["stackIds"] = stack_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_id = d.pop("networkId")

        vlan = d.pop("vlan")

        macs = cast(list[str], d.pop("macs", UNSET))

        stack_ids = cast(list[str], d.pop("stackIds", UNSET))

        osw_detail_open_api_vo = cls(
            network_id=network_id,
            vlan=vlan,
            macs=macs,
            stack_ids=stack_ids,
        )

        osw_detail_open_api_vo.additional_properties = d
        return osw_detail_open_api_vo

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
