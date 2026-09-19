from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_category_other_ids_open_api_vo import (
        LicenseCategoryOtherIdsOpenApiVO,
    )


T = TypeVar("T", bound="LicenseOthersIdsOpenApiVO")


@_attrs_define
class LicenseOthersIdsOpenApiVO:
    """Used license

    Attributes:
        basic (LicenseCategoryOtherIdsOpenApiVO | Unset): Gateway used license
        ap (LicenseCategoryOtherIdsOpenApiVO | Unset): Gateway used license
        l_2_switch (LicenseCategoryOtherIdsOpenApiVO | Unset): Gateway used license
        l_3_switch (LicenseCategoryOtherIdsOpenApiVO | Unset): Gateway used license
        gateway (LicenseCategoryOtherIdsOpenApiVO | Unset): Gateway used license
    """

    basic: LicenseCategoryOtherIdsOpenApiVO | Unset = UNSET
    ap: LicenseCategoryOtherIdsOpenApiVO | Unset = UNSET
    l_2_switch: LicenseCategoryOtherIdsOpenApiVO | Unset = UNSET
    l_3_switch: LicenseCategoryOtherIdsOpenApiVO | Unset = UNSET
    gateway: LicenseCategoryOtherIdsOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        basic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic, Unset):
            basic = self.basic.to_dict()

        ap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap, Unset):
            ap = self.ap.to_dict()

        l_2_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.l_2_switch, Unset):
            l_2_switch = self.l_2_switch.to_dict()

        l_3_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.l_3_switch, Unset):
            l_3_switch = self.l_3_switch.to_dict()

        gateway: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basic is not UNSET:
            field_dict["basic"] = basic
        if ap is not UNSET:
            field_dict["ap"] = ap
        if l_2_switch is not UNSET:
            field_dict["l2Switch"] = l_2_switch
        if l_3_switch is not UNSET:
            field_dict["l3Switch"] = l_3_switch
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.license_category_other_ids_open_api_vo import (
            LicenseCategoryOtherIdsOpenApiVO,
        )

        d = dict(src_dict)
        _basic = d.pop("basic", UNSET)
        basic: LicenseCategoryOtherIdsOpenApiVO | Unset
        if isinstance(_basic, Unset):
            basic = UNSET
        else:
            basic = LicenseCategoryOtherIdsOpenApiVO.from_dict(_basic)

        _ap = d.pop("ap", UNSET)
        ap: LicenseCategoryOtherIdsOpenApiVO | Unset
        if isinstance(_ap, Unset):
            ap = UNSET
        else:
            ap = LicenseCategoryOtherIdsOpenApiVO.from_dict(_ap)

        _l_2_switch = d.pop("l2Switch", UNSET)
        l_2_switch: LicenseCategoryOtherIdsOpenApiVO | Unset
        if isinstance(_l_2_switch, Unset):
            l_2_switch = UNSET
        else:
            l_2_switch = LicenseCategoryOtherIdsOpenApiVO.from_dict(_l_2_switch)

        _l_3_switch = d.pop("l3Switch", UNSET)
        l_3_switch: LicenseCategoryOtherIdsOpenApiVO | Unset
        if isinstance(_l_3_switch, Unset):
            l_3_switch = UNSET
        else:
            l_3_switch = LicenseCategoryOtherIdsOpenApiVO.from_dict(_l_3_switch)

        _gateway = d.pop("gateway", UNSET)
        gateway: LicenseCategoryOtherIdsOpenApiVO | Unset
        if isinstance(_gateway, Unset):
            gateway = UNSET
        else:
            gateway = LicenseCategoryOtherIdsOpenApiVO.from_dict(_gateway)

        license_others_ids_open_api_vo = cls(
            basic=basic,
            ap=ap,
            l_2_switch=l_2_switch,
            l_3_switch=l_3_switch,
            gateway=gateway,
        )

        license_others_ids_open_api_vo.additional_properties = d
        return license_others_ids_open_api_vo

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
