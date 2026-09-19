from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswPortLagListVO")


@_attrs_define
class OswPortLagListVO:
    """Switches Port And Lag List

    Attributes:
        mac (str): Switch Mac
        port_list (list[OswStandPortVO] | Unset): Port List
        lag_list (list[int] | Unset): LAG List
        stack_id (str | Unset): Stack ID
        unit (int | Unset): Unit
    """

    mac: str
    port_list: list[OswStandPortVO] | Unset = UNSET
    lag_list: list[int] | Unset = UNSET
    stack_id: str | Unset = UNSET
    unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = []
            for port_list_item_data in self.port_list:
                port_list_item = port_list_item_data.to_dict()
                port_list.append(port_list_item)

        lag_list: list[int] | Unset = UNSET
        if not isinstance(self.lag_list, Unset):
            lag_list = self.lag_list

        stack_id = self.stack_id

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
            }
        )
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if lag_list is not UNSET:
            field_dict["lagList"] = lag_list
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        mac = d.pop("mac")

        _port_list = d.pop("portList", UNSET)
        port_list: list[OswStandPortVO] | Unset = UNSET
        if _port_list is not UNSET:
            port_list = []
            for port_list_item_data in _port_list:
                port_list_item = OswStandPortVO.from_dict(port_list_item_data)

                port_list.append(port_list_item)

        lag_list = cast(list[int], d.pop("lagList", UNSET))

        stack_id = d.pop("stackId", UNSET)

        unit = d.pop("unit", UNSET)

        osw_port_lag_list_vo = cls(
            mac=mac,
            port_list=port_list,
            lag_list=lag_list,
            stack_id=stack_id,
            unit=unit,
        )

        osw_port_lag_list_vo.additional_properties = d
        return osw_port_lag_list_vo

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
