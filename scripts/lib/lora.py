from network import LoRa
import socket
import machine
import time

class LoRaController(object):

  MTU = 80  # TBD

  def __init__(self):
    """Constructor."""
    self.lora_ = LoRa(mode=LoRa.LORA,
                      region=LoRa.US915,
                      power_mode=LoRa.ALWAYS_ON,
                      tx_power=5,  # 5~20
                      bandwidth=LoRa.BW_500KHZ)

    # create a raw LoRa socket
    self.sock_ = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    self.sock_.setblocking(False)

    def send(self,data):
      """Send out data.

      Args:
        data: bytes.
      """
      s.setblocking(True)
      s.send(data)

    def recv(self):
      """Receive data.

      This is non-blocking call.

      Returns:
        bytes if a data is received.
        0 byte of data will be returned if no data is received.
      """
      s.setblocking(False)
      return s.recv(self.MTU)