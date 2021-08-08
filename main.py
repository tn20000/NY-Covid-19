from load_data import DataGrabber

grabber = DataGrabber()
grabber.load_data()

from gui import MainApp
print('Done')
app = MainApp()
app.run()