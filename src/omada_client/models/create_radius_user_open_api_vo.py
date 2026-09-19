from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius_user_info_open_api_vo import RadiusUserInfoOpenApiVO


T = TypeVar("T", bound="CreateRadiusUserOpenApiVO")


@_attrs_define
class CreateRadiusUserOpenApiVO:
    """
    Attributes:
        type_ (int): Type of Build-in RADIUS profile user, 0: user auth; 1: MAC auth
        user_info (RadiusUserInfoOpenApiVO | Unset): User name and password, required when parameter [type] is 0.
        mac_address (str | Unset): MAC address, required when parameter [type] is 1. Should be a valid MAC address
            format
        up_rate_limit (int | Unset): Build-in RADIUS profile user uplink rate limit, unit: Kbps. UpRateLimit should be
            within the range of 1-10485760
        down_rate_limit (int | Unset): Build-in RADIUS profile user downlink rate limit, unit: Kbps. DownRateLimit
            should be within the range of 1-10485760
        up_limit (int | Unset): Build-in RADIUS profile user uplink traffic limit, unit: MB. UpLimit should be within
            the range of 1-10485760
        down_limit (int | Unset): Build-in RADIUS profile user downlink traffic limit, unit: MB. DownLimit should be
            within the range of 1-10485760
        vlan_id (int | Unset): VLAN ID. VlanId should be within the range of 1-4096
        timeout (int | Unset): Session timeout, unit: second
        description (str | Unset): Description of radius user, should contain 1 to 256 characters
    """

    type_: int
    user_info: RadiusUserInfoOpenApiVO | Unset = UNSET
    mac_address: str | Unset = UNSET
    up_rate_limit: int | Unset = UNSET
    down_rate_limit: int | Unset = UNSET
    up_limit: int | Unset = UNSET
    down_limit: int | Unset = UNSET
    vlan_id: int | Unset = UNSET
    timeout: int | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict()

        mac_address = self.mac_address

        up_rate_limit = self.up_rate_limit

        down_rate_limit = self.down_rate_limit

        up_limit = self.up_limit

        down_limit = self.down_limit

        vlan_id = self.vlan_id

        timeout = self.timeout

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if up_rate_limit is not UNSET:
            field_dict["upRateLimit"] = up_rate_limit
        if down_rate_limit is not UNSET:
            field_dict["downRateLimit"] = down_rate_limit
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.radius_user_info_open_api_vo import (
            RadiusUserInfoOpenApiVO,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        _user_info = d.pop("userInfo", UNSET)
        user_info: RadiusUserInfoOpenApiVO | Unset
        if isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = RadiusUserInfoOpenApiVO.from_dict(_user_info)

        mac_address = d.pop("macAddress", UNSET)

        up_rate_limit = d.pop("upRateLimit", UNSET)

        down_rate_limit = d.pop("downRateLimit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        timeout = d.pop("timeout", UNSET)

        description = d.pop("description", UNSET)

        create_radius_user_open_api_vo = cls(
            type_=type_,
            user_info=user_info,
            mac_address=mac_address,
            up_rate_limit=up_rate_limit,
            down_rate_limit=down_rate_limit,
            up_limit=up_limit,
            down_limit=down_limit,
            vlan_id=vlan_id,
            timeout=timeout,
            description=description,
        )

        create_radius_user_open_api_vo.additional_properties = d
        return create_radius_user_open_api_vo

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
