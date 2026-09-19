from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isp_load_stat_vo import IspLoadStatVO


T = TypeVar("T", bound="IspLoadVO")


@_attrs_define
class IspLoadVO:
    """ISP Load

    Attributes:
        port_id (int | Unset): Port ID
        port_name (str | Unset): Port Name
        default_wan (bool | Unset): Whether it is the default WAN port
        data (list[IspLoadStatVO] | Unset): WAN port ISP load stat data list
    """

    port_id: int | Unset = UNSET
    port_name: str | Unset = UNSET
    default_wan: bool | Unset = UNSET
    data: list[IspLoadStatVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        port_name = self.port_name

        default_wan = self.default_wan

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if default_wan is not UNSET:
            field_dict["defaultWan"] = default_wan
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.isp_load_stat_vo import IspLoadStatVO

        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        port_name = d.pop("portName", UNSET)

        default_wan = d.pop("defaultWan", UNSET)

        _data = d.pop("data", UNSET)
        data: list[IspLoadStatVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = IspLoadStatVO.from_dict(data_item_data)

                data.append(data_item)

        isp_load_vo = cls(
            port_id=port_id,
            port_name=port_name,
            default_wan=default_wan,
            data=data,
        )

        isp_load_vo.additional_properties = d
        return isp_load_vo

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
