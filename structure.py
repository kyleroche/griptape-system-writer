import os
import sys

from griptape.drivers import WebhookEventListenerDriver
from griptape.events import EventListener, FinishStructureRunEvent
from griptape.rules import Rule, Ruleset
from griptape.structures import Agent


def build_writer(role: str, goal: str, backstory: str):
    """Builds a Writer Structure.

    Args:
        role: The role of the writer.
        goal: The goal of the writer.
        backstory: The backstory of the writer.
    """
    writer = Agent(
        id=role.lower().replace(" ", "_"),
        event_listeners=[
            EventListener(
                event_types=[FinishStructureRunEvent],
                driver=WebhookEventListenerDriver(
                    webhook_url=os.environ["ZAPIER_WEBHOOK_URL"],
                ),
            ),
            EventListener(
                event_types=[FinishStructureRunEvent],
                driver=WebhookEventListenerDriver(
                    webhook_url=os.environ["ZAPIER_WEBHOOK_URL"],
                ),
            ),
        ],
        rulesets=[
            Ruleset(
                name="Position",
                rules=[
                    Rule(
                        value=role,
                    )
                ],
            ),
            Ruleset(
                name="Objective",
                rules=[
                    Rule(
                        value=goal,
                    )
                ],
            ),
            Ruleset(
                name="Backstory",
                rules=[Rule(value=backstory)],
            ),
            Ruleset(
                name="Desired Outcome",
                rules=[
                    Rule(
                        value="Full blog post of at least 4 paragraphs",
                    )
                ],
            ),
        ],
    )

    return writer


role = sys.argv[1]
goal = sys.argv[2]
backstory = sys.argv[3]
input = sys.argv[4]

writer = build_writer(
    role=role,
    goal=goal,
    backstory=backstory,
)

writer.run(input)
