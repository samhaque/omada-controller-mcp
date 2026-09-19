from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dot1XPortInfoOpenApiVO")


@_attrs_define
class Dot1XPortInfoOpenApiVO:
    """Switch port information

    Attributes:
        port (int | Unset): Port number
        dot_1_x_enable (bool | Unset): 802.1x enable status
        mab_enable (bool | Unset): MAB enable status
        auth_type (int | Unset): The auth type of the port. AuthType should be a value as follows: 0: Authentication not
            enabled, 1: Only 802.1x auth enabled, 2: Only MAB auth enabled, 3: Both 802.1x auth and MAB auth, it will
            perform 802.1x auth first, and perform MAB auth after 802.1x auth failed.
        operation (str | Unset): switching or mirroring or aggregating
        lag (bool | Unset): Whether the port is a lag port. Lag ports do not suppot 802.1x or MAB authentication.
    """

    port: int | Unset = UNSET
    dot_1_x_enable: bool | Unset = UNSET
    mab_enable: bool | Unset = UNSET
    auth_type: int | Unset = UNSET
    operation: str | Unset = UNSET
    lag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        dot_1_x_enable = self.dot_1_x_enable

        mab_enable = self.mab_enable

        auth_type = self.auth_type

        operation = self.operation

        lag = self.lag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if dot_1_x_enable is not UNSET:
            field_dict["dot1xEnable"] = dot_1_x_enable
        if mab_enable is not UNSET:
            field_dict["mabEnable"] = mab_enable
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if operation is not UNSET:
            field_dict["operation"] = operation
        if lag is not UNSET:
            field_dict["lag"] = lag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        dot_1_x_enable = d.pop("dot1xEnable", UNSET)

        mab_enable = d.pop("mabEnable", UNSET)

        auth_type = d.pop("authType", UNSET)

        operation = d.pop("operation", UNSET)

        lag = d.pop("lag", UNSET)

        dot_1x_port_info_open_api_vo = cls(
            port=port,
            dot_1_x_enable=dot_1_x_enable,
            mab_enable=mab_enable,
            auth_type=auth_type,
            operation=operation,
            lag=lag,
        )

        dot_1x_port_info_open_api_vo.additional_properties = d
        return dot_1x_port_info_open_api_vo

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
