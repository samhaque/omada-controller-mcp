from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mesh_setting_vo import MeshSettingVO


T = TypeVar("T", bound="SiteMeshSetting")


@_attrs_define
class SiteMeshSetting:
    """Site mesh setting.

    Attributes:
        mesh (MeshSettingVO | Unset): Site mesh.
    """

    mesh: MeshSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mesh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mesh, Unset):
            mesh = self.mesh.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mesh is not UNSET:
            field_dict["mesh"] = mesh

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mesh_setting_vo import MeshSettingVO

        d = dict(src_dict)
        _mesh = d.pop("mesh", UNSET)
        mesh: MeshSettingVO | Unset
        if isinstance(_mesh, Unset):
            mesh = UNSET
        else:
            mesh = MeshSettingVO.from_dict(_mesh)

        site_mesh_setting = cls(
            mesh=mesh,
        )

        site_mesh_setting.additional_properties = d
        return site_mesh_setting

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
