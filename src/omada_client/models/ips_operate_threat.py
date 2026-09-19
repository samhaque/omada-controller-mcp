from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ips_operate_threat_id_and_time import IpsOperateThreatIdAndTime
    from ..models.signature_suppression import SignatureSuppression


T = TypeVar("T", bound="IpsOperateThreat")


@_attrs_define
class IpsOperateThreat:
    """
    Attributes:
        type_ (int): IPS Operate Threat type should be a value as follows: 0: block; 1:isolate device; 2: signature
            Suppression; 3: allow Example: 1.
        threat_id (list[IpsOperateThreatIdAndTime] | Unset): IPS signature type should be a value as follows: 0: all
            traffic; 1: packet tracking respectively.
        signature_suppression (SignatureSuppression | Unset): Signature suppression configuration
        block_name (str | Unset): IPS block name should not be empty when type is 0 or 1. Example: blockName.
    """

    type_: int
    threat_id: list[IpsOperateThreatIdAndTime] | Unset = UNSET
    signature_suppression: SignatureSuppression | Unset = UNSET
    block_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        threat_id: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.threat_id, Unset):
            threat_id = []
            for threat_id_item_data in self.threat_id:
                threat_id_item = threat_id_item_data.to_dict()
                threat_id.append(threat_id_item)

        signature_suppression: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signature_suppression, Unset):
            signature_suppression = self.signature_suppression.to_dict()

        block_name = self.block_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if threat_id is not UNSET:
            field_dict["threatId"] = threat_id
        if signature_suppression is not UNSET:
            field_dict["signatureSuppression"] = signature_suppression
        if block_name is not UNSET:
            field_dict["blockName"] = block_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ips_operate_threat_id_and_time import (
            IpsOperateThreatIdAndTime,
        )
        from ..models.signature_suppression import SignatureSuppression

        d = dict(src_dict)
        type_ = d.pop("type")

        _threat_id = d.pop("threatId", UNSET)
        threat_id: list[IpsOperateThreatIdAndTime] | Unset = UNSET
        if _threat_id is not UNSET:
            threat_id = []
            for threat_id_item_data in _threat_id:
                threat_id_item = IpsOperateThreatIdAndTime.from_dict(
                    threat_id_item_data
                )

                threat_id.append(threat_id_item)

        _signature_suppression = d.pop("signatureSuppression", UNSET)
        signature_suppression: SignatureSuppression | Unset
        if isinstance(_signature_suppression, Unset):
            signature_suppression = UNSET
        else:
            signature_suppression = SignatureSuppression.from_dict(
                _signature_suppression
            )

        block_name = d.pop("blockName", UNSET)

        ips_operate_threat = cls(
            type_=type_,
            threat_id=threat_id,
            signature_suppression=signature_suppression,
            block_name=block_name,
        )

        ips_operate_threat.additional_properties = d
        return ips_operate_threat

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
