from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pon_port_information_dto_status import PonPortInformationDTOStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PonPortInformationDTO")


@_attrs_define
class PonPortInformationDTO:
    """Content

    Attributes:
        port_id (str | Unset): OLT port id
        onu_num (int | Unset): The number of successfully registered ONU devices on this port, onuNum should be within
            the range of 0 to 128.
        status (PonPortInformationDTOStatus | Unset): Whether to enable the laser for the PON port.Status should be a
            value as follows:DISABLE,ENABLE.
        max_bandwidth (int | Unset): Maximum usable bandwidth of the PON port: 0 to 1310720 kbps.
        actual_bandwidth (int | Unset): Actual usable bandwidth of the PON port: 0 to 1310720 kbps.
        remain_bandwidth (int | Unset): Remaining usable bandwidth of the PON port: 0 to 1310720 kbps.
        optical_vcc (str | Unset): PON port optical voltage, in V.
        optical_bias (str | Unset): PON port optical current, in mA.
        optical_power (str | Unset): PON port power, in dBm.
    """

    port_id: str | Unset = UNSET
    onu_num: int | Unset = UNSET
    status: PonPortInformationDTOStatus | Unset = UNSET
    max_bandwidth: int | Unset = UNSET
    actual_bandwidth: int | Unset = UNSET
    remain_bandwidth: int | Unset = UNSET
    optical_vcc: str | Unset = UNSET
    optical_bias: str | Unset = UNSET
    optical_power: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        onu_num = self.onu_num

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        max_bandwidth = self.max_bandwidth

        actual_bandwidth = self.actual_bandwidth

        remain_bandwidth = self.remain_bandwidth

        optical_vcc = self.optical_vcc

        optical_bias = self.optical_bias

        optical_power = self.optical_power

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if onu_num is not UNSET:
            field_dict["onuNum"] = onu_num
        if status is not UNSET:
            field_dict["status"] = status
        if max_bandwidth is not UNSET:
            field_dict["maxBandwidth"] = max_bandwidth
        if actual_bandwidth is not UNSET:
            field_dict["actualBandwidth"] = actual_bandwidth
        if remain_bandwidth is not UNSET:
            field_dict["remainBandwidth"] = remain_bandwidth
        if optical_vcc is not UNSET:
            field_dict["opticalVcc"] = optical_vcc
        if optical_bias is not UNSET:
            field_dict["opticalBias"] = optical_bias
        if optical_power is not UNSET:
            field_dict["opticalPower"] = optical_power

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        onu_num = d.pop("onuNum", UNSET)

        _status = d.pop("status", UNSET)
        status: PonPortInformationDTOStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PonPortInformationDTOStatus(_status)

        max_bandwidth = d.pop("maxBandwidth", UNSET)

        actual_bandwidth = d.pop("actualBandwidth", UNSET)

        remain_bandwidth = d.pop("remainBandwidth", UNSET)

        optical_vcc = d.pop("opticalVcc", UNSET)

        optical_bias = d.pop("opticalBias", UNSET)

        optical_power = d.pop("opticalPower", UNSET)

        pon_port_information_dto = cls(
            port_id=port_id,
            onu_num=onu_num,
            status=status,
            max_bandwidth=max_bandwidth,
            actual_bandwidth=actual_bandwidth,
            remain_bandwidth=remain_bandwidth,
            optical_vcc=optical_vcc,
            optical_bias=optical_bias,
            optical_power=optical_power,
        )

        pon_port_information_dto.additional_properties = d
        return pon_port_information_dto

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
