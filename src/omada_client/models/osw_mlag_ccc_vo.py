from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mlag_ccc_result_vo import MlagCccResultVO


T = TypeVar("T", bound="OswMlagCccVO")


@_attrs_define
class OswMlagCccVO:
    """
    Attributes:
        mac (str | Unset): M-LAG group member mac
        mlag_ccc_result (list[MlagCccResultVO] | Unset): M-LAG group members configuration check result
    """

    mac: str | Unset = UNSET
    mlag_ccc_result: list[MlagCccResultVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        mlag_ccc_result: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mlag_ccc_result, Unset):
            mlag_ccc_result = []
            for mlag_ccc_result_item_data in self.mlag_ccc_result:
                mlag_ccc_result_item = mlag_ccc_result_item_data.to_dict()
                mlag_ccc_result.append(mlag_ccc_result_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mlag_ccc_result is not UNSET:
            field_dict["mlagCccResult"] = mlag_ccc_result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mlag_ccc_result_vo import MlagCccResultVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        _mlag_ccc_result = d.pop("mlagCccResult", UNSET)
        mlag_ccc_result: list[MlagCccResultVO] | Unset = UNSET
        if _mlag_ccc_result is not UNSET:
            mlag_ccc_result = []
            for mlag_ccc_result_item_data in _mlag_ccc_result:
                mlag_ccc_result_item = MlagCccResultVO.from_dict(
                    mlag_ccc_result_item_data
                )

                mlag_ccc_result.append(mlag_ccc_result_item)

        osw_mlag_ccc_vo = cls(
            mac=mac,
            mlag_ccc_result=mlag_ccc_result,
        )

        osw_mlag_ccc_vo.additional_properties = d
        return osw_mlag_ccc_vo

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
