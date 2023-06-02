import threading, zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, "w", zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print("Hoàn thành chép ảnh từ: ", self.infile)
