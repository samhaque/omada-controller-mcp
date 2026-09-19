from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_detail_config_dto import BasicDetailConfigDTO
    from ..models.capability_detail_config_dto import CapabilityDetailConfigDTO
    from ..models.optical_link_detail_config_dto import OpticalLinkDetailConfigDTO
    from ..models.software_detail_config_dto import SoftwareDetailConfigDTO


T = TypeVar("T", bound="OnuDetailConfigDTO")


@_attrs_define
class OnuDetailConfigDTO:
    """
    Attributes:
        onu_basic_information (BasicDetailConfigDTO | Unset):
        onu_capability_information (CapabilityDetailConfigDTO | Unset):
        onu_optical_link_information (OpticalLinkDetailConfigDTO | Unset):
        onu_software_information (SoftwareDetailConfigDTO | Unset):
    """

    onu_basic_information: BasicDetailConfigDTO | Unset = UNSET
    onu_capability_information: CapabilityDetailConfigDTO | Unset = UNSET
    onu_optical_link_information: OpticalLinkDetailConfigDTO | Unset = UNSET
    onu_software_information: SoftwareDetailConfigDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        onu_basic_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.onu_basic_information, Unset):
            onu_basic_information = self.onu_basic_information.to_dict()

        onu_capability_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.onu_capability_information, Unset):
            onu_capability_information = self.onu_capability_information.to_dict()

        onu_optical_link_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.onu_optical_link_information, Unset):
            onu_optical_link_information = self.onu_optical_link_information.to_dict()

        onu_software_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.onu_software_information, Unset):
            onu_software_information = self.onu_software_information.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if onu_basic_information is not UNSET:
            field_dict["onuBasicInformation"] = onu_basic_information
        if onu_capability_information is not UNSET:
            field_dict["onuCapabilityInformation"] = onu_capability_information
        if onu_optical_link_information is not UNSET:
            field_dict["onuOpticalLinkInformation"] = onu_optical_link_information
        if onu_software_information is not UNSET:
            field_dict["onuSoftwareInformation"] = onu_software_information

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.basic_detail_config_dto import (
            BasicDetailConfigDTO,
        )
        from ..models.capability_detail_config_dto import (
            CapabilityDetailConfigDTO,
        )
        from ..models.optical_link_detail_config_dto import (
            OpticalLinkDetailConfigDTO,
        )
        from ..models.software_detail_config_dto import (
            SoftwareDetailConfigDTO,
        )

        d = dict(src_dict)
        _onu_basic_information = d.pop("onuBasicInformation", UNSET)
        onu_basic_information: BasicDetailConfigDTO | Unset
        if isinstance(_onu_basic_information, Unset):
            onu_basic_information = UNSET
        else:
            onu_basic_information = BasicDetailConfigDTO.from_dict(
                _onu_basic_information
            )

        _onu_capability_information = d.pop("onuCapabilityInformation", UNSET)
        onu_capability_information: CapabilityDetailConfigDTO | Unset
        if isinstance(_onu_capability_information, Unset):
            onu_capability_information = UNSET
        else:
            onu_capability_information = CapabilityDetailConfigDTO.from_dict(
                _onu_capability_information
            )

        _onu_optical_link_information = d.pop("onuOpticalLinkInformation", UNSET)
        onu_optical_link_information: OpticalLinkDetailConfigDTO | Unset
        if isinstance(_onu_optical_link_information, Unset):
            onu_optical_link_information = UNSET
        else:
            onu_optical_link_information = OpticalLinkDetailConfigDTO.from_dict(
                _onu_optical_link_information
            )

        _onu_software_information = d.pop("onuSoftwareInformation", UNSET)
        onu_software_information: SoftwareDetailConfigDTO | Unset
        if isinstance(_onu_software_information, Unset):
            onu_software_information = UNSET
        else:
            onu_software_information = SoftwareDetailConfigDTO.from_dict(
                _onu_software_information
            )

        onu_detail_config_dto = cls(
            onu_basic_information=onu_basic_information,
            onu_capability_information=onu_capability_information,
            onu_optical_link_information=onu_optical_link_information,
            onu_software_information=onu_software_information,
        )

        onu_detail_config_dto.additional_properties = d
        return onu_detail_config_dto

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
