from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.internet_basic_info import InternetBasicInfo


T = TypeVar("T", bound="InternetBaseInfoTemplateOpenApiVO")


@_attrs_define
class InternetBaseInfoTemplateOpenApiVO:
    """
    Attributes:
        pre_configuration (bool): You can pre-configure the model-relative settings when it is true.
        gateway_model (int): Gateway model should be a value as follows: 2: Universal; 9: G36 v1; 10: G611 v1; 13:
            G36W-4G v1.
        port_list (list[InternetBasicInfo]): Port info list
        interval (int): Online detection interval(second), 0 means disable.
    """

    pre_configuration: bool
    gateway_model: int
    port_list: list[InternetBasicInfo]
    interval: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_configuration = self.pre_configuration

        gateway_model = self.gateway_model

        port_list = []
        for port_list_item_data in self.port_list:
            port_list_item = port_list_item_data.to_dict()
            port_list.append(port_list_item)

        interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preConfiguration": pre_configuration,
                "gatewayModel": gateway_model,
                "portList": port_list,
                "interval": interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.internet_basic_info import InternetBasicInfo

        d = dict(src_dict)
        pre_configuration = d.pop("preConfiguration")

        gateway_model = d.pop("gatewayModel")

        port_list = []
        _port_list = d.pop("portList")
        for port_list_item_data in _port_list:
            port_list_item = InternetBasicInfo.from_dict(port_list_item_data)

            port_list.append(port_list_item)

        interval = d.pop("interval")

        internet_base_info_template_open_api_vo = cls(
            pre_configuration=pre_configuration,
            gateway_model=gateway_model,
            port_list=port_list,
            interval=interval,
        )

        internet_base_info_template_open_api_vo.additional_properties = d
        return internet_base_info_template_open_api_vo

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
