import sys

from PyQt5.QtCore import QUrl

from PyQt5.QtWidgets import QApplication

from PyQt5.QtQuick import QQuickView

app = QApplication(sys.argv)

view = QQuickView()

view.setResizeMode(QQuickView.SizeRootObjectToView)

# Let QML close the main application

view.engine().quit.connect(app.quit)

view.setSource(QUrl('declarative-camera.qml'))

view.show()

sys.exit(app.exec_())

