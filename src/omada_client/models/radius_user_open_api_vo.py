from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusUserOpenApiVO")


@_attrs_define
class RadiusUserOpenApiVO:
    """
    Attributes:
        user_id (str | Unset): Build-in RADIUS profile user ID
        type_ (int | Unset): Type of Build-in RADIUS profile user, 0: user auth; 1: MAC auth
        username (str | Unset): Build-in RADIUS profile user name, when parameter [type] is 1, [username] is the MAC
            address
        password (str | Unset): Build-in RADIUS profile user password, when parameter [type] is 1, [password] is the MAC
            address
        up_rate_limit (int | Unset): Build-in RADIUS profile user uplink rate limit, unit: Kbps
        down_rate_limit (int | Unset): Build-in RADIUS profile user downlink rate limit, unit: Kbps
        up_limit (int | Unset): Build-in RADIUS profile user uplink traffic limit, unit: MB
        down_limit (int | Unset): Build-in RADIUS profile user downlink traffic limit, unit: MB
        vlan_id (int | Unset): VLAN ID, from 1 to 4096
        timeout (int | Unset): Session timeout
        description (str | Unset): Description of radius user, should contain 1 to 256 characters
    """

    user_id: str | Unset = UNSET
    type_: int | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    up_rate_limit: int | Unset = UNSET
    down_rate_limit: int | Unset = UNSET
    up_limit: int | Unset = UNSET
    down_limit: int | Unset = UNSET
    vlan_id: int | Unset = UNSET
    timeout: int | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        type_ = self.type_

        username = self.username

        password = self.password

        up_rate_limit = self.up_rate_limit

        down_rate_limit = self.down_rate_limit

        up_limit = self.up_limit

        down_limit = self.down_limit

        vlan_id = self.vlan_id

        timeout = self.timeout

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
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
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        type_ = d.pop("type", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        up_rate_limit = d.pop("upRateLimit", UNSET)

        down_rate_limit = d.pop("downRateLimit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        timeout = d.pop("timeout", UNSET)

        description = d.pop("description", UNSET)

        radius_user_open_api_vo = cls(
            user_id=user_id,
            type_=type_,
            username=username,
            password=password,
            up_rate_limit=up_rate_limit,
            down_rate_limit=down_rate_limit,
            up_limit=up_limit,
            down_limit=down_limit,
            vlan_id=vlan_id,
            timeout=timeout,
            description=description,
        )

        radius_user_open_api_vo.additional_properties = d
        return radius_user_open_api_vo

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
