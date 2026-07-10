"""
====================================================
KWENZA AI LEGACY
AI COMMAND CENTER V1.0
====================================================
"""

import os
import sys
import importlib
from datetime import datetime


class AICommandCenter:

    def __init__(self):

        self.name = "Kwenza AI Legacy"
        self.version = "1.0.0"
        self.owner = "Andile Mkhize"
        self.status = "ONLINE"
        self.start_time = datetime.now()

        self.load_brain()

        self.commands = {}

        self.register_commands()

    # ==================================================
    # BRAIN CONNECTION
    # ==================================================

    def load_brain(self):

        brain_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "Brain"
            )
        )

        if brain_path not in sys.path:
            sys.path.append(brain_path)

    # ==================================================
    # SAFE IMPORT
    # ==================================================

    def load_module(self, module_name):

        try:

            return importlib.import_module(module_name)

        except Exception:

            return None

    # ==================================================
    # COMMAND REGISTRY
    # ==================================================

    def register(self, command, function):

        self.commands[command] = function

    def register_commands(self):

        self.register("help", self.help)

        self.register("status", self.status_report)

        self.register("version", self.version_report)

    # ==================================================
    # EXECUTE
    # ==================================================

    def execute(self, command):

        command = command.lower().strip()

        if command in self.commands:

            try:

                return self.commands[command]()

            except Exception as e:

                return f"Command Error\n\n{e}"

        return (
            "Unknown command.\n\n"
            "Type 'help' to see available commands."
        )

    # ==================================================
    # HELP
    # ==================================================

    def help(self):

        lines = []

        lines.append("========== KWENZA AI ==========")
        lines.append("")
        lines.append("SYSTEM")
        lines.append("------")
        lines.append("help")
        lines.append("status")
        lines.append("version")
        lines.append("")
        lines.append("Future Commands")
        lines.append("----------------")
        lines.append("price")
        lines.append("analysis")
        lines.append("signal")
        lines.append("strategy")
        lines.append("scanner")
        lines.append("news")
        lines.append("journal")
        lines.append("trade")
        lines.append("risk")
        lines.append("backtest")
        lines.append("memory")
        lines.append("learn")
        lines.append("forecast")
        lines.append("voice")
        lines.append("vision")
        lines.append("")
        lines.append("==============================")

        return "\n".join(lines)

    # ==================================================
    # STATUS
    # ==================================================

    def status_report(self):

        return (
            "========== KWENZA AI ==========\n\n"
            f"Name : {self.name}\n"
            f"Version : {self.version}\n"
            f"Owner : {self.owner}\n"
            f"Status : {self.status}\n\n"
            "Brain : Connected\n"
            "Registry : Active\n"
            "=============================="
        )

    # ==================================================
    # VERSION
    # ==================================================

    def version_report(self):

        return (
            "KWENZA AI LEGACY\n\n"
            f"Version : {self.version}\n"
            f"Owner : {self.owner}"
        )