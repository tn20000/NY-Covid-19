from load_data import DataGrabber
from gui import MainApp

grabber = DataGrabber()
grabber.load_data()
app = MainApp()
app.run()