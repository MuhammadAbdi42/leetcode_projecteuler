from typing import List
from collections import deque
import bisect


class Router:
    packets = set()
    packet_queue = deque()
    dest_time = {}

    def __init__(self, memoryLimit: int):
        self.packets = set()
        self.packet_queue = deque()
        self.dest_time = {}
        self.memory_limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = self.__packet_code(source, destination, timestamp)

        if packet in self.packets:
            return False
        else:
            if len(self.packet_queue) == self.memory_limit:
                self.__return_oldest()

            self.__add_new_packet(source, destination, timestamp)

            return True

    def forwardPacket(self) -> List[int]:
        if len(self.packets) > 0:
            return self.__return_oldest()
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_time.keys():
            return 0
        else:
            timestamps = self.dest_time[destination]
            left = bisect.bisect_left(timestamps, startTime)
            right = bisect.bisect_right(timestamps, endTime)
            return right - left

    def __packet_code(self, source: int, destination: int, timestamp: int) -> str:
        return str(source) + '-' + str(destination) + '-' + str(timestamp)

    def __return_oldest(self) -> List[int]:
        oldest_packet = self.packet_queue.popleft()
        self.packets.remove(self.__packet_code(
            oldest_packet[0], oldest_packet[1], oldest_packet[2]))
        self.dest_time[oldest_packet[1]].pop(0)
        return oldest_packet

    def __add_new_packet(self, source: int, destination: int, timestamp: int):
        packet = self.__packet_code(source, destination, timestamp)
        self.packets.add(packet)
        self.packet_queue.append([source, destination, timestamp])
        if destination in self.dest_time:
            self.dest_time[destination].append(timestamp)
        else:
            self.dest_time[destination] = [timestamp]


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
