from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eth_unit_1_port_app_dto import EthUnit1PortAppDTO


T = TypeVar("T", bound="OperationResponseListEthUnit1PortAppDTO")


@_attrs_define
class OperationResponseListEthUnit1PortAppDTO:
    """
    Attributes:
        error_code (int | Unset):
        msg (str | Unset):
        result (list[EthUnit1PortAppDTO] | Unset):
    """

    error_code: int | Unset = UNSET
    msg: str | Unset = UNSET
    result: list[EthUnit1PortAppDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        msg = self.msg

        result: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item = result_item_data.to_dict()
                result.append(result_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if msg is not UNSET:
            field_dict["msg"] = msg
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eth_unit_1_port_app_dto import EthUnit1PortAppDTO

        d = dict(src_dict)
        error_code = d.pop("errorCode", UNSET)

        msg = d.pop("msg", UNSET)

        _result = d.pop("result", UNSET)
        result: list[EthUnit1PortAppDTO] | Unset = UNSET
        if _result is not UNSET:
            result = []
            for result_item_data in _result:
                result_item = EthUnit1PortAppDTO.from_dict(result_item_data)

                result.append(result_item)

        operation_response_list_eth_unit_1_port_app_dto = cls(
            error_code=error_code,
            msg=msg,
            result=result,
        )

        operation_response_list_eth_unit_1_port_app_dto.additional_properties = d
        return operation_response_list_eth_unit_1_port_app_dto

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
