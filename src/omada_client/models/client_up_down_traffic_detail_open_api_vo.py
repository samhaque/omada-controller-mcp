from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_up_down_traffic_detail_open_api_vo import (
        ApplicationUpDownTrafficDetailOpenApiVO,
    )
    from ..models.category_up_down_traffic_detail_open_api_vo import (
        CategoryUpDownTrafficDetailOpenApiVO,
    )


T = TypeVar("T", bound="ClientUpDownTrafficDetailOpenApiVO")


@_attrs_define
class ClientUpDownTrafficDetailOpenApiVO:
    """
    Attributes:
        client_mac (str | Unset): The mac of the client.
        client_name (str | Unset): The name of the client.
        type_ (str | Unset): Type of client.
        manager (bool | Unset): Whether it is the client currently being managed.
        up (int | Unset): Up traffic.
        down (int | Unset): Down traffic.
        applications (list[ApplicationUpDownTrafficDetailOpenApiVO] | Unset): Application uplink and downlink traffic
            data.
        categories (list[CategoryUpDownTrafficDetailOpenApiVO] | Unset): Application uplink and downlink categories.
        network (str | Unset): Network name.
        vlan_id (str | Unset): VLAN ID. The VLAN ID range is 1–4096 or Untag.
    """

    client_mac: str | Unset = UNSET
    client_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    manager: bool | Unset = UNSET
    up: int | Unset = UNSET
    down: int | Unset = UNSET
    applications: list[ApplicationUpDownTrafficDetailOpenApiVO] | Unset = UNSET
    categories: list[CategoryUpDownTrafficDetailOpenApiVO] | Unset = UNSET
    network: str | Unset = UNSET
    vlan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_mac = self.client_mac

        client_name = self.client_name

        type_ = self.type_

        manager = self.manager

        up = self.up

        down = self.down

        applications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.to_dict()
                applications.append(applications_item)

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        network = self.network

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_mac is not UNSET:
            field_dict["clientMac"] = client_mac
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if manager is not UNSET:
            field_dict["manager"] = manager
        if up is not UNSET:
            field_dict["up"] = up
        if down is not UNSET:
            field_dict["down"] = down
        if applications is not UNSET:
            field_dict["applications"] = applications
        if categories is not UNSET:
            field_dict["categories"] = categories
        if network is not UNSET:
            field_dict["network"] = network
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.application_up_down_traffic_detail_open_api_vo import (
            ApplicationUpDownTrafficDetailOpenApiVO,
        )
        from ..models.category_up_down_traffic_detail_open_api_vo import (
            CategoryUpDownTrafficDetailOpenApiVO,
        )

        d = dict(src_dict)
        client_mac = d.pop("clientMac", UNSET)

        client_name = d.pop("clientName", UNSET)

        type_ = d.pop("type", UNSET)

        manager = d.pop("manager", UNSET)

        up = d.pop("up", UNSET)

        down = d.pop("down", UNSET)

        _applications = d.pop("applications", UNSET)
        applications: list[ApplicationUpDownTrafficDetailOpenApiVO] | Unset = UNSET
        if _applications is not UNSET:
            applications = []
            for applications_item_data in _applications:
                applications_item = ApplicationUpDownTrafficDetailOpenApiVO.from_dict(
                    applications_item_data
                )

                applications.append(applications_item)

        _categories = d.pop("categories", UNSET)
        categories: list[CategoryUpDownTrafficDetailOpenApiVO] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = CategoryUpDownTrafficDetailOpenApiVO.from_dict(
                    categories_item_data
                )

                categories.append(categories_item)

        network = d.pop("network", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        client_up_down_traffic_detail_open_api_vo = cls(
            client_mac=client_mac,
            client_name=client_name,
            type_=type_,
            manager=manager,
            up=up,
            down=down,
            applications=applications,
            categories=categories,
            network=network,
            vlan_id=vlan_id,
        )

        client_up_down_traffic_detail_open_api_vo.additional_properties = d
        return client_up_down_traffic_detail_open_api_vo

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
