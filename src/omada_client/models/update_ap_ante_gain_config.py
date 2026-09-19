from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_ap_radio_ante_gain_config_open_api_vo import (
        UpdateApRadioAnteGainConfigOpenApiVO,
    )


T = TypeVar("T", bound="UpdateApAnteGainConfig")


@_attrs_define
class UpdateApAnteGainConfig:
    """
    Attributes:
        ante_gain_list (list[UpdateApRadioAnteGainConfigOpenApiVO] | Unset): Antenna gain list.
    """

    ante_gain_list: list[UpdateApRadioAnteGainConfigOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ante_gain_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ante_gain_list, Unset):
            ante_gain_list = []
            for ante_gain_list_item_data in self.ante_gain_list:
                ante_gain_list_item = ante_gain_list_item_data.to_dict()
                ante_gain_list.append(ante_gain_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ante_gain_list is not UNSET:
            field_dict["anteGainList"] = ante_gain_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_ap_radio_ante_gain_config_open_api_vo import (
            UpdateApRadioAnteGainConfigOpenApiVO,
        )

        d = dict(src_dict)
        _ante_gain_list = d.pop("anteGainList", UNSET)
        ante_gain_list: list[UpdateApRadioAnteGainConfigOpenApiVO] | Unset = UNSET
        if _ante_gain_list is not UNSET:
            ante_gain_list = []
            for ante_gain_list_item_data in _ante_gain_list:
                ante_gain_list_item = UpdateApRadioAnteGainConfigOpenApiVO.from_dict(
                    ante_gain_list_item_data
                )

                ante_gain_list.append(ante_gain_list_item)

        update_ap_ante_gain_config = cls(
            ante_gain_list=ante_gain_list,
        )

        update_ap_ante_gain_config.additional_properties = d
        return update_ap_ante_gain_config

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
