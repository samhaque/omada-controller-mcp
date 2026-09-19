from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswCableTestResultVO")


@_attrs_define
class OswCableTestResultVO:
    """Test results.

    Attributes:
        port (int | Unset): Port
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
        state (list[int] | Unset): Cable state List. Each item should be a value as follows: 0:OK  1:OPEN  2:short
            3:crosstalk 4:unknown-error 5:not-support 6:openshort
        length (list[int] | Unset): Cable length List.
        time_stamp (int | Unset): Timestamp of the test result
    """

    port: int | Unset = UNSET
    standard_port: OswStandPortVO | Unset = UNSET
    state: list[int] | Unset = UNSET
    length: list[int] | Unset = UNSET
    time_stamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        state: list[int] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        length: list[int] | Unset = UNSET
        if not isinstance(self.length, Unset):
            length = self.length

        time_stamp = self.time_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if state is not UNSET:
            field_dict["state"] = state
        if length is not UNSET:
            field_dict["length"] = length
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        _standard_port = d.pop("standardPort", UNSET)
        standard_port: OswStandPortVO | Unset
        if isinstance(_standard_port, Unset):
            standard_port = UNSET
        else:
            standard_port = OswStandPortVO.from_dict(_standard_port)

        state = cast(list[int], d.pop("state", UNSET))

        length = cast(list[int], d.pop("length", UNSET))

        time_stamp = d.pop("timeStamp", UNSET)

        osw_cable_test_result_vo = cls(
            port=port,
            standard_port=standard_port,
            state=state,
            length=length,
            time_stamp=time_stamp,
        )

        osw_cable_test_result_vo.additional_properties = d
        return osw_cable_test_result_vo

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
