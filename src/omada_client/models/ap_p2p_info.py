from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p2p_info_open_api_vo import P2PInfoOpenApiVO


T = TypeVar("T", bound="ApP2PInfo")


@_attrs_define
class ApP2PInfo:
    """
    Attributes:
        main_ap (P2PInfoOpenApiVO | Unset): Child aps info
        child_aps (list[P2PInfoOpenApiVO] | Unset): Child aps info
    """

    main_ap: P2PInfoOpenApiVO | Unset = UNSET
    child_aps: list[P2PInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_ap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_ap, Unset):
            main_ap = self.main_ap.to_dict()

        child_aps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_aps, Unset):
            child_aps = []
            for child_aps_item_data in self.child_aps:
                child_aps_item = child_aps_item_data.to_dict()
                child_aps.append(child_aps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_ap is not UNSET:
            field_dict["mainAp"] = main_ap
        if child_aps is not UNSET:
            field_dict["childAps"] = child_aps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.p2p_info_open_api_vo import P2PInfoOpenApiVO

        d = dict(src_dict)
        _main_ap = d.pop("mainAp", UNSET)
        main_ap: P2PInfoOpenApiVO | Unset
        if isinstance(_main_ap, Unset):
            main_ap = UNSET
        else:
            main_ap = P2PInfoOpenApiVO.from_dict(_main_ap)

        _child_aps = d.pop("childAps", UNSET)
        child_aps: list[P2PInfoOpenApiVO] | Unset = UNSET
        if _child_aps is not UNSET:
            child_aps = []
            for child_aps_item_data in _child_aps:
                child_aps_item = P2PInfoOpenApiVO.from_dict(child_aps_item_data)

                child_aps.append(child_aps_item)

        ap_p2p_info = cls(
            main_ap=main_ap,
            child_aps=child_aps,
        )

        ap_p2p_info.additional_properties = d
        return ap_p2p_info

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
