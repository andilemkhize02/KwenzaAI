"""
Kwenza AI - Memory System v1.0

Stores AI experiences and decisions.
"""

import json
import os
from datetime import datetime


MEMORY_FILE = "ai_memory.json"



class AIMemory:

    def __init__(self):

        self.file = MEMORY_FILE

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f)



    def save(self, data):

        with open(self.file, "r") as f:
            memory = json.load(f)


        data["time"] = str(datetime.now())


        memory.append(data)


        with open(self.file, "w") as f:
            json.dump(memory, f, indent=4)



    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)



    def count(self):

        return len(self.load())




def save_memory(data):

    brain = AIMemory()

    brain.save(data)




def get_memory():

    brain = AIMemory()

    return brain.load()



if __name__ == "__main__":


    save_memory({

        "symbol": "EURUSD",
        "decision": "BUY",
        "confidence": 85

    })


    print("Kwenza AI Memory")

    print(get_memory())