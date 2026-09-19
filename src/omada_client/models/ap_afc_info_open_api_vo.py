from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApAfcInfoOpenApiVO")


@_attrs_define
class ApAfcInfoOpenApiVO:
    """
    Attributes:
        status (bool | Unset): Ap AFC working status
        expiration_time_sec (int | Unset): The expiration timestamp of the current AFC information of the AP
        last_response (bool | Unset): The status of the last AFC information obtained by the AP
        last_response_time_sec (int | Unset): The timestamp of the last AFC information obtained by the AP
        err_code (int | Unset): The error code of last afc status
        err_main (int | Unset): The error main reason
        err_detail (int | Unset): The error detail
        processing (bool | Unset): Whether the afc status is being retrieved
        available6g (bool | Unset): 6G radio available status
    """

    status: bool | Unset = UNSET
    expiration_time_sec: int | Unset = UNSET
    last_response: bool | Unset = UNSET
    last_response_time_sec: int | Unset = UNSET
    err_code: int | Unset = UNSET
    err_main: int | Unset = UNSET
    err_detail: int | Unset = UNSET
    processing: bool | Unset = UNSET
    available6g: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        expiration_time_sec = self.expiration_time_sec

        last_response = self.last_response

        last_response_time_sec = self.last_response_time_sec

        err_code = self.err_code

        err_main = self.err_main

        err_detail = self.err_detail

        processing = self.processing

        available6g = self.available6g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if expiration_time_sec is not UNSET:
            field_dict["expirationTimeSec"] = expiration_time_sec
        if last_response is not UNSET:
            field_dict["lastResponse"] = last_response
        if last_response_time_sec is not UNSET:
            field_dict["lastResponseTimeSec"] = last_response_time_sec
        if err_code is not UNSET:
            field_dict["errCode"] = err_code
        if err_main is not UNSET:
            field_dict["errMain"] = err_main
        if err_detail is not UNSET:
            field_dict["errDetail"] = err_detail
        if processing is not UNSET:
            field_dict["processing"] = processing
        if available6g is not UNSET:
            field_dict["available6g"] = available6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        expiration_time_sec = d.pop("expirationTimeSec", UNSET)

        last_response = d.pop("lastResponse", UNSET)

        last_response_time_sec = d.pop("lastResponseTimeSec", UNSET)

        err_code = d.pop("errCode", UNSET)

        err_main = d.pop("errMain", UNSET)

        err_detail = d.pop("errDetail", UNSET)

        processing = d.pop("processing", UNSET)

        available6g = d.pop("available6g", UNSET)

        ap_afc_info_open_api_vo = cls(
            status=status,
            expiration_time_sec=expiration_time_sec,
            last_response=last_response,
            last_response_time_sec=last_response_time_sec,
            err_code=err_code,
            err_main=err_main,
            err_detail=err_detail,
            processing=processing,
            available6g=available6g,
        )

        ap_afc_info_open_api_vo.additional_properties = d
        return ap_afc_info_open_api_vo

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
