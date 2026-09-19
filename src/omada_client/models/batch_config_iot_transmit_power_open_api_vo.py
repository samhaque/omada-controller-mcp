from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchConfigIotTransmitPowerOpenApiVO")


@_attrs_define
class BatchConfigIotTransmitPowerOpenApiVO:
    """
    Attributes:
        macs (list[str]): Device mac list. If selectAll is true, mac in macs is excluded.
        override (bool): Whether to override the configuration.
        select_all (bool): Whether to select all device. The selected devices are the ones filtered out based on the
            searchKey.
        transmit_power (int | Unset): Broadcast transmission power.<br />The parameter [transmitPower] should be a value
            as follows:[-20, -18, -15, -12, -10, -9, -6, -5, -3, 0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 20].(0 by
            default)
        search_key (str | Unset): Look for a specific piece of data.
    """

    macs: list[str]
    override: bool
    select_all: bool
    transmit_power: int | Unset = UNSET
    search_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        macs = self.macs

        override = self.override

        select_all = self.select_all

        transmit_power = self.transmit_power

        search_key = self.search_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "macs": macs,
                "override": override,
                "selectAll": select_all,
            }
        )
        if transmit_power is not UNSET:
            field_dict["transmitPower"] = transmit_power
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        macs = cast(list[str], d.pop("macs"))

        override = d.pop("override")

        select_all = d.pop("selectAll")

        transmit_power = d.pop("transmitPower", UNSET)

        search_key = d.pop("searchKey", UNSET)

        batch_config_iot_transmit_power_open_api_vo = cls(
            macs=macs,
            override=override,
            select_all=select_all,
            transmit_power=transmit_power,
            search_key=search_key,
        )

        batch_config_iot_transmit_power_open_api_vo.additional_properties = d
        return batch_config_iot_transmit_power_open_api_vo

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
