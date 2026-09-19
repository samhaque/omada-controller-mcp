from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_density_current_detail_open_api_vo import (
        ApDensityCurrentDetailOpenApiVO,
    )
    from ..models.ap_density_trend_detail_open_api_vo import (
        ApDensityTrendDetailOpenApiVO,
    )
    from ..models.cci_current_detail_open_api_vo import CciCurrentDetailOpenApiVO
    from ..models.cci_trend_detail_open_api_vo import CciTrendDetailOpenApiVO


T = TypeVar("T", bound="WlanOptDashBoardDetailOpenApiVO")


@_attrs_define
class WlanOptDashBoardDetailOpenApiVO:
    """The RRM 6G radio metrics displayed on the WIFI Dashboard page.

    Attributes:
        cci_trend_detail (CciTrendDetailOpenApiVO | Unset): The trend of CCI metrics displayed on the WIFI Dashboard
            page.
        cci_current_detail (CciCurrentDetailOpenApiVO | Unset): The current detail of CCI metrics displayed on the WIFI
            Dashboard page.
        ap_density_trend_detail (ApDensityTrendDetailOpenApiVO | Unset): The trend of ap density displayed on the WIFI
            Dashboard page.
        ap_density_current_detail (ApDensityCurrentDetailOpenApiVO | Unset): The current detail of ap density displayed
            on the WIFI Dashboard page.
    """

    cci_trend_detail: CciTrendDetailOpenApiVO | Unset = UNSET
    cci_current_detail: CciCurrentDetailOpenApiVO | Unset = UNSET
    ap_density_trend_detail: ApDensityTrendDetailOpenApiVO | Unset = UNSET
    ap_density_current_detail: ApDensityCurrentDetailOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cci_trend_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cci_trend_detail, Unset):
            cci_trend_detail = self.cci_trend_detail.to_dict()

        cci_current_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cci_current_detail, Unset):
            cci_current_detail = self.cci_current_detail.to_dict()

        ap_density_trend_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap_density_trend_detail, Unset):
            ap_density_trend_detail = self.ap_density_trend_detail.to_dict()

        ap_density_current_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap_density_current_detail, Unset):
            ap_density_current_detail = self.ap_density_current_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cci_trend_detail is not UNSET:
            field_dict["cciTrendDetail"] = cci_trend_detail
        if cci_current_detail is not UNSET:
            field_dict["cciCurrentDetail"] = cci_current_detail
        if ap_density_trend_detail is not UNSET:
            field_dict["apDensityTrendDetail"] = ap_density_trend_detail
        if ap_density_current_detail is not UNSET:
            field_dict["apDensityCurrentDetail"] = ap_density_current_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_density_current_detail_open_api_vo import (
            ApDensityCurrentDetailOpenApiVO,
        )
        from ..models.ap_density_trend_detail_open_api_vo import (
            ApDensityTrendDetailOpenApiVO,
        )
        from ..models.cci_current_detail_open_api_vo import (
            CciCurrentDetailOpenApiVO,
        )
        from ..models.cci_trend_detail_open_api_vo import (
            CciTrendDetailOpenApiVO,
        )

        d = dict(src_dict)
        _cci_trend_detail = d.pop("cciTrendDetail", UNSET)
        cci_trend_detail: CciTrendDetailOpenApiVO | Unset
        if isinstance(_cci_trend_detail, Unset):
            cci_trend_detail = UNSET
        else:
            cci_trend_detail = CciTrendDetailOpenApiVO.from_dict(_cci_trend_detail)

        _cci_current_detail = d.pop("cciCurrentDetail", UNSET)
        cci_current_detail: CciCurrentDetailOpenApiVO | Unset
        if isinstance(_cci_current_detail, Unset):
            cci_current_detail = UNSET
        else:
            cci_current_detail = CciCurrentDetailOpenApiVO.from_dict(
                _cci_current_detail
            )

        _ap_density_trend_detail = d.pop("apDensityTrendDetail", UNSET)
        ap_density_trend_detail: ApDensityTrendDetailOpenApiVO | Unset
        if isinstance(_ap_density_trend_detail, Unset):
            ap_density_trend_detail = UNSET
        else:
            ap_density_trend_detail = ApDensityTrendDetailOpenApiVO.from_dict(
                _ap_density_trend_detail
            )

        _ap_density_current_detail = d.pop("apDensityCurrentDetail", UNSET)
        ap_density_current_detail: ApDensityCurrentDetailOpenApiVO | Unset
        if isinstance(_ap_density_current_detail, Unset):
            ap_density_current_detail = UNSET
        else:
            ap_density_current_detail = ApDensityCurrentDetailOpenApiVO.from_dict(
                _ap_density_current_detail
            )

        wlan_opt_dash_board_detail_open_api_vo = cls(
            cci_trend_detail=cci_trend_detail,
            cci_current_detail=cci_current_detail,
            ap_density_trend_detail=ap_density_trend_detail,
            ap_density_current_detail=ap_density_current_detail,
        )

        wlan_opt_dash_board_detail_open_api_vo.additional_properties = d
        return wlan_opt_dash_board_detail_open_api_vo

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
