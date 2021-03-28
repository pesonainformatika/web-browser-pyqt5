import sys
from utils import default_url
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit


# create main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(default_url))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # button config
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        # navigate home button
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        # url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # update Url
        self.browser.urlChanged.connect(self.update_url)

    # navigate home method
    def navigate_home(self):
        self.browser.setUrl(QUrl(default_url))

    # navigate url method
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    # update url method
    def update_url(self, query):
        self.url_bar.setText(query.toString())


# run app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # set App Name
    QApplication.setApplicationName('Yukina Browser')

    main_window = MainWindow()
    app.exec_()
