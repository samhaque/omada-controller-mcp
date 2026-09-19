from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_speed_test_results_open_api_vo_speed_test_result import (
        ApSpeedTestResultsOpenApiVOSpeedTestResult,
    )


T = TypeVar("T", bound="ApSpeedTestResultsOpenApiVO")


@_attrs_define
class ApSpeedTestResultsOpenApiVO:
    """
    Attributes:
        main_testing (bool | Unset): Whether the main AP is currently measuring speed.
        source_ap (str | Unset): The MAC address of the AP that initiates the speed measurement when the current device
            is measuring.
        target_ap (str | Unset): The MAC address of the AP whose speed is being measured when the current device is
            measuring.
        speed_test_result (ApSpeedTestResultsOpenApiVOSpeedTestResult | Unset): Speed measurement results of uplink and
            downlink devices.
    """

    main_testing: bool | Unset = UNSET
    source_ap: str | Unset = UNSET
    target_ap: str | Unset = UNSET
    speed_test_result: ApSpeedTestResultsOpenApiVOSpeedTestResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_testing = self.main_testing

        source_ap = self.source_ap

        target_ap = self.target_ap

        speed_test_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.speed_test_result, Unset):
            speed_test_result = self.speed_test_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_testing is not UNSET:
            field_dict["mainTesting"] = main_testing
        if source_ap is not UNSET:
            field_dict["sourceAP"] = source_ap
        if target_ap is not UNSET:
            field_dict["targetAP"] = target_ap
        if speed_test_result is not UNSET:
            field_dict["speedTestResult"] = speed_test_result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_speed_test_results_open_api_vo_speed_test_result import (
            ApSpeedTestResultsOpenApiVOSpeedTestResult,
        )

        d = dict(src_dict)
        main_testing = d.pop("mainTesting", UNSET)

        source_ap = d.pop("sourceAP", UNSET)

        target_ap = d.pop("targetAP", UNSET)

        _speed_test_result = d.pop("speedTestResult", UNSET)
        speed_test_result: ApSpeedTestResultsOpenApiVOSpeedTestResult | Unset
        if isinstance(_speed_test_result, Unset):
            speed_test_result = UNSET
        else:
            speed_test_result = ApSpeedTestResultsOpenApiVOSpeedTestResult.from_dict(
                _speed_test_result
            )

        ap_speed_test_results_open_api_vo = cls(
            main_testing=main_testing,
            source_ap=source_ap,
            target_ap=target_ap,
            speed_test_result=speed_test_result,
        )

        ap_speed_test_results_open_api_vo.additional_properties = d
        return ap_speed_test_results_open_api_vo

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
