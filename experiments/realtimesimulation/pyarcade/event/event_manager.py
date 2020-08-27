class EventListener:
    def notify(self, event):
        print("event")
        print(event)

class EventManager:

    events = []
    listeners = []


    def raise_event(self, event):
        self.events.append(event)

    def subscribe(self, event_listener):
        self.listeners.append(event_listener)

    def run(self):
        events_copy = self.events.copy()
        self.events.clear();
        for event in events_copy:
            for listener in self.listeners:
                listener.notify(event)


event_manager = EventManager()

event_listener = EventListener()
event_manager.subscribe(event_listener)

event_listener2 = EventListener()
event_manager.subscribe(event_listener2)

event_manager.raise_event({"siren"})
event_manager.raise_event(({"noise"}))

event_manager.run()
