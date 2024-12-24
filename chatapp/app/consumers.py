from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket Connected...',event)
    
    def websocket_receive(self,event):
        print('Websocket Client Data Recieved...',event)
    
    def websocket_disconnect(self,event):
        print('Websocket Disconnected...',event)
