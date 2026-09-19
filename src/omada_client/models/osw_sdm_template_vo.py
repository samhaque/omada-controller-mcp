from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_sdm_brief_vo import OswSdmBriefVO


T = TypeVar("T", bound="OswSdmTemplateVO")


@_attrs_define
class OswSdmTemplateVO:
    """Sdm template

    Attributes:
        in_use (str | Unset): Sdm template currently in use.
        templates (list[OswSdmBriefVO] | Unset): All sdm templates supported by the device.
    """

    in_use: str | Unset = UNSET
    templates: list[OswSdmBriefVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_use = self.in_use

        templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_use is not UNSET:
            field_dict["inUse"] = in_use
        if templates is not UNSET:
            field_dict["templates"] = templates

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_sdm_brief_vo import OswSdmBriefVO

        d = dict(src_dict)
        in_use = d.pop("inUse", UNSET)

        _templates = d.pop("templates", UNSET)
        templates: list[OswSdmBriefVO] | Unset = UNSET
        if _templates is not UNSET:
            templates = []
            for templates_item_data in _templates:
                templates_item = OswSdmBriefVO.from_dict(templates_item_data)

                templates.append(templates_item)

        osw_sdm_template_vo = cls(
            in_use=in_use,
            templates=templates,
        )

        osw_sdm_template_vo.additional_properties = d
        return osw_sdm_template_vo

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
