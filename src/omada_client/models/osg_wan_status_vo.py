from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgWanStatusVO")


@_attrs_define
class OsgWanStatusVO:
    """
    Attributes:
        port_uuid (str | Unset):
        port_name (str | Unset):
        enable (int | Unset):
        lan_id (str | Unset):
        proto (str | Unset):
        pd_enable (int | Unset):
        prefix (str | Unset):
        pd_size (int | Unset):
        type_ (int | Unset):
    """

    port_uuid: str | Unset = UNSET
    port_name: str | Unset = UNSET
    enable: int | Unset = UNSET
    lan_id: str | Unset = UNSET
    proto: str | Unset = UNSET
    pd_enable: int | Unset = UNSET
    prefix: str | Unset = UNSET
    pd_size: int | Unset = UNSET
    type_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        port_name = self.port_name

        enable = self.enable

        lan_id = self.lan_id

        proto = self.proto

        pd_enable = self.pd_enable

        prefix = self.prefix

        pd_size = self.pd_size

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if enable is not UNSET:
            field_dict["enable"] = enable
        if lan_id is not UNSET:
            field_dict["lanId"] = lan_id
        if proto is not UNSET:
            field_dict["proto"] = proto
        if pd_enable is not UNSET:
            field_dict["pdEnable"] = pd_enable
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if pd_size is not UNSET:
            field_dict["pdSize"] = pd_size
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid = d.pop("portUuid", UNSET)

        port_name = d.pop("portName", UNSET)

        enable = d.pop("enable", UNSET)

        lan_id = d.pop("lanId", UNSET)

        proto = d.pop("proto", UNSET)

        pd_enable = d.pop("pdEnable", UNSET)

        prefix = d.pop("prefix", UNSET)

        pd_size = d.pop("pdSize", UNSET)

        type_ = d.pop("type", UNSET)

        osg_wan_status_vo = cls(
            port_uuid=port_uuid,
            port_name=port_name,
            enable=enable,
            lan_id=lan_id,
            proto=proto,
            pd_enable=pd_enable,
            prefix=prefix,
            pd_size=pd_size,
            type_=type_,
        )

        osg_wan_status_vo.additional_properties = d
        return osg_wan_status_vo

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
