import time

class FSM:

    RESTING = 0
    EXPLORING = 1
    CHASING = 2

    current_state = RESTING

    current_frame = 0;
    action_expire_frame = 0;

    def update(self):
        self.current_frame += 1
        if self.current_frame >= self.action_expire_frame:
            self.update_state()


    def update_state(self):

        if self.current_state == self.RESTING:
            print("now exploring")
            self.current_state = self.EXPLORING
            self.action_expire_frame = self.current_frame + 10
            return

        if self.current_state == self.EXPLORING:
            print("now resting")
            self.current_state = self.RESTING
            self.action_expire_frame = self.current_frame + 2
            return

        if self.current_state == self.CHASING:
            print("now resting")
            self.current_state = self.RESTING
            self.action_expire_frame = self.current_frame + 2
            return

    def execute_action(self):

        if self.current_state == self.RESTING:
            # print("resting")
            return

        if self.current_state == self.EXPLORING:
            # print("exploring")
            return

        if self.current_state == self.CHASING:
            # print("chasing")
            return


if __name__ == "__main__":
    fsm = FSM()
    while True:
        fsm.update()
        fsm.execute_action()
        time.sleep(0.5)


# todo implement more complet FSM, with transiton check and trigger