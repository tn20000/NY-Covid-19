import wget

class DataGrabber:
    def load_data():
        u = 'https://health.data.ny.gov/api/views/xdss-u53e/rows.csv?accessType=DOWNLOAD'
        f = wget.download(u)