from lcu_driver import Connector
import json

lcu_connector = Connector()

# class Lcu():
#     def __init__(self):
#         self._connector = Connector()
#
#     def start(self):
#         self._connector.start()

# @lcu_connector.ready
# async def connect(connection):
#     print('LCU API is ready to be used.')
#
# @lcu_connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
# async def icon_changed(connection, event):
#     print(f'The summoner {event.data["displayName"]} was updated.')
#
# @lcu_connector.ws.register('/lol-gameflow/', event_types=('UPDATE',))
# async def gameflow(connection, event):
#     print("gameflow")
#     print(json.dumps(event.data, indent=2))
#
# @lcu_connector.ws.register('/lol-lobby/', event_types=('UPDATE',))
# async def lobby(connection, event):
#     print("lobby")
#     print(json.dumps(event.data, indent=2))
#
# @lcu_connector.ws.register('/lol-champ-select/', event_types=('UPDATE',))
# async def champ_select(connection, event):
#     print("lobby champ select")
#     print(json.dumps(event.data, indent=2))

# @lcu_connector.ws.register('/lol-champ-select/v1/summoners/0', event_types=('UPDATE',))
# async def champ_select_report_summoner_and_champ(connection, event):
#     summoner = event.data["cellId"]
#     champ_name = event.data['championName']
#     print(f'summoner w/ cellId {summoner} has locked in {champ_name}')

@lcu_connector.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
async def champ_select_report_summoner_and_champ(connection, event):
    print('~~~~~~~')
    print('New Session Received')
    if event.data["timer"]["phase"] == "FINALIZATION":
        print(event.uri)
        print(json.dumps(event.data, indent=2))
        for action in event.data["actions"]:
            for state in action:
                cell = state["actorCellId"]
                champ_id = state["championId"]
                pick_or_ban = state["type"]

                print(f'actorCellId {cell}, championId {champ_id}, type {pick_or_ban}')

@lcu_connector.ws.register('/lol-champ-select/v1/summoners/', event_types=('UPDATE',))
async def champ_select_report_summoner_and_champ(connection, event):
    cell_id = event.data["cellId"]
    slot_id = event.data["slotId"]
    champ_name = event.data["championName"]
    print(f'cell_id: {cell_id}, slot_id: {slot_id}, champ_name: {champ_name}')
