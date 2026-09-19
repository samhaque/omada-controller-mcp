from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_port_info_vo import OsgPortInfoVO


T = TypeVar("T", bound="GatewayPortInfos")


@_attrs_define
class GatewayPortInfos:
    """
    Attributes:
        osg_port_infos (list[OsgPortInfoVO] | Unset): Gateway port info list
    """

    osg_port_infos: list[OsgPortInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        osg_port_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.osg_port_infos, Unset):
            osg_port_infos = []
            for osg_port_infos_item_data in self.osg_port_infos:
                osg_port_infos_item = osg_port_infos_item_data.to_dict()
                osg_port_infos.append(osg_port_infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if osg_port_infos is not UNSET:
            field_dict["osgPortInfos"] = osg_port_infos

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_port_info_vo import OsgPortInfoVO

        d = dict(src_dict)
        _osg_port_infos = d.pop("osgPortInfos", UNSET)
        osg_port_infos: list[OsgPortInfoVO] | Unset = UNSET
        if _osg_port_infos is not UNSET:
            osg_port_infos = []
            for osg_port_infos_item_data in _osg_port_infos:
                osg_port_infos_item = OsgPortInfoVO.from_dict(osg_port_infos_item_data)

                osg_port_infos.append(osg_port_infos_item)

        gateway_port_infos = cls(
            osg_port_infos=osg_port_infos,
        )

        gateway_port_infos.additional_properties = d
        return gateway_port_infos

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
