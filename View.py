import sys
from PyQt5.QtWidgets import QApplication,QFileSystemModel,QMainWindow, QFileDialog, QLabel, QPushButton, QTreeView, QVBoxLayout, QWidget, QTreeWidgetItem
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree Structure")
        self.setGeometry(100, 100, 400, 300)
        self.my_dir = ''

        self.select_button = QPushButton('Select directory')
        self.select_button.clicked.connect(self.select_directory)

        self.directory_label = QLabel(self.my_dir)

        self.tree_view = QTreeView()
        self.tree_view.setColumnWidth(0, 20)
        self.tree_view.setColumnWidth(1, 300)
        self.tree_view.setHeaderHidden(False)
        self.tree_view.setHeaderLabels(["#", "Name"])

        layout = QVBoxLayout()
        layout.addWidget(self.select_button)
        layout.addWidget(self.directory_label)
        layout.addWidget(self.tree_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_directory(self):
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if path:
            self.my_dir = path
            self.directory_label.setText(path)

            root, dirnames, files = next(os.walk(path))
            self.tree_view.clear()

            i = 1
            f2i = 1
            for d in dirnames:
                item = QTreeWidgetItem(self.tree_view)
                item.setText(0, str(i))
                item.setText(1, d)

                path2 = os.path.join(path, d)
                files2 = next(os.walk(path2))[2]
                for f2 in files2:
                    sub_item = QTreeWidgetItem(item)
                    sub_item.setText(0, "sub" + str(f2i))
                    sub_item.setText(1, "-" + f2)
                    f2i += 1
                i += 1

            for f in files:
                item = QTreeWidgetItem(self.tree_view)
                item.setText(0, str(i))
                item.setText(1, f)
                i += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    path = sys.argv[1]  # Retrieve the passed directory path

    model = QFileSystemModel()
    model.setRootPath(path)

    tree = QTreeView()
    tree.setModel(model)
    tree.setRootIndex(model.index(path))

    tree.show()
    sys.exit(app.exec_())
