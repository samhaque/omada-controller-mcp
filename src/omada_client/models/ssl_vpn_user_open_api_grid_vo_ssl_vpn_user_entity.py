from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssl_vpn_user_entity import SslVpnUserEntity


T = TypeVar("T", bound="SslVpnUserOpenApiGridVOSslVpnUserEntity")


@_attrs_define
class SslVpnUserOpenApiGridVOSslVpnUserEntity:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[SslVpnUserEntity] | Unset):
        total (int | Unset): Total number of the SSL VPN user
        available (int | Unset): Available number of the SSL VPN user
        expired (int | Unset): Expired number of the SSL VPN user
        ssl_vpn_max_con_user_num (int | Unset):
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[SslVpnUserEntity] | Unset = UNSET
    total: int | Unset = UNSET
    available: int | Unset = UNSET
    expired: int | Unset = UNSET
    ssl_vpn_max_con_user_num: int | Unset = UNSET
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

        total = self.total

        available = self.available

        expired = self.expired

        ssl_vpn_max_con_user_num = self.ssl_vpn_max_con_user_num

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
        if total is not UNSET:
            field_dict["total"] = total
        if available is not UNSET:
            field_dict["available"] = available
        if expired is not UNSET:
            field_dict["expired"] = expired
        if ssl_vpn_max_con_user_num is not UNSET:
            field_dict["sslVpnMaxConUserNum"] = ssl_vpn_max_con_user_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssl_vpn_user_entity import SslVpnUserEntity

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[SslVpnUserEntity] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = SslVpnUserEntity.from_dict(data_item_data)

                data.append(data_item)

        total = d.pop("total", UNSET)

        available = d.pop("available", UNSET)

        expired = d.pop("expired", UNSET)

        ssl_vpn_max_con_user_num = d.pop("sslVpnMaxConUserNum", UNSET)

        ssl_vpn_user_open_api_grid_vo_ssl_vpn_user_entity = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            total=total,
            available=available,
            expired=expired,
            ssl_vpn_max_con_user_num=ssl_vpn_max_con_user_num,
        )

        ssl_vpn_user_open_api_grid_vo_ssl_vpn_user_entity.additional_properties = d
        return ssl_vpn_user_open_api_grid_vo_ssl_vpn_user_entity

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
