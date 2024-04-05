class Time:
    print("Salom bollar")
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def chiqar(self):
        print(self.hour*60+self.minute+self.second/60, "munut")

    def qosh_10_daq(self):
        self.minute += 10
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
            if self.hour >= 24:
                self.hour -= 24
        print(f"{self.hour}:{self.minute}:{self.second}")

class Train(Time):
    def __init__(self, num_train, route, *dep_time):
        super().__init__(dep_time[0], dep_time[1], dep_time[2])
        self.route = route
        self.num_train = num_train


    def qachon(self, *time):
        h = self.hour - time[0]
        m = self.minute-time[1]
        s = self.second - time[2]

        if s<0:
            m = m - 1
            s+=60
        if m<0:
            h = h - 1
            m+=60

        print(h, "soat",
              m, "daqiqa",
              s,"soniya qoldi")

l = []
for i in range(2):
    ntrain, route, h, m, s = map(int, input().split())
    l.append(Train(ntrain, route, h, m, s))

for i in l:
    i.qachon(5, 25, 10)









# for i in l:
#     i.qosh_10_daq()
# a = Time(10, 25, 30)
# b = Time(14, 20, 1)
# c = Time(8, 50, 0)
# d = Time(10, 5, 39)
# e = Time(19, 23, 45)

