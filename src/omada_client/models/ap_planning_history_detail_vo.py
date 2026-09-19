from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_planning_radio_vo import ApPlanningRadioVO


T = TypeVar("T", bound="ApPlanningHistoryDetailVO")


@_attrs_define
class ApPlanningHistoryDetailVO:
    """Optimization history details.

    Attributes:
        name (str | Unset): Device name.
        model (str | Unset): Device model.
        model_version (str | Unset): Device model version.
        type_ (str | Unset): Device type.
        ip (str | Unset): IP Address.
        optimize_success (bool | Unset): Parameter [optimizeSuccess] indicates whether the optimization has been
            executed successfully.
        support5g2 (bool | Unset): Parameter [support5g2] indicates whether the device supports 5 GHz-2.
        radio2g (ApPlanningRadioVO | Unset): Optimization results in band 6 GHz.
        radio5g (ApPlanningRadioVO | Unset): Optimization results in band 6 GHz.
        radio5g2 (ApPlanningRadioVO | Unset): Optimization results in band 6 GHz.
        radio6g (ApPlanningRadioVO | Unset): Optimization results in band 6 GHz.
        fail_msg (str | Unset): Fail message.
        fail_msg_type (int | Unset): Fail message type. -1: Success. 0: Failed to optimize device because of no scan
            result. 1: Failed to apply deploy config because the device is not connected or the configuration is invalid.
        trigger_reason (int | Unset): Trigger reason. 0: none. 1: Strong Interference. 2: new ap
    """

    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    ip: str | Unset = UNSET
    optimize_success: bool | Unset = UNSET
    support5g2: bool | Unset = UNSET
    radio2g: ApPlanningRadioVO | Unset = UNSET
    radio5g: ApPlanningRadioVO | Unset = UNSET
    radio5g2: ApPlanningRadioVO | Unset = UNSET
    radio6g: ApPlanningRadioVO | Unset = UNSET
    fail_msg: str | Unset = UNSET
    fail_msg_type: int | Unset = UNSET
    trigger_reason: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        ip = self.ip

        optimize_success = self.optimize_success

        support5g2 = self.support5g2

        radio2g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio2g, Unset):
            radio2g = self.radio2g.to_dict()

        radio5g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio5g, Unset):
            radio5g = self.radio5g.to_dict()

        radio5g2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio5g2, Unset):
            radio5g2 = self.radio5g2.to_dict()

        radio6g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio6g, Unset):
            radio6g = self.radio6g.to_dict()

        fail_msg = self.fail_msg

        fail_msg_type = self.fail_msg_type

        trigger_reason = self.trigger_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ip is not UNSET:
            field_dict["ip"] = ip
        if optimize_success is not UNSET:
            field_dict["optimizeSuccess"] = optimize_success
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if radio2g is not UNSET:
            field_dict["radio2g"] = radio2g
        if radio5g is not UNSET:
            field_dict["radio5g"] = radio5g
        if radio5g2 is not UNSET:
            field_dict["radio5g2"] = radio5g2
        if radio6g is not UNSET:
            field_dict["radio6g"] = radio6g
        if fail_msg is not UNSET:
            field_dict["failMsg"] = fail_msg
        if fail_msg_type is not UNSET:
            field_dict["failMsgType"] = fail_msg_type
        if trigger_reason is not UNSET:
            field_dict["triggerReason"] = trigger_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_planning_radio_vo import ApPlanningRadioVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        ip = d.pop("ip", UNSET)

        optimize_success = d.pop("optimizeSuccess", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        _radio2g = d.pop("radio2g", UNSET)
        radio2g: ApPlanningRadioVO | Unset
        if isinstance(_radio2g, Unset):
            radio2g = UNSET
        else:
            radio2g = ApPlanningRadioVO.from_dict(_radio2g)

        _radio5g = d.pop("radio5g", UNSET)
        radio5g: ApPlanningRadioVO | Unset
        if isinstance(_radio5g, Unset):
            radio5g = UNSET
        else:
            radio5g = ApPlanningRadioVO.from_dict(_radio5g)

        _radio5g2 = d.pop("radio5g2", UNSET)
        radio5g2: ApPlanningRadioVO | Unset
        if isinstance(_radio5g2, Unset):
            radio5g2 = UNSET
        else:
            radio5g2 = ApPlanningRadioVO.from_dict(_radio5g2)

        _radio6g = d.pop("radio6g", UNSET)
        radio6g: ApPlanningRadioVO | Unset
        if isinstance(_radio6g, Unset):
            radio6g = UNSET
        else:
            radio6g = ApPlanningRadioVO.from_dict(_radio6g)

        fail_msg = d.pop("failMsg", UNSET)

        fail_msg_type = d.pop("failMsgType", UNSET)

        trigger_reason = d.pop("triggerReason", UNSET)

        ap_planning_history_detail_vo = cls(
            name=name,
            model=model,
            model_version=model_version,
            type_=type_,
            ip=ip,
            optimize_success=optimize_success,
            support5g2=support5g2,
            radio2g=radio2g,
            radio5g=radio5g,
            radio5g2=radio5g2,
            radio6g=radio6g,
            fail_msg=fail_msg,
            fail_msg_type=fail_msg_type,
            trigger_reason=trigger_reason,
        )

        ap_planning_history_detail_vo.additional_properties = d
        return ap_planning_history_detail_vo

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
