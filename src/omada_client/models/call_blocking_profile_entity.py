from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incoming_calls_blocking_vo import IncomingCallsBlockingVO
    from ..models.outgoing_calls_blocking_vo import OutgoingCallsBlockingVO


T = TypeVar("T", bound="CallBlockingProfileEntity")


@_attrs_define
class CallBlockingProfileEntity:
    """
    Attributes:
        profile_id (str | Unset): Call blocking profile ID
        omadac_id (str | Unset): Omadac ID
        site_id (str | Unset): Site ID
        profile_name (str | Unset): Call blocking profile name
        incoming_calls_blocking_enable (bool | Unset): Enable incoming calls blocking or not.
        incoming_calls_blocking (IncomingCallsBlockingVO | Unset): Incoming calls blocking rules. Rules are valid if and
            only if parameter [incomingCallsBlockingEnable] equals true.
        outgoing_calls_blocking_enable (bool | Unset): Enable outgoing calls blocking or not.
        outgoing_calls_blocking (OutgoingCallsBlockingVO | Unset): Outgoing calls blocking rules. Rules are valid if and
            only if parameter [outgoingCallsBlockingEnable] equals true.
    """

    profile_id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    profile_name: str | Unset = UNSET
    incoming_calls_blocking_enable: bool | Unset = UNSET
    incoming_calls_blocking: IncomingCallsBlockingVO | Unset = UNSET
    outgoing_calls_blocking_enable: bool | Unset = UNSET
    outgoing_calls_blocking: OutgoingCallsBlockingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        omadac_id = self.omadac_id

        site_id = self.site_id

        profile_name = self.profile_name

        incoming_calls_blocking_enable = self.incoming_calls_blocking_enable

        incoming_calls_blocking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incoming_calls_blocking, Unset):
            incoming_calls_blocking = self.incoming_calls_blocking.to_dict()

        outgoing_calls_blocking_enable = self.outgoing_calls_blocking_enable

        outgoing_calls_blocking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outgoing_calls_blocking, Unset):
            outgoing_calls_blocking = self.outgoing_calls_blocking.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if incoming_calls_blocking_enable is not UNSET:
            field_dict["incomingCallsBlockingEnable"] = incoming_calls_blocking_enable
        if incoming_calls_blocking is not UNSET:
            field_dict["incomingCallsBlocking"] = incoming_calls_blocking
        if outgoing_calls_blocking_enable is not UNSET:
            field_dict["outgoingCallsBlockingEnable"] = outgoing_calls_blocking_enable
        if outgoing_calls_blocking is not UNSET:
            field_dict["outgoingCallsBlocking"] = outgoing_calls_blocking

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incoming_calls_blocking_vo import (
            IncomingCallsBlockingVO,
        )
        from ..models.outgoing_calls_blocking_vo import (
            OutgoingCallsBlockingVO,
        )

        d = dict(src_dict)
        profile_id = d.pop("profileId", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        profile_name = d.pop("profileName", UNSET)

        incoming_calls_blocking_enable = d.pop("incomingCallsBlockingEnable", UNSET)

        _incoming_calls_blocking = d.pop("incomingCallsBlocking", UNSET)
        incoming_calls_blocking: IncomingCallsBlockingVO | Unset
        if isinstance(_incoming_calls_blocking, Unset):
            incoming_calls_blocking = UNSET
        else:
            incoming_calls_blocking = IncomingCallsBlockingVO.from_dict(
                _incoming_calls_blocking
            )

        outgoing_calls_blocking_enable = d.pop("outgoingCallsBlockingEnable", UNSET)

        _outgoing_calls_blocking = d.pop("outgoingCallsBlocking", UNSET)
        outgoing_calls_blocking: OutgoingCallsBlockingVO | Unset
        if isinstance(_outgoing_calls_blocking, Unset):
            outgoing_calls_blocking = UNSET
        else:
            outgoing_calls_blocking = OutgoingCallsBlockingVO.from_dict(
                _outgoing_calls_blocking
            )

        call_blocking_profile_entity = cls(
            profile_id=profile_id,
            omadac_id=omadac_id,
            site_id=site_id,
            profile_name=profile_name,
            incoming_calls_blocking_enable=incoming_calls_blocking_enable,
            incoming_calls_blocking=incoming_calls_blocking,
            outgoing_calls_blocking_enable=outgoing_calls_blocking_enable,
            outgoing_calls_blocking=outgoing_calls_blocking,
        )

        call_blocking_profile_entity.additional_properties = d
        return call_blocking_profile_entity

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
