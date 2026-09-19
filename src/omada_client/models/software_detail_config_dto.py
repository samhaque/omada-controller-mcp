from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.software_detail_config_dto_software_0_active import (
    SoftwareDetailConfigDTOSoftware0Active,
)
from ..models.software_detail_config_dto_software_0_commited import (
    SoftwareDetailConfigDTOSoftware0Commited,
)
from ..models.software_detail_config_dto_software_0_valid import (
    SoftwareDetailConfigDTOSoftware0Valid,
)
from ..models.software_detail_config_dto_software_1_active import (
    SoftwareDetailConfigDTOSoftware1Active,
)
from ..models.software_detail_config_dto_software_1_commited import (
    SoftwareDetailConfigDTOSoftware1Commited,
)
from ..models.software_detail_config_dto_software_1_valid import (
    SoftwareDetailConfigDTOSoftware1Valid,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SoftwareDetailConfigDTO")


@_attrs_define
class SoftwareDetailConfigDTO:
    """
    Attributes:
        software_0_version (str | Unset): Software0 version should contain 1 to 14 ASCII characters.
        software_0_valid (SoftwareDetailConfigDTOSoftware0Valid | Unset): Validity of ONU software 0.Software0Valid
            should be a value as follows:VALID,INVALID
        software_0_active (SoftwareDetailConfigDTOSoftware0Active | Unset): Status of ONU software 0.Software0Active
            should be a value as follows:ACTIVE,INACTIVE
        software_0_commited (SoftwareDetailConfigDTOSoftware0Commited | Unset): Commit status of ONU software
            0.Software0Commited should be a value as follows:COMMITED,UNCOMMITED
        software_1_version (str | Unset): Software1 version should contain 1 to 14 ASCII characters.
        software_1_valid (SoftwareDetailConfigDTOSoftware1Valid | Unset): Validity of ONU software 1.software1Valid
            should be a value as follows:VALID,INVALID
        software_1_active (SoftwareDetailConfigDTOSoftware1Active | Unset): Status of ONU software 1.software1Active
            should be a value as follows:ACTIVE,INACTIVE
        software_1_commited (SoftwareDetailConfigDTOSoftware1Commited | Unset): Commit status of ONU software
            1.Software1Commited should be a value as follows:COMMITED,UNCOMMITED
    """

    software_0_version: str | Unset = UNSET
    software_0_valid: SoftwareDetailConfigDTOSoftware0Valid | Unset = UNSET
    software_0_active: SoftwareDetailConfigDTOSoftware0Active | Unset = UNSET
    software_0_commited: SoftwareDetailConfigDTOSoftware0Commited | Unset = UNSET
    software_1_version: str | Unset = UNSET
    software_1_valid: SoftwareDetailConfigDTOSoftware1Valid | Unset = UNSET
    software_1_active: SoftwareDetailConfigDTOSoftware1Active | Unset = UNSET
    software_1_commited: SoftwareDetailConfigDTOSoftware1Commited | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        software_0_version = self.software_0_version

        software_0_valid: str | Unset = UNSET
        if not isinstance(self.software_0_valid, Unset):
            software_0_valid = self.software_0_valid.value

        software_0_active: str | Unset = UNSET
        if not isinstance(self.software_0_active, Unset):
            software_0_active = self.software_0_active.value

        software_0_commited: str | Unset = UNSET
        if not isinstance(self.software_0_commited, Unset):
            software_0_commited = self.software_0_commited.value

        software_1_version = self.software_1_version

        software_1_valid: str | Unset = UNSET
        if not isinstance(self.software_1_valid, Unset):
            software_1_valid = self.software_1_valid.value

        software_1_active: str | Unset = UNSET
        if not isinstance(self.software_1_active, Unset):
            software_1_active = self.software_1_active.value

        software_1_commited: str | Unset = UNSET
        if not isinstance(self.software_1_commited, Unset):
            software_1_commited = self.software_1_commited.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if software_0_version is not UNSET:
            field_dict["software0Version"] = software_0_version
        if software_0_valid is not UNSET:
            field_dict["software0Valid"] = software_0_valid
        if software_0_active is not UNSET:
            field_dict["software0Active"] = software_0_active
        if software_0_commited is not UNSET:
            field_dict["software0Commited"] = software_0_commited
        if software_1_version is not UNSET:
            field_dict["software1Version"] = software_1_version
        if software_1_valid is not UNSET:
            field_dict["software1Valid"] = software_1_valid
        if software_1_active is not UNSET:
            field_dict["software1Active"] = software_1_active
        if software_1_commited is not UNSET:
            field_dict["software1Commited"] = software_1_commited

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        software_0_version = d.pop("software0Version", UNSET)

        _software_0_valid = d.pop("software0Valid", UNSET)
        software_0_valid: SoftwareDetailConfigDTOSoftware0Valid | Unset
        if isinstance(_software_0_valid, Unset):
            software_0_valid = UNSET
        else:
            software_0_valid = SoftwareDetailConfigDTOSoftware0Valid(_software_0_valid)

        _software_0_active = d.pop("software0Active", UNSET)
        software_0_active: SoftwareDetailConfigDTOSoftware0Active | Unset
        if isinstance(_software_0_active, Unset):
            software_0_active = UNSET
        else:
            software_0_active = SoftwareDetailConfigDTOSoftware0Active(
                _software_0_active
            )

        _software_0_commited = d.pop("software0Commited", UNSET)
        software_0_commited: SoftwareDetailConfigDTOSoftware0Commited | Unset
        if isinstance(_software_0_commited, Unset):
            software_0_commited = UNSET
        else:
            software_0_commited = SoftwareDetailConfigDTOSoftware0Commited(
                _software_0_commited
            )

        software_1_version = d.pop("software1Version", UNSET)

        _software_1_valid = d.pop("software1Valid", UNSET)
        software_1_valid: SoftwareDetailConfigDTOSoftware1Valid | Unset
        if isinstance(_software_1_valid, Unset):
            software_1_valid = UNSET
        else:
            software_1_valid = SoftwareDetailConfigDTOSoftware1Valid(_software_1_valid)

        _software_1_active = d.pop("software1Active", UNSET)
        software_1_active: SoftwareDetailConfigDTOSoftware1Active | Unset
        if isinstance(_software_1_active, Unset):
            software_1_active = UNSET
        else:
            software_1_active = SoftwareDetailConfigDTOSoftware1Active(
                _software_1_active
            )

        _software_1_commited = d.pop("software1Commited", UNSET)
        software_1_commited: SoftwareDetailConfigDTOSoftware1Commited | Unset
        if isinstance(_software_1_commited, Unset):
            software_1_commited = UNSET
        else:
            software_1_commited = SoftwareDetailConfigDTOSoftware1Commited(
                _software_1_commited
            )

        software_detail_config_dto = cls(
            software_0_version=software_0_version,
            software_0_valid=software_0_valid,
            software_0_active=software_0_active,
            software_0_commited=software_0_commited,
            software_1_version=software_1_version,
            software_1_valid=software_1_valid,
            software_1_active=software_1_active,
            software_1_commited=software_1_commited,
        )

        software_detail_config_dto.additional_properties = d
        return software_detail_config_dto

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
