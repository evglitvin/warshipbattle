from src.core.context import Context
from src.core.state import BeforeGameState, InGameState

if __name__ == "__main__":
    context = Context(BeforeGameState)
    # change the state from the <Context> obj
    context.transition_to(InGameState)
