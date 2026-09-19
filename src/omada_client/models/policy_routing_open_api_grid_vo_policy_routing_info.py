from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy_routing_info import PolicyRoutingInfo


T = TypeVar("T", bound="PolicyRoutingOpenApiGridVOPolicyRoutingInfo")


@_attrs_define
class PolicyRoutingOpenApiGridVOPolicyRoutingInfo:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[PolicyRoutingInfo] | Unset):
        support_multi (bool | Unset): Whether multiple WAN interface is supported in Policy Routing.
        support_location_group_dest (bool | Unset): Whether Location Group is supported as Destination in Policy
            Routing.
        support_domain_group_dest (bool | Unset): Whether Domain Group is supported as Interface in Policy Routing.
        support_vpn_client (bool | Unset): Whether Vpn Client is supported as Interface in Policy Routing.
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[PolicyRoutingInfo] | Unset = UNSET
    support_multi: bool | Unset = UNSET
    support_location_group_dest: bool | Unset = UNSET
    support_domain_group_dest: bool | Unset = UNSET
    support_vpn_client: bool | Unset = UNSET
    support_by_ds_lite_and_map_e: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        support_multi = self.support_multi

        support_location_group_dest = self.support_location_group_dest

        support_domain_group_dest = self.support_domain_group_dest

        support_vpn_client = self.support_vpn_client

        support_by_ds_lite_and_map_e = self.support_by_ds_lite_and_map_e

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data
        if support_multi is not UNSET:
            field_dict["supportMulti"] = support_multi
        if support_location_group_dest is not UNSET:
            field_dict["supportLocationGroupDest"] = support_location_group_dest
        if support_domain_group_dest is not UNSET:
            field_dict["supportDomainGroupDest"] = support_domain_group_dest
        if support_vpn_client is not UNSET:
            field_dict["supportVpnClient"] = support_vpn_client
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_routing_info import PolicyRoutingInfo

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[PolicyRoutingInfo] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = PolicyRoutingInfo.from_dict(data_item_data)

                data.append(data_item)

        support_multi = d.pop("supportMulti", UNSET)

        support_location_group_dest = d.pop("supportLocationGroupDest", UNSET)

        support_domain_group_dest = d.pop("supportDomainGroupDest", UNSET)

        support_vpn_client = d.pop("supportVpnClient", UNSET)

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        policy_routing_open_api_grid_vo_policy_routing_info = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_multi=support_multi,
            support_location_group_dest=support_location_group_dest,
            support_domain_group_dest=support_domain_group_dest,
            support_vpn_client=support_vpn_client,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
        )

        policy_routing_open_api_grid_vo_policy_routing_info.additional_properties = d
        return policy_routing_open_api_grid_vo_policy_routing_info

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
