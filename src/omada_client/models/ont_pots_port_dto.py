from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.ont_pots_port_dto_vlan_config_mode import OntPotsPortDTOVlanConfigMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ont_port_vlan_config_item_dto import OntPortVlanConfigItemDTO


T = TypeVar("T", bound="OntPotsPortDTO")


@_attrs_define
class OntPotsPortDTO:
    """
    Attributes:
        vlan_config_mode (OntPotsPortDTOVlanConfigMode): Vlan config mode.VlanConfigMode should be a value as
            follows:TRANSPARENT,OTHERS
        config_item_list (list[OntPortVlanConfigItemDTO] | Unset): Config item list
    """

    vlan_config_mode: OntPotsPortDTOVlanConfigMode
    config_item_list: list[OntPortVlanConfigItemDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan_config_mode = self.vlan_config_mode.value

        config_item_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config_item_list, Unset):
            config_item_list = []
            for config_item_list_item_data in self.config_item_list:
                config_item_list_item = config_item_list_item_data.to_dict()
                config_item_list.append(config_item_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vlanConfigMode": vlan_config_mode,
            }
        )
        if config_item_list is not UNSET:
            field_dict["configItemList"] = config_item_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ont_port_vlan_config_item_dto import (
            OntPortVlanConfigItemDTO,
        )

        d = dict(src_dict)
        vlan_config_mode = OntPotsPortDTOVlanConfigMode(d.pop("vlanConfigMode"))

        _config_item_list = d.pop("configItemList", UNSET)
        config_item_list: list[OntPortVlanConfigItemDTO] | Unset = UNSET
        if _config_item_list is not UNSET:
            config_item_list = []
            for config_item_list_item_data in _config_item_list:
                config_item_list_item = OntPortVlanConfigItemDTO.from_dict(
                    config_item_list_item_data
                )

                config_item_list.append(config_item_list_item)

        ont_pots_port_dto = cls(
            vlan_config_mode=vlan_config_mode,
            config_item_list=config_item_list,
        )

        ont_pots_port_dto.additional_properties = d
        return ont_pots_port_dto

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
