from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ospf_process_area_network_open_api_vo import (
        OspfProcessAreaNetworkOpenApiVO,
    )


T = TypeVar("T", bound="OspfProcessAreaOpenApiVO")


@_attrs_define
class OspfProcessAreaOpenApiVO:
    """Up to 16 entries are allowed for the areaList.

    Attributes:
        area_id (str): The 32 bit unsigned integer that uniquely identifies the area. It can be in decimal format or
            dotted decimal format.
        area_type (int): OSPF area type should be a value as follows: 0: Normal, 1: Stub, or 2: NSSA.
        network_list (list[OspfProcessAreaNetworkOpenApiVO] | Unset): Up to 16 entries are allowed for the networkList.
    """

    area_id: str
    area_type: int
    network_list: list[OspfProcessAreaNetworkOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area_id = self.area_id

        area_type = self.area_type

        network_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = []
            for network_list_item_data in self.network_list:
                network_list_item = network_list_item_data.to_dict()
                network_list.append(network_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "areaId": area_id,
                "areaType": area_type,
            }
        )
        if network_list is not UNSET:
            field_dict["networkList"] = network_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ospf_process_area_network_open_api_vo import (
            OspfProcessAreaNetworkOpenApiVO,
        )

        d = dict(src_dict)
        area_id = d.pop("areaId")

        area_type = d.pop("areaType")

        _network_list = d.pop("networkList", UNSET)
        network_list: list[OspfProcessAreaNetworkOpenApiVO] | Unset = UNSET
        if _network_list is not UNSET:
            network_list = []
            for network_list_item_data in _network_list:
                network_list_item = OspfProcessAreaNetworkOpenApiVO.from_dict(
                    network_list_item_data
                )

                network_list.append(network_list_item)

        ospf_process_area_open_api_vo = cls(
            area_id=area_id,
            area_type=area_type,
            network_list=network_list,
        )

        ospf_process_area_open_api_vo.additional_properties = d
        return ospf_process_area_open_api_vo

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
