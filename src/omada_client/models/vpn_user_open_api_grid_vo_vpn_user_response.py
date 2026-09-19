from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vpn_user_response import VpnUserResponse


T = TypeVar("T", bound="VpnUserOpenApiGridVOVpnUserResponse")


@_attrs_define
class VpnUserOpenApiGridVOVpnUserResponse:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[VpnUserResponse] | Unset):
        support_local_ip (bool | Unset): Whether the local IP address configuration is supported by the VPN user.
        support_l2tp (bool | Unset): Whether the L2TP configuration is supported by the VPN user.
        support_pptp (bool | Unset): Whether the PPTP configuration is supported by the VPN user.
        support_protocol (bool | Unset): Whether protocol configuration is supported of the VPN user
        support_open_vpn (bool | Unset): Whether the OpenVPN configuration is supported by the VPN user.
        support_ssl_vpn (bool | Unset): Whether the SSLVPN configuration is supported by the VPN user.
        max_concurrent_user (int | Unset): The maximum number of concurrent users supported by VPN.
        ssl_vpn_max_con_user_num (int | Unset): The maximum number of concurrent users supported by SSL VPN.
        subnets_limit_size (int | Unset): The maximum number of subnets allowed for a VPN user.
        support_server_optional (bool | Unset): Whether VPN server is optional.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[VpnUserResponse] | Unset = UNSET
    support_local_ip: bool | Unset = UNSET
    support_l2tp: bool | Unset = UNSET
    support_pptp: bool | Unset = UNSET
    support_protocol: bool | Unset = UNSET
    support_open_vpn: bool | Unset = UNSET
    support_ssl_vpn: bool | Unset = UNSET
    max_concurrent_user: int | Unset = UNSET
    ssl_vpn_max_con_user_num: int | Unset = UNSET
    subnets_limit_size: int | Unset = UNSET
    support_server_optional: bool | Unset = UNSET
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

        support_local_ip = self.support_local_ip

        support_l2tp = self.support_l2tp

        support_pptp = self.support_pptp

        support_protocol = self.support_protocol

        support_open_vpn = self.support_open_vpn

        support_ssl_vpn = self.support_ssl_vpn

        max_concurrent_user = self.max_concurrent_user

        ssl_vpn_max_con_user_num = self.ssl_vpn_max_con_user_num

        subnets_limit_size = self.subnets_limit_size

        support_server_optional = self.support_server_optional

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
        if support_local_ip is not UNSET:
            field_dict["supportLocalIp"] = support_local_ip
        if support_l2tp is not UNSET:
            field_dict["supportL2TP"] = support_l2tp
        if support_pptp is not UNSET:
            field_dict["supportPptp"] = support_pptp
        if support_protocol is not UNSET:
            field_dict["supportProtocol"] = support_protocol
        if support_open_vpn is not UNSET:
            field_dict["supportOpenVpn"] = support_open_vpn
        if support_ssl_vpn is not UNSET:
            field_dict["supportSslVpn"] = support_ssl_vpn
        if max_concurrent_user is not UNSET:
            field_dict["maxConcurrentUser"] = max_concurrent_user
        if ssl_vpn_max_con_user_num is not UNSET:
            field_dict["sslVpnMaxConUserNum"] = ssl_vpn_max_con_user_num
        if subnets_limit_size is not UNSET:
            field_dict["subnetsLimitSize"] = subnets_limit_size
        if support_server_optional is not UNSET:
            field_dict["supportServerOptional"] = support_server_optional

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vpn_user_response import VpnUserResponse

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[VpnUserResponse] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = VpnUserResponse.from_dict(data_item_data)

                data.append(data_item)

        support_local_ip = d.pop("supportLocalIp", UNSET)

        support_l2tp = d.pop("supportL2TP", UNSET)

        support_pptp = d.pop("supportPptp", UNSET)

        support_protocol = d.pop("supportProtocol", UNSET)

        support_open_vpn = d.pop("supportOpenVpn", UNSET)

        support_ssl_vpn = d.pop("supportSslVpn", UNSET)

        max_concurrent_user = d.pop("maxConcurrentUser", UNSET)

        ssl_vpn_max_con_user_num = d.pop("sslVpnMaxConUserNum", UNSET)

        subnets_limit_size = d.pop("subnetsLimitSize", UNSET)

        support_server_optional = d.pop("supportServerOptional", UNSET)

        vpn_user_open_api_grid_vo_vpn_user_response = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_local_ip=support_local_ip,
            support_l2tp=support_l2tp,
            support_pptp=support_pptp,
            support_protocol=support_protocol,
            support_open_vpn=support_open_vpn,
            support_ssl_vpn=support_ssl_vpn,
            max_concurrent_user=max_concurrent_user,
            ssl_vpn_max_con_user_num=ssl_vpn_max_con_user_num,
            subnets_limit_size=subnets_limit_size,
            support_server_optional=support_server_optional,
        )

        vpn_user_open_api_grid_vo_vpn_user_response.additional_properties = d
        return vpn_user_open_api_grid_vo_vpn_user_response

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
