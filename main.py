import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
from ui_warthog_window import Ui_MainWindow
from ui_selecter import Ui_Dialog
from ui_error import Ui_Dialog_Err
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtCore import QUrl
import requests

ICON_URL = 'https://i.postimg.cc/1XRLvH7V/icon.png'
class ErrorWindow(QMainWindow):
    def __init__(self):
        super(ErrorWindow,self).__init__()
        self.ui_err = Ui_Dialog_Err()
        self.ui_err.setupUi(self)
        self.nam = QNetworkAccessManager(self)
        self.nam.finished.connect(self.set_window_icon_from_reply)
        self.nam.get(QNetworkRequest(QUrl(ICON_URL)))

    def set_window_icon_from_reply(self, reply):
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)


class Selecter(QMainWindow):
    def __init__(self, window):
        super(Selecter,self).__init__()
        self.ui_selecter = Ui_Dialog()
        self.ui_selecter.setupUi(self)
        self.window = window
        self.ui_selecter.blocks.setText("20")
        self.nam = QNetworkAccessManager(self)
        self.nam.finished.connect(self.set_window_icon_from_reply)
        self.nam.get(QNetworkRequest(QUrl(ICON_URL)))
        self.ui_selecter.node_button.clicked.connect(self.nodes)
        self.ui_selecter.miners_button.clicked.connect(self.miners)
        self.ui_selecter.trans_button.clicked.connect(self.transactions)
    def set_window_icon_from_reply(self, reply):
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)
    def miners(self):
        amount_blocks = int(self.ui_selecter.blocks.text())
        ip_node = f'http://{window.ui.input_text.text()}:3000'

        height = requests.get(f"{ip_node}/chain/head").json()['data']['height']

        list_miners = {}
        for i in range(height - amount_blocks, height):
            url_block_info = requests.get(f'{ip_node}/chain/block/{i}').json()
            if url_block_info['data']['body']['rewards'][0]['toAddress'] in list_miners:
                list_miners[url_block_info['data']['body']['rewards'][0]['toAddress']] += 3
            else:
                list_miners[url_block_info['data']['body']['rewards'][0]['toAddress']] = 3
        for miners in list_miners:
            mine = str(miners)
            amount = str(list_miners[miners])
            res = mine + ' ' + amount
            window.ui.items.addItem(res)
        self.close()


    def nodes(self):
        ip_node = window.ui.input_text.text()
        url = f'http://{ip_node}:3000/peers/ip_count'
        peers = list(requests.get(url).json())
        list_peers = []
        for i in peers:
            url2 = f'http://{i}:3000'
            try:
                connect_peers = requests.get(url2, timeout=1)
                if connect_peers.status_code == 200:
                    list_peers.append(i)
            except:
                continue
        for peer in list_peers:
            window.ui.items.addItem(peer)
        self.close()

    def transactions(self):
        ip_node = window.ui.input_text.text()
        amount_blocks = int(self.ui_selecter.blocks.text())
        url = f'http://{ip_node}:3000'
        height = requests.get(f'{url}/chain/head').json()['data']['height']
        list_transactions = []
        for i in range(height - amount_blocks, height):
            url_block = f'{url}/chain/block/{i}'
            get_block = requests.get(url_block).json()['data']['body']['transfers']
            if len(get_block) > 0:
                for j in range(len(get_block)):
                    list_transactions.append({get_block[j]['amount']: \
                            {f'from {get_block[j]["fromAddress"]}': f'to {get_block[j]["toAddress"]}'}})
        for i in range(len(list_transactions)):
            res = f'{i + 1} {str(list_transactions[i])}'
            window.ui.items.addItem(res)
        self.close()
    def set_window_icon_from_reply(self, reply):
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)
class WarthogNetwork(QMainWindow):
    def __init__(self):
        super(WarthogNetwork, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.nam = QNetworkAccessManager(self)
        self.nam.finished.connect(self.set_window_icon_from_reply)
        self.nam.get(QNetworkRequest(QUrl(ICON_URL)))

        self.ui.select_button.clicked.connect(self.select)

    def errorWindow(self):
        self.error = ErrorWindow()
        self.error.show()
    def select(self):

        ip_node = self.ui.input_text.text()
        try:
            if requests.get(f'http://{ip_node}:3000', \
                            timeout=1).status_code == 200:
                self.selecter = Selecter(self)
                self.selecter.show()
                return ip_node
        except:
            self.errorWindow()

    def set_window_icon_from_reply(self, reply):
        pixmap = QPixmap()
        pixmap.loadFromData(reply.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WarthogNetwork()
    window.show()

    sys.exit(app.exec())