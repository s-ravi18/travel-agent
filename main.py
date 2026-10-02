"""Small CLI entry point for quick non-Streamlit checks."""
from __future__ import annotations

import sys

from agent import build_agent


# def main() -> None:
#     prompt = " ".join(sys.argv[1:]).strip()
#     if not prompt:
#         prompt = "Plan a 3-day standard-budget trip to Rome for two people in USD."

#     agent = build_agent(debug=False)
#     result = agent.invoke({"messages": [("human", prompt)]})
#     print(result["messages"][-1].content)

def main() -> None:
    prompt = " ".join(sys.argv[1:]).strip()

    if not prompt:
        prompt = "Plan a 3-day standard-budget trip to Rome for two people in USD."

    agent = build_agent(debug=False)

    final_result = None

    for event in agent.stream(
        {"messages": [("human", prompt)]},
        stream_mode="updates"
    ):
        for node, data in event.items():
            print(f"\n{'=' * 60}")
            print(f"NODE: {node}")
            print(f"{'=' * 60}")

            if "messages" in data:
                for message in data["messages"]:
                    print(f"\n{message}")

            final_result = data

    print("\n" + "=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)

    if final_result and "messages" in final_result:
        print(final_result["messages"][-1].content)


if __name__ == "__main__":
    main()
