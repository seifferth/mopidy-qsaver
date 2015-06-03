from __future__ import unicode_literals

import logging

import json

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
        logger.info("Qsaver is saving the tracklist")
        with open(self.backup_file, 'w') as f:
            tracklistFuture = self.core.tracklist.get_tracks() # uses pykka.ThreadingActor
            tracklist = str(tracklistFuture.get()) # get the future (promise) value
            # logger.info(tracklist)
            f.write(tracklist)
        f.closed

    def restoreQueue(self):
        # TODO: restore the queue from a local file
        logger.info("Qsaver is restoring your tracklist")

    def on_start(self):
        self.restoreQueue()

    def on_stop(self):
        self.saveQueue()

    def track_playback_started(self, tl_track):
        self.saveQueue()
