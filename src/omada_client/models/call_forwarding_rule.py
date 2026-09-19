from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallForwardingRule")


@_attrs_define
class CallForwardingRule:
    """
    Attributes:
        enable (bool): Enable this rule or not
        condition (int): Forwarding condition. 0- no answer, 1- unconditional
        type_ (int): The call type to be forwarded. 0: All Incoming Calls - If this option is selected, all incoming
            calls will be forwarded.
            1: Calls to the Telephone Number - If this option is selected, select a telephone number from the list. Any
            incoming calls to this number will be forwarded.
            2: Calls to the Phone - If this option is selected, select a telephony device from the list. Any incoming calls
            to this device will be forwarded.
            3: Calls from a Person in the Telephone Book - If this option is selected, select a contact from the list. Any
            incoming calls from this contact will be forwarded.
            4: Calls from the Telephone Number - If this option is selected, enter a specific telephone number. Any incoming
            calls from this number will be forwarded.
        dest_number (str): The Destination Telephone Number that incoming calls will be redirected to.
        omadac_id (str | Unset): Omadac ID
        site_id (str | Unset): Site ID
        rule_id (str | Unset): Call forwarding rule id
        to_numbers (list[str] | Unset): Any incoming calls to these numbers will be forwarded.
        to_devices (list[int] | Unset): Any incoming calls to these devices will be forwarded.
        from_persons (list[str] | Unset): Any incoming calls from these contacts will be forwarded.
        from_numbers (list[str] | Unset): Any incoming calls from these numbers will be forwarded.
        forward_via (str | Unset): "Auto" by default.
    """

    enable: bool
    condition: int
    type_: int
    dest_number: str
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    rule_id: str | Unset = UNSET
    to_numbers: list[str] | Unset = UNSET
    to_devices: list[int] | Unset = UNSET
    from_persons: list[str] | Unset = UNSET
    from_numbers: list[str] | Unset = UNSET
    forward_via: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        condition = self.condition

        type_ = self.type_

        dest_number = self.dest_number

        omadac_id = self.omadac_id

        site_id = self.site_id

        rule_id = self.rule_id

        to_numbers: list[str] | Unset = UNSET
        if not isinstance(self.to_numbers, Unset):
            to_numbers = self.to_numbers

        to_devices: list[int] | Unset = UNSET
        if not isinstance(self.to_devices, Unset):
            to_devices = self.to_devices

        from_persons: list[str] | Unset = UNSET
        if not isinstance(self.from_persons, Unset):
            from_persons = self.from_persons

        from_numbers: list[str] | Unset = UNSET
        if not isinstance(self.from_numbers, Unset):
            from_numbers = self.from_numbers

        forward_via = self.forward_via

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "condition": condition,
                "type": type_,
                "destNumber": dest_number,
            }
        )
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if to_numbers is not UNSET:
            field_dict["toNumbers"] = to_numbers
        if to_devices is not UNSET:
            field_dict["toDevices"] = to_devices
        if from_persons is not UNSET:
            field_dict["fromPersons"] = from_persons
        if from_numbers is not UNSET:
            field_dict["fromNumbers"] = from_numbers
        if forward_via is not UNSET:
            field_dict["forwardVia"] = forward_via

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        condition = d.pop("condition")

        type_ = d.pop("type")

        dest_number = d.pop("destNumber")

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        to_numbers = cast(list[str], d.pop("toNumbers", UNSET))

        to_devices = cast(list[int], d.pop("toDevices", UNSET))

        from_persons = cast(list[str], d.pop("fromPersons", UNSET))

        from_numbers = cast(list[str], d.pop("fromNumbers", UNSET))

        forward_via = d.pop("forwardVia", UNSET)

        call_forwarding_rule = cls(
            enable=enable,
            condition=condition,
            type_=type_,
            dest_number=dest_number,
            omadac_id=omadac_id,
            site_id=site_id,
            rule_id=rule_id,
            to_numbers=to_numbers,
            to_devices=to_devices,
            from_persons=from_persons,
            from_numbers=from_numbers,
            forward_via=forward_via,
        )

        call_forwarding_rule.additional_properties = d
        return call_forwarding_rule

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
