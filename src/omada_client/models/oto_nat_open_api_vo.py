from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtoNatOpenApiVO")


@_attrs_define
class OtoNatOpenApiVO:
    """
    Attributes:
        name (str): Name, name should contain 1 to 64 characters.
        status (bool): Status
        interface_ids (list[str]): This field represents WAN port ID. WAN port ID can be obtained from can be obtained
            from 'Get internet basic info' interface.
        internal_ip (str): Internal IP
        external_ip (str): External IP
        dmz (bool): Whether to enable the h323 dmz
        description (str | Unset): Description should contain 1 to 64 characters.
    """

    name: str
    status: bool
    interface_ids: list[str]
    internal_ip: str
    external_ip: str
    dmz: bool
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        interface_ids = self.interface_ids

        internal_ip = self.internal_ip

        external_ip = self.external_ip

        dmz = self.dmz

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "interfaceIds": interface_ids,
                "internalIp": internal_ip,
                "externalIp": external_ip,
                "dmz": dmz,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        interface_ids = cast(list[str], d.pop("interfaceIds"))

        internal_ip = d.pop("internalIp")

        external_ip = d.pop("externalIp")

        dmz = d.pop("dmz")

        description = d.pop("description", UNSET)

        oto_nat_open_api_vo = cls(
            name=name,
            status=status,
            interface_ids=interface_ids,
            internal_ip=internal_ip,
            external_ip=external_ip,
            dmz=dmz,
            description=description,
        )

        oto_nat_open_api_vo.additional_properties = d
        return oto_nat_open_api_vo

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
