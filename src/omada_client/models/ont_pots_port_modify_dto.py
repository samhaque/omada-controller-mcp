from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.ont_pots_port_modify_dto_vlan_config_mode import (
    OntPotsPortModifyDTOVlanConfigMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ont_port_vlan_config_add_item_dto import OntPortVlanConfigAddItemDTO
    from ..models.ont_port_vlan_config_item_dto import OntPortVlanConfigItemDTO


T = TypeVar("T", bound="OntPotsPortModifyDTO")


@_attrs_define
class OntPotsPortModifyDTO:
    """
    Attributes:
        vlan_config_mode (OntPotsPortModifyDTOVlanConfigMode): Vlan config mode.VlanConfigMode should be a value as
            follows:TRANSPARENT,OTHERS
        service_id (int | Unset): The associated Service Profile ID
        config_item_add_list (list[OntPortVlanConfigAddItemDTO] | Unset): Config item add list
        config_item_delete_list (list[int] | Unset): Config item delete list
        config_item_edit_list (list[OntPortVlanConfigItemDTO] | Unset): Config item edit list
    """

    vlan_config_mode: OntPotsPortModifyDTOVlanConfigMode
    service_id: int | Unset = UNSET
    config_item_add_list: list[OntPortVlanConfigAddItemDTO] | Unset = UNSET
    config_item_delete_list: list[int] | Unset = UNSET
    config_item_edit_list: list[OntPortVlanConfigItemDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan_config_mode = self.vlan_config_mode.value

        service_id = self.service_id

        config_item_add_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config_item_add_list, Unset):
            config_item_add_list = []
            for config_item_add_list_item_data in self.config_item_add_list:
                config_item_add_list_item = config_item_add_list_item_data.to_dict()
                config_item_add_list.append(config_item_add_list_item)

        config_item_delete_list: list[int] | Unset = UNSET
        if not isinstance(self.config_item_delete_list, Unset):
            config_item_delete_list = self.config_item_delete_list

        config_item_edit_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config_item_edit_list, Unset):
            config_item_edit_list = []
            for config_item_edit_list_item_data in self.config_item_edit_list:
                config_item_edit_list_item = config_item_edit_list_item_data.to_dict()
                config_item_edit_list.append(config_item_edit_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vlanConfigMode": vlan_config_mode,
            }
        )
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if config_item_add_list is not UNSET:
            field_dict["configItemAddList"] = config_item_add_list
        if config_item_delete_list is not UNSET:
            field_dict["configItemDeleteList"] = config_item_delete_list
        if config_item_edit_list is not UNSET:
            field_dict["configItemEditList"] = config_item_edit_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ont_port_vlan_config_add_item_dto import (
            OntPortVlanConfigAddItemDTO,
        )
        from ..models.ont_port_vlan_config_item_dto import (
            OntPortVlanConfigItemDTO,
        )

        d = dict(src_dict)
        vlan_config_mode = OntPotsPortModifyDTOVlanConfigMode(d.pop("vlanConfigMode"))

        service_id = d.pop("serviceId", UNSET)

        _config_item_add_list = d.pop("configItemAddList", UNSET)
        config_item_add_list: list[OntPortVlanConfigAddItemDTO] | Unset = UNSET
        if _config_item_add_list is not UNSET:
            config_item_add_list = []
            for config_item_add_list_item_data in _config_item_add_list:
                config_item_add_list_item = OntPortVlanConfigAddItemDTO.from_dict(
                    config_item_add_list_item_data
                )

                config_item_add_list.append(config_item_add_list_item)

        config_item_delete_list = cast(list[int], d.pop("configItemDeleteList", UNSET))

        _config_item_edit_list = d.pop("configItemEditList", UNSET)
        config_item_edit_list: list[OntPortVlanConfigItemDTO] | Unset = UNSET
        if _config_item_edit_list is not UNSET:
            config_item_edit_list = []
            for config_item_edit_list_item_data in _config_item_edit_list:
                config_item_edit_list_item = OntPortVlanConfigItemDTO.from_dict(
                    config_item_edit_list_item_data
                )

                config_item_edit_list.append(config_item_edit_list_item)

        ont_pots_port_modify_dto = cls(
            vlan_config_mode=vlan_config_mode,
            service_id=service_id,
            config_item_add_list=config_item_add_list,
            config_item_delete_list=config_item_delete_list,
            config_item_edit_list=config_item_edit_list,
        )

        ont_pots_port_modify_dto.additional_properties = d
        return ont_pots_port_modify_dto

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
