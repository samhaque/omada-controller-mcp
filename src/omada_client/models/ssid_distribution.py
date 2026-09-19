from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssid_stat import SSIDStat


T = TypeVar("T", bound="SsidDistribution")


@_attrs_define
class SsidDistribution:
    """Distribution of the number of clients on SSID.

    Attributes:
        first_ssid (SSIDStat | Unset): The total client number of other SSIDs.
        second_ssid (SSIDStat | Unset): The total client number of other SSIDs.
        third_ssid (SSIDStat | Unset): The total client number of other SSIDs.
        fourth_ssid (SSIDStat | Unset): The total client number of other SSIDs.
        fifth_ssid (SSIDStat | Unset): The total client number of other SSIDs.
        other_ssid (SSIDStat | Unset): The total client number of other SSIDs.
    """

    first_ssid: SSIDStat | Unset = UNSET
    second_ssid: SSIDStat | Unset = UNSET
    third_ssid: SSIDStat | Unset = UNSET
    fourth_ssid: SSIDStat | Unset = UNSET
    fifth_ssid: SSIDStat | Unset = UNSET
    other_ssid: SSIDStat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_ssid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_ssid, Unset):
            first_ssid = self.first_ssid.to_dict()

        second_ssid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.second_ssid, Unset):
            second_ssid = self.second_ssid.to_dict()

        third_ssid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.third_ssid, Unset):
            third_ssid = self.third_ssid.to_dict()

        fourth_ssid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fourth_ssid, Unset):
            fourth_ssid = self.fourth_ssid.to_dict()

        fifth_ssid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fifth_ssid, Unset):
            fifth_ssid = self.fifth_ssid.to_dict()

        other_ssid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_ssid, Unset):
            other_ssid = self.other_ssid.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_ssid is not UNSET:
            field_dict["firstSsid"] = first_ssid
        if second_ssid is not UNSET:
            field_dict["secondSsid"] = second_ssid
        if third_ssid is not UNSET:
            field_dict["thirdSsid"] = third_ssid
        if fourth_ssid is not UNSET:
            field_dict["fourthSsid"] = fourth_ssid
        if fifth_ssid is not UNSET:
            field_dict["fifthSsid"] = fifth_ssid
        if other_ssid is not UNSET:
            field_dict["otherSsid"] = other_ssid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssid_stat import SSIDStat

        d = dict(src_dict)
        _first_ssid = d.pop("firstSsid", UNSET)
        first_ssid: SSIDStat | Unset
        if isinstance(_first_ssid, Unset):
            first_ssid = UNSET
        else:
            first_ssid = SSIDStat.from_dict(_first_ssid)

        _second_ssid = d.pop("secondSsid", UNSET)
        second_ssid: SSIDStat | Unset
        if isinstance(_second_ssid, Unset):
            second_ssid = UNSET
        else:
            second_ssid = SSIDStat.from_dict(_second_ssid)

        _third_ssid = d.pop("thirdSsid", UNSET)
        third_ssid: SSIDStat | Unset
        if isinstance(_third_ssid, Unset):
            third_ssid = UNSET
        else:
            third_ssid = SSIDStat.from_dict(_third_ssid)

        _fourth_ssid = d.pop("fourthSsid", UNSET)
        fourth_ssid: SSIDStat | Unset
        if isinstance(_fourth_ssid, Unset):
            fourth_ssid = UNSET
        else:
            fourth_ssid = SSIDStat.from_dict(_fourth_ssid)

        _fifth_ssid = d.pop("fifthSsid", UNSET)
        fifth_ssid: SSIDStat | Unset
        if isinstance(_fifth_ssid, Unset):
            fifth_ssid = UNSET
        else:
            fifth_ssid = SSIDStat.from_dict(_fifth_ssid)

        _other_ssid = d.pop("otherSsid", UNSET)
        other_ssid: SSIDStat | Unset
        if isinstance(_other_ssid, Unset):
            other_ssid = UNSET
        else:
            other_ssid = SSIDStat.from_dict(_other_ssid)

        ssid_distribution = cls(
            first_ssid=first_ssid,
            second_ssid=second_ssid,
            third_ssid=third_ssid,
            fourth_ssid=fourth_ssid,
            fifth_ssid=fifth_ssid,
            other_ssid=other_ssid,
        )

        ssid_distribution.additional_properties = d
        return ssid_distribution

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
