import wget

class DataGrabber:
    def load_data(self):
        u = 'https://health.data.ny.gov/api/views/xdss-u53e/rows.csv?accessType=DOWNLOAD'
        wget.download(u)