from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carrier_open_api_vo import CarrierOpenApiVO


T = TypeVar("T", bound="WifiCallingProfileOpenApiVO")


@_attrs_define
class WifiCallingProfileOpenApiVO:
    """
    Attributes:
        id (str | Unset): Wi-Fi Calling Profile ID
        name (str | Unset): Wi-Fi Calling Profile Name. It should contain 1 to 32 UTF-8 characters.
        description (str | Unset): The Description of Wi-Fi Calling Profile. It should contain 1 to 32 UTF-8 characters.
        carrier_list (list[CarrierOpenApiVO] | Unset): carrierList
        resource (int | Unset): The incident notifiction setting creation resource, such as: 0: new created, 1: from
            template, 2: override.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    carrier_list: list[CarrierOpenApiVO] | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        carrier_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.carrier_list, Unset):
            carrier_list = []
            for carrier_list_item_data in self.carrier_list:
                carrier_list_item = carrier_list_item_data.to_dict()
                carrier_list.append(carrier_list_item)

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if carrier_list is not UNSET:
            field_dict["carrierList"] = carrier_list
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.carrier_open_api_vo import CarrierOpenApiVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _carrier_list = d.pop("carrierList", UNSET)
        carrier_list: list[CarrierOpenApiVO] | Unset = UNSET
        if _carrier_list is not UNSET:
            carrier_list = []
            for carrier_list_item_data in _carrier_list:
                carrier_list_item = CarrierOpenApiVO.from_dict(carrier_list_item_data)

                carrier_list.append(carrier_list_item)

        resource = d.pop("resource", UNSET)

        wifi_calling_profile_open_api_vo = cls(
            id=id,
            name=name,
            description=description,
            carrier_list=carrier_list,
            resource=resource,
        )

        wifi_calling_profile_open_api_vo.additional_properties = d
        return wifi_calling_profile_open_api_vo

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
