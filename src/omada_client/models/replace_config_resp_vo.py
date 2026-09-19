from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplaceConfigRespVO")


@_attrs_define
class ReplaceConfigRespVO:
    """
    Attributes:
        old_model (str | Unset): Old model.
        new_model (str | Unset): New model.
        need_prompt (bool | Unset): Whether to show a prompt.
        feature_list (list[str] | Unset): List of incompatible features.
    """

    old_model: str | Unset = UNSET
    new_model: str | Unset = UNSET
    need_prompt: bool | Unset = UNSET
    feature_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_model = self.old_model

        new_model = self.new_model

        need_prompt = self.need_prompt

        feature_list: list[str] | Unset = UNSET
        if not isinstance(self.feature_list, Unset):
            feature_list = self.feature_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if old_model is not UNSET:
            field_dict["oldModel"] = old_model
        if new_model is not UNSET:
            field_dict["newModel"] = new_model
        if need_prompt is not UNSET:
            field_dict["needPrompt"] = need_prompt
        if feature_list is not UNSET:
            field_dict["featureList"] = feature_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        old_model = d.pop("oldModel", UNSET)

        new_model = d.pop("newModel", UNSET)

        need_prompt = d.pop("needPrompt", UNSET)

        feature_list = cast(list[str], d.pop("featureList", UNSET))

        replace_config_resp_vo = cls(
            old_model=old_model,
            new_model=new_model,
            need_prompt=need_prompt,
            feature_list=feature_list,
        )

        replace_config_resp_vo.additional_properties = d
        return replace_config_resp_vo

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
