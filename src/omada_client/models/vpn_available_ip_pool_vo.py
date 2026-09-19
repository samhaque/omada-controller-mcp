from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_subnets_open_api_vo import IPSubnetsOpenApiVO


T = TypeVar("T", bound="VpnAvailableIpPoolVO")


@_attrs_define
class VpnAvailableIpPoolVO:
    """
    Attributes:
        ip_pool (list[IPSubnetsOpenApiVO] | Unset): Available IP pools.
    """

    ip_pool: list[IPSubnetsOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_pool: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip_pool, Unset):
            ip_pool = []
            for ip_pool_item_data in self.ip_pool:
                ip_pool_item = ip_pool_item_data.to_dict()
                ip_pool.append(ip_pool_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip_pool is not UNSET:
            field_dict["ipPool"] = ip_pool

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ip_subnets_open_api_vo import IPSubnetsOpenApiVO

        d = dict(src_dict)
        _ip_pool = d.pop("ipPool", UNSET)
        ip_pool: list[IPSubnetsOpenApiVO] | Unset = UNSET
        if _ip_pool is not UNSET:
            ip_pool = []
            for ip_pool_item_data in _ip_pool:
                ip_pool_item = IPSubnetsOpenApiVO.from_dict(ip_pool_item_data)

                ip_pool.append(ip_pool_item)

        vpn_available_ip_pool_vo = cls(
            ip_pool=ip_pool,
        )

        vpn_available_ip_pool_vo.additional_properties = d
        return vpn_available_ip_pool_vo

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
