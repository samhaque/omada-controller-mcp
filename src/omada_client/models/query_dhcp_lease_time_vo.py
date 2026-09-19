from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.query_dhcp_lease_time_param_vo import QueryDhcpLeaseTimeParamVO


T = TypeVar("T", bound="QueryDhcpLeaseTimeVO")


@_attrs_define
class QueryDhcpLeaseTimeVO:
    """
    Attributes:
        query_dhcp_lease_time_param_vos (list[QueryDhcpLeaseTimeParamVO]):
    """

    query_dhcp_lease_time_param_vos: list[QueryDhcpLeaseTimeParamVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_dhcp_lease_time_param_vos = []
        for (
            query_dhcp_lease_time_param_vos_item_data
        ) in self.query_dhcp_lease_time_param_vos:
            query_dhcp_lease_time_param_vos_item = (
                query_dhcp_lease_time_param_vos_item_data.to_dict()
            )
            query_dhcp_lease_time_param_vos.append(query_dhcp_lease_time_param_vos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queryDhcpLeaseTimeParamVOS": query_dhcp_lease_time_param_vos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.query_dhcp_lease_time_param_vo import (
            QueryDhcpLeaseTimeParamVO,
        )

        d = dict(src_dict)
        query_dhcp_lease_time_param_vos = []
        _query_dhcp_lease_time_param_vos = d.pop("queryDhcpLeaseTimeParamVOS")
        for (
            query_dhcp_lease_time_param_vos_item_data
        ) in _query_dhcp_lease_time_param_vos:
            query_dhcp_lease_time_param_vos_item = QueryDhcpLeaseTimeParamVO.from_dict(
                query_dhcp_lease_time_param_vos_item_data
            )

            query_dhcp_lease_time_param_vos.append(query_dhcp_lease_time_param_vos_item)

        query_dhcp_lease_time_vo = cls(
            query_dhcp_lease_time_param_vos=query_dhcp_lease_time_param_vos,
        )

        query_dhcp_lease_time_vo.additional_properties = d
        return query_dhcp_lease_time_vo

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
