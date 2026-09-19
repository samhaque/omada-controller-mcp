from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eth_unit_1_port_dto import EthUnit1PortDTO
    from ..models.pon_port_dto import PonPortDTO


T = TypeVar("T", bound="EthAndPonListDTO")


@_attrs_define
class EthAndPonListDTO:
    """
    Attributes:
        eth_unit_1_port_dto_list (list[EthUnit1PortDTO] | Unset): Eth unit1 port list
        pon_port_dto_list (list[PonPortDTO] | Unset): Pon port list
    """

    eth_unit_1_port_dto_list: list[EthUnit1PortDTO] | Unset = UNSET
    pon_port_dto_list: list[PonPortDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eth_unit_1_port_dto_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eth_unit_1_port_dto_list, Unset):
            eth_unit_1_port_dto_list = []
            for eth_unit_1_port_dto_list_item_data in self.eth_unit_1_port_dto_list:
                eth_unit_1_port_dto_list_item = (
                    eth_unit_1_port_dto_list_item_data.to_dict()
                )
                eth_unit_1_port_dto_list.append(eth_unit_1_port_dto_list_item)

        pon_port_dto_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pon_port_dto_list, Unset):
            pon_port_dto_list = []
            for pon_port_dto_list_item_data in self.pon_port_dto_list:
                pon_port_dto_list_item = pon_port_dto_list_item_data.to_dict()
                pon_port_dto_list.append(pon_port_dto_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eth_unit_1_port_dto_list is not UNSET:
            field_dict["ethUnit1PortDTOList"] = eth_unit_1_port_dto_list
        if pon_port_dto_list is not UNSET:
            field_dict["ponPortDTOList"] = pon_port_dto_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eth_unit_1_port_dto import EthUnit1PortDTO
        from ..models.pon_port_dto import PonPortDTO

        d = dict(src_dict)
        _eth_unit_1_port_dto_list = d.pop("ethUnit1PortDTOList", UNSET)
        eth_unit_1_port_dto_list: list[EthUnit1PortDTO] | Unset = UNSET
        if _eth_unit_1_port_dto_list is not UNSET:
            eth_unit_1_port_dto_list = []
            for eth_unit_1_port_dto_list_item_data in _eth_unit_1_port_dto_list:
                eth_unit_1_port_dto_list_item = EthUnit1PortDTO.from_dict(
                    eth_unit_1_port_dto_list_item_data
                )

                eth_unit_1_port_dto_list.append(eth_unit_1_port_dto_list_item)

        _pon_port_dto_list = d.pop("ponPortDTOList", UNSET)
        pon_port_dto_list: list[PonPortDTO] | Unset = UNSET
        if _pon_port_dto_list is not UNSET:
            pon_port_dto_list = []
            for pon_port_dto_list_item_data in _pon_port_dto_list:
                pon_port_dto_list_item = PonPortDTO.from_dict(
                    pon_port_dto_list_item_data
                )

                pon_port_dto_list.append(pon_port_dto_list_item)

        eth_and_pon_list_dto = cls(
            eth_unit_1_port_dto_list=eth_unit_1_port_dto_list,
            pon_port_dto_list=pon_port_dto_list,
        )

        eth_and_pon_list_dto.additional_properties = d
        return eth_and_pon_list_dto

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
