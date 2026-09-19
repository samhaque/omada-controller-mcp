from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isp_info_vo import IspInfoVO


T = TypeVar("T", bound="GatewayIspLoadInfoVO")


@_attrs_define
class GatewayIspLoadInfoVO:
    """Gateway isp info list.

    Attributes:
        name (str | Unset): Gateway name.
        mac (str | Unset): Gateway MAC.
        status (int | Unset): Gateway status, should be a value as follows:-1 : disconnected1 : active0 : backup gateway
            under multiple gateways
        isp_info (IspInfoVO | Unset): Isp info.
        speed_test_limit (int | Unset): The limited bandwidth of the gateway speed test.
        support_speed_test (bool | Unset): Whether speed measurement is supported.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    status: int | Unset = UNSET
    isp_info: IspInfoVO | Unset = UNSET
    speed_test_limit: int | Unset = UNSET
    support_speed_test: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        status = self.status

        isp_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.isp_info, Unset):
            isp_info = self.isp_info.to_dict()

        speed_test_limit = self.speed_test_limit

        support_speed_test = self.support_speed_test

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if status is not UNSET:
            field_dict["status"] = status
        if isp_info is not UNSET:
            field_dict["ispInfo"] = isp_info
        if speed_test_limit is not UNSET:
            field_dict["speedTestLimit"] = speed_test_limit
        if support_speed_test is not UNSET:
            field_dict["supportSpeedTest"] = support_speed_test

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.isp_info_vo import IspInfoVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        status = d.pop("status", UNSET)

        _isp_info = d.pop("ispInfo", UNSET)
        isp_info: IspInfoVO | Unset
        if isinstance(_isp_info, Unset):
            isp_info = UNSET
        else:
            isp_info = IspInfoVO.from_dict(_isp_info)

        speed_test_limit = d.pop("speedTestLimit", UNSET)

        support_speed_test = d.pop("supportSpeedTest", UNSET)

        gateway_isp_load_info_vo = cls(
            name=name,
            mac=mac,
            status=status,
            isp_info=isp_info,
            speed_test_limit=speed_test_limit,
            support_speed_test=support_speed_test,
        )

        gateway_isp_load_info_vo.additional_properties = d
        return gateway_isp_load_info_vo

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
