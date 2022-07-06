import sys
from PyQt5.QtWidgets import *
from window import *
import sqlite3


Application=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_Window()
ui.setupUi(penAna)
penAna.show()


global curs
global conn

conn=sqlite3.connect('database.db')
curs=conn.cursor()
queryCreTblSpor=("CREATE TABLE IF NOT EXISTS karaokay(     \
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,      \
        Emp_No TEXT NOT NULL UNIQUE,                       \
        Emp_Name TEXT NOT NULL,                     \
        Song TEXT NOT NULL,                          \
        Artist TEXT NOT NULL,                          \
        Duration FLOAT NOT NULL,                          \
        Genre TEXT NOT NULL,                          \
        Signal_Distortion FLOAT NOT NULL)")
curs.execute(queryCreTblSpor)
conn.commit()



def Add():
    emp_no = ui.ln_emp_no.text()
    emp_name = ui.ln_emp_name.text()
    song = ui.ln_song.text()
    artist = ui.ln_artist.text()
    duration = float(ui.ln_duration.text())
    genre = ui.ln_genre.text()
    signal_distortion = float(ui.ln_signal_distortion.text())
    answer=QMessageBox.question(penAna,"ADD DATA","Are you sure to add?",\
                         QMessageBox.Yes | QMessageBox.No)
    if answer==QMessageBox.Yes:
        curs.execute("INSERT INTO karaokay \
                      (Emp_No,Emp_Name,Song,Artist,Duration,Genre,Signal_Distortion) \
                    VALUES (?,?,?,?,?,?,?)",
                     (emp_no, emp_name, song, artist, duration, genre, signal_distortion))
        conn.commit()
    List()

def List():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("ID","EmpNo","EmpName","Song","Artist","Duration","Genre","SDR"))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT * FROM karaokay")
    for rowIndex, rowData in enumerate(curs):
        for columnIndex, columnData in enumerate (rowData):
            ui.tableWidget.setItem(rowIndex,columnIndex,QTableWidgetItem(str(columnData)))
            ui.ln_emp_no.clear()
            ui.ln_emp_name.clear()
            ui.ln_song.clear()
            ui.ln_artist.clear()
            ui.ln_duration.clear()
            ui.ln_genre.clear()
            ui.ln_signal_distortion.clear()


def Exit():
    answer=QMessageBox.question(penAna,"EXIT","Are you sure to exit?",\
                         QMessageBox.Yes | QMessageBox.No)
    if answer==QMessageBox.Yes:
        conn.close()
        sys.exit(Application.exec_())
    else:
        penAna.show()


def Delete():
    answer=QMessageBox.question(penAna,"DELETE DATA","Are you sure to delete?",\
                         QMessageBox.Yes | QMessageBox.No)
    if answer == QMessageBox.Yes:
        selected = ui.tableWidget.selectedItems()
        deleted = selected[1].text()
        try:
            curs.execute("DELETE FROM karaokay WHERE Emp_No='%s'" % (deleted))
            conn.commit()

            List()

            ui.statusbar.showMessage("Successfull!", 10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Error: " + str(Hata))
    else:
        ui.statusbar.showMessage("Delete was cancelled...", 10000)

def Search():

    search1 = ui.ln_emp_no.text()
    search2 = ui.ln_emp_name.text()
    search3 = ui.ln_song.text()
    search4 = ui.ln_artist.text()
    search5 = ui.ln_duration.text()
    search6 = ui.ln_genre.text()
    curs.execute("SELECT * FROM karaokay WHERE Emp_No=? OR Emp_Name=? OR Song=? OR Artist=? OR Duration=? OR Genre=?",(search1, search2, search3, search4, search5, search6))
    conn.commit()
    ui.tableWidget.clear()
    for rowIndex, rowData in enumerate(curs):
        for columnIndex, columnData in enumerate (rowData):
            ui.tableWidget.setItem(rowIndex,columnIndex,QTableWidgetItem(str(columnData)))

def Clear():
    ui.ln_emp_no.clear()
    ui.ln_emp_name.clear()
    ui.ln_song.clear()
    ui.ln_artist.clear()
    ui.ln_duration.clear()
    ui.ln_genre.clear()
    ui.ln_signal_distortion.clear()

def Fill():
    try:
        selected=ui.tableWidget.selectedItems()
        ui.ln_emp_no.setText(selected[1].text())
        ui.ln_emp_name.setText(selected[2].text())
        ui.ln_song.setText(selected[3].text())
        ui.ln_artist.setText(selected[4].text())
        ui.ln_duration.setText(selected[5].text())
        ui.ln_genre.setText(selected[6].text())
        ui.ln_signal_distortion.setText(selected[7].text())
    except Exception as hata:
        ui.ln_emp_no.clear()
        ui.ln_emp_name.clear()
        ui.ln_song.clear()
        ui.ln_artist.clear()
        ui.ln_duration.clear()
        ui.ln_genre.clear()
        ui.ln_signal_distortion.clear()


def Update():
    answer=QMessageBox.question(penAna,"UPDATE DATA","Are you sure to update?",\
                         QMessageBox.Yes | QMessageBox.No)
    if answer==QMessageBox.Yes:
        try:
            selected=ui.tableWidget.selectedItems()
            _Id=int(selected[0].text())
            _emp_no=ui.ln_emp_no.text()
            _emp_name=ui.ln_emp_name.text()
            _song=ui.ln_song.text()
            _artist=ui.ln_artist.text()
            _duration=ui.ln_duration.text()
            _genre=ui.ln_genre.text()
            _signal_distortion = ui.ln_signal_distortion.text()

            curs.execute("UPDATE karaokay SET Emp_No=?, Emp_Name=?, Song=?, Artist=?, Duration=?, Genre=?, Signal_Distortion=? WHERE Id=?",(_emp_no,_emp_name,_song,_artist,_duration,_genre,_signal_distortion,_Id))
            conn.commit()
            List()
        except Exception as hata:
            ui.statusbar.showMessage("Error: " + str(hata))
    else:
        ui.statusbar.showMessage("Update was cancelled",5000)

List()
ui.btn_save.clicked.connect(Add)
ui.btn_exit.clicked.connect(Exit)
ui.btn_delete.clicked.connect(Delete)
ui.btn_search.clicked.connect(Search)
ui.btn_clear.clicked.connect(Clear)
ui.btn_update.clicked.connect(Update)
ui.btn_view.clicked.connect(List)
ui.tableWidget.itemSelectionChanged.connect(Fill)

sys.exit(Application.exec_())