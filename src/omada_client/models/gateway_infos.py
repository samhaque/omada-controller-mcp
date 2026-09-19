from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_wan_status import GatewayWanStatus


T = TypeVar("T", bound="GatewayInfos")


@_attrs_define
class GatewayInfos:
    """
    Attributes:
        site_id (str | Unset): site id.
        device_mac (str | Unset): device mac.
        uptime (str | Unset): up time.
        wan_status (list[GatewayWanStatus] | Unset): wan status infos.
    """

    site_id: str | Unset = UNSET
    device_mac: str | Unset = UNSET
    uptime: str | Unset = UNSET
    wan_status: list[GatewayWanStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        device_mac = self.device_mac

        uptime = self.uptime

        wan_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_status, Unset):
            wan_status = []
            for wan_status_item_data in self.wan_status:
                wan_status_item = wan_status_item_data.to_dict()
                wan_status.append(wan_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if wan_status is not UNSET:
            field_dict["wanStatus"] = wan_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.gateway_wan_status import GatewayWanStatus

        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        uptime = d.pop("uptime", UNSET)

        _wan_status = d.pop("wanStatus", UNSET)
        wan_status: list[GatewayWanStatus] | Unset = UNSET
        if _wan_status is not UNSET:
            wan_status = []
            for wan_status_item_data in _wan_status:
                wan_status_item = GatewayWanStatus.from_dict(wan_status_item_data)

                wan_status.append(wan_status_item)

        gateway_infos = cls(
            site_id=site_id,
            device_mac=device_mac,
            uptime=uptime,
            wan_status=wan_status,
        )

        gateway_infos.additional_properties = d
        return gateway_infos

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
