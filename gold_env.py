class GoldDetectionEnv:

    def __init__(self):
        self.state = "ready"

    def reset(self):
        self.state = "scan_started"
        return self.state

    def step(self, action):
        if action == "scan":
            reward = 1.0
            done = True
            result = "Gold signal detected"
        else:
            reward = 0.0
            done = False
            result = "No signal"

        return result, reward, done

    def state(self):
        return self.state
