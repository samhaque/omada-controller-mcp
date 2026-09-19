from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sdm_resource_usage import SdmResourceUsage


T = TypeVar("T", bound="OswL3SdmApplicationVO")


@_attrs_define
class OswL3SdmApplicationVO:
    """
    Attributes:
        cur_tmpl_name (str | Unset): Current used sdm template.
        sdm_resource_usage_list (list[SdmResourceUsage] | Unset): The list contains usage details of SDM resources on
            the device, including used and available resources.
        tcam_utilization (int | Unset): The overall TCAM utilization, calculated as usedTcam / totalTcam.
    """

    cur_tmpl_name: str | Unset = UNSET
    sdm_resource_usage_list: list[SdmResourceUsage] | Unset = UNSET
    tcam_utilization: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cur_tmpl_name = self.cur_tmpl_name

        sdm_resource_usage_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sdm_resource_usage_list, Unset):
            sdm_resource_usage_list = []
            for sdm_resource_usage_list_item_data in self.sdm_resource_usage_list:
                sdm_resource_usage_list_item = (
                    sdm_resource_usage_list_item_data.to_dict()
                )
                sdm_resource_usage_list.append(sdm_resource_usage_list_item)

        tcam_utilization = self.tcam_utilization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cur_tmpl_name is not UNSET:
            field_dict["curTmplName"] = cur_tmpl_name
        if sdm_resource_usage_list is not UNSET:
            field_dict["sdmResourceUsageList"] = sdm_resource_usage_list
        if tcam_utilization is not UNSET:
            field_dict["tcamUtilization"] = tcam_utilization

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sdm_resource_usage import SdmResourceUsage

        d = dict(src_dict)
        cur_tmpl_name = d.pop("curTmplName", UNSET)

        _sdm_resource_usage_list = d.pop("sdmResourceUsageList", UNSET)
        sdm_resource_usage_list: list[SdmResourceUsage] | Unset = UNSET
        if _sdm_resource_usage_list is not UNSET:
            sdm_resource_usage_list = []
            for sdm_resource_usage_list_item_data in _sdm_resource_usage_list:
                sdm_resource_usage_list_item = SdmResourceUsage.from_dict(
                    sdm_resource_usage_list_item_data
                )

                sdm_resource_usage_list.append(sdm_resource_usage_list_item)

        tcam_utilization = d.pop("tcamUtilization", UNSET)

        osw_l3_sdm_application_vo = cls(
            cur_tmpl_name=cur_tmpl_name,
            sdm_resource_usage_list=sdm_resource_usage_list,
            tcam_utilization=tcam_utilization,
        )

        osw_l3_sdm_application_vo.additional_properties = d
        return osw_l3_sdm_application_vo

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
