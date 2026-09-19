from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPsecFailoverConfiguration")


@_attrs_define
class IPsecFailoverConfiguration:
    """
    Attributes:
        name (str): Name should contain 1 to 64 characters.
        primary (str): Primary of the IPSec failover. IPsec VPN can be created using 'Create site-to-site VPN'
            interface, and ID can be obtained from 'Get site-to-site VPN list' interface.
        candidates (list[str]): Candidates of the IPSec failover. IPsec VPN can be created using 'Create site-to-site
            VPN' interface, and ID can be obtained from 'Get site-to-site VPN list' interface.
        id (str | Unset): ID of the IPSec failover.
        failback (bool | Unset): Failback of the IPSec failover.
        failback_time (int | Unset): Failback time should be within the range of 10–3600s.
    """

    name: str
    primary: str
    candidates: list[str]
    id: str | Unset = UNSET
    failback: bool | Unset = UNSET
    failback_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        primary = self.primary

        candidates = self.candidates

        id = self.id

        failback = self.failback

        failback_time = self.failback_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "primary": primary,
                "candidates": candidates,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if failback is not UNSET:
            field_dict["failback"] = failback
        if failback_time is not UNSET:
            field_dict["failbackTime"] = failback_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        primary = d.pop("primary")

        candidates = cast(list[str], d.pop("candidates"))

        id = d.pop("id", UNSET)

        failback = d.pop("failback", UNSET)

        failback_time = d.pop("failbackTime", UNSET)

        i_psec_failover_configuration = cls(
            name=name,
            primary=primary,
            candidates=candidates,
            id=id,
            failback=failback,
            failback_time=failback_time,
        )

        i_psec_failover_configuration.additional_properties = d
        return i_psec_failover_configuration

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
