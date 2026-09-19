from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_brief_port_info_open_api_vo import OswBriefPortInfoOpenApiVO


T = TypeVar("T", bound="OswCableTestLogOpenApiVO")


@_attrs_define
class OswCableTestLogOpenApiVO:
    """
    Attributes:
        type_ (int | Unset): Log type. It should be a value as follows: 0:start test. 1: test done. 2:test interrupts
            3:time out
        time_stamp (int | Unset): Timestamp of the log
        test_port_list (list[OswBriefPortInfoOpenApiVO] | Unset): All test port. Used for type 0
        complete_port_list (list[OswBriefPortInfoOpenApiVO] | Unset): Ports that have been tested completely. Used for
            type 1,2,3
        cancel_port_list (list[OswBriefPortInfoOpenApiVO] | Unset): Ports that were not detected due to cancel. Used for
            type 2
        timeout_port_list (list[OswBriefPortInfoOpenApiVO] | Unset): Timeout ports. Used for type 3
    """

    type_: int | Unset = UNSET
    time_stamp: int | Unset = UNSET
    test_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
    complete_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
    cancel_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
    timeout_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        time_stamp = self.time_stamp

        test_port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.test_port_list, Unset):
            test_port_list = []
            for test_port_list_item_data in self.test_port_list:
                test_port_list_item = test_port_list_item_data.to_dict()
                test_port_list.append(test_port_list_item)

        complete_port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.complete_port_list, Unset):
            complete_port_list = []
            for complete_port_list_item_data in self.complete_port_list:
                complete_port_list_item = complete_port_list_item_data.to_dict()
                complete_port_list.append(complete_port_list_item)

        cancel_port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cancel_port_list, Unset):
            cancel_port_list = []
            for cancel_port_list_item_data in self.cancel_port_list:
                cancel_port_list_item = cancel_port_list_item_data.to_dict()
                cancel_port_list.append(cancel_port_list_item)

        timeout_port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timeout_port_list, Unset):
            timeout_port_list = []
            for timeout_port_list_item_data in self.timeout_port_list:
                timeout_port_list_item = timeout_port_list_item_data.to_dict()
                timeout_port_list.append(timeout_port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if test_port_list is not UNSET:
            field_dict["testPortList"] = test_port_list
        if complete_port_list is not UNSET:
            field_dict["completePortList"] = complete_port_list
        if cancel_port_list is not UNSET:
            field_dict["cancelPortList"] = cancel_port_list
        if timeout_port_list is not UNSET:
            field_dict["timeoutPortList"] = timeout_port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_brief_port_info_open_api_vo import (
            OswBriefPortInfoOpenApiVO,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        time_stamp = d.pop("timeStamp", UNSET)

        _test_port_list = d.pop("testPortList", UNSET)
        test_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
        if _test_port_list is not UNSET:
            test_port_list = []
            for test_port_list_item_data in _test_port_list:
                test_port_list_item = OswBriefPortInfoOpenApiVO.from_dict(
                    test_port_list_item_data
                )

                test_port_list.append(test_port_list_item)

        _complete_port_list = d.pop("completePortList", UNSET)
        complete_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
        if _complete_port_list is not UNSET:
            complete_port_list = []
            for complete_port_list_item_data in _complete_port_list:
                complete_port_list_item = OswBriefPortInfoOpenApiVO.from_dict(
                    complete_port_list_item_data
                )

                complete_port_list.append(complete_port_list_item)

        _cancel_port_list = d.pop("cancelPortList", UNSET)
        cancel_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
        if _cancel_port_list is not UNSET:
            cancel_port_list = []
            for cancel_port_list_item_data in _cancel_port_list:
                cancel_port_list_item = OswBriefPortInfoOpenApiVO.from_dict(
                    cancel_port_list_item_data
                )

                cancel_port_list.append(cancel_port_list_item)

        _timeout_port_list = d.pop("timeoutPortList", UNSET)
        timeout_port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
        if _timeout_port_list is not UNSET:
            timeout_port_list = []
            for timeout_port_list_item_data in _timeout_port_list:
                timeout_port_list_item = OswBriefPortInfoOpenApiVO.from_dict(
                    timeout_port_list_item_data
                )

                timeout_port_list.append(timeout_port_list_item)

        osw_cable_test_log_open_api_vo = cls(
            type_=type_,
            time_stamp=time_stamp,
            test_port_list=test_port_list,
            complete_port_list=complete_port_list,
            cancel_port_list=cancel_port_list,
            timeout_port_list=timeout_port_list,
        )

        osw_cable_test_log_open_api_vo.additional_properties = d
        return osw_cable_test_log_open_api_vo

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
