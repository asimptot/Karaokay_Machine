from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject
class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        print(self.args)
        result = self.fn(
            *self.args, **self.kwargs
        )

        self.signals.result.emit(result)  # Return the result of the processing
        self.signals.finished.emit()
