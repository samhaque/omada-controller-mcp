from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_wired_uplink_info import ApWiredUplinkInfo


T = TypeVar("T", bound="ApWiredUplink")


@_attrs_define
class ApWiredUplink:
    """
    Attributes:
        wired_uplink (ApWiredUplinkInfo | Unset): Wired uplink info
    """

    wired_uplink: ApWiredUplinkInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wired_uplink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wired_uplink, Unset):
            wired_uplink = self.wired_uplink.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wired_uplink is not UNSET:
            field_dict["wiredUplink"] = wired_uplink

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_wired_uplink_info import ApWiredUplinkInfo

        d = dict(src_dict)
        _wired_uplink = d.pop("wiredUplink", UNSET)
        wired_uplink: ApWiredUplinkInfo | Unset
        if isinstance(_wired_uplink, Unset):
            wired_uplink = UNSET
        else:
            wired_uplink = ApWiredUplinkInfo.from_dict(_wired_uplink)

        ap_wired_uplink = cls(
            wired_uplink=wired_uplink,
        )

        ap_wired_uplink.additional_properties = d
        return ap_wired_uplink

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
