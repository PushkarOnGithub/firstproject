import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLineEdit
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Browser")

        # Create a web view widget and set it as the central widget of the window
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Create toolbar actions for navigating back, forward, and refreshing
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.web_view.back)

        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.web_view.forward)

        refresh_action = QAction("Refresh", self)
        refresh_action.triggered.connect(self.web_view.reload)
        refresh_action.setShortcut(QKeySequence.Refresh)  # Set shortcut to Ctrl+R

        # Create a menu action for downloading files
        download_action = QAction("Download", self)
        download_action.triggered.connect(self.download_file)

        # Add the actions to a toolbar
        self.toolbar = self.addToolBar("Navigation")
        self.toolbar.addAction(back_action)
        self.toolbar.addAction(forward_action)
        self.toolbar.addAction(refresh_action)

        # Add the actions to the menu
        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction(download_action)

        # Create a URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)
        self.toolbar.addWidget(self.url_bar)

    def load_url(self):
        url = self.url_bar.text()
        self.web_view.load(QUrl.fromUserInput(url))

    def download_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*)")
        if file_path:
            download_item = self.web_view.page().download(self.web_view.page().url())
            download_item.setPath(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = BrowserWindow()
    browser.show()
    browser.load_url()
    sys.exit(app.exec_())
