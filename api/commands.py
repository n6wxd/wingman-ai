from typing import Literal, Optional
from pydantic import BaseModel
from api.enums import (
    CommandTag,
    KeyboardRecordingType,
    LogSource,
    LogType,
    RecordingDevice,
    ToastType,
)
from api.interface import CommandActionConfig, BenchmarkResult


# We use this Marker base class for reflection to "iterate all commands"
class WebSocketCommandModel(BaseModel):
    command: str


# RECEIVED FROM CLIENT


class ClientReadyCommand(WebSocketCommandModel):
    command: Literal["client_ready"] = "client_ready"


# TODO: make this a regular POST request
class SaveSecretCommand(WebSocketCommandModel):
    command: Literal["save_secret"] = "save_secret"
    secret_name: str
    secret_value: str
    show_message: Optional[bool] = True


class RecordKeyboardActionsCommand(WebSocketCommandModel):
    command: Literal["record_keyboard_actions"] = "record_keyboard_actions"
    recording_type: KeyboardRecordingType


class RecordMouseActionsCommand(WebSocketCommandModel):
    command: Literal["record_mouse_actions"] = "record_mouse_actions"


class RecordJoystickActionsCommand(WebSocketCommandModel):
    command: Literal["record_joystick_actions"] = "record_joystick_actions"


class StopRecordingCommand(WebSocketCommandModel):
    command: Literal["stop_recording"] = "stop_recording"
    recording_type: KeyboardRecordingType = KeyboardRecordingType.SINGLE
    recording_device: RecordingDevice = RecordingDevice.KEYBOARD


class ClientLoggedInCommand(WebSocketCommandModel):
    command: Literal["client_logged_in"] = "client_logged_in"
    is_pro: bool
    account_name: str


class ClientLoggedOutCommand(WebSocketCommandModel):
    command: Literal["client_logged_out"] = "client_logged_out"


# SENT TO CLIENT


class LogCommand(WebSocketCommandModel):
    command: Literal["log"] = "log"
    text: str
    log_type: LogType
    source_name: Optional[str] = None
    wingman_name: Optional[str] = None
    source: LogSource = "system"
    tag: Optional[CommandTag] = None
    skill_name: Optional[str] = None
    additional_data: Optional[dict] = None
    benchmark_result: Optional[BenchmarkResult] = None


class PromptSecretCommand(WebSocketCommandModel):
    command: Literal["prompt_secret"] = "prompt_secret"
    requester: str
    secret_name: str


class ToastCommand(WebSocketCommandModel):
    command: Literal["toast"] = "toast"
    text: str
    toast_type: ToastType


class ActionsRecordedCommand(WebSocketCommandModel):
    command: Literal["actions_recorded"] = "actions_recorded"
    actions: list[CommandActionConfig]


class VoiceActivationMutedCommand(WebSocketCommandModel):
    command: Literal["voice_activation_muted"] = "voice_activation_muted"
    muted: bool
