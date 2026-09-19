from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interference import Interference


T = TypeVar("T", bound="RFScanRadio5G2")


@_attrs_define
class RFScanRadio5G2:
    """Channel 5g2

    Attributes:
        chan (int | Unset): Channel number
        chan_width (int | Unset): ChanWidth should be a value as follows: 2: 20MHz, 3: 40MHz, 5: 80MHz
        util (int | Unset): Channel utilization should be within the range of 0–100.
        inter (list[Interference] | Unset): At most two types of interference data are reported in Inter, sorted in
            descending order of interference intensity
    """

    chan: int | Unset = UNSET
    chan_width: int | Unset = UNSET
    util: int | Unset = UNSET
    inter: list[Interference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chan = self.chan

        chan_width = self.chan_width

        util = self.util

        inter: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inter, Unset):
            inter = []
            for inter_item_data in self.inter:
                inter_item = inter_item_data.to_dict()
                inter.append(inter_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chan is not UNSET:
            field_dict["chan"] = chan
        if chan_width is not UNSET:
            field_dict["chanWidth"] = chan_width
        if util is not UNSET:
            field_dict["util"] = util
        if inter is not UNSET:
            field_dict["inter"] = inter

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.interference import Interference

        d = dict(src_dict)
        chan = d.pop("chan", UNSET)

        chan_width = d.pop("chanWidth", UNSET)

        util = d.pop("util", UNSET)

        _inter = d.pop("inter", UNSET)
        inter: list[Interference] | Unset = UNSET
        if _inter is not UNSET:
            inter = []
            for inter_item_data in _inter:
                inter_item = Interference.from_dict(inter_item_data)

                inter.append(inter_item)

        rf_scan_radio_5g2 = cls(
            chan=chan,
            chan_width=chan_width,
            util=util,
            inter=inter,
        )

        rf_scan_radio_5g2.additional_properties = d
        return rf_scan_radio_5g2

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
