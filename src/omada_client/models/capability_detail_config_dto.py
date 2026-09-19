from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapabilityDetailConfigDTO")


@_attrs_define
class CapabilityDetailConfigDTO:
    """
    Attributes:
        omcc_version (str | Unset): OmccVersion should contain uppercase and lowercase letters, numbers, and the symbols
            -@_:/.
        total_eth_number (int | Unset): The number of Ethernet ports on the ONU, totalEthNumber should be within the
            range of 0 to 24.
        total_voip_number (int | Unset): The number of VoIP ports on the ONU, totalVoipNumber should be within the range
            of 0 to 4.
        total_gem_port_number (int | Unset): The number of configured GEM Ports,totalGemPortNumber should be within the
            range of 0 to 31.
        total_tcont_number (int | Unset): The number of configured T-conts, totalTcontNumber should be within the range
            of 0 to 8.
    """

    omcc_version: str | Unset = UNSET
    total_eth_number: int | Unset = UNSET
    total_voip_number: int | Unset = UNSET
    total_gem_port_number: int | Unset = UNSET
    total_tcont_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        omcc_version = self.omcc_version

        total_eth_number = self.total_eth_number

        total_voip_number = self.total_voip_number

        total_gem_port_number = self.total_gem_port_number

        total_tcont_number = self.total_tcont_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if omcc_version is not UNSET:
            field_dict["omccVersion"] = omcc_version
        if total_eth_number is not UNSET:
            field_dict["totalEthNumber"] = total_eth_number
        if total_voip_number is not UNSET:
            field_dict["totalVoipNumber"] = total_voip_number
        if total_gem_port_number is not UNSET:
            field_dict["totalGemPortNumber"] = total_gem_port_number
        if total_tcont_number is not UNSET:
            field_dict["totalTcontNumber"] = total_tcont_number

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        omcc_version = d.pop("omccVersion", UNSET)

        total_eth_number = d.pop("totalEthNumber", UNSET)

        total_voip_number = d.pop("totalVoipNumber", UNSET)

        total_gem_port_number = d.pop("totalGemPortNumber", UNSET)

        total_tcont_number = d.pop("totalTcontNumber", UNSET)

        capability_detail_config_dto = cls(
            omcc_version=omcc_version,
            total_eth_number=total_eth_number,
            total_voip_number=total_voip_number,
            total_gem_port_number=total_gem_port_number,
            total_tcont_number=total_tcont_number,
        )

        capability_detail_config_dto.additional_properties = d
        return capability_detail_config_dto

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
