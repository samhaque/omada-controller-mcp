from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.band_result_open_api_vo import BandResultOpenApiVO


T = TypeVar("T", bound="BandScanResultOpenApiVO")


@_attrs_define
class BandScanResultOpenApiVO:
    """
    Attributes:
        status (int | Unset): The status of the band scan: 0 - Failed, 1 - Succeeded, 2 - Scanning.
        bands (list[BandResultOpenApiVO] | Unset): The result of the band scan.
        isp (str | Unset): Internet service provider.
        sim_card (int | Unset): When the device supports Dual-SIM card, parameter [simCard] should not be null.1: SIM1;
            2: SIM2.
    """

    status: int | Unset = UNSET
    bands: list[BandResultOpenApiVO] | Unset = UNSET
    isp: str | Unset = UNSET
    sim_card: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        bands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bands, Unset):
            bands = []
            for bands_item_data in self.bands:
                bands_item = bands_item_data.to_dict()
                bands.append(bands_item)

        isp = self.isp

        sim_card = self.sim_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if bands is not UNSET:
            field_dict["bands"] = bands
        if isp is not UNSET:
            field_dict["isp"] = isp
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.band_result_open_api_vo import (
            BandResultOpenApiVO,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        _bands = d.pop("bands", UNSET)
        bands: list[BandResultOpenApiVO] | Unset = UNSET
        if _bands is not UNSET:
            bands = []
            for bands_item_data in _bands:
                bands_item = BandResultOpenApiVO.from_dict(bands_item_data)

                bands.append(bands_item)

        isp = d.pop("isp", UNSET)

        sim_card = d.pop("simCard", UNSET)

        band_scan_result_open_api_vo = cls(
            status=status,
            bands=bands,
            isp=isp,
            sim_card=sim_card,
        )

        band_scan_result_open_api_vo.additional_properties = d
        return band_scan_result_open_api_vo

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
