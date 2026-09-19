from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_mdns_rule_open_api_vo import ApMdnsRuleOpenApiVO
    from ..models.osg_mdns_rule_template_open_api_vo import OsgMdnsRuleTemplateOpenApiVO


T = TypeVar("T", bound="CreateMdnsRuleTemplateOpenApiVO")


@_attrs_define
class CreateMdnsRuleTemplateOpenApiVO:
    """
    Attributes:
        name (str): MDNS rule name. Name should contain 1 to 64 characters
        status (bool): MDNS rule enable status
        profile_ids (list[str]): This field represents Bonjour service profile ID. Bonjour Service Profile can be
            created using 'Create new Bonjour Service' interface, and Bonjour service profile ID can be obtained from 'Get
            Bonjour Service list' interface
        type_ (int | Unset): MDNS rule band VLAN type. Type should be a value as follows: 0: By VLAN ID, 1: By Network
        ap (ApMdnsRuleOpenApiVO | Unset): MDNS rule by VLAN ID config, valid when parameter [type] is 0
        osg (OsgMdnsRuleTemplateOpenApiVO | Unset): MDNS rule by network config, valid when parameter [type] is 1
    """

    name: str
    status: bool
    profile_ids: list[str]
    type_: int | Unset = UNSET
    ap: ApMdnsRuleOpenApiVO | Unset = UNSET
    osg: OsgMdnsRuleTemplateOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        profile_ids = self.profile_ids

        type_ = self.type_

        ap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap, Unset):
            ap = self.ap.to_dict()

        osg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osg, Unset):
            osg = self.osg.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "profileIds": profile_ids,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ap is not UNSET:
            field_dict["ap"] = ap
        if osg is not UNSET:
            field_dict["osg"] = osg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_mdns_rule_open_api_vo import (
            ApMdnsRuleOpenApiVO,
        )
        from ..models.osg_mdns_rule_template_open_api_vo import (
            OsgMdnsRuleTemplateOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        profile_ids = cast(list[str], d.pop("profileIds"))

        type_ = d.pop("type", UNSET)

        _ap = d.pop("ap", UNSET)
        ap: ApMdnsRuleOpenApiVO | Unset
        if isinstance(_ap, Unset):
            ap = UNSET
        else:
            ap = ApMdnsRuleOpenApiVO.from_dict(_ap)

        _osg = d.pop("osg", UNSET)
        osg: OsgMdnsRuleTemplateOpenApiVO | Unset
        if isinstance(_osg, Unset):
            osg = UNSET
        else:
            osg = OsgMdnsRuleTemplateOpenApiVO.from_dict(_osg)

        create_mdns_rule_template_open_api_vo = cls(
            name=name,
            status=status,
            profile_ids=profile_ids,
            type_=type_,
            ap=ap,
            osg=osg,
        )

        create_mdns_rule_template_open_api_vo.additional_properties = d
        return create_mdns_rule_template_open_api_vo

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
