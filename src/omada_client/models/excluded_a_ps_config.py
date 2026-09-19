from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.select_macs_vo import SelectMacsVO


T = TypeVar("T", bound="ExcludedAPsConfig")


@_attrs_define
class ExcludedAPsConfig:
    """
    Attributes:
        delete (bool): Whether to delete device(s) from the excluded AP list.
        exclude_aps (str | Unset): Parameter [excludeAps] should not be null when parameter [delete] is true. It
            contains device MAC that should not be excluded. MAC should be concatenated with ','.
        select_macs (SelectMacsVO | Unset): Parameter [selectMacs] should not be null when parameter [delete] is false.
    """

    delete: bool
    exclude_aps: str | Unset = UNSET
    select_macs: SelectMacsVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete = self.delete

        exclude_aps = self.exclude_aps

        select_macs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.select_macs, Unset):
            select_macs = self.select_macs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delete": delete,
            }
        )
        if exclude_aps is not UNSET:
            field_dict["excludeAps"] = exclude_aps
        if select_macs is not UNSET:
            field_dict["selectMacs"] = select_macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.select_macs_vo import SelectMacsVO

        d = dict(src_dict)
        delete = d.pop("delete")

        exclude_aps = d.pop("excludeAps", UNSET)

        _select_macs = d.pop("selectMacs", UNSET)
        select_macs: SelectMacsVO | Unset
        if isinstance(_select_macs, Unset):
            select_macs = UNSET
        else:
            select_macs = SelectMacsVO.from_dict(_select_macs)

        excluded_a_ps_config = cls(
            delete=delete,
            exclude_aps=exclude_aps,
            select_macs=select_macs,
        )

        excluded_a_ps_config.additional_properties = d
        return excluded_a_ps_config

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
