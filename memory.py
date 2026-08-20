from typing import List, Dict, Any

class ConversationMemory:
    def __init__(self, max_history_turns: int = 10):
        self.max_history_turns = max_history_turns
        self.history: List[Dict[str, Any]] = []

    def add_message(self, role: str, content: Any):
        self.history.append({"role": role, "content": content})
        if len(self.history) > (self.max_history_turns * 2):
            self.history = self.history[-(self.max_history_turns * 2):]

    def get_messages(self, system_prompt: str = None) -> List[Dict[str, Any]]:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.extend(self.history)
        return messages

    def clear(self):
        self.history = []
