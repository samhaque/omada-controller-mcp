from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_member_sdm_vo import OswStackMemberSdmVO


T = TypeVar("T", bound="OswStackSdmApplicationVO")


@_attrs_define
class OswStackSdmApplicationVO:
    """
    Attributes:
        cur_tmpl_name (str | Unset): Current used sdm template.
        tcam_utilization (int | Unset): The overall TCAM utilization, calculated as usedTcam / totalTcam.
        stack_member_sdm_list (list[OswStackMemberSdmVO] | Unset): The sdm resources usage detail of stack members
    """

    cur_tmpl_name: str | Unset = UNSET
    tcam_utilization: int | Unset = UNSET
    stack_member_sdm_list: list[OswStackMemberSdmVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cur_tmpl_name = self.cur_tmpl_name

        tcam_utilization = self.tcam_utilization

        stack_member_sdm_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_member_sdm_list, Unset):
            stack_member_sdm_list = []
            for stack_member_sdm_list_item_data in self.stack_member_sdm_list:
                stack_member_sdm_list_item = stack_member_sdm_list_item_data.to_dict()
                stack_member_sdm_list.append(stack_member_sdm_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cur_tmpl_name is not UNSET:
            field_dict["curTmplName"] = cur_tmpl_name
        if tcam_utilization is not UNSET:
            field_dict["tcamUtilization"] = tcam_utilization
        if stack_member_sdm_list is not UNSET:
            field_dict["stackMemberSdmList"] = stack_member_sdm_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_member_sdm_vo import (
            OswStackMemberSdmVO,
        )

        d = dict(src_dict)
        cur_tmpl_name = d.pop("curTmplName", UNSET)

        tcam_utilization = d.pop("tcamUtilization", UNSET)

        _stack_member_sdm_list = d.pop("stackMemberSdmList", UNSET)
        stack_member_sdm_list: list[OswStackMemberSdmVO] | Unset = UNSET
        if _stack_member_sdm_list is not UNSET:
            stack_member_sdm_list = []
            for stack_member_sdm_list_item_data in _stack_member_sdm_list:
                stack_member_sdm_list_item = OswStackMemberSdmVO.from_dict(
                    stack_member_sdm_list_item_data
                )

                stack_member_sdm_list.append(stack_member_sdm_list_item)

        osw_stack_sdm_application_vo = cls(
            cur_tmpl_name=cur_tmpl_name,
            tcam_utilization=tcam_utilization,
            stack_member_sdm_list=stack_member_sdm_list,
        )

        osw_stack_sdm_application_vo.additional_properties = d
        return osw_stack_sdm_application_vo

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
