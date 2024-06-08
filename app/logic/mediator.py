from dataclasses import dataclass, field
from typing import DefaultDict, Iterable

from domain.events.base import BaseEvent
from logic.commands.base import CR, CT, BaseCommand, CommandHandler
from logic.events.base import ER, ET, EventHandler
from logic.exceptions.mediator import CommandHandlersNotRegisteredException, EventHandlersNotRegisteredException


@dataclass
class Mediator:
    events_map: dict[ET, list[EventHandler]] = field(
        default_factory=lambda: DefaultDict(list), kw_only=True
    )
    commands_map: dict[CT, list[CommandHandler]] = field(
        default_factory=lambda: DefaultDict(list), kw_only=True
    )

    def register_event(
        self, event: ET, handlers: Iterable[EventHandler[ET, ER]]
    ):
        self.events_map[event].extend(handlers)

    def register_command(
        self, command: CT, handlers: Iterable[CommandHandler[CT, CR]]
    ):
        self.commands_map[command].extend(handlers)

    async def publish(self, events: Iterable[BaseEvent]) -> Iterable[ER]:
        event_type = type(events)
        handlers = self.events_map.get(event_type)

        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)

        result = []

        for event in events:
            result.extend(await handler.handle(event) for handler in handlers)

        return result

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = type(command)
        handlers = self.commands_map.get(command_type)
        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)

        return [await handler.handle(command) for handler in handlers]
