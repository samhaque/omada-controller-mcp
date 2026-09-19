from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wlan_opt_dash_board_detail_open_api_vo import (
        WlanOptDashBoardDetailOpenApiVO,
    )


T = TypeVar("T", bound="WlanOptDashBoardOpenApiVO")


@_attrs_define
class WlanOptDashBoardOpenApiVO:
    """
    Attributes:
        wlan_opt_dash_board_detail_2_g (WlanOptDashBoardDetailOpenApiVO | Unset): The RRM 6G radio metrics displayed on
            the WIFI Dashboard page.
        wlan_opt_dash_board_detail_5_g (WlanOptDashBoardDetailOpenApiVO | Unset): The RRM 6G radio metrics displayed on
            the WIFI Dashboard page.
        wlan_opt_dash_board_detail_6_g (WlanOptDashBoardDetailOpenApiVO | Unset): The RRM 6G radio metrics displayed on
            the WIFI Dashboard page.
    """

    wlan_opt_dash_board_detail_2_g: WlanOptDashBoardDetailOpenApiVO | Unset = UNSET
    wlan_opt_dash_board_detail_5_g: WlanOptDashBoardDetailOpenApiVO | Unset = UNSET
    wlan_opt_dash_board_detail_6_g: WlanOptDashBoardDetailOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wlan_opt_dash_board_detail_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wlan_opt_dash_board_detail_2_g, Unset):
            wlan_opt_dash_board_detail_2_g = (
                self.wlan_opt_dash_board_detail_2_g.to_dict()
            )

        wlan_opt_dash_board_detail_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wlan_opt_dash_board_detail_5_g, Unset):
            wlan_opt_dash_board_detail_5_g = (
                self.wlan_opt_dash_board_detail_5_g.to_dict()
            )

        wlan_opt_dash_board_detail_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wlan_opt_dash_board_detail_6_g, Unset):
            wlan_opt_dash_board_detail_6_g = (
                self.wlan_opt_dash_board_detail_6_g.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wlan_opt_dash_board_detail_2_g is not UNSET:
            field_dict["wlanOptDashBoardDetail2g"] = wlan_opt_dash_board_detail_2_g
        if wlan_opt_dash_board_detail_5_g is not UNSET:
            field_dict["wlanOptDashBoardDetail5g"] = wlan_opt_dash_board_detail_5_g
        if wlan_opt_dash_board_detail_6_g is not UNSET:
            field_dict["wlanOptDashBoardDetail6g"] = wlan_opt_dash_board_detail_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wlan_opt_dash_board_detail_open_api_vo import (
            WlanOptDashBoardDetailOpenApiVO,
        )

        d = dict(src_dict)
        _wlan_opt_dash_board_detail_2_g = d.pop("wlanOptDashBoardDetail2g", UNSET)
        wlan_opt_dash_board_detail_2_g: WlanOptDashBoardDetailOpenApiVO | Unset
        if isinstance(_wlan_opt_dash_board_detail_2_g, Unset):
            wlan_opt_dash_board_detail_2_g = UNSET
        else:
            wlan_opt_dash_board_detail_2_g = WlanOptDashBoardDetailOpenApiVO.from_dict(
                _wlan_opt_dash_board_detail_2_g
            )

        _wlan_opt_dash_board_detail_5_g = d.pop("wlanOptDashBoardDetail5g", UNSET)
        wlan_opt_dash_board_detail_5_g: WlanOptDashBoardDetailOpenApiVO | Unset
        if isinstance(_wlan_opt_dash_board_detail_5_g, Unset):
            wlan_opt_dash_board_detail_5_g = UNSET
        else:
            wlan_opt_dash_board_detail_5_g = WlanOptDashBoardDetailOpenApiVO.from_dict(
                _wlan_opt_dash_board_detail_5_g
            )

        _wlan_opt_dash_board_detail_6_g = d.pop("wlanOptDashBoardDetail6g", UNSET)
        wlan_opt_dash_board_detail_6_g: WlanOptDashBoardDetailOpenApiVO | Unset
        if isinstance(_wlan_opt_dash_board_detail_6_g, Unset):
            wlan_opt_dash_board_detail_6_g = UNSET
        else:
            wlan_opt_dash_board_detail_6_g = WlanOptDashBoardDetailOpenApiVO.from_dict(
                _wlan_opt_dash_board_detail_6_g
            )

        wlan_opt_dash_board_open_api_vo = cls(
            wlan_opt_dash_board_detail_2_g=wlan_opt_dash_board_detail_2_g,
            wlan_opt_dash_board_detail_5_g=wlan_opt_dash_board_detail_5_g,
            wlan_opt_dash_board_detail_6_g=wlan_opt_dash_board_detail_6_g,
        )

        wlan_opt_dash_board_open_api_vo.additional_properties = d
        return wlan_opt_dash_board_open_api_vo

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
