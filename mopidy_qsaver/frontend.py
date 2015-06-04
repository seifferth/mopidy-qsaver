from __future__ import unicode_literals

import logging

import os.path

from mopidy.core import CoreListener

import pykka

logger = logging.getLogger(__name__)


class QSaverFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(QSaverFrontend, self).__init__()
        self.config = config
        self.core = core
        self.backup_file = self.config.get('qsaver')['backup_file']

    def saveQueue(self):
        logger.info("Qsaver is saving your tracklist")
        with open(self.backup_file, 'w') as f:
            tracklist = self.core.tracklist.get_tracks().get()
            uri_list = [t.uri for t in tracklist]
            f.write(str(uri_list))
        f.closed
        logger.info("Qsaver has saved your tracklist!")

    def restoreQueue(self):
        logger.info("Qsaver is restoring your tracklist")
        if os.path.exists(self.backup_file):
            with open(self.backup_file, 'r') as f:
                uri_list_str = f.read()
                uri_list = eval(uri_list_str)  # convert to array
                self.core.tracklist.add(None, None, None, uri_list)
            f.closed
            logger.info("Qsaver has restored your tracklist!")
        else:
            logger.info("Qsaver unable to restore tracklist file")

    def on_start(self):
        self.restoreQueue()

    def on_stop(self):
        self.saveQueue()

    def tracklist_changed(self):
        self.saveQueue()

    def getUri(track):
        return track.uri
