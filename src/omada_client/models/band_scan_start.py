from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandScanStart")


@_attrs_define
class BandScanStart:
    """
    Attributes:
        port_uuid (str): The ID of the port.
        sim_card (int | Unset): When the device supports Dual-SIM card, parameter [simCard] should not be null.1: SIM1;
            2: SIM2.
        mode (int | Unset): Band mode. 1: 4G scan; 2: 5G scan.
    """

    port_uuid: str
    sim_card: int | Unset = UNSET
    mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        sim_card = self.sim_card

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portUuid": port_uuid,
            }
        )
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid = d.pop("portUuid")

        sim_card = d.pop("simCard", UNSET)

        mode = d.pop("mode", UNSET)

        band_scan_start = cls(
            port_uuid=port_uuid,
            sim_card=sim_card,
            mode=mode,
        )

        band_scan_start.additional_properties = d
        return band_scan_start

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
