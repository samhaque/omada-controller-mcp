from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.license_num_open_api_vo import LicenseNumOpenApiVO
    from ..models.license_others_ids_open_api_vo import LicenseOthersIdsOpenApiVO


T = TypeVar("T", bound="LicenseAssignmentOpenApiVO")


@_attrs_define
class LicenseAssignmentOpenApiVO:
    """
    Attributes:
        customer_id (str): Customer ID
        license_num (list[LicenseNumOpenApiVO]): License num
        others (LicenseOthersIdsOpenApiVO): Used license
    """

    customer_id: str
    license_num: list[LicenseNumOpenApiVO]
    others: LicenseOthersIdsOpenApiVO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        license_num = []
        for license_num_item_data in self.license_num:
            license_num_item = license_num_item_data.to_dict()
            license_num.append(license_num_item)

        others = self.others.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "licenseNum": license_num,
                "others": others,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.license_num_open_api_vo import (
            LicenseNumOpenApiVO,
        )
        from ..models.license_others_ids_open_api_vo import (
            LicenseOthersIdsOpenApiVO,
        )

        d = dict(src_dict)
        customer_id = d.pop("customerId")

        license_num = []
        _license_num = d.pop("licenseNum")
        for license_num_item_data in _license_num:
            license_num_item = LicenseNumOpenApiVO.from_dict(license_num_item_data)

            license_num.append(license_num_item)

        others = LicenseOthersIdsOpenApiVO.from_dict(d.pop("others"))

        license_assignment_open_api_vo = cls(
            customer_id=customer_id,
            license_num=license_num,
            others=others,
        )

        license_assignment_open_api_vo.additional_properties = d
        return license_assignment_open_api_vo

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
