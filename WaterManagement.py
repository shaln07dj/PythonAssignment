import sys


class WaterManagement:
    def __init__(self, guests=0, total_water_consumed=0, bill=0):
        self.total_water_consumed = total_water_consumed
        self.guests = guests
        self.bill = bill

    def addGuest(self, guest):

        self.guests = self.guests+guest

    def bill_cal(self, flat_bhk, corporation_water, borewell_water):
        total_tank_bill = 0
        flat_water_bill = 0
        if flat_bhk > 2:
            self.total_water_consumed = (
                (flat_bhk+2)*10*30)+(self.guests*10*30)
            corporation_water_bill = 1 * \
                ((flat_bhk+2)*10*30)*(corporation_water /
                                      (corporation_water+borewell_water))
            borewell_water_bill = 1.5 * \
                ((flat_bhk+2)*10*30)*(borewell_water /
                                      (corporation_water+borewell_water))
            flat_water_bill = int(corporation_water_bill+borewell_water_bill)

        else:
            self.total_water_consumed = (
                (flat_bhk+1)*10*30)+(self.guests*10*30)
            corporation_water_bill = 1 * \
                ((flat_bhk+1)*10*30)*(corporation_water /
                                      (corporation_water+borewell_water))
            borewell_water_bill = 1.5 * \
                ((flat_bhk+1)*10*30)*(borewell_water /
                                      (corporation_water+borewell_water))
            flat_water_bill = int(corporation_water_bill+borewell_water_bill)

        if(self.guests*10*30 <= 500):
            total_tank_bill = (self.guests*10*30)*2
        elif((self.guests*10*30) > 500 and (self.guests*10*30) <= 1500):
            total_tank_bill = 500*2+(self.guests*10*30-500)*3
        elif((self.guests*10*30) > 1500 and (self.guests*10*30) <= 3000):
            total_tank_bill = 500*2+1000*3+(self.guests*10*30-1500)*5
        elif(self.guests*10*30 > 3000):
            total_tank_bill = 500*2+1000*3+1500*5+(self.guests*10*30-3000)*8

        self.bill = flat_water_bill+total_tank_bill

        print(f'{self.total_water_consumed} {self.bill}')


ratio = sys.argv[3].split(':')
flat_bhk = int(sys.argv[2])
corporation_water = int(ratio[0])
borewell_water = int(ratio[1])
w = WaterManagement()

while(True):
    option = input()
    if("ADD_GUESTS" in option):
        ls = option.split(" ")
        guest = int(ls[-1])

        w.addGuest(guest)
    elif(option == "BILL"):

        w.bill_cal(flat_bhk, corporation_water, borewell_water)
        sys.exit()
