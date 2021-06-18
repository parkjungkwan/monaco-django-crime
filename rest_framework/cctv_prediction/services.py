from rest_framework.common.entity import FileDTO
from rest_framework.common.services import Reader, Printer
'''
살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
'''
class Service(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()

        self.crime_rate_columns = ['살인검거율','강도검거율','강간검거율','절도검거율','폭력검거율']
        self.crime_columns = ['살인','강도','강간','절도','폭력']

    def save_police_pos(self):
        f = self.f
        r = self.r
        p = self.p
        f.context = './data/'
        f.fname = 'crime_in_seoul'
        crime = r.csv(f)
        p.dframe(crime)

if __name__ == '__main__':
    s = Service()
    s.save_police_pos()







