from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pathlib
import shutil
import subprocess
import matplotlib.pyplot as plt

fileFormat = {
    "Web": [".htm15", ".html", ".htm", ".xhtml"],
    "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "Video": [".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn",
                 ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", "oga", ".raw", ".vox",
              ".wav", ".vma"],
}

fileTypes = list(fileFormat.keys())
fileFormats = list(fileFormat.values())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(20, 20, 1880, 271))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.icon_label = QtWidgets.QLabel(self.frame_1)
        self.icon_label.setGeometry(QtCore.QRect(200, 10, 211, 221))
        self.icon_label.setText("")
        self.icon_label.setPixmap(QtGui.QPixmap("icon.jpeg"))
        self.icon_label.setScaledContents(True)
        self.icon_label.setObjectName("icon_label")
        self.title_label = QtWidgets.QLabel(self.frame_1)
        self.title_label.setGeometry(QtCore.QRect(340, 0, 1511, 241))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 310, 1880, 191))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.path_label = QtWidgets.QLabel(self.frame_2)
        self.path_label.setGeometry(QtCore.QRect(470, 0, 191, 151))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.path_tf = QtWidgets.QPlainTextEdit(self.frame_2)
        self.path_tf.setGeometry(QtCore.QRect(640, 50, 871, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.path_tf.setFont(font)
        self.path_tf.setObjectName("path_tf")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 529, 1880, 471))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.organize = QtWidgets.QPushButton(self.frame_3)
        self.organize.setGeometry(QtCore.QRect(20, 20, 600, 400))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.organize.setFont(font)
        self.organize.setObjectName("organize")
        self.view = QtWidgets.QPushButton(self.frame_3)
        self.view.setGeometry(QtCore.QRect(640, 20, 600, 400))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.view.setFont(font)
        self.view.setObjectName("view")
        self.visualize = QtWidgets.QPushButton(self.frame_3)
        self.visualize.setGeometry(QtCore.QRect(1260, 20, 600, 400))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.visualize.setFont(font)
        self.visualize.setObjectName("visualize")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect organize button to function
        self.organize.clicked.connect(self.organize_action)
        self.view.clicked.connect(self.view_action)
        self.visualize.clicked.connect(self.visualize_action)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Organize System"))
        self.title_label.setText(_translate("MainWindow", "File Organize System"))
        self.path_label.setText(_translate("MainWindow", "Path :"))
        self.organize.setText(_translate("MainWindow", "Organize"))
        self.view.setText(_translate("MainWindow", "View"))
        self.visualize.setText(_translate("MainWindow", "Visualize"))

    def organize_action(self):
        path = self.path_tf.toPlainText()
        if path:
            # Change directory to the provided path
            os.chdir(path)
            print("Path:", path)
            print("File Organizer Started")

            # Your file organization code here
            for file in os.scandir():
                fileName = pathlib.Path(file)
                fileFormatType = fileName.suffix.lower()

                src = str(fileName)
                dest = "Other"
                if fileFormatType == "":
                    print(f"{src} has no file format")
                else:
                    for formats in fileFormats:
                        if fileFormatType in formats:
                            folder = fileTypes[fileFormats.index(formats)]
                            if not os.path.isdir(folder):
                                os.mkdir(folder)
                            dest = folder

                            print(dest)

                    else:
                        if not os.path.isdir("Other"):
                            os.mkdir("Other")

                print(src, "moved to", dest)
                shutil.move(src, dest)

            print("File Organizer Completed")
        else:
            print("Please provide a valid path.")

    def view_action(self):
        path = self.path_tf.toPlainText()
        if path:
            view_script_path = os.path.join(os.path.dirname(__file__), "view.py")  # Full path to view.py
            subprocess.run(["python", view_script_path, path])  # Pass the selected directory path as an argument
        else:
            print("Please provide a valid path.")

    def count_files_by_type(self,path):
        file_counts = {}

        # Iterate over all files and directories in the given path
        for root, dirs, files in os.walk(path):
            for file in files:
                # Get the file extension
                _, extension = os.path.splitext(file)
                # Increment the count for this extension
                file_counts[extension] = file_counts.get(extension, 0) + 1

        return file_counts

    def get_highest_file_per_type(self,path):
        file_info = {}

        # Iterate over all files and directories in the given path
        for root, dirs, files in os.walk(path):
            for file in files:
                # Get the file extension
                _, extension = os.path.splitext(file)
                # Calculate the size of the file
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                # Check if this file type is already recorded and if its size is larger than previously recorded
                if extension not in file_info or file_size > file_info[extension][1]:
                    file_info[extension] = (file, file_size)

        return file_info

    def visualize_action(self):
        # Get the selected directory path from the text field
        selected_dir = self.path_tf.toPlainText()
        if selected_dir:

            # Call the functions from vis.py with the selected directory path as argument
            selected_dir = selected_dir.replace("\\", "/")

            file_counts = self.count_files_by_type(selected_dir)
            file_info = self.get_highest_file_per_type(selected_dir)

            # Plot the charts using the data returned from vis.py functions
            plt.figure(figsize=(12, 6))

            plt.subplot(1, 2, 1)
            file_names = [file_info[ext][0] for ext in file_info]
            sizes = [file_info[ext][1] for ext in file_info]
            plt.bar(file_names, sizes, color='skyblue')
            plt.xlabel('File Names')
            plt.ylabel('Highest File Size (Bytes)')
            plt.title('Highest File Sizes by File Name and Type')
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

            plt.subplot(1, 2, 2)
            labels = list(file_counts.keys())
            sizes = list(file_counts.values())
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title('File Counts by Type')

            plt.tight_layout()
            plt.show()
        else:
            print("Please provide a valid directory path.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
