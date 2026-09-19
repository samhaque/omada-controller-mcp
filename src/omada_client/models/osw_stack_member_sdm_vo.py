from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sdm_resource_usage import SdmResourceUsage


T = TypeVar("T", bound="OswStackMemberSdmVO")


@_attrs_define
class OswStackMemberSdmVO:
    """The sdm resources usage detail of stack members

    Attributes:
        device_mac (str | Unset): Mac of device.
        model (str | Unset): Device model.
        model_version (str | Unset): Device model Version.
        is_stack_master (bool | Unset): Whether the device is the master unit in a stack.
        status (int | Unset): Device status.
        sdm_resource_usage_list (list[SdmResourceUsage] | Unset): The list contains usage details of SDM resources on
            the device, including used and available resources.
    """

    device_mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    is_stack_master: bool | Unset = UNSET
    status: int | Unset = UNSET
    sdm_resource_usage_list: list[SdmResourceUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        model = self.model

        model_version = self.model_version

        is_stack_master = self.is_stack_master

        status = self.status

        sdm_resource_usage_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sdm_resource_usage_list, Unset):
            sdm_resource_usage_list = []
            for sdm_resource_usage_list_item_data in self.sdm_resource_usage_list:
                sdm_resource_usage_list_item = (
                    sdm_resource_usage_list_item_data.to_dict()
                )
                sdm_resource_usage_list.append(sdm_resource_usage_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if is_stack_master is not UNSET:
            field_dict["isStackMaster"] = is_stack_master
        if status is not UNSET:
            field_dict["status"] = status
        if sdm_resource_usage_list is not UNSET:
            field_dict["sdmResourceUsageList"] = sdm_resource_usage_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sdm_resource_usage import SdmResourceUsage

        d = dict(src_dict)
        device_mac = d.pop("deviceMac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        is_stack_master = d.pop("isStackMaster", UNSET)

        status = d.pop("status", UNSET)

        _sdm_resource_usage_list = d.pop("sdmResourceUsageList", UNSET)
        sdm_resource_usage_list: list[SdmResourceUsage] | Unset = UNSET
        if _sdm_resource_usage_list is not UNSET:
            sdm_resource_usage_list = []
            for sdm_resource_usage_list_item_data in _sdm_resource_usage_list:
                sdm_resource_usage_list_item = SdmResourceUsage.from_dict(
                    sdm_resource_usage_list_item_data
                )

                sdm_resource_usage_list.append(sdm_resource_usage_list_item)

        osw_stack_member_sdm_vo = cls(
            device_mac=device_mac,
            model=model,
            model_version=model_version,
            is_stack_master=is_stack_master,
            status=status,
            sdm_resource_usage_list=sdm_resource_usage_list,
        )

        osw_stack_member_sdm_vo.additional_properties = d
        return osw_stack_member_sdm_vo

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
