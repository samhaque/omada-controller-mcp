from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IspResultOpenApiVO")


@_attrs_define
class IspResultOpenApiVO:
    """The list of the isp, contains the ISP name and the ID and the state of the ISP.

    Attributes:
        isp (str | Unset): ISP name.
        isp_num (int | Unset): The ID of the ISP.
        state (bool | Unset): Whether the ISP available or not.
    """

    isp: str | Unset = UNSET
    isp_num: int | Unset = UNSET
    state: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        isp = self.isp

        isp_num = self.isp_num

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if isp is not UNSET:
            field_dict["isp"] = isp
        if isp_num is not UNSET:
            field_dict["ispNum"] = isp_num
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        isp = d.pop("isp", UNSET)

        isp_num = d.pop("ispNum", UNSET)

        state = d.pop("state", UNSET)

        isp_result_open_api_vo = cls(
            isp=isp,
            isp_num=isp_num,
            state=state,
        )

        isp_result_open_api_vo.additional_properties = d
        return isp_result_open_api_vo

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
